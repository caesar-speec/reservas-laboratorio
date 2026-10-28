# Instrucciones del proyecto

- Utilizar Python para desarrollar la aplicación.
- Utilizar SQLite para persistir los datos entre ejecuciones.
- Utilizar unittest para las pruebas automatizadas.
- Evitar reservas superpuestas para un mismo equipo.
- Permitir horarios consecutivos: una reserva puede comenzar cuando termina otra.
- Conservar las reservas canceladas y su estado; no eliminarlas del historial.
- No inventar resultados de pruebas ni evidencias de uso.
- La estructura inicial no debe incluir lógica del sistema; implementarla cuando se solicite.

## Desarrollo autorizado

La consigna de desarrollo completo autoriza implementar una aplicación local de consola sin dependencias externas de ejecución. Usar Python compatible con 3.12, SQLite, argparse, JSON y unittest.

- Objetivo: consultar inventario y disponibilidad, crear y cancelar reservas y consultar historial persistente.
- Organización: app.py contiene la CLI; reservas.py, validaciones y lógica; database.py, conexión y esquema SQLite; tests/, pruebas con bases temporales.
- Una reserva que comienza exactamente cuando termina otra no debe considerarse superpuesta. La disponibilidad y la creación deben compartir esta regla. Debe existir una prueba automática que demuestre este comportamiento.
- Conflicto solo entre reservas ACTIVA del mismo equipo: inicio_nuevo < fin_existente AND fin_nuevo > inicio_existente.
- Validar equipo conocido, solicitante no vacío e intervalo creciente en formato estricto YYYY-MM-DDTHH:MM. Horarios locales de America/Argentina/Cordoba; permitir fechas pasadas.
- Persistir en data/reservas.db, crear tablas sin borrar datos y conservar cancelaciones. No implementar reinicio destructivo.
- Ejecutar python -m unittest discover -s tests -v; usar bases temporales independientes y verificar procesos separados.
- Modificar solo archivos del proyecto necesarios para la consigna. No agregar servicios, autenticación, secretos ni datos personales reales.
- No publicar, enviar correo ni reescribir historial. Revisión humana de cada episodio pendiente hasta decisión explícita; no atribuir aceptación automática.
- Registrar acciones y resultados reales durante cada etapa en docs/PROGRESO.md, docs/DELEGACION.md y docs/VERIFICACION.md. Mantener pendientes humanos explícitos.
