# Decisiones

Este registro reúne las decisiones documentadas del proyecto. Las alternativas técnicas fueron analizadas por el agente; las consecuencias previstas se distinguen de los resultados comprobados.

## Decisiones de la estructura inicial — 2026-10-28

| ID | Decisión o restricción | Estado y referencia actual |
| --- | --- | --- |
| D-01 | Utilizar Python, SQLite y unittest | Implementado; versiones y herramientas documentadas en D-06, D-07 y D-09 |
| D-02 | Evitar superposiciones y permitir horarios consecutivos | Implementado con regla compartida y pruebas; véase D-15 |
| D-03 | Conservar cancelaciones y persistir datos | Implementado con SQLite y estados; véanse D-07 y D-13 |
| D-04 | Inventario JSON con códigos como claves y nombres como valores | Conservado en [inventario.json](../inventario.json); cinco unidades identificadas por códigos distintos. No se registró una comparación inicial de formatos |
| D-05 | Mantener módulos vacíos en la estructura inicial | Cumplido en el commit inicial 63c0c77; superado por la autorización posterior de implementar la aplicación |

La fecha corresponde al registro documental. Las revisiones humanas están cerradas por confirmación expresa del usuario, según [DELEGACION.md](DELEGACION.md).

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
| D-19 | Conservar el historial real y versionar el desarrollo acumulado | Crear commits ficticios de etapas ya finalizadas | No había instantáneas Git separadas de cada etapa | Se conservaron 63c0c77 y el commit de implementación 65ee4b5; main fue publicada en GitHub y su acceso público fue comprobado | Publicación autorizada por el usuario; evidencia en [VERIFICACION.md](VERIFICACION.md) |

Fuentes verificables: [AGENTS.md](../AGENTS.md), [reservas.py](../reservas.py), [database.py](../database.py), [tests](../tests/test_reservas.py) y [VERIFICACION.md](VERIFICACION.md).

## Estado actual de revisión — 2026-10-28

Motivo de elección del agente, aportado directamente por el usuario el 28/10/2026: «el motivo principal por el que elegi el agente es que ya tenia su version paga». Se eligió Codex para aprovechar ese acceso existente. No se atribuye una comparación de rendimiento o de precios con otros agentes que el usuario no haya comunicado. La suscripción se utilizó para desarrollar; no es una dependencia de ejecución de la aplicación.

El usuario confirmó el cierre de las revisiones humanas del proyecto, incluidos los tres episodios. La tabla inicial refleja el estado final de sus decisiones. Las comprobaciones aportadas por el usuario y los motivos de aceptación de los tres episodios están registrados en [DELEGACION.md](DELEGACION.md) y [VERIFICACION.md](VERIFICACION.md).
