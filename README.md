# reservas-laboratorio

## Especificación breve

Un laboratorio necesita asignar cinco unidades físicas sin duplicar sus horarios. Este prototipo local permite consultar inventario y disponibilidad, reservar, cancelar y consultar historial. Funciona sin cuentas, modelos de IA ni conexión a Internet. Inventario fijo: [inventario.json](inventario.json).

Requisitos y criterios de aceptación:

- Mostrar MIC-01, MIC-02, OSC-01, MUL-01 y FUE-01, con sus nombres.
- Crear reservas con identificador único, equipo, solicitante ficticio, inicio, fin y estado ACTIVA.
- Rechazar conflictos activos del mismo equipo usando `inicio_nuevo < fin_existente AND fin_nuevo > inicio_existente`. Compartir la regla entre disponibilidad y creación.
- Aceptar intervalos consecutivos y reservas simultáneas en equipos distintos.
- Rechazar equipo desconocido, solicitante vacío o con solo espacios, fechas/horas inválidas e inicio mayor o igual a fin.
- Cancelar conservando todos los datos originales, cambiando solo el estado a CANCELADA y liberando el intervalo.
- Mostrar reservas activas y canceladas y recuperarlas después de reiniciar.

Supuestos: entrada estricta `YYYY-MM-DDTHH:MM`, interpretada como hora local de `America/Argentina/Cordoba`. Se permiten fechas pasadas y no se limita duración ni anticipación. Cada código es una unidad física distinta. No se administran cambios de inventario.

Alcance: uso local por consola; sin autenticación, nube, notificaciones ni interfaz gráfica. Criterios técnicos comprobados en [VERIFICACION.md](docs/VERIFICACION.md); revisión humana cerrada por confirmación del usuario el 28/10/2026.

Evolución: el commit existente `63c0c77b83650aac9cfcb7c937254e3403c98d5d` conserva la estructura y especificación breve inicial. Puede consultarse con `git show 63c0c77:README.md`. La consigna posterior autorizó implementar el sistema; su síntesis está en [ESPECIFICACION.md](docs/ESPECIFICACION.md). La implementación final quedó registrada en el commit `65ee4b5`; [PROGRESO.md](docs/PROGRESO.md) registra las etapas. No se atribuyen commits futuros a hechos ya versionados.

## Solución

Tecnologías: biblioteca estándar de Python, SQLite, argparse, JSON y unittest. Verificado en Windows 11 con Python 3.12.10 y SQLite 3.49.1; otras versiones no se probaron. No requiere pip ni paquetes externos.

Arquitectura: `app.py` interpreta comandos y presenta resultados; `reservas.py` valida y aplica las reglas; `database.py` crea y conecta el esquema sin borrar datos. La inserción toma una transacción `BEGIN IMMEDIATE` antes de comprobar conflictos. Se usan parámetros SQL.

```text
reservas-laboratorio/
├── app.py
├── reservas.py
├── database.py
├── inventario.json
├── AGENTS.md
├── README.md
├── .gitignore
├── data/.gitkeep
├── tests/
│   ├── .gitkeep
│   ├── test_reservas.py
│   ├── test_persistencia.py
│   └── registrar_evidencia.py
└── docs/
    ├── .gitkeep
    ├── PROGRESO.md
    ├── DELEGACION.md
    ├── VERIFICACION.md
    ├── DECISIONES.md
    ├── ESPECIFICACION.md
    ├── ENTREGA.md
    └── evidencias/
```

Preparación en Windows 11 desde VS Code:

1. Instalar Python 3.12 si no está disponible y habilitar su acceso en PATH. Reiniciar la terminal tras instalarlo. Git es necesario para versionar y publicar, no para ejecutar la aplicación.
2. Abrir la carpeta raíz del repositorio y una terminal PowerShell.
3. Comprobar `python --version` y `git --version`.
4. Ejecutar `python app.py --help` y `python app.py inventario`.
5. Ejecutar `python app.py listar`: crea automáticamente `data/reservas.db` y las tablas si faltan. No elimina reservas existentes. El comando inventario no necesita abrir la base.

En esta sesión no había Python en PATH. Para verificar se descargó Python embebido oficial 3.12.10 en una carpeta temporal; el comando equivalente usado desde PowerShell es:

```powershell
$pythonReservas = Join-Path $env:TEMP 'reservas-python-3.12.10\python.exe'
& $pythonReservas app.py --help
& $pythonReservas -m unittest discover -s tests -v
```

Ese runtime temporal tiene la ruta de este repositorio agregada a `python312._pth`; no se distribuye con el proyecto ni sustituye la instalación normal indicada arriba. Si se elimina TEMP, instalar Python antes de reproducir.

Comandos disponibles, desde la raíz:

```powershell
python app.py --help
python app.py inventario
python app.py disponibilidad MIC-01 2026-11-02T10:00 2026-11-02T11:00
python app.py reservar MIC-01 "Ana" 2026-11-02T10:00 2026-11-02T11:00
python app.py listar
python app.py cancelar 1
```

`--db RUTA` permite seleccionar otra base y debe escribirse antes del subcomando, por ejemplo `python app.py --db data/demo.db listar`. La ruta predeterminada se resuelve respecto del archivo del proyecto, independientemente de la carpeta de ejecución. Una ruta personalizada relativa se resuelve desde la terminal.

Ejemplos de salidas realmente observadas en una base temporal nueva; los identificadores dependen de los datos existentes:

```text
reservar MIC-01 Ana 2026-11-02T10:00 2026-11-02T11:00
Reserva 1 creada: ACTIVA

reservar MIC-01 Juan 2026-11-02T10:30 2026-11-02T11:30
Error: El equipo ya tiene una reserva activa superpuesta.

reservar MIC-01 María 2026-11-02T11:00 2026-11-02T12:00
Reserva 2 creada: ACTIVA

cancelar 1
Reserva 1 cancelada: CANCELADA

listar
1 | MIC-01 | Ana | 2026-11-02T10:00 | 2026-11-02T11:00 | CANCELADA
2 | MIC-01 | María | 2026-11-02T11:00 | 2026-11-02T12:00 | ACTIVA
```

La transcripción completa con comandos está en [demo.txt](docs/evidencias/demo.txt). Cancelar una reserva inexistente o ya cancelada devuelve un error claro sin modificar el historial. Los códigos de salida son 0 para operaciones correctas (incluida consulta NO DISPONIBLE), 1 para errores de negocio/almacenamiento y 2 para argumentos inválidos.

Persistencia: `data/reservas.db`. No hay comando de reinicio ni borrado automático. No borrar ese archivo si se necesita conservar el historial; `.gitignore` excluye las bases generadas y sus auxiliares.

Pruebas reproducibles:

```powershell
python -m unittest discover -s tests -v
python tests/registrar_evidencia.py demo
```

La suite usa únicamente bases temporales y ejecuta procesos separados para verificar la persistencia. La demo también usa una base temporal que se elimina al terminar y guarda la salida en `docs/evidencias/demo.txt`. Última suite ejecutada: 21 pruebas, 21 aprobadas, 0 fallidas. Evidencia y correspondencia con requisitos en [VERIFICACION.md](docs/VERIFICACION.md).

Limitaciones: prototipo con horas civiles locales, sin conversión entre zonas ni interpretación de offsets, sin gestión de inventario y sin mecanismos de producción distribuidos. No quedan funcionalidades obligatorias pendientes según las comprobaciones del agente; la revisión humana está cerrada; la implementación está registrada en `65ee4b5` y la publicación está disponible en https://github.com/caesar-speec/reservas-laboratorio (acceso público comprobado el 28/10/2026).

## Preparación del agente

Se eligió Codex principalmente porque el autor ya contaba con su versión paga, según su declaración del 28/10/2026. Esto permitió utilizar el acceso que ya tenía disponible para el trabajo. Su función fue inspeccionar y modificar el repositorio, ejecutar pruebas y documentar resultados; la aplicación resultante no necesita esa suscripción.

Agente: Codex; versión de la aplicación e identificador exacto del modelo no expuestos por las herramientas utilizadas: NO DISPONIBLES. No se presume un identificador. Entorno observado: Windows 11 (10.0.26200), PowerShell 5.1.26100.9711, Git 2.51.0.windows.1, Python 3.12.10 temporal y SQLite 3.49.1.

Contexto consultado: la consigna adjunta, [AGENTS.md](AGENTS.md), README, inventario, documentos previos, estructura y Git. No se incorporaron credenciales, conversaciones privadas completas ni datos personales de estudiantes. No se inspeccionó contenido de bases reales; la evidencia usa Ana, Juan y María como nombres ficticios.

Herramientas: ejecución de comandos PowerShell, edición mediante apply_patch y archivos, Git de lectura, Python/unittest/subprocess y solicitudes de revisión en el chat. No se usaron subagentes ni servicios de IA en la aplicación. Permisos: lectura del entorno, escritura del repositorio y TEMP, red restringida. La descarga oficial de Python requirió una solicitud de escalamiento y luego se ejecutó correctamente. No se modificó PATH global, no se publicó ni se envió correo.

Adaptación específica configurada en [AGENTS.md](AGENTS.md): «Una reserva que comienza exactamente cuando termina otra no debe considerarse superpuesta. La disponibilidad y la creación deben compartir esta regla. Debe existir una prueba automática que demuestre este comportamiento». Se aplicó usando `disponible` desde `reservar` en [reservas.py](reservas.py), y se demostró con `test_consecutivas_disponibilidad_y_creacion` en [test_reservas.py](tests/test_reservas.py).

Los avances se registraron durante las etapas en [PROGRESO.md](docs/PROGRESO.md). Evidencias de ejecuciones: [etapa1](docs/evidencias/etapa1.txt), [etapa2](docs/evidencias/etapa2.txt), [etapa3](docs/evidencias/etapa3.txt) y [demo](docs/evidencias/demo.txt). El usuario confirmó el 28/10/2026 que ya no queda ninguna revisión humana pendiente. Posteriormente el usuario aportó una ejecución de la suite de 21 pruebas en OK y una comprobación manual de inventario e historial persistente; sus resultados y límites están registrados en [VERIFICACION.md](docs/VERIFICACION.md) y [la transcripción](docs/evidencias/revision-humana.txt).

## Registro de decisiones y delegación

[DECISIONES.md](docs/DECISIONES.md) compara tecnologías y registra motivos y consecuencias: Python para simplicidad local, SQLite para transacciones y persistencia, consola para evitar dependencias, unittest por estar incluido. También registra formato de fechas, zona, fechas pasadas, cancelaciones y conflicto compartido; distingue requisitos de propuestas técnicas del agente.

[DELEGACION.md](docs/DELEGACION.md) documenta tres etapas reales delegadas a Codex por la consigna: inventario/disponibilidad; creación/validaciones; cancelación/persistencia/pruebas. Incluye instrucciones recibidas, archivos, comprobaciones y el cierre de las revisiones humanas confirmado por el usuario. El usuario aceptó expresamente los tres episodios por la suite de 21 pruebas aprobadas, el inventario correcto y la conservación del historial al abrir otra terminal; reconoció que los rechazos manuales correspondían a reservas ya existentes. La decisión y su evidencia están registradas en DELEGACION.md. No son tres conversaciones ficticias ni intervenciones de tres subagentes.

Commits comprobados: estructura inicial `63c0c77b83650aac9cfcb7c937254e3403c98d5d` e implementación final `65ee4b5`. Las decisiones humanas se registran por separado en DELEGACION.md. [ENTREGA.md](docs/ENTREGA.md) contiene propuestas de commits, comandos para registrar el estado final, pasos de publicación y acceso en GitHub y un borrador de correo con asunto «Challenge IA» que no se envió.
