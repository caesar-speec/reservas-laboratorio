# Progreso

Fechas expresadas según America/Buenos_Aires. Registrar nuevas tareas al final y enlazar evidencia reproducible. Una inspección de archivos no equivale a una prueba funcional.

| Fecha | Tarea | Cambios o estado comprobado | Resultado | Evidencia | Revisión humana |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Estructura inicial registrada en Git | Tres archivos Python vacíos, inventario de cinco equipos, AGENTS.md, README.md, .gitignore y carpetas con .gitkeep | Commit existente con mensaje «Estructura inicial del sistema de reservas» | `git show --stat 63c0c77b83650aac9cfcb7c937254e3403c98d5d` | PENDIENTE |
| 2026-10-28 | Inspección previa a la documentación | Lectura de instrucciones, README e inventario; consulta del historial y archivos | Archivos Python de 0 bytes; tests/ y data/ solo contienen .gitkeep; git status --short sin salida al iniciar esta tarea | Comandos y observaciones en [VERIFICACION.md](VERIFICACION.md) | PENDIENTE |
| 2026-10-28 | Preparación de documentación | Actualización de README y creación de PROGRESO, DELEGACION, VERIFICACION y DECISIONES | Documentos preparados; campos sin evidencia marcados PENDIENTE | Archivos en docs/ y `git diff -- README.md`; archivos nuevos visibles mediante `git status --short` | PENDIENTE |
| PENDIENTE | Próxima tarea | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE |

No se ejecutaron pruebas funcionales durante esta tarea documental. No se creó un commit como parte de esta tarea.

## Desarrollo completo — 2026-10-28

Inspección: único commit existente 63c0c77; se conservaron cambios documentales locales sin commit. Los módulos seguían vacíos. Se recibió autorización para implementar el sistema completo por tres etapas. No hay remoto Git configurado. El comando python no está disponible en PATH; se está buscando un intérprete compatible antes de ejecutar pruebas. Revisión humana de las etapas: PENDIENTE.

### Etapa 1 en desarrollo — 2026-10-28

Se actualizaron AGENTS.md, database.py, reservas.py, app.py y tests/test_reservas.py: inventario, esquema no destructivo, validación estricta y disponibilidad con límites consecutivos. Se agregó --db para aislar demostraciones y pruebas. Pruebas iniciales escritas; ejecución pendiente mientras se prepara Python. La descarga inicial fue bloqueada por red; se solicitó escalamiento para descargar Python embebido oficial a TEMP, sin cambiar la configuración del sistema. Commit propuesto: feat: inventario y disponibilidad con SQLite. No creado.

### Etapa 2 — 2026-10-28

Se implementó reservar en reservas.py y app.py con transacción BEGIN IMMEDIATE, parámetros SQL y validaciones. Se ampliaron tests/test_reservas.py para conflictos, límites consecutivos, unidades distintas, solicitantes y fechas inválidos y fechas pasadas. Se aplicó la adaptación específica de AGENTS.md mediante la misma función disponible para consulta e inserción. Commit propuesto: feat: reservas y validaciones compartidas. No creado. Revisión humana: PENDIENTE.

### Etapa 3 — 2026-10-28

Se agregaron cancelar y listar en reservas.py y app.py, pruebas de cancelación en tests/test_reservas.py y tests/test_persistencia.py. Se creó tests/registrar_evidencia.py para capturar salidas sin el envoltorio de stderr de PowerShell. Resultado real: 21 pruebas aprobadas, 0 fallidas; demo de 10 comandos con códigos de salida esperados en procesos separados. Base de datos temporal: no se tocaron reservas del usuario. Evidencias: docs/evidencias/etapa3.txt y demo.txt. Commit propuesto: feat: cancelaciones historial y pruebas de persistencia. No creado.

El usuario indicó «Pendiente de revisar» para los episodios 1 y 2. No se registró aceptación. Se presentó el episodio 3 para revisión; decisión PENDIENTE.

### Incidencias verificadas y correcciones — 2026-10-28

- python y py no disponibles en PATH: se descargó Python embebido 3.12.10 desde python.org a TEMP mediante el escalamiento solicitado. Se añadió la ruta del proyecto al archivo python312._pth de ese runtime temporal; no se cambió PATH global.
- El primer comando inventario falló al imprimir Multímetro con codificación cp932. Se configuraron stdout y stderr UTF-8 en app.py y se comprobó nuevamente el inventario completo.
- Las suites de etapas 1 y 2 pasaron (3 y 13 casos); las capturas de PowerShell incluyen NativeCommandError porque unittest escribe en stderr. No se interpretó ese envoltorio como fallo de prueba: los resultados terminan en OK. Las capturas originales se conservan. La captura final usa subprocess y guarda salida y código reales en UTF-8.
- No fallaron casos unittest en las ejecuciones realizadas. No se afirma revisión humana ni publicación en GitHub.

### Verificación final y preparación de entrega — 2026-10-28

Se completaron README.md (exactamente cuatro secciones principales), AGENTS.md, DELEGACION.md, VERIFICACION.md y DECISIONES.md y se agregaron ESPECIFICACION.md y ENTREGA.md. Este último incluye comandos de Git/publicación y borrador de correo «Challenge IA» sin enviar. No se borraron archivos previos. El usuario respondió «Pendiente de revisar» también para el episodio 3; las tres revisiones siguen pendientes.

Se ejecutó otra vez la suite completa mediante tests/registrar_evidencia.py final: 21 aprobadas, 0 fallidas, salida 0; evidencia docs/evidencias/final.txt. Se comprobaron todos los enlaces locales de los documentos y los cuatro encabezados principales del README. git diff --check terminó sin errores de espacios (Git advierte normalización LF/CRLF). git check-ignore confirmó exclusión de data/reservas.db, su WAL y caché Python. data/ sigue con solo .gitkeep: no se generó una base real de usuario.

Una búsqueda de patrones de claves privadas, tokens ghp_ y claves AKIA no encontró coincidencias en los archivos revisados; es una revisión limitada de patrones, no una garantía de auditoría exhaustiva. No se agregaron secretos ni datos de estudiantes.

Las evidencias de etapas 1 y 2 se recodificaron a UTF-8 conservando su contenido original, incluidos los avisos de PowerShell. No se reconstruyeron salidas ni resultados pasados.

Entorno consultado: Windows-11-10.0.26200-SP0, PowerShell 5.1.26100.9711, Git 2.51.0.windows.1, Python 3.12.10 AMD64, SQLite 3.49.1. Versión de la aplicación Codex e identificador exacto del modelo: no disponibles por las herramientas consultadas.

Pendientes de entrega: revisión humana de los tres episodios y justificación; comprobación independiente del usuario; commit del estado final, publicación autorizada, verificación de acceso y envío humano del correo. No hay defectos funcionales conocidos después de las pruebas, pero no se declara aceptación total. Único commit existente: 63c0c77b83650aac9cfcb7c937254e3403c98d5d. No se hicieron commits nuevos, push ni cambios de historial.

## Cierre de revisiones humanas — 2026-10-28

El usuario indicó expresamente: «ya no esta pendiente nada de revision humana». Esta confirmación cierra las revisiones de los tres episodios y de la documentación del proyecto; sustituye el estado pendiente registrado en las entradas anteriores, que se conservan como historial. Se actualizaron README.md, DELEGACION.md, VERIFICACION.md, DECISIONES.md, ESPECIFICACION.md y ENTREGA.md.

No se atribuyen al usuario comandos, pruebas, resultados ni justificaciones técnicas que no haya comunicado. No se ejecutaron pruebas nuevas porque el cambio es documental. El cierre de revisión no implica que se hayan creado commits, publicado el repositorio o enviado el correo; esas acciones siguen sin realizarse por el agente.

### Revisión contra PDF — 2026-10-28
Se contrastaron las tres páginas de challenge-agents.pdf con el proyecto. Suite reejecutada: 21 pruebas OK, salida 0; Git conserva solo el commit inicial y no tiene remoto. Informe: [REVISION_PDF.md](REVISION_PDF.md). Se añadieron registros de revisión sin modificar la implementación. Aceptación humana de esta revisión: PENDIENTE; no se presume aceptación ni se alteran cierres históricos.


## Correcciones documentales solicitadas — 2026-10-28

Se corrigieron en ESPECIFICACION.md el título y las cadenas README.md, FUE-01, ACTIVA, CANCELADA, YYYY-MM-DDTHH:MM y AGENTS.md. Se documentó en README.md y DECISIONES.md el motivo comunicado directamente por el usuario para elegir Codex: ya contaba con su versión paga.

Las comprobaciones técnicas disponibles son las pruebas y salidas ejecutadas por el agente, enlazadas por episodio en DELEGACION.md. Se solicitó al usuario qué revisó personalmente, qué observó y por qué aceptó cada episodio. Los detalles adicionales siguen pendientes de respuesta real; no se convierten los resultados del agente en comprobaciones humanas. Se conserva el cierre histórico informado.

Cambios solo documentales: no se repitió la suite funcional. La revisión inmediatamente anterior ejecutó 21 pruebas, todas OK. No se publicaron cambios ni se enviaron mensajes externos.

## Evidencia aportada por el usuario — 2026-10-28

Fuente: [transcripción de terminal aportada por el usuario](evidencias/revision-humana.txt), quien indicó «hize estas pruebas». El agente leyó la transcripción; no se atribuye su ejecución al agente ni se infiere aceptación humana adicional.

- Suite: `python -m unittest discover -s tests -v`, 21 casos enumerados en ok y resumen `Ran 21 tests in 2.726s`, `OK`. El pegado contiene también otro resumen de 21 pruebas en 1.772s sin comando separado; no se cuenta como una segunda ejecución acreditada. La versión del intérprete del comando python no figura en la salida.
- Episodio 1: inventario manual con las cinco unidades correctas; consulta de MIC-01 de 10:00 a 11:00 devuelve NO DISPONIBLE y concuerda con la reserva 4 ACTIVA mostrada en el listado. La suite ejecutada por el usuario cubre inventario y disponibilidad.
- Episodio 2: las altas de MIC-01 de 10:00 a 11:00 y de 10:30 a 11:30, de MIC-01 de 11:00 a 12:00 y de MIC-02 de 10:00 a 11:00 fueron rechazadas por superposición. El listado final muestra reservas activas 4, 2 y 3 en esos horarios: la base ya tenía datos. Por tanto, esta secuencia manual no demuestra nuevas altas consecutivas ni en unidades distintas; esos comportamientos sí están cubiertos por los tests correspondientes que el usuario ejecutó en OK.
- Episodio 3: cancelar 1 informa que ya está cancelada. El listado conserva la reserva 1 CANCELADA y las reservas 2, 3 y 4 ACTIVA; una nueva terminal muestra los mismos cuatro registros. Se acredita conservación del historial y persistencia entre ejecuciones. El horario de 10:00 a 11:00 sigue ocupado por la reserva 4 ACTIVA; no es evidencia de que una cancelada bloquee. La cancelación nueva y liberación aislada no se demostraron en esta secuencia manual; sus pruebas automáticas ejecutadas por el usuario dieron OK.

Estos resultados aportan comprobaciones humanas reales a los tres episodios. Explican técnicamente los resultados observados, pero no sustituyen el motivo personal de aceptación del usuario. Se conserva el cierre histórico registrado; no se inventa una nueva decisión ni una justificación personal. No hace falta borrar datos: para repetir altas desde cero se puede elegir otra ruta SQLite todavía inexistente.

## Aceptación humana de los tres episodios — 2026-10-28

El usuario confirmó expresamente «si ya podes hacerlo» ante la propuesta de registrar esta decisión: «Acepto los tres episodios porque las 21 pruebas pasaron, el inventario es correcto y comprobé que el historial se conserva al abrir otra terminal. Entiendo que los rechazos manuales ocurrieron porque la base ya tenía reservas».

Evidencia de las comprobaciones: [salida de terminal aportada por el usuario](evidencias/revision-humana.txt). La decisión se vincula con la implementación actual y sus pruebas en app.py, reservas.py, database.py y tests/; no se atribuye un commit final todavía inexistente.

| Episodio | Decisión humana y motivo confirmado | Comprobación real que la sustenta |
| --- | --- | --- |
| 1: Inventario y disponibilidad | Aceptar: inventario correcto y suite aprobada | Cinco unidades mostradas; disponibilidad ocupada coherente con la reserva activa 4; tests de inventario y disponibilidad en OK |
| 2: Creación y validaciones | Aceptar: las 21 pruebas pasaron y los rechazos manuales se explican por las reservas existentes | Tests de creación válida, superposición, consecutivas, unidades distintas y entradas inválidas en OK; la secuencia manual sobre una base ya poblada no acredita nuevas altas exitosas |
| 3: Cancelación y persistencia | Aceptar: historial conservado al abrir otra terminal y suite aprobada | Mismos cuatro registros y estados en ambas terminales; tests de cancelación, liberación y persistencia en OK; no se atribuye una cancelación manual nueva exitosa |

Queda completado el requisito de motivos y comprobaciones humanas de los tres episodios. Esta aceptación es posterior a las comprobaciones aportadas; no altera los resultados ni crea revisiones retrospectivas ficticias. Los pendientes de commit, publicación y entrega son independientes.

## Preparación de versionado y publicación autorizada — 2026-10-28

El usuario solicitó guardar el estado final en Git, publicar y verificar acceso. Suite reejecutada antes del commit: 21 pruebas OK, salida 0, mediante Python temporal 3.12.10. Rama main; sin remoto configurado al iniciar. Se excluyen tmp/ y las bases SQLite. Se prepara un único commit del estado acumulado, sin simular commits históricos. Publicación y comprobación de acceso todavía no ejecutadas: se solicitó conexión de GitHub. El envío de correo sigue fuera de esta acción.

## Estado actualizado de Git — 2026-10-28

Se creó realmente el commit `65ee4b5` en main, «feat: sistema local de reservas con pruebas y documentacion», con la implementación, pruebas y documentación final. El commit inicial 63c0c77 se conserva. Las afirmaciones anteriores sobre cambios sin commit describen el estado previo y quedan superadas por este registro.

Verificación previa: 21 pruebas OK. La revisión del índice incluyó todos los archivos nuevos; git diff --cached --check detectó espacios finales y líneas vacías en las transcripciones originales etapa1.txt y etapa2.txt, conservadas sin alterar. No se incluyeron bases SQLite, cachés ni tmp/.

Publicación: todavía no ejecutada. No hay remoto configurado y se requiere conexión de GitHub para crear o seleccionar el repositorio y verificar acceso. No se envió correo. La evidencia humana posterior está en evidencias/revision-humana.txt y su aceptación consta en DELEGACION.md; las menciones históricas a falta de pruebas humanas ya están superadas.

## Continuación de publicación — 2026-10-28

El usuario proporcionó y autorizó el destino https://github.com/caesar-speec/reservas-laboratorio. Se comprobó mediante git ls-remote que el remoto no tenía referencias y se configuró origin con esa URL. Historial local conservado: 63c0c77, 65ee4b5 y 70a8045. Trabajo realizado por el agente principal, sin subagentes. Se prepara la publicación de main; su resultado se registrará después de ejecutar el push. No se repitieron pruebas funcionales porque no cambió el código. No se envió correo ni se infirió una nueva aceptación humana.

Resultado real del intento: git push -u origin main fue rechazado por GitHub con «Invalid username or token» y «Authentication failed». No se publicó ningún commit. Se inició git credential-manager github login --username caesar-speec --device --force; requiere completar la autenticación por el usuario. La conexión del conector GitHub no autentica automáticamente el cliente Git local. Publicación y comprobación de acceso continúan pendientes; commit documental local a7f13c2.

## Publicación completada — 2026-10-28

La autenticación oficial de Git terminó con salida 0. El reintento de git push -u origin main terminó con salida 0 y creó main en GitHub, siguiendo origin/main. git ls-remote confirmó a7f13c28e8f428b8c27df7c923c1ec34b78b0ad1. Una solicitud HTTP nueva sin credenciales a https://github.com/caesar-speec/reservas-laboratorio devolvió 200 y contenido con el nombre del repositorio: acceso público comprobado. Se publica este cierre documental mediante un commit adicional, sin reescribir historial. No se repitió la suite por cambios exclusivamente documentales. No se envió correo; su revisión y envío continúan pendientes del titular. Las aceptaciones humanas anteriores se conservan sin atribuir nuevas decisiones.
