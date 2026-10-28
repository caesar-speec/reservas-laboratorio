"""Conexión y esquema persistente; nunca elimina reservas al iniciar."""

import sqlite3
from pathlib import Path

DEFAULT_DB = Path(__file__).resolve().parent / "data" / "reservas.db"


def conectar(ruta=DEFAULT_DB):
    ruta = Path(ruta)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    conexion = sqlite3.connect(ruta)
    conexion.row_factory = sqlite3.Row
    conexion.executescript("""
        CREATE TABLE IF NOT EXISTS reservas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            equipo TEXT NOT NULL,
            solicitante TEXT NOT NULL CHECK(length(trim(solicitante)) > 0),
            inicio TEXT NOT NULL,
            fin TEXT NOT NULL CHECK(inicio < fin),
            estado TEXT NOT NULL DEFAULT 'ACTIVA'
                CHECK(estado IN ('ACTIVA', 'CANCELADA'))
        );
        CREATE INDEX IF NOT EXISTS idx_reservas_equipo_estado
            ON reservas(equipo, estado);
    """)
    return conexion
