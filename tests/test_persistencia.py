import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from database import conectar
from reservas import cancelar, listar, reservar

RAIZ = Path(__file__).resolve().parents[1]


class PruebasPersistencia(unittest.TestCase):
    def setUp(self):
        self.temporal = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporal.cleanup)
        self.ruta = Path(self.temporal.name) / "subcarpeta" / "reservas.db"

    def test_reabrir_conserva_activa_y_cancelada(self):
        conexion = conectar(self.ruta)
        try:
            primera = reservar(conexion, "MIC-01", "Ana", "2026-11-02T10:00", "2026-11-02T11:00")
            reservar(conexion, "MIC-02", "Juan", "2026-11-02T10:00", "2026-11-02T11:00")
            cancelar(conexion, primera)
            originales = listar(conexion)
        finally:
            conexion.close()
        conexion = conectar(self.ruta)
        try:
            self.assertEqual(listar(conexion), originales)
            self.assertEqual([r["estado"] for r in originales], ["CANCELADA", "ACTIVA"])
        finally:
            conexion.close()

    def cli(self, *argumentos, esperado=0):
        resultado = subprocess.run(
            [sys.executable, str(RAIZ / "app.py"), "--db", str(self.ruta), *argumentos],
            cwd=self.temporal.name, capture_output=True, text=True, encoding="utf-8",
            env=dict(os.environ, PYTHONUTF8="1"),
        )
        self.assertEqual(resultado.returncode, esperado, resultado.stdout + resultado.stderr)
        return resultado.stdout + resultado.stderr

    def test_persistencia_procesos_separados(self):
        self.assertIn("Reserva 1 creada: ACTIVA", self.cli("reservar", "MIC-01", "Ana", "2026-11-02T10:00", "2026-11-02T11:00"))
        self.assertIn("ACTIVA", self.cli("listar"))
        self.assertIn("NO DISPONIBLE", self.cli("disponibilidad", "MIC-01", "2026-11-02T10:00", "2026-11-02T11:00"))
        self.assertIn("CANCELADA", self.cli("cancelar", "1"))
        self.assertIn("CANCELADA", self.cli("listar"))
        self.assertEqual(self.cli("disponibilidad", "MIC-01", "2026-11-02T10:00", "2026-11-02T11:00").strip(), "DISPONIBLE")

    def test_cli_error_y_ayuda(self):
        self.assertIn("Equipo desconocido", self.cli("reservar", "XXX", "Ana", "2026-11-02T10:00", "2026-11-02T11:00", esperado=1))
        self.assertIn("inexistente", self.cli("cancelar", "999", esperado=1))
        self.assertIn("usage:", self.cli("--help"))
        self.cli("cancelar", "texto", esperado=2)


if __name__ == "__main__":
    unittest.main()
