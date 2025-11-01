# Recolección de datos a través de formularios web

## ¿Qué son los formularios web?

[Los formularios web Enketo](enketo.md) son utilizados por KoboToolbox para previsualizar tus formularios y para ingresar datos directamente en tu computadora. También puedes usar formularios web para recolectar datos en tus dispositivos móviles, incluso si estás sin conexión en el momento de la recolección de datos. Funciona en prácticamente cualquier dispositivo, incluyendo iPhones, iPads o cualquier otro teléfono inteligente, tableta o computadora. Algunas funcionalidades aún están siendo desarrolladas activamente para Enketo, por lo que algunas preguntas especiales pueden no ser completamente compatibles todavía en todos los dispositivos.

## ¿Por qué necesito formularios web en lugar de la aplicación de Android de KoboCollect?

Siempre usarás formularios web Enketo si no estás utilizando [la aplicación de Android de KoboCollect](https://support.kobotoolbox.org/kobocollect_on_android_latest.html) en un dispositivo Android para la recolección de datos. Sin embargo, también hay algunas configuraciones de aspecto como likert para el tipo de pregunta Seleccionar una, multiples líneas para el tipo de pregunta Texto, etc., y configuraciones de estilo para el Diseño y Configuración de KoboToolbox que funcionan mejor en formularios web en comparación con la aplicación de KoboCollect.

## ¿Cómo uso los formularios web para la recolección de datos?

### Configuración de recolección:

Para comenzar a recolectar datos, primero necesitarás desplegar tu proyecto. Una vez que tu proyecto esté desplegado, verás una pantalla como la que se muestra a continuación con opciones sobre cómo **Recolectar datos**.

![image](/images/data_through_webforms/collection_settings.png)

En el menú desplegable bajo **Recolectar datos**, tienes varias opciones disponibles para Formularios Web:

**En línea-Sin conexión (múltiples envíos):** Esto permite envíos en línea y sin conexión y es la mejor opción para recolectar datos en el campo.

**Solo en línea (múltiples envíos):** Esta es la mejor opción cuando se ingresan muchos registros a la vez en una computadora, por ejemplo, para transcribir registros en papel.

**Solo en línea (envío único):** Esto permite un solo envío y puede combinarse con el parámetro 'return_url' (explicado a continuación) para redirigir al/a la usuario/a a una URL de tu elección después de que el formulario haya sido enviado.

**Solo en línea (una vez por encuestado/a):** Esto permite que tu formulario web solo sea enviado una vez por usuario/a, utilizando protección básica para evitar que el/la mismo/a usuario/a (en el mismo navegador y dispositivo) envíe más de una vez.

**Código de formulario web integrable:** Usa este fragmento de código html5 para integrar tu formulario en tu propio sitio web usando márgenes más pequeños.

**Solo visualización:** Usa esta versión para probar, obtener retroalimentación. No permite enviar datos.

**Aplicación de Android:** Usa esta opción para recolectar datos en el campo con tu dispositivo Android.

### Iniciar la recolección de datos:

Selecciona una opción apropiada del menú desplegable de **Recolectar datos** y luego click en COPIAR para copiar el enlace de la encuesta y compartirlo con otras personas, o click en ABRIR para abrir el formulario de la encuesta en una nueva pestaña en tu navegador. Una vez que el formulario esté abierto, deberías ver una pantalla como la que se muestra en la imagen a continuación:

![image](/images/data_through_webforms/data_collection.jpg)

**1. Barras de señal:** Las barras de señal indican si el formulario puede ser lanzado sin conexión o no. Los formularios web están diseñados para poder recolectar datos mientras estás sin conexión, sin embargo, es esencial visitar la URL del formulario con una conexión a internet antes de quedar sin conexión. Una vez que tu formulario haya sido cargado y almacenado en caché, verás el ícono de disponibilidad sin conexión (barras de "señal" vacías y una marca de verificación) en la esquina superior izquierda indicando que ahora puedes acceder al formulario sin conexión.

**2. Ícono de impresora:** El ícono de impresora te proporciona acceso para imprimir tu formulario o guardarlo como una versión PDF. Para esto, click en el ícono de impresora y luego selecciona Destino (una impresora apropiada conectada a tu dispositivo para imprimir tu formulario de encuesta o Guardar como PDF para guardar tu formulario de encuesta como un PDF).

**3. Elegir idioma:** Esta funcionalidad en el formulario web se activa si tienes múltiples idiomas para tu proyecto de encuesta. Puedes alternar entre el idioma predeterminado y otros idiomas presentes en tu formulario de encuesta.

**4. Guardar como borrador:** Usa esta funcionalidad para editar o actualizar tus registros antes de enviarlos al servidor de KoboToolbox. Una vez que hayas marcado Guardar como borrador tendrás una opción para Guardar borrador. El registro Borrador queda en cola pero no se sincroniza con el servidor de KoboToolbox. Para sincronizarlo con el servidor tendrás que abrir el registro de la lista en cola y desmarcar Guardar como borrador y click en Enviar.

**5. Enviar:** Click en el botón Enviar si has completado la recolección de información y deseas enviar el formulario completado al servidor de KoboToolbox. Después de hacer click en el botón Enviar, no tendrás una opción para editar los registros en tu dispositivo.

**6. Contador de registros en cola:** El Contador de registros en cola te muestra el número total de registros enviados y esperando ser cargados a un servidor. Los registros en cola se cargan automáticamente en segundo plano cada 5 minutos cuando la página web está abierta y hay una conexión a internet disponible.

**7. Panel de registros en cola:** Al hacer click en el botón lateral se muestran los registros que están disponibles como Borradores (que aún pueden ser editados) y registros enviados finalizados en cola para ser cargados a tu servidor con una conexión a internet o exportados como archivo zip como se describe en el [artículo de ayuda aquí](manual_upload.md).

## ¿Cómo guardo un formulario web sin conexión en un dispositivo móvil?

Sigue los pasos descritos a continuación para guardar un formulario y recolectar datos en un formulario web usando un dispositivo móvil:

1. Conecta tu dispositivo a internet.

2. Abre un navegador web disponible (Chrome preferido) en tu dispositivo móvil.

3. Escribe o pega la URL de tu formulario web para abrir una página de formulario que se parezca a la que se muestra a continuación:

    ![image](/images/data_through_webforms/offline_webform.jpg)

4. Haz click en el ícono de 3 PUNTOS en la parte superior derecha (marcado con un círculo en la imagen de arriba) y selecciona AÑADIR A LA PANTALLA DE INICIO para crear un acceso directo en tu dispositivo.

5. Aparecerá una ventana para escribir un nombre para el acceso directo de tu proyecto. Nombra el acceso directo y luego click en AÑADIR.

6. Ahora verás un ícono de acceso directo del formulario web de KoboToolbox en tu dispositivo, similar al que se muestra a continuación:

    ![image](/images/data_through_webforms/kobo_icon.png)

7. Selecciona el ícono de acceso directo para comenzar a recolectar datos para tu proyecto de encuesta.

## Reenvío al enviar

Por defecto, el formulario se actualiza para la siguiente entrada una vez que los datos han sido enviados. Si los/as usuarios/as solo deben ingresar una entrada (por ejemplo, en una encuesta en línea) puedes enviarlos a otro sitio web al enviar. Para usar esta funcionalidad necesitas 1) usar la forma Solo en línea del formulario, y 2) agregar `?return_url=https://www.algunsitio.com` a tu URL.

![image](/images/data_through_webforms/url-single.png)

## Solución de problemas de formularios web

Siempre usa la última versión del navegador. Recomendamos a los/as usuarios/as usar Chrome como su navegador mientras trabajan con formularios web. Para otros detalles sobre la solución de problemas de formularios web, por favor visita nuestro [artículo de ayuda (Solución de problemas de formularios web Enketo) aquí](troubleshooting_webforms.md).