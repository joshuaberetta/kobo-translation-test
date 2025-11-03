# Cargar envíos manualmente

<p class="note">Ten en cuenta que esta sigue siendo una funcionalidad experimental y no evita que crees envíos duplicados.</p>

En ciertas situaciones, es posible que no puedas usar la opción estándar de carga después de recolectar datos con **KoboCollect** o **Formularios web de Enketo**. Esto puede ser resultado de problemas con tu dispositivo móvil que está parcialmente dañado (por ejemplo, la pantalla está rota), o debido a que te encuentras en una ubicación remota sin acceso a Internet. Es posible que desees descargar tus envíos desde el dispositivo de recolección de datos a tu computadora local y luego cargarlos al servidor cuando hayas recuperado la conectividad a Internet.

## Exportar datos desde formularios web

1. En tu **Formulario web** habilitado sin conexión, abre el "Panel lateral" haciendo clic en el corchete de la izquierda.

![Panel lateral](/images/manual_upload/Side_Panel.png)

2. Haz clic en el botón **Exportar** y se guardará un archivo ZIP en tu computadora. Si no es así, haz clic en el botón **Exportar** nuevamente. Para algunos navegadores esto puede no funcionar y necesitarás hacer clic en el enlace "descarga alternativa - en línea", que requerirá una conexión a Internet.

![Exportar](/images/manual_upload/Export.png)

3. Ahora sigue las [instrucciones descritas a continuación](#importar-un-archivo-zip-de-datos) para importar tus envíos.

## Exportar datos desde KoboCollect

1. Conecta el dispositivo a tu computadora mediante un cable USB.

2. Abre el almacenamiento interno del dispositivo en tu computadora. (Para **Windows**, los controladores se instalarán automáticamente y el dispositivo se puede abrir en **Mi PC**. En **MacOS** necesitarás [Android File Transfer](https://www.android.com/intl/en_us/filetransfer/) de Google para acceder a los archivos del dispositivo.)

3. En tu dispositivo, navega a la carpeta **KoboCollect** (se puede encontrar en la ruta a continuación):

    `Teléfono\Android\data\org.koboc.collect.android\files\projects`

    Puedes obtener más información sobre la ruta de almacenamiento del dispositivo [aquí](transferring_forms.md).

4. Copia la carpeta "instances" y pégala en algún lugar de tu computadora.

5. Si tienes más de un dispositivo, repite los pasos anteriores y renombra cada una de las carpetas "instances" con un nombre o número único.

6. Crea un archivo ZIP de la carpeta.

7. Ahora sigue las [instrucciones descritas a continuación](#importar-un-archivo-zip-de-datos) para importar tus envíos.

## Importar un archivo ZIP de datos

1. Inicia sesión en tu cuenta de KoboToolbox, luego visita: `https://kc-eu.kobotoolbox.org/tu_nombre_de_usuario/bulk-submission-form` O `https://kc.kobotoolbox.org/tu_nombre_de_usuario/bulk-submission-form` (dependiendo de dónde te hayas registrado), y reemplaza `tu_nombre_de_usuario` con **tu propio nombre de usuario**.

2. Selecciona y carga el archivo ZIP. Todos los registros se cargarán al servidor, asumiendo que corresponden a un formulario existente.

Una vez que se hayan cargado todas las instancias, verás un mensaje de confirmación para cada registro. Si ves un mensaje de tiempo de espera agotado, puedes intentar cargar varios archivos ZIP más pequeños con menos registros. Cargar los mismos registros dos veces no es un problema, ya que los registros duplicados serán rechazados.