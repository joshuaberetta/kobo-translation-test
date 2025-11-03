# Iniciar con KoboCollect

<iframe src="https://www.youtube.com/embed/qC2Bz8jZkIM?si=xSyTOxOMR6nE8tum" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

KoboCollect es una aplicación gratuita y de código abierto de KoboToolbox diseñada para la recolección de datos en dispositivos móviles Android. Sus capacidades sin conexión y su compatibilidad con la mayoría de los dispositivos Android la hacen ideal para el trabajo de campo.

Antes de usar KoboCollect, debes [configurar una cuenta de KoboToolbox](https://support.kobotoolbox.org/creating_account.html) en el sitio web de KoboToolbox y [desplegar formularios de recolección de datos](https://support.kobotoolbox.org/quick_start.html).

<p class="note">
    Este artículo cubre cómo conectarse a KoboCollect para la recolección de datos. Para obtener más información sobre la configuración de los ajustes de KoboCollect y la recolección de datos con la aplicación, consulta <a href="https://support.kobotoolbox.org/kobocollect_settings.html">Personalización de los ajustes de KoboCollect</a> y <a href="https://support.kobotoolbox.org/data_collection_kobocollect.html">Recolección de datos usando KoboCollect</a>.
</p>

## Instalación de la aplicación KoboCollect

La aplicación de Android de KoboCollect puede descargarse desde [Google Play Store](https://play.google.com/store/apps/details?id=org.koboc.collect.android) para dispositivos Android con versión 5 o superior.

<p class="note">
    <strong>Nota:</strong> Recomendamos usar la última versión de la aplicación (v2025.2), ya que incluye funcionalidades y correcciones de errores que no están disponibles en versiones anteriores.
</p>

## Configuración de la aplicación KoboCollect

Para recolectar datos con KoboCollect, debes configurar la aplicación KoboCollect en tu dispositivo móvil para conectarte al servidor de KoboToolbox. Esto te permite descargar formularios desplegados desde KoboToolbox y enviar los datos recolectados de vuelta al servidor.

Para conectar KoboCollect al servidor de KoboToolbox, necesitarás tu **URL de KoboCollect**, tu **nombre de usuario** y tu **contraseña**. Después de la configuración manual inicial, puedes [generar un código QR](https://support.kobotoolbox.org/kobocollect_on_android_latest.html#setting-up-kobocollect-with-a-qr-code) para configurar otros dispositivos.

<p class="note">
    <strong>Nota:</strong> En la aplicación KoboCollect, las cuentas de usuario se llaman <strong>Proyectos</strong>.
</p>

### Configuración manual de KoboCollect
Para configurar KoboCollect manualmente, necesitarás identificar tu **URL de KoboCollect**. Esta URL es específica para KoboCollect y difiere de la URL utilizada para acceder a tu cuenta de KoboToolbox.

Tu URL de KoboCollect depende del servidor de tu cuenta:

| **Servidor de KoboToolbox**    | **URL de KoboCollect**                     |
| :----------------- | :--------------------------------------------- |
| Servidor Global               | https://kc.kobotoolbox.org/ |
| Servidor con sede en la Unión Europea      | https://kc-eu.kobotoolbox.org/ |
| Servidor Privado           | Única para cada organización            |

También puedes encontrar la URL de KoboCollect en la plataforma de KoboToolbox. Ve a la ventana **FORMULARIO** de tu proyecto y selecciona **Aplicación de Android** del menú desplegable **Recolectar datos**. La URL de KoboCollect aparecerá en el paso 3.

![Select Android app in browser](images/kobocollect_on_android_latest/select_android_app_in_browser.png)

Una vez que hayas identificado tu URL de KoboCollect, sigue estos pasos para configurar la conexión al servidor:

1. Abre la aplicación KoboCollect.
2. Selecciona **Entrar los detalles del proyecto manualmente**.
3. Ingresa la **URL de KoboCollect**, tu **nombre de usuario** y **contraseña**.
4. Toca **Agregar**.
5. Cuando se complete la configuración, se mostrará el menú principal.

### Configuración de KoboCollect con un código QR

Usar un código QR configura eficientemente KoboCollect en múltiples dispositivos con la **misma configuración de servidor** (URL de KoboCollect, nombre de usuario, contraseña y <a href="https://support.kobotoolbox.org/kobocollect_settings.html">ajustes de configuración del proyecto</a>). Esto puede ser útil para evitar repetir pasos manuales o para configurar dispositivos de encuestadores/as sin compartir contraseñas de cuenta.

<p class="note">
    <strong>Nota:</strong> Para usar el método del código QR, primero debes configurar manualmente un dispositivo y luego copiar el código QR generado a los otros dispositivos.
</p>

Para acceder a tu código QR:

1. Ve al menú **Proyectos** y selecciona el proyecto que deseas copiar.
2. Toca **Ajustes**.
3. Selecciona **Gestión de proyectos**.
4. Toca **Reconfigurar con código QR**.
5. Elige **Código QR**. Tu código QR aparecerá en la pantalla.
6. **Toma una captura de pantalla** del código QR para compartirlo y configurar otros dispositivos. También puedes volver a este menú en cualquier momento para acceder al código QR nuevamente.

Para configurar otros dispositivos usando el código QR:

1. Abre **KoboCollect** en el dispositivo que deseas configurar.
2. Toca **Configurar con código QR**.
3. Escanea un código QR con la cámara del dispositivo, o toca los <i class="k-icon-more"></i> **tres puntos** en la esquina superior derecha y selecciona **Importar código QR** para usar una captura de pantalla guardada en tu dispositivo.

Si la configuración es exitosa, la aplicación se configurará automáticamente.

<p class="note">
    <strong>Nota:</strong> El código QR contiene las credenciales de tu cuenta, incluida tu contraseña. Cualquier persona que lo escanee tendrá los mismos permisos de acceso que la cuenta desde la cual se generó. Si solo deseas que alguien recolecte datos (por ejemplo, un/a encuestador/a), <strong>asegúrate de que la cuenta utilizada para generar el código QR no tenga permisos para ver, editar o eliminar datos.</strong> Para mantener tus datos seguros, evita compartir códigos QR de cuentas con acceso completo.
</p>

### Configuración de múltiples proyectos en KoboCollect

Los/as usuarios/as pueden conectar múltiples cuentas de KoboToolbox y cambiar fácilmente entre diferentes proyectos dentro de la misma aplicación KoboCollect, independientemente de si están en el mismo servidor o en servidores diferentes.

Para configurar proyectos adicionales en KoboCollect:

1. Toca el **ícono de Proyecto** ubicado en la esquina superior derecha.
2. En el menú **Proyectos**, toca **Agregar proyecto**.
3. Configura un nuevo proyecto usando el método manual o escaneando un código QR.
4. Cuando se complete la configuración, se mostrará el menú principal.
5. Toca el **ícono de Proyecto** para abrir el menú. Ambos proyectos deberían estar ahora visibles.

Se pueden agregar proyectos adicionales repitiendo el mismo proceso. El proyecto activo aparecerá primero en el menú **Proyectos**. Para cambiar a un proyecto diferente, simplemente toca su ícono.

<p class="note">
    Para obtener más información sobre cómo cambiar la forma en que se muestran los proyectos para facilitar su reconocimiento y cambio, consulta <a href="https://support.kobotoolbox.org/kobocollect_settings.html#project-display-settings">Ajustes de visualización de proyectos</a>.
</p>

### Configuración de un proyecto en KoboCollect sin autenticación

También es posible acceder a proyectos en KoboCollect sin una contraseña. Esto es útil para proyectos con muchos/as encuestadores/as, ya que evita la necesidad de crear cuentas individuales o compartir credenciales.

<p class="note">
    <strong>Nota:</strong> Este método requiere habilitar "Permitir envíos a este formulario sin nombre de usuario y contraseña" para tus formularios. Para obtener más información sobre los ajustes de uso compartido a nivel de proyecto, consulta <a href="https://support.kobotoolbox.org/project_sharing_settings.html">Compartir proyectos con ajustes a nivel de proyecto</a>.
</p>

Para conectarte a KoboCollect sin autenticación:
1. Habilita "Permitir envíos a este formulario sin nombre de usuario y contraseña" para tus formularios.
2. [Opcional] Crea una cuenta dedicada de KoboToolbox para recolectores/as de datos y [comparte tus formularios](https://support.kobotoolbox.org/managing_permissions.html) con esta cuenta.
3. Conéctate a KoboCollect usando las siguientes credenciales:
    - **URL**: URL de KoboCollect seguida del nombre de usuario de la cuenta (`https://[kobocollect_url]/[username]`)
    - **Nombre de usuario**: (Dejar en blanco)
    - **Contraseña**: (Dejar en blanco)

Este método permite a los/as usuarios/as descargar y enviar datos a cualquier formulario compartido con `username` que no [requiera autenticación](https://support.kobotoolbox.org/project_sharing_settings.html).

Para diferenciar a los/as encuestadores/as y rastrear los envíos, puedes pedirles que ingresen un nombre de usuario personalizado, número de teléfono y dirección de correo electrónico en los [Ajustes de identidad de usuario y dispositivo](https://support.kobotoolbox.org/kobocollect_settings.html#user-and-device-identity-settings).

<p class="note">
    <strong>Nota:</strong> Este método puede ser útil cuando tu cuenta usa <a href="https://support.kobotoolbox.org/two_factor_authentication.html">autenticación de dos factores</a>, ya que no podrás descargar formularios ni enviar datos usando el método normal.
</p>