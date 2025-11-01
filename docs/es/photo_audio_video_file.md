# Tipos de preguntas "Foto", "Audio", "Video" y "Archivo"

Con KoboToolbox, puedes recolectar diferentes tipos de datos multimedia como parte de tu proyecto de recolección de datos.

Cuando quieras capturar imágenes como parte de tus envíos, usa el tipo de pregunta "Foto".

Si una pregunta requiere que grabes o adjuntes un archivo de audio, como cuando se espera una explicación larga del encuestado, usa el tipo de pregunta "Audio". La última versión de KoboCollect te permite grabar audio dentro de la aplicación sin necesidad de abrir una aplicación separada.

Con el tipo de pregunta "Video", podrás grabar un video usando la cámara del dispositivo o adjuntar un archivo de video.

Si una pregunta requiere que adjuntes un archivo como un PDF, puedes usar el tipo de pregunta "Archivo".

## Cómo configurar los tipos de preguntas "Foto", "Audio", "Video" y "Archivo"

### Configuración en el editor de formularios de KoboToolbox (Formbuilder)

Añadir preguntas multimedia es simple:

- Haz click en el botón <i class="k-icon k-icon-plus"></i> para añadir una nueva pregunta
- Escribe el texto de la pregunta, por ejemplo "Toma una foto de la unidad de vivienda", luego haz click en **AÑADIR PREGUNTA** o presiona ENTER en tu teclado
- Elige el tipo de pregunta

![Adding media question](images/photo_audio_video_file/add.gif)

### Configuración en XLSForm

Para añadir preguntas multimedia en XLSForm, usa los tipos de pregunta `image`, `audio`, `video` o `file` como se muestra en el siguiente ejemplo:

| type   | name        | label                                                                  | hint                |
| :----- | :---------- | :--------------------------------------------------------------------- | :------------------ |
| image  | house_photo | Toma una foto de la unidad de vivienda                                 |                     |
| audio  | impact      | ¿Cuál ha sido el impacto del proyecto en tu hogar?                     | Grabar como audio   |
| video  | preparation | Graba un video del encuestado mientras prepara el VitaMeal             |                     |
| file   | CV          | Adjunta tu CV                                                          |                     |
| survey |

## Aspecto de los tipos de preguntas "Foto", "Audio", "Video" y "Archivo"

### Aspecto predeterminado

![Default appearances](images/photo_audio_video_file/default_appearances.png)

### Aspectos avanzados para el tipo de pregunta "Foto"

Al añadir el tipo de pregunta "Foto", puedes elegir entre varios aspectos (en la configuración de la pregunta). Los aspectos cambian la forma en que se muestra la pregunta en formularios web y KoboCollect.

![Advanced appearances for photo question type](images/photo_audio_video_file/advanced_appearances_photo.png)

![Advanced appearances](images/photo_audio_video_file/advanced_appearances.png)

### Añadir aspectos avanzados en XLSForm

Puedes especificar aspectos avanzados de la pregunta "Foto" en XLSForm bajo la columna appearance (aspecto) como se muestra en el siguiente ejemplo:

| type   | name       | label                           | appearance |
| :----- | :--------- | :------------------------------ | :--------- |
| image  | sign       | Firma aquí                      | signature  |
| image  | drawing    | Dibuja aquí                     | draw       |
| image  | annotation | Toma una imagen y anota         | annotate   |
| survey |

## Grabación de audio de fondo

Puedes grabar audio de fondo cuando abres el formulario en KoboCollect. Esto puede ser útil en varios escenarios de recolección de datos, incluyendo discusiones de grupos focales y entrevistas con informantes clave.

Activa la grabación de audio de fondo en el editor de formularios de KoboToolbox (Formbuilder) haciendo click en **Diseño y Configuración** y habilitando la función.

![Background audio](images/photo_audio_video_file/background_audio.png)

<p class="note">
  La grabación de audio de fondo solo está disponible en KoboCollect y <strong>no</strong> en formularios web de Enketo.
</p>

En XLSForm, puedes habilitar la grabación de fondo con el tipo de pregunta `background-audio`. Este se considera un tipo de pregunta "meta" y por lo tanto no se requiere `label` (etiqueta), solo un `name` (nombre). La calidad del audio se puede configurar bajo la columna `parameters` (parámetros), como se explica [aquí](recording-interviews.md).

| type             | name             | label |
| :--------------- | :--------------- | :---- |
| background-audio | background_audio |       |
| survey           |

<p class="note">
  No es posible grabar audio usando el tipo de pregunta "Audio" mientras la grabación de audio de fondo está en curso en el formulario. Cuando la grabación de audio de fondo está activada, todos los tipos de pregunta "Audio" se desactivan.
</p>

Puedes leer más sobre la grabación de audio de fondo [aquí](recording-interviews.md).

## Reducir el tamaño de archivo de los datos multimedia recolectados

Si estás recolectando muchos datos multimedia en tu proyecto, podrías tener dificultades para cargarlos a KoboToolbox dependiendo de la velocidad de tu conexión a internet. Si estás usando el [Servidor Global o el Servidor con sede en la Unión Europea](creating_account.md), también estás limitado a solo 1GB de almacenamiento gratuito. Es una buena idea manejar los tamaños de archivo de los archivos multimedia recolectados como imágenes, audio y videos.

Puedes definir el tamaño máximo de las imágenes que recolectas usando el tipo de pregunta "Foto" yendo a la configuración de la pregunta y estableciendo la configuración "max-pixels" en el editor de formularios de KoboToolbox (Formbuilder).

![Max pixels](images/photo_audio_video_file/max-pixels.png)

En XLSForm, puedes hacer lo mismo añadiendo "max-pixels" en la columna `parameters` (parámetros) de la siguiente manera:

| type   | name  | label          | parameters     |
| :----- | :---- | :------------- | :------------- |
| image  | photo | Capturar foto  | max-pixels=480 |
| survey |

En KoboCollect, también puedes elegir la calidad del video y el tamaño de la foto a través de la sección de Manejo de Formularios en la configuración del proyecto.

Puedes leer más sobre cómo reducir los tamaños de archivo [aquí](lower_file_size.md).

## Limitar los tipos de archivo aceptados para el tipo de pregunta "Archivo"

Todos los tipos de archivo son aceptados por defecto para el tipo de pregunta "Archivo". En el editor de formularios de KoboToolbox (Formbuilder) puedes restringir esto haciendo lo siguiente:

- Ve a la configuración de la pregunta "Archivo"
- Bajo el cuadro "Archivos Aceptados", ingresa las extensiones de archivo de los archivos que te gustaría permitir, separadas por una coma, por ejemplo ".doc, .pdf, .xlsx"

![File types](images/photo_audio_video_file/file_types.png)

En XLSForm, puedes limitar los tipos de archivo aceptados especificando las extensiones de archivo en la columna `body::accept` de la siguiente manera:

| type   | name | label          | body::accept |
| :----- | :--- | :------------- | :----------- |
| file   | CV   | Adjunta tu CV  | .pdf, .doc   |
| survey |

<p class="note">
  Descarga un XLSForm con ejemplos de este artículo <a download class="reference" href="./_static/files/photo_audio_video_file/media_question_types.xlsx">aquí</a>.
</p>