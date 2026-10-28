# Preparación de entrega

## Estado

Aplicación y pruebas implementadas. La revisión humana de los tres episodios está cerrada por confirmación expresa del usuario del 28/10/2026. No hay remoto configurado. No se ejecutaron commits nuevos, push, publicación ni envío de correo. Único commit verificado: `63c0c77b83650aac9cfcb7c937254e3403c98d5d` («Estructura inicial del sistema de reservas»).

La carpeta .git tiene permiso de lectura en este entorno. Se proporcionan los comandos exactos para registrar los cambios desde la terminal del usuario. No se presentan como acciones ya ejecutadas ni como aprobaciones.

## Revisión y commit

Propuestas formuladas al finalizar las etapas:

1. `feat: inventario y disponibilidad con SQLite`
2. `feat: reservas y validaciones compartidas`
3. `feat: cancelaciones historial y pruebas de persistencia`

No existen instantáneas Git de esas etapas: los archivos actuales contienen la implementación acumulada. No crear tres commits ficticios atribuidos a etapas pasadas. Para registrar ahora el estado final, revisar primero:

```powershell
git status --short
git diff -- AGENTS.md README.md app.py reservas.py database.py
python -m unittest discover -s tests -v
```

Revisar también los archivos nuevos de docs/ y tests/ que git diff no muestra antes de agregarlos. Tras decidir aceptar el trabajo, comandos para un commit real del estado final:

```powershell
git add AGENTS.md README.md app.py reservas.py database.py inventario.json .gitignore docs tests
git diff --cached --stat
git diff --cached --check
git commit -m "feat: sistema local de reservas con pruebas y documentacion"
git log -3 --oneline
git status --short
```

No se necesita borrar nada ni reescribir historial. El nuevo hash debe registrarse en PROGRESO.md y en los documentos pertinentes después de existir. Nunca sustituir un hash pendiente por uno inventado. Un commit técnico no constituye por sí mismo una revisión humana.

## Publicación en GitHub

Acciones pendientes del titular de la cuenta:

1. Crear un repositorio vacío en GitHub, sin inicializar README, licencia ni .gitignore para evitar conflictos con este repositorio.
2. Decidir si será público o privado. Si es privado, invitar al evaluador y comprobar que aceptó la invitación.
3. Copiar la URL HTTPS real. Comprobar la rama con `git branch --show-current`.
4. Desde PowerShell, registrar y subir usando la URL real cuando se autorice la publicación:

```powershell
$urlRepositorio = Read-Host 'Pegá la URL HTTPS real del repositorio GitHub'
git remote add origin $urlRepositorio
$ramaReservas = git branch --show-current
git push -u origin $ramaReservas
```

Estos comandos suponen que origin sigue sin existir, como se observó en esta sesión. Si ya existe, inspeccionar `git remote -v` y usarlo si es correcto; no reemplazarlo sin revisar.

5. Autenticarse mediante el mecanismo de GitHub que corresponda. No guardar tokens en archivos del proyecto.
6. Comprobar `git remote -v`, `git status --short` y `git log -1 --oneline`; abrir GitHub y verificar que el commit y los archivos están visibles.
7. Para un repositorio público, abrir el enlace sin iniciar sesión. Para uno privado, verificar el acceso con la cuenta del evaluador: no basta con que el propietario pueda abrirlo. URL, permisos y comprobación humana: PENDIENTE.

## Borrador de correo — no enviado

Destinatario: PENDIENTE

Asunto: Challenge IA

Hola:

Comparto mi trabajo práctico «Desarrollo de un sistema de reservas con agentes».

Repositorio: PENDIENTE — agregar la URL real y comprobar acceso.

El README incluye la especificación, la instalación, los comandos, las pruebas y las referencias a los tres episodios de trabajo con Codex. El sistema funciona localmente con Python y SQLite sin depender de servicios de IA. Las evidencias automatizadas del agente están en docs/VERIFICACION.md y docs/evidencias/.

La revisión humana de los episodios está cerrada por confirmación del usuario. Antes de enviar: registrar el commit final y verificar el acceso al repositorio. No se documentó una ejecución independiente de pruebas por el usuario.

Saludos,

PENDIENTE — firma del remitente

## Acciones de entrega restantes

- Revisión de los tres episodios: cerrada por confirmación del usuario del 28/10/2026; no requiere una nueva solicitud.
- No se dispone de resultados de pruebas ejecutadas por una persona; no se atribuyen resultados humanos a las pruebas del agente.
- Versionar los cambios finales y registrar el hash existente.
- Publicar, comprobar acceso y completar URL, destinatario y firma.
- Revisar este borrador y enviarlo personalmente cuando todo esté confirmado.

## Estado actualizado de Git — 2026-10-28

Se creó realmente el commit `65ee4b5` en main, «feat: sistema local de reservas con pruebas y documentacion», con la implementación, pruebas y documentación final. El commit inicial 63c0c77 se conserva. Las afirmaciones anteriores sobre cambios sin commit describen el estado previo y quedan superadas por este registro.

Verificación previa: 21 pruebas OK. La revisión del índice incluyó todos los archivos nuevos; git diff --cached --check detectó espacios finales y líneas vacías en las transcripciones originales etapa1.txt y etapa2.txt, conservadas sin alterar. No se incluyeron bases SQLite, cachés ni tmp/.

Publicación: todavía no ejecutada. No hay remoto configurado y se requiere conexión de GitHub para crear o seleccionar el repositorio y verificar acceso. No se envió correo. La evidencia humana posterior está en evidencias/revision-humana.txt y su aceptación consta en DELEGACION.md; las menciones históricas a falta de pruebas humanas ya están superadas.
