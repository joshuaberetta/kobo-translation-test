# Opciones de preguntas en XLSForm

Al diseñar un formulario en XLSForm, puedes personalizar las preguntas agregando sugerencias, configurando aspectos, haciendo que una pregunta sea obligatoria y más. Para hacer esto, puedes agregar nuevas columnas en la **hoja survey** de tu XLSForm. Estas columnas se pueden agregar en cualquier lugar de la hoja de trabajo, siempre que el nombre de la columna se escriba exactamente como se requiere.

Este artículo cubre las opciones de preguntas más comunes y cómo agregarlas a tu XLSForm, incluyendo sugerencias de preguntas, preguntas obligatorias, respuestas predeterminadas y parámetros de preguntas.

<p class="note">
  <strong>Nota:</strong> Este artículo se centra en definir opciones de preguntas en <a href="../es/getting_started_xlsform.html">XLSForm</a>. Para aprender sobre las opciones de preguntas en el editor de formularios de KoboToolbox (Formbuilder), consulta <a href="../es/question_options.html">Usar las opciones de preguntas</a>.
<br><br>
Para práctica práctica con opciones de preguntas en XLSForm, consulta el <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">curso XLSForm Fundamentals</a> de la KoboToolbox Academy.
</p>

## Sugerencias de preguntas

Las **sugerencias de preguntas** te permiten agregar instrucciones o información adicional a tu formulario. Hay dos tipos de sugerencias que puedes agregar en XLSForm:
- Las **sugerencias comunes** se utilizan para proporcionar información adicional a los/as encuestados/as o encuestadores/as directamente en el formulario. Siempre están visibles y se muestran debajo de la etiqueta de la pregunta.
- Las **sugerencias adicionales** se utilizan para proporcionar información adicional durante el desarrollo del formulario, la capacitación de encuestadores/as o la recolección de datos. No se muestran de forma predeterminada.

### Agregar sugerencias de preguntas en XLSForm

Para agregar una **sugerencia común** en XLSForm:
1. Agrega una columna **hint** a la hoja `survey`.
2. En la misma fila que tu pregunta, ingresa el texto que debe mostrarse como sugerencia para esa pregunta.

Para agregar una **sugerencia adicional** en XLSForm:
1. Agrega una columna **guidance_hint** a la hoja `survey`.
2. En la misma fila que tu pregunta, ingresa el texto que debe incluirse como orientación adicional.

**hoja survey**

| type | name | label | hint | guidance_hint |
| :--- | :--- | :--- | :--- | :--- |
| integer | height | ¿Cuál es tu altura? | En centímetros | Si el/la encuestado/a no conoce su altura, ingresa 0 |
| survey |

<p class="note">
<strong>Nota:</strong> Las sugerencias de preguntas también se pueden traducir a varios idiomas. Para obtener más información sobre la traducción de formularios, consulta <a class="reference" href="../es/language_xls.html">Añadir traducciones en XLSForm</a>.
</p>

### Mostrar sugerencias adicionales en KoboCollect

En los formularios web de Enketo, las sugerencias adicionales aparecen en una sección plegable **Más detalles**. En KoboCollect, están ocultas de forma predeterminada, pero puedes [cambiar la configuración de tu proyecto](../es/kobocollect_settings.html#form-management-settings) para mostrarlas siempre o mostrarlas en una sección plegable.

Para mostrar sugerencias adicionales en KoboCollect, sigue los pasos a continuación:
1. Haz clic en el **ícono de Proyecto** en la esquina superior derecha de tu pantalla.
2. Haz clic en **Ajustes**.
3. En **Gestión de formularios**, selecciona **Mostrar orientación para preguntas**.
4. Elige una opción de visualización: **No**, **Sí - siempre mostrado** o **Sí - contraído**.

<p class="note">
<strong>Nota:</strong> Las sugerencias adicionales siempre se muestran en los formularios impresos.
</p>

## Preguntas obligatorias

De forma predeterminada, las preguntas en un formulario son opcionales. Configurar una pregunta como **obligatoria** hace que sea obligatorio que el/la encuestado/a responda. Esto puede ser útil para garantizar que los envíos estén completos y evitar datos faltantes.

<p class="note">
<strong>Nota:</strong> Las condiciones de lógica de omisión tienen prioridad sobre la configuración <strong>obligatoria</strong>, lo que significa que si una pregunta obligatoria está oculta por la lógica de omisión, ya no es obligatorio responderla.
</p>

Para configurar una pregunta como obligatoria en XLSForm:
1. Agrega una columna `required` a la hoja `survey`.
2. En la columna `required`, ingresa cualquiera de los siguientes: **TRUE**, **true** o **yes**.
3. Para preguntas opcionales, deja la columna `required` en blanco o ingresa cualquiera de los siguientes: **FALSE**, **false** o **no**.

Si un/a encuestado/a no responde una pregunta obligatoria, no podrá continuar a la siguiente página ni enviar el formulario. Se mostrará el mensaje obligatorio predeterminado "Este campo es obligatorio".

<p class="note">
<strong>Nota:</strong> Solo las preguntas que requieren una entrada deben marcarse como obligatorias en tu XLSForm. Si las preguntas de tipo <code>note</code> se marcan como obligatorias, no podrás continuar ni enviar el formulario.
</p>

### Cambiar el mensaje obligatorio predeterminado

Puedes cambiar el mensaje obligatorio predeterminado en tu XLSForm siguiendo los pasos a continuación:

1. Agrega una columna **required_message** a la hoja `survey`.
2. Ingresa el texto que deseas mostrar cuando los/as usuarios/as dejen una pregunta obligatoria en blanco.

**hoja survey**

| type | name | label | required | required_message |
| :--- | :--- | :--- | :--- | :--- |
| select_one education | education_level | ¿Cuál es el nivel más alto de educación que has completado? | TRUE | |
| integer | age | ¿Cuál es tu edad? | TRUE | Por favor responde a esta pregunta antes de continuar. |
| survey |

<p class="note">
<strong>Nota:</strong> Se puede usar lógica de formulario personalizada para hacer que una pregunta sea obligatoria u opcional según una respuesta anterior. Para obtener más información sobre la lógica obligatoria basada en condiciones, consulta <a class="reference" href="../es/required_logic_xls.html">Añadir lógica de obligación en un XLSForm</a>.
</p>

## Respuestas predeterminadas

Una **respuesta predeterminada** completa una pregunta con una respuesta predefinida basada en una respuesta común o esperada. La respuesta predeterminada puede ser fija o [determinada dinámicamente](../es/question_options_xls.html#setting-dynamic-default-responses) según la respuesta a una pregunta anterior.

La respuesta predeterminada se registrará como la respuesta final cuando se envíe el formulario **a menos que sea modificada por el/la encuestado/a** durante la recolección de datos. Para evitar que los/as encuestados/as editen una respuesta predeterminada, agrega una columna **read-only** y configúrala como **TRUE**.

<p class="note">
<strong>Nota:</strong> Aunque las respuestas predeterminadas pueden hacer que la recolección de datos sea más eficiente al completar previamente el formulario con respuestas esperadas o comunes, también corren el riesgo de introducir sesgos o errores en los datos, y deben usarse con precaución.
</p>

Para configurar una respuesta predeterminada fija en XLSForm:
1. Agrega una columna **default** a la hoja `survey`.
2. Ingresa la respuesta predeterminada, siguiendo el [formato apropiado](../es/question_options_xls.html#default-response-format) para el tipo de pregunta.

**hoja survey**

| type | name | label | default |
| :--- | :--- | :--- | :--- |
| text | name | ¿Cuál es tu nombre? | John Doe |
| integer | age | ¿Cuál es tu edad? | 50 |
| select_one marital_options | marital_status | ¿Cuál es tu estado civil? | married |
| select_multiple income_options | income_sources | ¿Cuáles son tus fuentes de ingresos? | formal_work farm_business |
| date | dob | ¿Cuándo naciste? | 1990-03-25 |
| date | interview_date | ¿Cuándo se realizó esta entrevista? | today() |
| survey |

### Formato de respuesta predeterminada

El formato de la respuesta predeterminada depende del tipo de pregunta y los datos que se recolectan:

| Tipo de pregunta | Formato de respuesta predeterminada |
| :--- | :--- |
| integer | Número |
| text | Texto (sin comillas) |
| select_one | **Nombre** de la opción (como se define en la hoja choices) |
| select_multiple | **Nombre(s)** de la opción, separados por un **espacio** si hay varios |
| date | Fecha en formato AAAA-MM-DD. Si es necesario, antepón la fecha con una comilla simple (') en Excel para evitar posibles problemas de formato. |

### Configurar respuestas predeterminadas dinámicas

Las respuestas predeterminadas ingresadas en el campo `default` deben ser valores fijos. Para configurar una **respuesta predeterminada dinámica** basada en una respuesta anterior, usa las columnas **calculation** y **trigger** en lugar de la columna `default`:
1. En la columna `calculation`, ingresa la **referencia a la pregunta** que completará dinámicamente la respuesta predeterminada.
2. En la columna `trigger`, ingresa la pregunta que activará el cálculo.
    - Por lo general, esta sería la misma pregunta a la que se hace referencia en la columna `calculation`, de modo que cualquier cambio en la pregunta de activación también actualizará la respuesta predeterminada.

**hoja survey**

| type | name | label | calculation | trigger |
| :--- | :--- | :--- | :--- | :--- |
| text | hh_name | Nombre del/la jefe/a de hogar | | |
| text | phone | Número de teléfono del hogar | | |
| text | phone_name | Nombre del/la propietario/a del teléfono | ${hh_name} | ${hh_name} |
| survey |

## Parámetros de preguntas

Los parámetros de preguntas en XLSForm te permiten ajustar cómo se comportan tus preguntas más allá de la configuración básica.

Para agregar parámetros de preguntas en XLSForm:
1. Agrega una columna **parameters** a la hoja `survey`.
2. Ingresa el [parámetro](../es/question_options_xls.html#common-question-parameters) apropiado para tu tipo de pregunta.
3. Algunos parámetros se pueden combinar y aplicar a la misma pregunta. Combina parámetros ingresándolos en la misma celda y separándolos con un espacio.

**hoja survey**

| type | name | label | parameters |
| :--- | :--- | :--- | :--- |
| select_one reasons | reasons | Por favor selecciona todas las razones que apliquen. | randomize=true |
| range | phone | Por favor selecciona un número entre 1 y 5. | start=1 end=5 step=1 |
| survey |

### Parámetros de preguntas comunes

Los diferentes tipos de preguntas en `XLSForm` tienen diferentes parámetros. Los parámetros más comunes son:

| Parámetro | Tipo de pregunta | Descripción |
| :--- | :--- | :--- |
| randomize=true | rank, select_one, select_multiple | Aleatoriza el orden de las opciones de respuesta |
| start=1 end=5 step=1 | range | Define el valor mínimo, el valor máximo y el intervalo entre números |
| capture-accuracy=20 | geopoint | Especifica la precisión GPS mínima aceptable (en metros) para capturar automáticamente una ubicación |
| warning-accuracy=50 | geopoint | Activa un mensaje de advertencia si la precisión del GPS no está dentro del umbral de precisión especificado |
| max-pixels=480 | image | Limita los píxeles máximos para una foto, para reducir el tamaño del archivo de imagen y mejorar la velocidad de carga |
| quality=low | audio | Captura una grabación de audio de menor calidad |
| quality=voice-only | audio | Captura la grabación de audio de menor calidad |

## Opciones de preguntas adicionales

Los XLSForms pueden incluir columnas adicionales en la hoja survey para formularios y funcionalidades más avanzados. A continuación se enumeran algunos.

| Columna XLSForm | Descripción |
| :--- | :--- |
| read_only | Si se ingresa `yes` en el campo `read_only`, la pregunta no puede ser editada por el/la encuestado/a. Los campos `read_only` se pueden combinar con los campos `default` o `calculation` para mostrar información al/la encuestado/a. |
| trigger | La columna trigger se puede usar para ejecutar un cálculo solo cuando se cambia la respuesta a otra pregunta visible en el formulario. Para obtener más información, consulta la <a href="https://xlsform.org/en/#trigger">documentación de XLSForm</a>. |
| body::accept | Para limitar los tipos de archivo aceptados para preguntas de tipo `file`, especifica las extensiones de archivo en la columna `body::accept`, separadas por una coma (por ejemplo, .pdf, .doc). |

También se pueden agregar otras columnas para incorporar lógica de formulario en tu XLSForm.

<p class="note">
    Para obtener más información sobre cómo agregar lógica de formulario, consulta <a href="../es/skip_logic_xls.html">Añadir lógica de salto a un XLSForm</a>, <a href="../es/constraints_xls.html">Agregar restricciones a un XLSForm</a>, <a href="../es/required_logic_xls.html">Añadir lógica de obligación en un XLSForm</a>, <a href="../es/choice_filters_xls.html">Agregar filtros de selección a un XLSForm</a> y <a href="../es/calculations_xls.html">Agregar cálculos a un XLSForm</a>.
</p>