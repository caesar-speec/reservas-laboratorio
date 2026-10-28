# Especificación de desarrollo completo

Registrada el 28/10/2026 a partir de la consigna adjunta por el usuario. Síntesis de requisitos; no es una transcripción de una conversación. La especificación breve inicial sigue disponible en `git show 63c0c77:README.md`; esta ampliación todavía no está registrada en un nuevo commit.

| ID | Requisito y aceptación |
| --- | --- |
| R01 | Inventario JSON fijo con exactamente MIC-01, MIC-02, OSC-01, MUL-01 y FUE-01 y nombres solicitados |
| R02 | Consulta de disponibilidad por equipo e intervalo con la misma regla de creación |
| R03 | Crear reserva con ID único, equipo, solicitante ficticio, inicio, fin y estado ACTIVA |
| R04 | Rechazar superposición activa para el mismo equipo: inicio_nuevo < fin_existente AND fin_nuevo > inicio_existente |
| R05 | Aceptar límites consecutivos en ambos sentidos |
| R06 | Permitir reservas simultáneas de unidades diferentes |
| R07 | Rechazar equipo desconocido, solicitante vacío/espacios, fechas u horas inválidas e inicio >= fin |
| R08 | Cancelar por ID; conservar datos y estado CANCELADA y liberar el horario |
| R09 | Listar el historial de activas y canceladas |
| R10 | Persistir en data/reservas.db, crear esquema si falta, conservar registros tras reiniciar |
| R11 | Python compatible con 3.12, biblioteca estándar, SQLite, unittest, argparse, JSON, Git y Markdown |
| R12 | YYYY-MM-DDTHH:MM local America/Argentina/Cordoba; sin prohibir pasado ni limitar duración/anticipación |
| R13 | Pruebas con bases temporales, cubrir las reglas y persistencia con procesos separados |
| R14 | AGENTS.md operativo, adaptación de consecutivas aplicada, documentación y tres episodios reales con revisión humana explícita |
| R15 | Preparar entrega, GitHub y borrador de correo Challenge IA; no enviar ni publicar sin autorización |

Fuera de alcance: autenticación, usuarios reales, roles, pagos, nube, APIs, notificaciones, interfaz gráfica/web y concurrencia distribuida. No agregar credenciales ni evidencia inventada. No borrar reservas reales ni reescribir Git. La aplicación no debe depender del agente.

La decisión técnica del agente sobre cancelaciones repetidas es rechazar con mensaje claro sin cambios; está documentada en DECISIONES y cubierta por pruebas. El usuario confirmó el 28/10/2026 el cierre de todas las revisiones humanas de implementación.
