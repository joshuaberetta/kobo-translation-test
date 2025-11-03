# Añadir varios tipos de datos multimedia (imagen, audio, video) a un formulario

<a href="https://github.com/kobotoolbox/docs/blob/511ea4cb3c698a4b45e7c2b4efd1af4e356e811f/source/media.md" class="reference">15
Feb 2022</a>

Además de preguntas de texto y opciones de texto, también puedes añadir varios tipos
de datos multimedia (como _imagen_, _audio_ y _video_) a tus formularios. Tener datos multimedia en
un formulario a veces puede ayudarte a expresar tus preguntas y opciones
de una manera mucho mejor.

Los datos multimedia en un formulario funcionan tanto en la **aplicación de Android de KoboCollect** como en los **formularios web
(Enketo)**. Estos son los archivos multimedia que actualmente son compatibles:

| Datos multimedia | Archivos                                                      |
| :---- | :------------------------------------------------------------ |
| Imagen | jpeg, png, svg                                                |
| Audio | aac, aacp, flac, mp3, mp4, mpeg, ogg, wav, webm, x-m4a, x-wav |
| Video | 3gpp, avi, flv, mov, mp4, ogg, quicktime (qtff), webm, wmv    |

Este artículo de ayuda tiene como objetivo ilustrar cómo se pueden crear formularios con datos multimedia con
**KoboToolbox**. Sigue las instrucciones que se describen a continuación para incluir datos multimedia en tu
proyecto de encuesta.

## Paso 1: Descargar el formulario como XLSForm

Crea un proyecto de encuesta en la interfaz del editor de formularios de KoboToolbox (Formbuilder) y luego descarga tu formulario como XLS
para añadir configuraciones de datos multimedia. Actualmente, el editor de formularios no admite añadir
datos multimedia al formulario directamente, por lo que necesitarás editar el XLSForm descargado para
completar esta acción.

<video controls><source src="./_static/files/media/download_xlsform.mp4" type="video/mp4"></video>

## Paso 2: Añadir columnas de datos multimedia a tu XLSForm

<p class='note'>Los nombres de archivo añadidos al XLSForm deben coincidir con los nombres de archivo que
diste a tus archivos de <em>imagen</em>, <em>audio</em> y
<em>video</em>.</p>

### Añadir columnas de datos multimedia de imagen:

Si deseas añadir una **imagen** a una pregunta, escribe `media::image` como
encabezado de columna en la pestaña **survey** de tu XLSForm. Escribe el nombre del archivo de imagen
junto con una extensión en la pregunta correspondiente justo debajo del
encabezado de columna `media::image`.

De manera similar, si deseas añadir una **imagen** a una opción, escribe
`media::image` como encabezado de columna en la pestaña **choices** de tu XLSForm. Una
vez más, escribe el nombre del archivo de imagen junto con una extensión en la opción correspondiente
justo debajo del encabezado de columna `media::image`.

<video controls><source src="./_static/files/media/adding_media_image.mp4" type="video/mp4"></video>

### Añadir columnas de datos multimedia de audio:

Si deseas añadir **audio** a una pregunta, escribe `media::audio` como encabezado de columna
en la pestaña **survey** de tu XLSForm. Escribe el nombre del archivo de audio junto
con una extensión en la pregunta correspondiente justo debajo del
encabezado de columna `media::audio`.

De manera similar, si deseas añadir **audio** a una opción, escribe `media::audio` como
encabezado de columna en la pestaña **choices** de tu XLSForm. Una vez más, escribe el
nombre del archivo de audio junto con una extensión en la opción correspondiente justo debajo del
encabezado de columna `media::audio`.

<video controls><source src="./_static/files/media/adding_media_audio.mp4" type="video/mp4"></video>

### Añadir columnas de datos multimedia de video:

Si deseas añadir video a una pregunta, escribe `media::video` como encabezado de columna
en la pestaña **survey** de tu XLSForm. Escribe el nombre del archivo de video junto
con una extensión en la pregunta correspondiente justo debajo del
encabezado de columna `media::video`.

De manera similar, si deseas añadir video a una opción, escribe `media::video` como
encabezado de columna en la pestaña **choices** de tu XLSForm. Una vez más, escribe el nombre del archivo de video
junto con una extensión en la opción correspondiente justo debajo del
encabezado de columna `media::video`.

<video controls><source src="./_static/files/media/adding_media_video.mp4" type="video/mp4"></video>

## Paso 3: Gestionar columnas de datos multimedia para múltiples idiomas

<p class='note'>Este paso es para quienes tienen múltiples idiomas en su proyecto de
encuesta.</p>

Puedes tener una encuesta con múltiples idiomas y querer añadir varios tipos de
datos multimedia relevantes para idiomas específicos. En tales casos, puedes seguir las
ilustraciones proporcionadas a continuación.

### Gestionar columna de datos multimedia para datos multimedia de imagen:

Si deseas añadir una imagen a una pregunta, escribe `media::image` como encabezado de columna
en la pestaña **survey** de tu XLSForm. Escribe el nombre del archivo de imagen junto
con una extensión en la pregunta correspondiente justo debajo del
encabezado de columna `media::image::Language (language code)`.

De manera similar, si deseas añadir una imagen a una opción, escribe
`media::image::Language (language code)` como encabezado de columna en la pestaña **choices**
de tu XLSForm. Una vez más, escribe el nombre del archivo de imagen junto con una extensión
en la opción correspondiente justo debajo del
encabezado de columna `media::image::Language (language code)`.

<video controls><source src="./_static/files/media/adding_media_image_language.mp4" type="video/mp4"></video>

### Gestionar columna de datos multimedia para datos multimedia de audio:

Si deseas añadir audio a una pregunta, escribe
`media::audio::Language (language code)` como encabezado de columna en la pestaña **survey**
de tu XLSForm. Escribe el nombre del archivo de audio junto con una extensión en la
pregunta correspondiente justo debajo del
encabezado de columna `media::audio::Language (language code)`.

De manera similar, si deseas añadir audio a una opción, escribe
`media::audio::Language (language code)` como encabezado de columna en la pestaña **choices**
de tu XLSForm. Una vez más, escribe el nombre del archivo de audio junto con una extensión
en la opción correspondiente justo debajo del
encabezado de columna `media::audio::Language (language code)`.

<video controls><source src="./_static/files/media/adding_media_audio_language.mp4" type="video/mp4"></video>

### Gestionar columna de datos multimedia para datos multimedia de video:

Si deseas añadir video a una pregunta, escribe
`media::video::Language (language code)` como encabezado de columna en la pestaña **survey**
de tu XLSForm. Escribe el nombre del archivo de video junto con una extensión en la
pregunta correspondiente justo debajo del
encabezado de columna `media::video::Language (language code)`.

De manera similar, si deseas añadir video a una opción, escribe
`media::video::Language (language code)` como encabezado de columna en la pestaña **choices**
de tu XLSForm. Una vez más, escribe el nombre del archivo de video junto con una extensión
en la opción correspondiente justo debajo del
encabezado de columna `media::video::Language (language code)`.

<video controls><source src="./_static/files/media/adding_media_video_language.mp4" type="video/mp4"></video>

## Paso 4: Reemplazar el XLSForm

Carga y reemplaza tu XLSForm en el proyecto existente o crea un nuevo
proyecto.

<video controls><source src="./_static/files/media/replacing_xlsform.mp4" type="video/mp4"></video>

## Paso 5: Cargar archivos multimedia

Ve a **SETTINGS>Media**. Carga todos los archivos multimedia que se han referenciado en
tu formulario.

<video controls><source src="./_static/files/media/uploading_media.mp4" type="video/mp4"></video>

<p class='note'><strong>Consejo:</strong> Reúne todos los archivos multimedia que incluirás en tu proyecto de
encuesta. Proporciona un nombre de archivo corto para cada uno de los datos multimedia. Los nombres de archivo
con un espacio (por ejemplo, "libro rojo") no son compatibles con el sistema. Por lo tanto,
necesitarás eliminar el espacio entre los nombres (por ejemplo,
"librorojo") o usar '_' para un espacio (por ejemplo, "libro_rojo").</p>

## Paso 6: Desplegar el formulario

Una vez que hayas reemplazado el XLSForm y luego cargado todos los archivos multimedia,
necesitarás desplegar tu encuesta.

<video controls><source src="./_static/files/media/deploying_form.mp4" type="video/mp4"></video>

<p class='note'>Cada vez que se añaden o cambian nuevos archivos multimedia, necesitas
<strong>redesplegar</strong> tu proyecto para que el cambio surta efecto.
Puedes ver tus nuevos datos multimedia al previsualizar tu formulario
<em>antes</em> del redespliegue.</p>

## Paso 7: Recolectar datos

Ahora puedes volver a **Form>Collect Data**, y luego hacer click en **Open** para verificar
si los datos multimedia se muestran correctamente.

<video controls><source src="./_static/files/media/collecting_data.mp4" type="video/mp4"></video>

<p class='note'>Los archivos GIF animados actualmente no son compatibles con Enketo o
la aplicación de Android de KoboCollect. Alinear los datos multimedia en una ubicación deseada del formulario (alineación a la izquierda,
alineación al centro o alineación a la derecha) tampoco es
posible.</p>

## Consejos y trucos

### Identificar el nombre de archivo, la extensión y el tamaño de un archivo multimedia en Windows

-   Selecciona un archivo multimedia (imagen, audio o video).
-   Haz click derecho con el ratón cuando el archivo multimedia aún esté seleccionado.

![Dropdown select properties](images/media/dropdown_select_properties.png)

-   Luego selecciona **Properties**.
-   Ahora deberías poder ver el *nombre de archivo* y la *extensión* del archivo multimedia
    en la pestaña **General**.

![Image properties](images/media/image_properties.png)

-   También deberías poder identificar las dimensiones y el tamaño de los datos multimedia en la
    pestaña **Details**. Si deseas tener imágenes pequeñas en tu pregunta u
    opciones, necesitarás cargar datos multimedia con una dimensión más pequeña, o
    viceversa.

<p class='note'>Los datos multimedia en un formulario Enketo tardarán más tiempo en cargarse si tienes
archivos grandes. Intenta reducir los tamaños de los archivos de imagen, video o audio
antes de cargarlos al servidor.</p>

![Image details](images/media/image_details.png)

<p class='note'>Puedes acceder al XLSForm <a download class='reference'
href='./_static/files/media/xlsform-example.xls'>aquí</a> y a los archivos multimedia <a
download class='reference'
href='./_static/files/media/xlsform-example-media.zip'>aquí</a> que se utilizaron
en este artículo.</p>