"""Interfaz de consola del sistema de reservas."""

import argparse
import sqlite3
import sys

from database import DEFAULT_DB, conectar
from reservas import cancelar, disponible, inventario, listar, reservar


def main(argv=None):
    # Mantener los acentos también al redirigir la salida en Windows.
    for flujo in (sys.stdout, sys.stderr):
        if hasattr(flujo, "reconfigure"):
            flujo.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Reservas de equipos de laboratorio")
    parser.add_argument("--db", default=str(DEFAULT_DB), help="Ruta SQLite (por defecto data/reservas.db)")
    comandos = parser.add_subparsers(dest="comando", required=True)
    comandos.add_parser("inventario", help="Consultar equipos")
    consulta = comandos.add_parser("disponibilidad", help="Consultar un intervalo local de Córdoba")
    consulta.add_argument("equipo")
    consulta.add_argument("inicio")
    consulta.add_argument("fin")
    alta = comandos.add_parser("reservar", help="Crear una reserva activa")
    alta.add_argument("equipo")
    alta.add_argument("solicitante")
    alta.add_argument("inicio")
    alta.add_argument("fin")
    comandos.add_parser("listar", help="Historial de reservas activas y canceladas")
    baja = comandos.add_parser("cancelar", help="Cancelar conservando el historial")
    baja.add_argument("id", type=int)
    args = parser.parse_args(argv)
    conexion = None
    try:
        if args.comando == "inventario":
            for codigo, nombre in inventario().items():
                print(f"{codigo}: {nombre}")
        else:
            conexion = conectar(args.db)
            if args.comando == "disponibilidad":
                libre = disponible(conexion, args.equipo, args.inicio, args.fin)
                print("DISPONIBLE" if libre else "NO DISPONIBLE")
            elif args.comando == "reservar":
                identificador = reservar(conexion, args.equipo, args.solicitante, args.inicio, args.fin)
                print(f"Reserva {identificador} creada: ACTIVA")
            elif args.comando == "cancelar":
                cancelar(conexion, args.id)
                print(f"Reserva {args.id} cancelada: CANCELADA")
            elif args.comando == "listar":
                filas = listar(conexion)
                if not filas:
                    print("Sin reservas.")
                for fila in filas:
                    print(f"{fila['id']} | {fila['equipo']} | {fila['solicitante']} | "
                          f"{fila['inicio']} | {fila['fin']} | {fila['estado']}")
        return 0
    except (ValueError, sqlite3.Error, OSError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    finally:
        if conexion is not None:
            conexion.close()


if __name__ == "__main__":
    sys.exit(main())
