"""Ejecutar suite o demo con procesos reales y guardar una transcripción UTF-8."""

import os
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]


def ejecutar(argumentos):
    resultado = subprocess.run([sys.executable, *argumentos], cwd=RAIZ,
                               capture_output=True, text=True, encoding="utf-8",
                               env=dict(os.environ, PYTHONUTF8="1"))
    return resultado


def main():
    destino = RAIZ / "docs" / "evidencias" / (sys.argv[1] + ".txt")
    partes = [f"Python {sys.version}\nEjecutor: agente (ejecución automatizada)\n"]
    codigo = 0
    if sys.argv[1] == "demo":
        with tempfile.TemporaryDirectory() as temporal:
            db = str(Path(temporal) / "demo.db")
            casos = [(["--help"], 0), (["inventario"], 0),
                     (["disponibilidad", "MIC-01", "2026-11-02T10:00", "2026-11-02T11:00"], 0),
                     (["reservar", "MIC-01", "Ana", "2026-11-02T10:00", "2026-11-02T11:00"], 0),
                     (["reservar", "MIC-01", "Juan", "2026-11-02T10:30", "2026-11-02T11:30"], 1),
                     (["reservar", "MIC-01", "María", "2026-11-02T11:00", "2026-11-02T12:00"], 0),
                     (["listar"], 0), (["cancelar", "1"], 0), (["listar"], 0),
                     (["disponibilidad", "MIC-01", "2026-11-02T10:00", "2026-11-02T11:00"], 0)]
            for argumentos, esperado in casos:
                resultado = ejecutar(["app.py", "--db", db, *argumentos])
                partes.append(f"$ python app.py --db <BASE_TEMPORAL> {' '.join(argumentos)}\n"
                              f"{resultado.stdout}{resultado.stderr}Salida: {resultado.returncode}; esperada: {esperado}\n")
                if resultado.returncode != esperado:
                    codigo = 1
    else:
        argumentos = ["-m", "unittest", "discover", "-s", "tests", "-v"]
        resultado = ejecutar(argumentos)
        partes.append("$ python " + " ".join(argumentos) + "\n" + resultado.stdout + resultado.stderr)
        partes.append(f"Salida: {resultado.returncode}\n")
        codigo = resultado.returncode
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text("\n".join(partes), encoding="utf-8")
    print(destino)
    return codigo


if __name__ == "__main__":
    sys.exit(main())
