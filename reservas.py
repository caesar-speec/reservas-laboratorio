"""Reglas de reservas. Horas locales de America/Argentina/Cordoba."""

import json
import re
from datetime import datetime
from pathlib import Path

INVENTARIO = Path(__file__).resolve().parent / "inventario.json"
ZONA_HORARIA = "America/Argentina/Cordoba"
FORMATO = "%Y-%m-%dT%H:%M"


def inventario():
    with INVENTARIO.open(encoding="utf-8-sig") as archivo:
        return json.load(archivo)


def validar_intervalo(equipo, inicio, fin):
    if equipo not in inventario():
        raise ValueError(f"Equipo desconocido: {equipo}")
    fechas = []
    for valor in (inicio, fin):
        if not isinstance(valor, str) or not re.fullmatch(
            r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}", valor
        ):
            raise ValueError("Fecha u horario inválido; use YYYY-MM-DDTHH:MM.")
        try:
            fechas.append(datetime.strptime(valor, FORMATO))
        except ValueError:
            raise ValueError("Fecha u horario inválido; use YYYY-MM-DDTHH:MM.") from None
    if fechas[0] >= fechas[1]:
        raise ValueError("El inicio debe ser anterior a la finalización.")


def disponible(conexion, equipo, inicio, fin):
    validar_intervalo(equipo, inicio, fin)
    conflicto = conexion.execute(
        "SELECT 1 FROM reservas WHERE equipo = ? AND estado = 'ACTIVA' "
        "AND ? < fin AND ? > inicio LIMIT 1", (equipo, inicio, fin)
    ).fetchone()
    return conflicto is None


def reservar(conexion, equipo, solicitante, inicio, fin):
    validar_intervalo(equipo, inicio, fin)
    if not isinstance(solicitante, str) or not solicitante.strip():
        raise ValueError("El solicitante no puede estar vacío ni contener solo espacios.")
    # Bloqueo de escritura antes de consultar para evitar comprobación e inserción separadas.
    with conexion:
        conexion.execute("BEGIN IMMEDIATE")
        if not disponible(conexion, equipo, inicio, fin):
            raise ValueError("El equipo ya tiene una reserva activa superpuesta.")
        cursor = conexion.execute(
            "INSERT INTO reservas(equipo, solicitante, inicio, fin) VALUES (?, ?, ?, ?)",
            (equipo, solicitante.strip(), inicio, fin),
        )
        return cursor.lastrowid


def cancelar(conexion, identificador):
    with conexion:
        cursor = conexion.execute(
            "UPDATE reservas SET estado = 'CANCELADA' WHERE id = ? AND estado = 'ACTIVA'",
            (identificador,),
        )
        if cursor.rowcount == 0:
            fila = conexion.execute("SELECT estado FROM reservas WHERE id = ?", (identificador,)).fetchone()
            if fila is None:
                raise ValueError(f"Reserva inexistente: {identificador}")
            raise ValueError(f"La reserva {identificador} ya está cancelada.")


def listar(conexion):
    return [dict(fila) for fila in conexion.execute("SELECT * FROM reservas ORDER BY id")]
