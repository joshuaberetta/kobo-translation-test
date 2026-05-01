# Registros de actividad

Los registros de actividad son registros digitales que capturan acciones y eventos importantes en tu cuenta de KoboToolbox. Los registros de actividad te brindan un historial detallado del acceso a la cuenta y la actividad del proyecto.
Estos registros pueden ser útiles para:

-   Monitoreo de seguridad: ver quién accedió a tu cuenta y desde dónde
-   Seguimiento de cambios: saber cuándo se modificaron los elementos del proyecto
-   Responsabilidad: identificar qué miembros del equipo realizaron cambios específicos
-   Solución de problemas: comprender cuándo y cómo pueden haber ocurrido los problemas

KoboToolbox proporciona dos tipos de registros de actividad para ayudarte a monitorear diferentes aspectos de tu trabajo:

-   **Registros de acceso:** respaldan la seguridad de la cuenta al mostrar todos los inicios de sesión.
-   **Registros del historial del proyecto:** realizan un seguimiento de todas las acciones y cambios realizados por cualquier usuario/a dentro de un proyecto específico y sus datos.


<p class="note">
  <b>Nota:</b> Los registros de actividad son una adición relativamente reciente a KoboToolbox. Estamos trabajando activamente para expandir estas funciones en los próximos meses y proporcionar una cuenta aún más detallada de las acciones en tus cuentas y proyectos.
</p>

## Registros de acceso

Los registros de acceso registran todos los eventos de autenticación (inicios de sesión) para tu cuenta de KoboToolbox. Te ayudan a monitorear la seguridad de la cuenta al mostrarte cuándo y dónde se accedió a tu cuenta.

Se pueden encontrar bajo el título 'Actividad reciente de la cuenta', al que puedes acceder fácilmente abriendo la Configuración de tu cuenta en la sección Seguridad.

Los registros de acceso muestran:

-   Fecha y hora de cada inicio de sesión
-   Dirección IP (información de ubicación)
-   Fuente (información del dispositivo y navegador)

![image](/images/activity_logs/Logs-image01.jpg)

Ten en cuenta que los eventos similares (autenticaciones) que ocurran dentro de los 60 minutos posteriores se agruparán.

### Exportar registros de acceso

![image](images/activity_logs/Logs-image02.jpg)

Esta sección también te permite exportar todos tus registros de acceso haciendo clic en el botón 'Exportar datos de actividad' en la esquina superior derecha de la tabla. Hacer clic en este botón activará el proceso de exportación de datos:
1. Comenzará el procesamiento de los registros en un archivo de exportación .csv
2. Se mostrará una ventana modal que te informará que el proceso ha comenzado y cuáles son los próximos pasos.
3. Recibirás un correo electrónico con un enlace para descargar el archivo una vez que esté listo. La cantidad de datos incluidos en tus registros determinará cuánto tiempo puede tardar en recibir el correo electrónico.
4. Hacer clic en la URL del correo electrónico debería iniciar inmediatamente la descarga del archivo .csv, dependiendo de la configuración de tu navegador.

El archivo de exportación incluirá información más detallada de todos los eventos de autenticación, incluido el tipo de autenticación y el momento exacto.

### Cerrar sesión en todos los dispositivos

Puedes forzar que todos los dispositivos que actualmente tienen sesión iniciada en tu cuenta cierren sesión inmediatamente haciendo clic en el enlace 'Cerrar sesión en todos los dispositivos' a la izquierda del botón de exportación de datos.

Esta acción también cerrará tu sesión actual.

## Registros del historial del proyecto

Los registros del historial del proyecto proporcionan un registro detallado de todas las actividades dentro de un proyecto específico. Muestran cada acción realizada, ya sea por los/as usuarios/as o por procesos automatizados, brindándote visibilidad completa del historial de tu proyecto.

Para ver los registros de un proyecto específico, ve a la ventana CONFIGURACIÓN de tu proyecto y ve a la sección Actividad.

![image](/images/activity_logs/Logs-image3.jpg)

En esta página encontrarás una vista de tabla con toda la actividad del proyecto, ordenada por fecha. Cada acción única se enumera junto con el/la usuario/a que la realizó y la marca de fecha asociada con esa actividad.

Los registros del historial del proyecto capturan casi todas las acciones posibles que se pueden realizar en un proyecto.

| Categoría                      | Acciones incluidas                                                                                                                                    |
| :----------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cambios en el proyecto         | Actualizaciones del nombre del proyecto, implementaciones y reimplementaciones, archivado y desarchivado, conexiones de proyectos                     |
| Cambios en el formulario       | Cargas de XLSForm, ediciones de formularios, creación de preguntas de análisis cualitativo                                                           |
| Cambios en el manejo de datos  | Exportaciones de datos, modificaciones de archivos multimedia adjuntos, cambios en la configuración de uso compartido de datos, modificaciones del servicio REST |
| Permisos                       | Actualizaciones de acceso de usuarios/as, configuración de acceso público, transferencias de propiedad                                               |
| Envíos                         | El/la usuario/a modifica o elimina envíos. Agregar envíos se muestra en la exportación de registros, pero no en la interfaz de KoboToolbox          |

### Encontrar e investigar actividades específicas

Puedes filtrar el registro del historial por tipo de actividad (por ejemplo, implementaciones, ediciones de formularios, cambios de permisos, etc.) utilizando la funcionalidad de alternancia en la esquina superior derecha. Esto también permitirá a los/as propietarios/as y administradores/as del proyecto realizar un seguimiento de los cambios/actualizaciones en aspectos específicos del proyecto rápidamente.

![image](/images/activity_logs/Logs-GIF01.gif)

También puedes exportar todos los datos del historial de tu proyecto utilizando el botón de exportación en la esquina superior derecha de tu tabla.
Si necesitas más información sobre una actividad específica, simplemente haz clic en 'Ver detalles' para obtener una vista ampliada de esa entrada. Esto mostrará toda la información sobre ese evento, revelando lo que ocurrió en el backend y cualquier metadato asociado.

## Problemas comunes con los registros de actividad

**"No veo actividades recientes"**
-   Verifica que estés viendo el proyecto correcto
-   Asegúrate de tener los permisos correctos para ver los registros. Solo los/as propietarios/as del proyecto y los/as usuarios/as con permisos de 'gestionar proyecto' pueden ver los registros.
-   Ten en cuenta que los registros solo están disponibles por un período de 60 días. Los registros más antiguos se eliminan y no se pueden recuperar. Este período se puede configurar a nivel de administrador para organizaciones con un servidor privado.

**"Necesito datos de registro más antiguos"**
-   Los datos que superan el período de retención se eliminan automáticamente y no se pueden recuperar. Si necesitas tener acceso a datos de registro de más de 60 días y estás utilizando un servidor privado, puedes comunicarte con tu administrador/a para aumentar el período de retención.

**"No puedo descargar el archivo de exportación de datos de registro"**
-   Cuando haces clic en el enlace que recibiste por correo electrónico para descargar el archivo de exportación de datos de registro, es posible que se abra una página web con texto en lugar de descargar el archivo csv.
-   Para descargar el archivo .csv desde la página web, haz clic derecho en la página y selecciona Guardar página como…. Mantén el formato como "Código fuente de la página"
-   Si haces clic en el enlace y recibes un mensaje de error, como 403 Prohibido, intenta abrir el enlace con otro navegador (por ejemplo, Safari).

![image](/images/getting_started_organization_feature/organizations_project_views.gif)