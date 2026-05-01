# Apariencia de preguntas en XLSForm

La apariencia de preguntas te permite personalizar cómo se muestran las preguntas en el formulario y el tipo de respuestas que recolectan. Este artículo explica cómo agregar apariencias de preguntas en XLSForm y enumera las apariencias comunes por tipo de pregunta.

Es importante tener en cuenta que algunas apariencias solo funcionan en [formularios web de Enketo](https://support.kobotoolbox.org/enketo.html), mientras que otras solo son compatibles con [KoboCollect](https://support.kobotoolbox.org/kobocollect_on_android_latest.html). Considera tu método de recolección de datos al seleccionar apariencias.

<p class="note">
  <b>Nota:</b> Este artículo se enfoca en configurar apariencias de preguntas en <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">XLSForm</a>. Para aprender sobre cómo configurar apariencias en el editor de formularios de KoboToolbox (Formbuilder), consulta la documentación <a href="https://support.kobotoolbox.org/using-formbuilder.html">Usar el Formbuilder</a>.
<br><br>
Para práctica con apariencias de preguntas en XLSForm, consulta el <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">curso XLSForm Fundamentals</a> de la KoboToolbox Academy.
</p>

## Agregar apariencias de preguntas

Para agregar apariencias de preguntas en XLSForm:
1. En la hoja de trabajo `survey`, añade una columna **appearance**.
2. Ingresa el nombre de la apariencia en la columna `appearance`. Asegúrate de usar la ortografía y puntuación exactas del nombre de la apariencia.
3. Algunas apariencias se pueden combinar y aplicar a la misma pregunta. Combina apariencias ingresándolas en la misma celda y separándolas con un espacio.

**hoja de trabajo survey**

| type | name | label | appearance |
| :--- | :--- | :--- | :--- |
| text | description | Describe el proyecto. | multiline |
| select_one country_list | country | ¿En qué país se está llevando a cabo este proyecto? | autocomplete minimal |
| survey |


## Apariencias de preguntas disponibles en XLSForm
Las tablas a continuación enumeran las apariencias de preguntas comunes por tipo de pregunta y muestran cuáles son compatibles con formularios web de Enketo y KoboCollect.

### Tipos de pregunta de selección múltiple
Las preguntas de selección múltiple permiten a los/as encuestados/as [elegir entre opciones predefinidas](https://support.kobotoolbox.org/question_types_xls.html#select-question-types).

| Apariencia | Descripción | Compatibilidad |
| :--- | :--- | :--- |
| `minimal` | Muestra las opciones en un menú desplegable. | Enketo y KoboCollect |
| `compact` | Muestra las opciones una al lado de la otra con espaciado mínimo y sin casillas de selección. | Enketo y KoboCollect |
| `label` | Muestra las etiquetas de las opciones sin las casillas de selección. | Enketo y KoboCollect |
| `list-nolabel` | Muestra las casillas de selección sin las etiquetas. | Enketo y KoboCollect |
| `autocomplete` | Agrega una barra de búsqueda en la parte superior de la lista de opciones. | Enketo y KoboCollect (combinar con apariencia minimal) |
| `horizontal` | Muestra las opciones de respuesta horizontalmente en columnas. | Solo Enketo |
| `horizontal-compact` | Muestra las opciones de respuesta horizontalmente, con espaciado mínimo y sin casillas de selección. | Solo Enketo |
| `likert` | Muestra las opciones de respuesta como una escala Likert (solo `select_one`). | Enketo y KoboCollect  |
| `quick` | Avanza automáticamente el formulario a la siguiente pregunta después de seleccionar una respuesta (solo `select_one`). | Solo KoboCollect |
| `quickcompact` | Muestra las opciones una al lado de la otra con espaciado mínimo y sin casillas de selección, y avanza automáticamente a la siguiente pregunta después de seleccionar una respuesta (solo `select_one`). | Solo KoboCollect |
| `columns` | Muestra las opciones disponibles en 2, 3, 4 o 5 columnas dependiendo del tamaño de la pantalla. | Enketo y KoboCollect |
| `columns-pack` | Muestra las opciones disponibles con tantas como sea posible en una línea. | Enketo y KoboCollect |
| `columns-n` | Muestra las opciones disponibles en el número especificado (n) de columnas. | Enketo y KoboCollect |
| `map` | Muestra un mapa para seleccionar opciones. Requiere <a href="https://support.kobotoolbox.org/select_from_map_xls.html">definir coordenadas GPS</a> en la hoja `choices` (solo `select_one`). | Solo KoboCollect |
| `quick map` | Muestra un mapa para seleccionar opciones, registrando automáticamente la primera ubicación seleccionada sin mostrar información adicional. Requiere <a href="https://support.kobotoolbox.org/select_from_map_xls.html">definir coordenadas GPS</a> en la hoja `choices` (solo `select_one`). | Solo KoboCollect |

<p class="note">
  <b>Nota:</b> Las apariencias para preguntas <code>select_one</code> y <code>select_multiple</code> también se pueden usar para preguntas de <a href="https://support.kobotoolbox.org/select_from_file_xls.html">selección desde archivo</a>.
</p>

### Tipos de pregunta número (enteros y decimales)
Las preguntas numéricas se utilizan para [recolectar números enteros o números decimales](https://support.kobotoolbox.org/question_types_xls.html#numeric-question-types).

| Apariencia | Descripción | Compatibilidad |
| :--- | :--- | :--- |
| `thousands-sep` | Formatea números grandes usando un separador de coma para miles. | Enketo y KoboCollect |
| `bearing` | Registra una lectura de brújula en grados (solo `decimal`). | Solo KoboCollect  |
| `counter` | Muestra botones para aumentar y disminuir dígitos (solo `integer`). | Solo KoboCollect |


### Tipo de pregunta rango
Las preguntas de rango se utilizan para [seleccionar valores dentro de un rango especificado](https://support.kobotoolbox.org/question_types_xls.html#numeric-question-types).

| Apariencia | Descripción | Compatibilidad |
| :--- | :--- | :--- |
| `vertical` | Cambia la orientación de la línea numérica a una línea vertical. | Enketo y KoboCollect |
| `picker` | En KoboCollect, muestra un selector giratorio emergente para seleccionar valores. En Enketo, muestra un menú desplegable. | Enketo y KoboCollect |
| `rating` | Muestra estrellas en lugar de una línea numérica. | Enketo y KoboCollect |
| `distress` | Muestra un termómetro en lugar de una línea numérica. | Enketo y KoboCollect  |


### Tipo de pregunta texto
Las preguntas de texto permiten a los/as usuarios/as [recolectar respuestas abiertas](https://support.kobotoolbox.org/question_types_xls.html#text-and-note-question-types).

| Apariencia | Descripción | Compatibilidad |
| :--- | :--- | :--- |
| `numbers` | Muestra un teclado numérico en lugar de un teclado de texto (por ejemplo, para recolectar números de teléfono). | Solo KoboCollect |
| `multiline` | Muestra un cuadro de texto de múltiples líneas para respuestas de texto más largas. | Enketo y KoboCollect |
| `url` | Muestra una URL en la que se puede hacer clic debajo del texto de la pregunta y hace que la pregunta sea de solo lectura. Requiere ingresar una URL en la columna `default` de la pregunta, o en la columna `calculation` si la URL incluye valores dinámicos. También funciona con preguntas `note`. | Enketo y KoboCollect |
| `masked` | Enmascara el texto ingresado por el/la encuestado/a (por ejemplo, una contraseña o información confidencial). | Solo KoboCollect |


### Tipo de pregunta fecha
Las preguntas de fecha se utilizan para [capturar fechas específicas del calendario](https://support.kobotoolbox.org/question_types_xls.html#date-and-time-question-types).

| Apariencia | Descripción | Compatibilidad |
| :--- | :--- | :--- |
| `month-year` | Captura un mes y un año. | Enketo y KoboCollect |
| `year` | Captura solo un año. | Enketo y KoboCollect |
| `no-calendar` | Muestra un selector giratorio para seleccionar el día, mes y año, en lugar del selector de estilo calendario predeterminado. | Solo KoboCollect |
| `coptic` | Muestra el calendario copto. | Solo KoboCollect |
| `ethiopian` | Muestra el calendario etíope. | Solo KoboCollect |
| `islamic` | Muestra el calendario islámico. | Solo KoboCollect  |
| `bikram-sambat` | Muestra el calendario Bikram Sambat. | Solo KoboCollect |
| `myanmar` | Muestra el calendario de Myanmar. | Solo KoboCollect |
| `persian` | Muestra el calendario persa. | Solo KoboCollect |
| `buddhist` | Muestra el calendario budista. | Solo KoboCollect |


### Tipos de pregunta GPS
Las preguntas GPS se utilizan para [capturar las coordenadas geográficas](https://support.kobotoolbox.org/question_types_xls.html#gps-question-types) de una ubicación, ruta o área directamente dentro de tus formularios.

| Apariencia | Descripción | Compatibilidad |
| :--- | :--- | :--- |
| `maps` | Muestra un mapa para que los/as usuarios/as visualicen la ubicación que se está registrando automáticamente (solo `geopoint`). | Solo KoboCollect (incluido en la apariencia predeterminada de Enketo)  |
| `placement-map` | Permite la selección manual de una ubicación en un mapa (solo `geopoint`). | Solo KoboCollect (incluido en la apariencia predeterminada de Enketo)  |
| `hide-input` | Muestra un mapa más grande y oculta otros campos de entrada (latitud, longitud, altitud, precisión). | Solo Enketo |


### Preguntas de imagen
Las preguntas de imagen permiten a los/as usuarios/as [cargar o registrar imágenes](https://support.kobotoolbox.org/question_types_xls.html#media-question-types) directamente en sus formularios.

| Apariencia | Descripción | Compatibilidad |
| :--- | :--- | :--- |
| `signature` | Permite a los/as usuarios/as dibujar su firma. | Enketo y KoboCollect |
| `draw` | Permite a los/as usuarios/as hacer bocetos o crear dibujos. | Enketo y KoboCollect |
| `annotate` | Permite a los/as usuarios/as anotar una imagen dibujando o escribiendo sobre ella. | Enketo y KoboCollect |
| `new` | Solicita a los/as usuarios/as tomar una nueva foto usando la cámara del dispositivo (sin carga de archivo). | Solo KoboCollect |
| `new-front` | Solicita a los/as usuarios/as tomar una nueva foto usando la cámara frontal del dispositivo. | Solo KoboCollect |


### Preguntas de código de barras
Las preguntas de código de barras permiten a los/as usuarios/as [escanear un código QR](https://support.kobotoolbox.org/question_types_xls.html#media-question-types) usando la cámara del dispositivo en KoboCollect.

| Apariencia | Descripción | Compatibilidad |
| :--- | :--- | :--- |
| `hidden-answer` | Oculta el valor del código de barras escaneado. | Solo KoboCollect |