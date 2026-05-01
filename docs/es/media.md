# Agregar archivos multimedia a un XLSForm

<iframe src="https://www.youtube.com/embed/7TrVmKIuCa8?si=QCr1IzvDXaASEZg7&cc_lang_pref=es&hl=es" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

KoboToolbox te permite agregar archivos multimedia, incluyendo **imágenes**, **archivos de audio** y **videos**, a notas, preguntas y opciones en tu formulario. Agregar archivos multimedia puede aumentar la participación de los/as usuarios/as y hacer que los formularios sean más accesibles para usuarios/as con discapacidades visuales o barreras de alfabetización.

Los archivos multimedia del formulario funcionan tanto con [KoboCollect](../es/kobocollect_on_android_latest.md) como con [formularios web de Enketo](../es/enketo.md). Actualmente se admiten los siguientes tipos de archivos multimedia:

| Multimedia | Archivos |
| :--- | :--- |
| Imagen | jpeg, png, svg |
| Audio | aac, aacp, flac, mp3, mp4, mpeg, ogg, wav, webm, x-m4a, x-wav |
| Video | 3gpp, avi, flv, mov, mp4, ogg, quicktime (qtff), webm, wmv |

Este artículo cubre los siguientes temas:
- Agregar archivos multimedia a preguntas de la encuesta
- Agregar archivos multimedia a opciones de respuesta
- Agregar archivos multimedia a traducciones del formulario
- Cargar archivos multimedia a KoboToolbox

<p class="note">
    <strong>Nota:</strong> El <a href="../es/formbuilder.md">editor de formularios de KoboToolbox (Formbuilder)</a> no admite actualmente agregar archivos multimedia dentro de tus formularios. Para agregar archivos multimedia, necesitarás usar XLSForm y luego cargar tu XLSForm a KoboToolbox. Para obtener más información sobre cómo descargar y editar tu formulario como XLSForm, consulta <a href="../es/xlsform_with_kobotoolbox.md">Usar XLSForm con KoboToolbox</a>.
<br><br>
Para práctica con agregar archivos multimedia en XLSForm, consulta el <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">curso XLSForm Fundamentals</a> de la KoboToolbox Academy.
</p>

## Agregar archivos multimedia a preguntas en XLSForm

Para agregar archivos multimedia a preguntas o notas en tu XLSForm:
1. Agrega una nueva pregunta en la **hoja survey**, especificando el **type** (tipo), **name** (nombre) y **label** (etiqueta) (opcional).
    - Utiliza un tipo de pregunta **note** (nota) si deseas mostrar el archivo multimedia sin recolectar ningún dato (por ejemplo, un logotipo de la organización o un video de introducción).
    - Agregar una etiqueta es opcional al incluir un archivo multimedia.
2. Agrega una columna para el archivo multimedia que deseas incluir. Nómbrala `image` (imagen), `video` o `audio`, según el tipo de archivo multimedia.
3. En la columna de archivos multimedia, en la fila de la pregunta que has agregado, ingresa el nombre exacto del archivo multimedia **incluyendo la extensión**.
    - Por ejemplo: `logo.png` o `intro.mp4`.

**hoja survey**

| type | name | label | image |
| :--- | :--- | :--- | :--- |
| text | Q1 | Con tus propias palabras, ¿cómo describirías la imagen de arriba? | q1.png |
| survey |

<p class="note">
    <strong>Nota:</strong> Anteriormente, se usaba el formato <code>media::file_type</code> para los nombres de columnas de archivos multimedia (por ejemplo, <code>media::image</code>, <code>media::video</code>, <code>media::audio</code>). El formato simplificado que usa solo el tipo de archivo multimedia sin el prefijo <code>media::</code> es ahora más comúnmente adoptado (por ejemplo, <code>image</code>, <code>video</code>, <code>audio</code>).
</p>

### Cargar archivos multimedia a KoboToolbox

Para cargar los archivos multimedia a KoboToolbox:
1. Ve a tu [cuenta de KoboToolbox](https://www.kobotoolbox.org/sign-up/).
2. En tu proyecto de KoboToolbox, navega a **CONFIGURACIONES > Archivos multimedia**.
3. Carga los archivos multimedia que has agregado a tu XLSForm, asegurándote de que el nombre del archivo sea exactamente el mismo.
4. Implementa o vuelve a implementar tu formulario para ver los cambios en los archivos multimedia.

![Cargar archivos multimedia](images/media/upload_media.png)

## Agregar archivos multimedia a opciones en XLSForm

Para agregar archivos multimedia a opciones de respuesta en tu XLSForm:
1. Agrega una [pregunta de tipo selección](../es/question_types_xls.md#tipos-de-pregunta-de-selección-múltiple) en la **hoja survey**.
2. En la **hoja choices**, agrega un **list_name** (nombre de la lista), **name** (nombre) y **label** (etiqueta) (opcional) para tus opciones.
    - Agregar una etiqueta es opcional al incluir un archivo multimedia. Si deseas usar los archivos multimedia como etiquetas de opciones, omite el texto de la etiqueta.
3. Agrega una columna para el archivo multimedia que deseas incluir. Nómbrala `image` (imagen), `video` o `audio`, según el tipo de archivo multimedia.
4. En la columna de archivos multimedia, en la fila de las opciones que has agregado, ingresa el nombre del archivo multimedia **incluyendo la extensión**.
    - Por ejemplo: `goat.png` o `fish.png`

**hoja survey**

| name | type | label |
| :--- | :--- | :--- |
| select_one animals | animals | ¿Cuál de estos es tu animal favorito? |
| survey |

**hoja choices**

| list_name | name | label | image |
| :--- | :--- | :--- | :--- |
| animals | goats | Cabras | goat.png |
| animals | cows | Vacas | cow.png |
| animals | chicken | Pollos | chicken.png |
| animals | pigs | Cerdos | pig.png |
| animals | fish | Peces | fish.png |
| choices |

### Cargar archivos multimedia a KoboToolbox

Para cargar los archivos multimedia a KoboToolbox:
1. Ve a tu [cuenta de KoboToolbox](https://www.kobotoolbox.org/sign-up/).
2. En tu proyecto de KoboToolbox, navega a **CONFIGURACIONES > Archivos multimedia**.
3. Carga los archivos multimedia que has agregado a tu XLSForm, asegurándote de que el nombre del archivo sea exactamente el mismo.
4. Implementa o vuelve a implementar tu formulario para ver los cambios en los archivos multimedia.

## Agregar archivos multimedia a traducciones

En XLSForms que están [traducidos en varios idiomas](../es/language_xls.md), puedes incluir diferentes archivos multimedia para cada idioma agregando nuevas columnas **image** (imagen), **audio** o **video**.

Para agregar archivos multimedia para diferentes idiomas en tu hoja survey:

1. Cambia el nombre de tus columnas de archivos multimedia usando el formato **tipo_de_multimedia::idioma (código)**, donde `tipo_de_multimedia` es el tipo de archivo multimedia e `idioma` es el idioma predeterminado.
    - Por ejemplo: `image::English (en)`
2. Agrega una nueva columna de archivos multimedia para cada idioma de traducción usando el formato **tipo_de_multimedia::idioma (código)**.
    - Por ejemplo: `audio::Spanish (es)`
3. En la columna de archivos multimedia para cada idioma, ingresa el nombre del archivo multimedia que deseas incluir, incluyendo la extensión.
    - Para usar el mismo archivo multimedia para cada idioma, ingresa el mismo nombre de archivo que el de la columna del idioma predeterminado.

<p class="note">
    <strong>Nota:</strong> Si un archivo multimedia no aparece en una columna de traducción, no se mostrará para ese idioma.
</p>

**hoja survey**

| type | name | label | video::English (en) | video::Chichewa (ny) |
| :--- | :--- | :--- | :--- | :--- |
| note | intro | Antes de responder el formulario, mira el video a continuación: | intro.mp4 | intro_ny.mp4 |
| survey |

### Cargar archivos multimedia a KoboToolbox

Para cargar los archivos multimedia traducidos a KoboToolbox:
1. Ve a tu [cuenta de KoboToolbox](https://www.kobotoolbox.org/sign-up/).
2. En tu proyecto de KoboToolbox, navega a **CONFIGURACIONES > Archivos multimedia**.
3. Carga los archivos multimedia que has agregado a tu XLSForm, asegurándote de que el nombre del archivo sea exactamente el mismo.
4. Implementa o vuelve a implementar tu formulario para ver los cambios en los archivos multimedia.

<p class="note">
    <strong>Nota:</strong> Para obtener más información sobre cómo gestionar traducciones en XLSForm, consulta <a href="../es/language_xls.md">Añadir traducciones en XLSForm</a>.
</p>

## Solución de problemas

<details>
<summary><strong>Error al implementar o ver el formulario</strong></summary>
Si enfrentas un error al implementar o ver tu formulario, verifica lo siguiente:
    <ul>
      <li>El archivo multimedia se ha cargado a KoboToolbox en la ventana <strong>Archivos multimedia</strong> de la página <strong>CONFIGURACIONES</strong>.</li>
      <li>El nombre del archivo en tu XLSForm coincide exactamente con el nombre del archivo multimedia y la extensión.</li>
    </ul>
</details>

<br>

<details>
<summary><strong>Los archivos multimedia no aparecen en el formulario implementado</strong></summary>
Si los archivos multimedia no aparecen en tu formulario implementado, verifica lo siguiente:
    <ul>
      <li>El archivo multimedia se ha cargado a KoboToolbox en la ventana <strong>Archivos multimedia</strong> de la página <strong>CONFIGURACIONES</strong>.</li>
      <li>El nombre del archivo en tu XLSForm coincide exactamente con el nombre del archivo multimedia y la extensión.</li>
      <li>El formulario se ha <strong>vuelto a implementar</strong> desde que cargaste los archivos multimedia.</li>
      <li>Has incluido archivos multimedia para cada traducción del formulario, si corresponde.</li>
    </ul>
</details>

<br>

<details>
<summary><strong>Cambiar el tamaño de un archivo multimedia</strong></summary>
Para controlar el tamaño de las imágenes mostradas en tus preguntas u opciones, debes cargar archivos multimedia con las dimensiones deseadas. Ten en cuenta que usar archivos muy grandes puede aumentar los tiempos de carga en los formularios de Enketo.
</details>

<br>

<details>
<summary><strong>El formulario tarda mucho en cargar</strong></summary>
Los formularios de Enketo se cargarán lentamente si tus archivos multimedia son grandes. Reduce el tamaño de los archivos de imagen, video o audio antes de cargarlos al servidor para mejorar los tiempos de carga.
</details>

<br>

<details>
<summary><strong>Cambiar la alineación de los archivos multimedia</strong></summary>
Los archivos multimedia en los formularios de KoboToolbox están alineados al centro de forma predeterminada, y la alineación personalizada (izquierda o derecha) no es posible.
</details>

<br>

<details>
<summary><strong>Los archivos GIF animados no son compatibles</strong></summary>
Los archivos GIF animados no son compatibles actualmente ni con los formularios web de Enketo ni con la aplicación Android KoboCollect.
</details>

<br>

<details>
<summary><strong>No se puede cargar el archivo multimedia</strong></summary>
El tamaño máximo para cargas de archivos multimedia es de 100 MB. Los archivos que excedan este límite deben reducirse de tamaño antes de cargarlos.
</details>