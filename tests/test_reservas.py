import tempfile
import unittest
from pathlib import Path

from database import conectar
from reservas import cancelar, disponible, inventario, listar, reservar


class PruebasReservas(unittest.TestCase):
    def setUp(self):
        self.temporal = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporal.cleanup)
        self.conexion = conectar(Path(self.temporal.name) / "pruebas.db")
        self.addCleanup(self.conexion.close)

    def test_inventario_exacto(self):
        self.assertEqual(inventario(), {
            "MIC-01": "Microscopio digital", "MIC-02": "Microscopio digital",
            "OSC-01": "Osciloscopio", "MUL-01": "Multímetro",
            "FUE-01": "Fuente de alimentación",
        })

    def test_disponibilidad_inicial(self):
        self.assertTrue(disponible(self.conexion, "MIC-01", "2026-11-02T10:00", "2026-11-02T11:00"))

    def test_disponibilidad_limites_y_conflicto(self):
        self.conexion.execute(
            "INSERT INTO reservas(equipo, solicitante, inicio, fin) VALUES (?, ?, ?, ?)",
            ("MIC-01", "Ana", "2026-11-02T10:00", "2026-11-02T11:00"))
        for inicio, fin, esperado in [("09:00", "10:00", True), ("11:00", "12:00", True),
                                      ("10:30", "11:30", False)]:
            with self.subTest(inicio=inicio):
                self.assertEqual(disponible(self.conexion, "MIC-01", "2026-11-02T" + inicio,
                                           "2026-11-02T" + fin), esperado)

    def crear(self, equipo="MIC-01", solicitante="Ana", inicio="2026-11-02T10:00", fin="2026-11-02T11:00"):
        return reservar(self.conexion, equipo, solicitante, inicio, fin)

    def test_reserva_valida(self):
        identificador = self.crear()
        fila = self.conexion.execute("SELECT * FROM reservas WHERE id = ?", (identificador,)).fetchone()
        self.assertEqual((fila["equipo"], fila["solicitante"], fila["inicio"], fila["fin"], fila["estado"]),
                         ("MIC-01", "Ana", "2026-11-02T10:00", "2026-11-02T11:00", "ACTIVA"))

    def test_superposiciones(self):
        self.crear()
        for inicio, fin in [("10:00", "11:00"), ("10:30", "11:30"), ("09:30", "10:30"),
                            ("09:00", "12:00"), ("10:10", "10:50")]:
            with self.subTest(inicio=inicio, fin=fin):
                self.assertFalse(disponible(self.conexion, "MIC-01", "2026-11-02T" + inicio, "2026-11-02T" + fin))
                with self.assertRaisesRegex(ValueError, "superpuesta"):
                    self.crear(inicio="2026-11-02T" + inicio, fin="2026-11-02T" + fin)
        self.assertEqual(self.conexion.execute("SELECT count(*) FROM reservas").fetchone()[0], 1)

    def test_consecutivas_disponibilidad_y_creacion(self):
        self.crear()
        for inicio, fin in [("09:00", "10:00"), ("11:00", "12:00")]:
            self.assertTrue(disponible(self.conexion, "MIC-01", "2026-11-02T" + inicio, "2026-11-02T" + fin))
            self.crear(inicio="2026-11-02T" + inicio, fin="2026-11-02T" + fin)
        self.assertEqual(self.conexion.execute("SELECT count(*) FROM reservas").fetchone()[0], 3)

    def test_unidades_distintas(self):
        self.crear()
        self.assertTrue(disponible(self.conexion, "MIC-02", "2026-11-02T10:00", "2026-11-02T11:00"))
        self.crear(equipo="MIC-02")

    def test_equipo_desconocido(self):
        with self.assertRaisesRegex(ValueError, "desconocido"):
            self.crear(equipo="XXX")
        with self.assertRaises(ValueError):
            disponible(self.conexion, "XXX", "2026-11-02T10:00", "2026-11-02T11:00")

    def test_solicitantes_invalidos(self):
        for nombre in ("", "   ", "\t\n"):
            with self.subTest(nombre=nombre), self.assertRaisesRegex(ValueError, "solicitante"):
                self.crear(solicitante=nombre)

    def test_fechas_invalidas(self):
        for fecha in ("2026-02-30T10:00", "2026-11-02T24:00", "2026-1-02T10:00",
                      "2026-11-02 10:00", "2026-11-02T10:00:00", "2026-11-02T10:60", "texto", "2026-11-02T10:00Z"):
            for extremo in ("inicio", "fin"):
                with self.subTest(fecha=fecha, extremo=extremo), self.assertRaises(ValueError):
                    self.crear(**{extremo: fecha})

    def test_inicio_igual_fin(self):
        with self.assertRaisesRegex(ValueError, "anterior"):
            self.crear(fin="2026-11-02T10:00")

    def test_inicio_posterior_fin(self):
        with self.assertRaisesRegex(ValueError, "anterior"):
            self.crear(fin="2026-11-02T09:00")

    def test_fechas_pasadas_y_duracion_sin_limites(self):
        self.crear(inicio="2000-01-01T00:00", fin="2001-01-01T00:00")

    def test_cancelacion_conserva_datos(self):
        identificador = self.crear()
        original = listar(self.conexion)[0]
        cancelar(self.conexion, identificador)
        self.assertEqual(listar(self.conexion), [dict(original, estado="CANCELADA")])

    def test_cancelacion_libera_horario(self):
        identificador = self.crear()
        cancelar(self.conexion, identificador)
        self.assertTrue(disponible(self.conexion, "MIC-01", "2026-11-02T10:00", "2026-11-02T11:00"))
        nuevo = self.crear()
        self.assertNotEqual(identificador, nuevo)

    def test_cancelacion_inexistente(self):
        with self.assertRaisesRegex(ValueError, "inexistente"):
            cancelar(self.conexion, 999)

    def test_cancelacion_repetida(self):
        identificador = self.crear()
        cancelar(self.conexion, identificador)
        with self.assertRaisesRegex(ValueError, "ya está cancelada"):
            cancelar(self.conexion, identificador)
        self.assertEqual(listar(self.conexion)[0]["estado"], "CANCELADA")

    def test_historial_ambos_estados(self):
        identificador = self.crear()
        self.crear(equipo="MIC-02")
        cancelar(self.conexion, identificador)
        self.assertEqual([r["estado"] for r in listar(self.conexion)], ["CANCELADA", "ACTIVA"])


if __name__ == "__main__":
    unittest.main()
