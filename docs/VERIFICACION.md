# Verificación

Registrar resultados solo después de ejecutar el comando correspondiente. Las inspecciones siguientes se ejecutaron el 28/10/2026 en PowerShell; no son pruebas funcionales de la aplicación. No se ejecutó unittest en esta tarea.

| Fecha | Prueba o inspección | Comando | Resultado esperado | Resultado observado | Estado |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Historial disponible | `git log -5 --format=fuller` | Consultar los commits existentes | Se mostró el commit 63c0c77b83650aac9cfcb7c937254e3403c98d5d del 28/10/2026, «Estructura inicial del sistema de reservas» | INSPECCIONADO |
| 2026-10-28 | Archivos registrados | `git ls-tree -r --name-only HEAD` | Identificar la estructura versionada | Diez archivos: siete archivos raíz y data/.gitkeep, docs/.gitkeep y tests/.gitkeep | INSPECCIONADO |
| 2026-10-28 | Tamaño de módulos | `Get-Item app.py,reservas.py,database.py` (consulta de Name y Length) | Comprobar el estado de los módulos | Los tres archivos tienen 0 bytes | INSPECCIONADO |
| 2026-10-28 | Carpetas de datos y pruebas | `Get-ChildItem tests,data -Force` | Identificar archivos existentes | Cada carpeta contiene únicamente .gitkeep | INSPECCIONADO |
| 2026-10-28 | Inventario inicial | `Get-Content inventario.json -Encoding UTF8` | Comprobar los cinco equipos solicitados | MIC-01, MIC-02, OSC-01, MUL-01 y FUE-01 con sus nombres solicitados | INSPECCIONADO |
| 2026-10-28 | Estado previo a los cambios documentales | `git status --short` | Consultar cambios locales | Sin salida | INSPECCIONADO |
| PENDIENTE | Evitar superposición de reservas del mismo equipo | PENDIENTE | Rechazar reservas superpuestas | PENDIENTE | PENDIENTE |
| PENDIENTE | Permitir horarios consecutivos | PENDIENTE | Aceptar una reserva que comienza al terminar otra | PENDIENTE | PENDIENTE |
| PENDIENTE | Conservar cancelaciones | PENDIENTE | Mantener la reserva cancelada y su estado | PENDIENTE | PENDIENTE |
| PENDIENTE | Persistencia entre ejecuciones | PENDIENTE | Recuperar los datos guardados en SQLite | PENDIENTE | PENDIENTE |

Los comandos de pruebas futuras se definirán al implementar la aplicación y las pruebas. Una ejecución sin casos de prueba no acredita el comportamiento del sistema. Evidencias externas o transcripciones conservadas de las inspecciones: PENDIENTE.


## Desarrollo completo: ejecuciones del agente del 28/10/2026

El registro inicial anterior corresponde a cuando los módulos estaban vacíos. Las filas siguientes documentan ejecuciones posteriores reales. Todas fueron realizadas por el agente con Python 3.12.10 (SQLite 3.49.1) en Windows 11. Ninguna constituye aprobación humana.

Comando de suite: `python -m unittest discover -s tests -v`. Como python no está en PATH en este entorno, se invocó el ejecutable temporal mediante `& (Join-Path $env:TEMP 'reservas-python-3.12.10\python.exe')`; PYTHONUTF8=1. El capturador final ejecutó el mismo comando mediante sys.executable y subprocess. Resultado completo: [etapa3.txt](evidencias/etapa3.txt), 21 tests, 0 errores, 0 fallos, salida 0. Los subTest comprueban variantes adicionales; no se cuentan como pruebas independientes.

| Prueba | Requisito | Comando ejecutado | Python | Esperado | Observado | Estado | Fecha | Ejecutor |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Suite inicial | R01, R02, R05 | python -m unittest discover -s tests -v | 3.12.10 | Inventario y disponibilidad correctos | 3 tests, OK, evidencia etapa1.txt | APROBADA | 2026-10-28 | Agente |
| Suite etapa 2 | R03 a R07, R12 | python -m unittest discover -s tests -v | 3.12.10 | Creación y validaciones correctas | 13 tests, OK, evidencia etapa2.txt | APROBADA | 2026-10-28 | Agente |
| test_inventario_exacto | R01 | Suite final | 3.12.10 | Cinco IDs y nombres exactos | ok | APROBADA | 2026-10-28 | Agente |
| test_disponibilidad_inicial | R02 | Suite final | 3.12.10 | Intervalo vacío disponible | ok | APROBADA | 2026-10-28 | Agente |
| test_disponibilidad_limites_y_conflicto | R02, R04, R05 | Suite final | 3.12.10 | Límites libres y cruce ocupado | ok | APROBADA | 2026-10-28 | Agente |
| test_reserva_valida | R03 | Suite final | 3.12.10 | Fila con ID y datos esperados ACTIVA | ok | APROBADA | 2026-10-28 | Agente |
| test_superposiciones | R04 | Suite final | 3.12.10 | Rechazo en igualdad, cruces y contención sin insertar | ok | APROBADA | 2026-10-28 | Agente |
| test_consecutivas_disponibilidad_y_creacion | R02, R05 | Suite final | 3.12.10 | Disponibilidad y alta aceptan ambos límites | ok | APROBADA | 2026-10-28 | Agente |
| test_unidades_distintas | R06 | Suite final | 3.12.10 | MIC-01 y MIC-02 simultáneos aceptados | ok | APROBADA | 2026-10-28 | Agente |
| test_equipo_desconocido | R07 | Suite final | 3.12.10 | Rechazo en consulta y alta | ok | APROBADA | 2026-10-28 | Agente |
| test_solicitantes_invalidos | R07 | Suite final | 3.12.10 | Vacío y espacios rechazados | ok | APROBADA | 2026-10-28 | Agente |
| test_fechas_invalidas | R07, R12 | Suite final | 3.12.10 | Calendario y formato inválidos rechazados en ambos extremos | ok | APROBADA | 2026-10-28 | Agente |
| test_inicio_igual_fin | R07 | Suite final | 3.12.10 | Intervalo vacío rechazado | ok | APROBADA | 2026-10-28 | Agente |
| test_inicio_posterior_fin | R07 | Suite final | 3.12.10 | Intervalo invertido rechazado | ok | APROBADA | 2026-10-28 | Agente |
| test_fechas_pasadas_y_duracion_sin_limites | R12 | Suite final | 3.12.10 | Pasado y duración larga aceptados | ok | APROBADA | 2026-10-28 | Agente |
| test_cancelacion_conserva_datos | R08 | Suite final | 3.12.10 | Solo cambia el estado | ok | APROBADA | 2026-10-28 | Agente |
| test_cancelacion_libera_horario | R08 | Suite final | 3.12.10 | Nueva reserva mismo intervalo con nuevo ID | ok | APROBADA | 2026-10-28 | Agente |
| test_cancelacion_inexistente | R08 | Suite final | 3.12.10 | Error claro | ok | APROBADA | 2026-10-28 | Agente |
| test_cancelacion_repetida | R08 | Suite final | 3.12.10 | Error sin cambios | ok | APROBADA | 2026-10-28 | Agente |
| test_historial_ambos_estados | R09 | Suite final | 3.12.10 | Cancelada y activa visibles | ok | APROBADA | 2026-10-28 | Agente |
| test_reabrir_conserva_activa_y_cancelada | R10 | Suite final | 3.12.10 | Misma lista tras cerrar y reabrir | ok | APROBADA | 2026-10-28 | Agente |
| test_persistencia_procesos_separados | R10, R13 | Suite final | 3.12.10 | Alta, consulta, cancelación y disponibilidad entre procesos | ok | APROBADA | 2026-10-28 | Agente |
| test_cli_error_y_ayuda | R07, R11 | Suite final | 3.12.10 | Mensajes y códigos 0/1/2 según operación | ok | APROBADA | 2026-10-28 | Agente |
| Demo de comandos y reinicio | R01 a R05, R08 a R10 | python tests/registrar_evidencia.py demo | 3.12.10 | Diez procesos con resultados y códigos esperados | Todos coinciden; ACTIVA recuperada y CANCELADA recuperada tras procesos previos | APROBADA | 2026-10-28 | Agente |
| Ejecución funcional independiente por una persona | R01 a R15 | No informado | No informado | Evidencia de ejecución independiente | Sin ejecución documentada; la revisión humana está cerrada por confirmación del usuario | NO EJECUTADA | Sin fecha de ejecución informada | Humano |

«Suite final» en cada fila significa exactamente el comando de suite indicado al comienzo. Evidencias: [etapa1](evidencias/etapa1.txt), [etapa2](evidencias/etapa2.txt), [etapa3](evidencias/etapa3.txt) y [demo](evidencias/demo.txt). Las dos primeras contienen mensajes de PowerShell al capturar stderr; unittest terminó OK. No son casos de prueba fallidos. Sí se observó un fallo real de codificación al ejecutar inventario antes de la corrección UTF-8, registrado en PROGRESO.md; la ejecución posterior fue correcta.

### Persistencia reproducible

1. Ejecutar `python tests/registrar_evidencia.py demo` desde la raíz.
2. El script crea una base temporal independiente y lanza un proceso nuevo para cada comando. No modifica data/reservas.db.
3. Un proceso crea la reserva 1; otro crea la reserva 2 consecutiva; un proceso listar recupera ambas ACTIVA.
4. Un proceso cancelar cambia la reserva 1; otro listar recupera CANCELADA y ACTIVA con los datos originales.
5. Un proceso disponibilidad verifica que el intervalo cancelado está libre.
6. El script compara códigos de salida y guarda la salida real. La suite test_persistencia.py además hace aserciones sobre los contenidos y comprueba reapertura de conexión.

Resultado observado: la transcripción demo.txt contiene las dos reservas tras procesos separados y la liberación del intervalo; la prueba automática entre procesos pasó. No se verificó un reinicio del sistema operativo; se verificó el cierre y nueva ejecución de la aplicación según la consigna.

### Cobertura documental y entrega

| Requisito | Evidencia | Estado real |
| --- | --- | --- |
| R11 herramientas obligatorias | app.py, database.py, reservas.py, tests/ y versiones observadas | Implementado, sin paquetes externos |
| R14 agente y adaptación | AGENTS.md, README.md, DELEGACION.md y prueba de consecutivas | Tres episodios ejecutados; revisión humana cerrada por confirmación del usuario |
| R15 entrega | ENTREGA.md | Instrucciones y borrador preparados; publicación, acceso y envío NO EJECUTADOS |
| Evolución versionada | git log --oneline | Solo 63c0c77 existe; cambios actuales aún sin commit |

El usuario confirmó el cierre de las revisiones humanas el 28/10/2026. La publicación y el registro de cambios en Git siguen sin acreditarse; no se atribuyen pruebas humanas no documentadas.

### Cierre de verificación del agente — 2026-10-28

| Prueba | Requisito | Comando | Python | Esperado | Observado | Estado | Fecha | Ejecutor |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Reejecución final de la suite | R01 a R13 | python tests/registrar_evidencia.py final (ejecuta python -m unittest discover -s tests -v) | 3.12.10 | Todos los casos correctos | 21 aprobadas, 0 fallidas, salida 0; [final.txt](evidencias/final.txt) | APROBADA | 2026-10-28 | Agente |
| Enlaces locales y secciones README | R14 | Inspección PowerShell con regex de enlaces y encabezados; Test-Path de cada destino | No aplica | Destinos existentes y cuatro secciones | Todos los destinos existentes; cuatro secciones con nombres solicitados | APROBADA | 2026-10-28 | Agente |
| Espacios y exclusiones de Git | R15 | git diff --check; git check-ignore data/reservas.db data/reservas.db-wal __pycache__/app.cpython-312.pyc | No aplica | Sin errores de espacios; archivos generados ignorados | Sin errores; tres rutas ignoradas; advertencias normales LF/CRLF | APROBADA | 2026-10-28 | Agente |

Revisión de patrones de secretos: no se encontraron coincidencias de claves privadas, tokens ghp_ o claves AKIA en la búsqueda realizada; alcance limitado, sin afirmar una auditoría completa. Estado de datos reales: data/ contiene solamente .gitkeep. El código, las pruebas y la demo no requieren servicios de IA.

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

## Limpieza de DECISIONES.md — 2026-10-28

Por solicitud del usuario se eliminaron los marcadores de pendientes y la fila vacía de decisiones futuras en DECISIONES.md. Se resumieron las decisiones iniciales con referencias a su implementación final, se actualizó el estado de versionado/publicación y se corrigió la referencia a las comprobaciones humanas ya aportadas. No se inventaron comparaciones ni aprobaciones. Trabajo documental del agente principal, sin subagentes. Verificación: búsqueda de marcadores y git diff --check; no corresponde repetir pruebas funcionales al no cambiar código. No se solicita una nueva aceptación humana.
