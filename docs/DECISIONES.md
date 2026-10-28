# Decisiones

| ID | Fecha | Decisión técnica o restricción documentada | Alternativas consideradas | Motivo documentado | Consecuencias previstas o estado comprobado | Fuente | Revisión humana |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D-01 | 2026-10-28 | Utilizar Python, SQLite y unittest | PENDIENTE | Requisito del proyecto en AGENTS.md | La implementación y las pruebas futuras deben respetar esas herramientas; versiones PENDIENTE | [AGENTS.md](../AGENTS.md) | PENDIENTE |
| D-02 | 2026-10-28 | Evitar superposiciones para un mismo equipo y permitir horarios consecutivos | PENDIENTE | Reglas del proyecto en AGENTS.md | La validación futura debe distinguir superposición de límites consecutivos; algoritmo PENDIENTE | [AGENTS.md](../AGENTS.md) | PENDIENTE |
| D-03 | 2026-10-28 | Conservar cancelaciones y persistir datos | PENDIENTE | Reglas del proyecto en AGENTS.md | Se requerirá conservar el estado de cancelación y datos entre ejecuciones; esquema SQLite PENDIENTE | [AGENTS.md](../AGENTS.md) | PENDIENTE |
| D-04 | 2026-10-28 | Inventario JSON con códigos como claves y nombres como valores | PENDIENTE | Motivo de elección del formato: PENDIENTE | El archivo actual representa cinco equipos mediante cinco claves distintas | [inventario.json](../inventario.json), commit 63c0c77 | PENDIENTE |
| D-05 | 2026-10-28 | Mantener módulos Python vacíos en la estructura inicial | PENDIENTE | Instrucción documentada de implementar lógica cuando se solicite | app.py, reservas.py y database.py tienen 0 bytes al inspeccionarlos | [AGENTS.md](../AGENTS.md), [VERIFICACION.md](VERIFICACION.md) | PENDIENTE |
| PENDIENTE | PENDIENTE | Próxima decisión | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE |

La fecha corresponde al registro o constatación en esta documentación; no acredita una reunión o aprobación humana. No se documentaron elecciones de versiones, esquema de base de datos ni algoritmo de reservas.

## Decisiones del desarrollo completo — 2026-10-28

Las filas anteriores describen la etapa inicial: D-05 (módulos vacíos) queda superada por la nueva autorización de implementación. Las versiones y el esquema ya se comprobaron o implementaron según lo siguiente. El análisis de alternativas fue realizado por el agente; no representa una aprobación humana.

| ID | Decisión | Alternativas analizadas por el agente | Motivo | Consecuencias | Origen y revisión |
| --- | --- | --- | --- | --- | --- |
| D-06 | Python, verificado 3.12.10 | Java o JavaScript | Python es obligatorio y permite CLI, SQL y pruebas sin paquetes | Instalación local de Python; no se probaron otras versiones | Requisito del usuario; revisión cerrada por confirmación del usuario del 28/10/2026 |
| D-07 | SQLite para reservas; JSON solo para inventario | Reservas en JSON | SQLite es obligatorio y ofrece transacciones, consultas y persistencia sin servidor | Archivo local data/reservas.db; esquema con estados y clave autoincremental | Requisito; esquema propuesto por agente, revisión cerrada por confirmación del usuario del 28/10/2026 |
| D-08 | CLI argparse | Interfaz gráfica o web | Consigna exige consola; biblioteca estándar reduce instalación | Uso por terminal y salida textual; sin UI gráfica | Requisito; revisión cerrada por confirmación del usuario del 28/10/2026 |
| D-09 | unittest | pytest u otro framework | Consigna y ausencia de dependencias externas | Descubrimiento con python -m unittest discover -s tests -v y bases temporales | Requisito; revisión cerrada por confirmación del usuario del 28/10/2026 |
| D-10 | YYYY-MM-DDTHH:MM estricto, validado por regex y datetime | Formatos flexibles o entrada con segundos | Formato obligatorio; regex exige ancho y datetime valida calendario | Comparación textual SQLite válida tras validar ancho fijo; rechaza offsets y segundos | Requisito; implementación del agente, revisión cerrada por confirmación del usuario del 28/10/2026 |
| D-11 | Horas civiles locales America/Argentina/Cordoba | UTC y conversión con zoneinfo | Consigna usa una única zona y no requiere conversión | Se guardan textos locales sin offset; no se requiere tzdata en Windows. No se resuelven cambios históricos de zona ni horas ambiguas | Requisito de zona; representación propuesta por agente, revisión cerrada por confirmación del usuario del 28/10/2026 |
| D-12 | Permitir pasado y cualquier duración positiva | Prohibir pasado o limitar duración | Consigna explícita | Se pueden probar ejemplos históricos y no hay políticas de anticipación | Requisito; revisión cerrada por confirmación del usuario del 28/10/2026 |
| D-13 | Estados ACTIVA y CANCELADA, cancelar con UPDATE | Borrar filas o moverlas a otra tabla | Conservar datos originales e historial | Canceladas no bloquean; identificadores permanecen; CHECK restringe estados | Requisito; revisión cerrada por confirmación del usuario del 28/10/2026 |
| D-14 | Cancelación inexistente o repetida devuelve error sin cambios | Hacer cancelación repetida silenciosamente idempotente | Distinguir errores de identificación o repetición para el usuario | CLI retorna 1 y explica el caso; ambas situaciones tienen pruebas | Propuesta del agente; revisión cerrada por confirmación del usuario del 28/10/2026 |
| D-15 | Regla compartida en disponible, usada desde reservar | Duplicar consultas o usar límites inclusivos | Evitar divergencia y aceptar intervalos consecutivos | SELECT solo ACTIVA y mismo equipo; predicado estricto < y >; prueba automática de ambos límites | Requisito y adaptación AGENTS; revisión cerrada por confirmación del usuario del 28/10/2026 |
| D-16 | BEGIN IMMEDIATE antes de comprobar e insertar | SELECT e INSERT sin transacción conjunta | Evitar que dos escrituras locales intercalen comprobación y alta | SQLite serializa escritores; error de almacenamiento si hay bloqueo prolongado. No es un sistema distribuido | Propuesta del agente; revisión cerrada por confirmación del usuario del 28/10/2026 |
| D-17 | --db antes del subcomando, ruta predeterminada relativa al código | Ruta fija desde carpeta de trabajo | Separar datos reales de pruebas y funcionar desde otras carpetas | Pruebas/demo usan TEMP; no hay comando destructivo de reinicio | Propuesta del agente; revisión cerrada por confirmación del usuario del 28/10/2026 |
| D-18 | Salida CLI UTF-8 | Depender de codificación regional | La primera ejecución falló con cp932 al imprimir acentos | Salidas redirigidas reproducibles con nombres en español | Corrección observada por agente; revisión cerrada por confirmación del usuario del 28/10/2026 |
| D-19 | Registrar comandos de commit sin ejecutarlos | Crear commits de etapas ya finalizadas | Al formular esta propuesta las revisiones estaban pendientes y no había instantáneas Git separadas; posteriormente el usuario confirmó su cierre | Único commit existente 63c0c77; entrega pendiente de versionar, sin historia ficticia | Propuesta del agente; revisión cerrada por confirmación del usuario del 28/10/2026 |

Fuentes verificables: [AGENTS.md](../AGENTS.md), [reservas.py](../reservas.py), [database.py](../database.py), [tests](../tests/test_reservas.py) y [VERIFICACION.md](VERIFICACION.md).

## Estado actual de revisión — 2026-10-28

Motivo de elección del agente, aportado directamente por el usuario el 28/10/2026: «el motivo principal por el que elegi el agente es que ya tenia su version paga». Se eligió Codex para aprovechar ese acceso existente. No se atribuye una comparación de rendimiento o de precios con otros agentes que el usuario no haya comunicado. La suscripción se utilizó para desarrollar; no es una dependencia de ejecución de la aplicación.

El usuario confirmó: «ya no esta pendiente nada de revision humana». Quedan cerradas las revisiones humanas del proyecto, incluidos los tres episodios. Los PENDIENTE de la tabla inicial son el registro histórico previo al desarrollo, no solicitudes actuales de revisión. No se aportaron motivos técnicos adicionales ni se atribuye al usuario la ejecución de pruebas.
