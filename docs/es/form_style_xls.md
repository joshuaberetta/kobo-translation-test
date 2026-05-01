# Personalizar formularios usando XLSForm

Con KoboToolbox, puedes personalizar la apariencia de tus formularios y preguntas para resaltar información clave y adaptar el diseño a tus necesidades de recolección de datos. Esto incluye aplicar temas a los formularios web de Enketo, agregar encabezados y listas en preguntas de tipo nota, y usar color o formato en negrita para dar énfasis.

Este artículo cubre temas para formularios web de Enketo, así como opciones de diseño para notas y preguntas dentro de un formulario.

<p class="note">
<strong>Nota:</strong> Este artículo se enfoca en diseñar formularios en <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">XLSForm</a>. Para aprender sobre cómo configurar temas de Enketo en el editor de formularios de KoboToolbox (Formbuilder), ver <a href="https://support.kobotoolbox.org/alternative_enketo.html">Usar estilos alternativos de formularios web de Enketo</a>.
</p>

## Temas para formularios web de Enketo

Los temas de Enketo te permiten personalizar la apariencia y el diseño de los [formularios web de Enketo](https://support.kobotoolbox.org/enketo.html). Los temas se aplican solo a los formularios web de Enketo y no son visibles en KoboCollect.

### Agregar temas en XLSForm

Para agregar un tema en un XLSForm:
1. Añadir una columna **style** en tu **hoja settings**.
2. Especificar el tema que deseas usar, utilizando el nombre exacto que se muestra en la tabla a continuación.

**hoja settings**

| style       |
|:------------|
| theme-grid  |

<p class="note">
<strong>Nota:</strong> Los temas se pueden combinar ingresando ambos temas en la misma celda de la columna <code>style</code>, separados por un espacio (ej., <code>theme-grid pages</code>).
</p>

### Temas disponibles para formularios web de Enketo

Los siguientes temas están disponibles para personalizar tus formularios:

| Tema XLSForm                | Descripción                                                                 | Vista previa |
|:-----------------------------|:----------------------------------------------------------------------------|:--------|
| Tema predeterminado                | Muestra las preguntas una después de otra, en una sola página.                     | ![Default style](images/form_style_xls/theme_default.png) |
| <code>pages</code>           | Muestra una pregunta por pantalla o un <a href="https://support.kobotoolbox.org/grouping_questions_xls.html">grupo de preguntas</a> juntas en la misma pantalla, similar al diseño de KoboCollect. | ![Pages style](images/form_style_xls/theme_pages.png) |
| <code>theme-grid</code>      | Una visualización alternativa que es más compacta, similar a los formularios en papel, y utiliza el espacio de manera eficiente, organizando múltiples preguntas por fila. Las preguntas se muestran en mayúsculas de forma predeterminada. Requiere <a href="https://support.kobotoolbox.org/form_style_xls.html#setting-up-an-xlsform-for-theme-grid">configurar tu XLSForm</a>. | ![Theme-grid](images/form_style_xls/theme_grid.png) |
| <code>theme-grid no-text-transform</code> | Igual que theme-grid, pero sin la capitalización automática de las preguntas. | ![Theme-grid no-text-transform](images/form_style_xls/theme_grid_no_text_transform.png) |

### Configurar un XLSForm para theme_grid

En los formularios web de Enketo, el diseño `theme_grid` te permite mostrar preguntas en múltiples columnas, haciendo que tu formulario sea más compacto y visualmente organizado. La configuración de estas columnas, incluyendo cuántas hay y qué tan ancha debe ser cada una, se controla asignando `valores-w` a cada pregunta dentro de la columna **appearance** de tu XLSForm.

<p class="note">
  Para una descripción completa del uso de <code>theme_grid</code> en XLSForm, ver este <a href="https://ee.kobotoolbox.org/n41GqUkf">Tutorial de Tema Grid</a> y <a href="https://docs.google.com/spreadsheets/d/1qKmxPTA4B0vihU6GsKgi1CJE2Db2FfE7KZpOig4nTEI/edit?gid=0#gid=0">XLSForm de ejemplo</a>.
</p>

Antes de asignar `valores-w` a cada pregunta, comienza colocando todas las preguntas en [grupos de preguntas](https://support.kobotoolbox.org/grouping_questions_xls.html). El ancho predeterminado para un grupo o grupo de repetición es de cuatro columnas (`w4`), por lo que un grupo con `w4` puede contener un máximo de cuatro preguntas `w1` en una sola fila. El `valor-w` de una pregunta es relativo al `valor-w` de su grupo.

Para especificar el ancho relativo de cada pregunta dentro de una fila:
1. Añadir una columna **appearance** en tu **hoja survey**.
2. Para cada pregunta, asignar valores de apariencia (ej., `w1`, `w2`, `w3`) para especificar su ancho relativo dentro de una fila.
3. Modificar el ancho del grupo si es necesario usando el mismo enfoque.

Las filas siempre se expandirán automáticamente al ancho completo de la página. Por ejemplo, una fila que contiene una pregunta con un valor de apariencia de `w2` y otra con `w1` dividirá la fila en dos tercios y un tercio, respectivamente.

<p class="note">
<strong>Nota:</strong> Aplicar <code>valores-w</code> solo a grupos o grupos de repetición de nivel superior. Aunque aplicarlos a grupos o grupos de repetición anidados es compatible, puede que no se visualice bien.
</p>

## Diseñar texto

Puedes usar Markdown y HTML en XLSForm para **diseñar texto**, **agregar énfasis** con negrita o cursiva, **crear encabezados** de diferentes tamaños, **cambiar fuentes y colores**, y **agregar enlaces web en los que se puede hacer clic**. El diseño de texto se puede aplicar a preguntas, notas y etiquetas de opciones de respuesta.

<p class="note">
<strong>Nota:</strong> Algunas funcionalidades de diseño pueden no ser compatibles en KoboCollect o Enketo. Se recomienda previsualizar tus formularios en el método de recolección de datos que hayas elegido para confirmar que todas las funcionalidades de diseño sean totalmente compatibles.
</p>

Las funcionalidades de diseño de texto en XLSForm incluyen:
| Funcionalidad        | Formato |
|:---------------|:-----------|
| Cursiva        | `*cursiva*` o `_cursiva_` |
| Negrita           | `**negrita**` o `__negrita__` |
| Hipervínculo      | `[nombre del enlace](url)` |
| Encabezados        | `# Encabezado 1` (más grande) a `###### Encabezado 6` (más pequeño) |
| Listas con viñetas   | - Esta es una lista sin ordenar<br>- en markdown |
| Listas numeradas | 1. Esta es una lista numerada<br>2. en markdown |
| Emojis         | Por ejemplo, 🙂 😐 🙁 😦 😧 😩 😱 |
| Superíndice    | `100 m<sup>2</sup>` se convierte en 100 m² |
| Subíndice      | `H<sub>2</sub>O` se convierte en H₂O |
| Texto de color   | `<span style="color:#f58a1f">naranja</span>` se convierte en <span style="color:#f58a1f">naranja</span> <br>`<span style="color:red">rojo</span>` se convierte en <span style="color:red">rojo</span> |
| Fuente           | `<span style="font-family:cursive">cursiva</span>` se convierte en <span style="font-family:cursive">cursiva</span> <br>`<span style="color:red; font-family:cursive">rojo y cursiva</span>` se convierte en <span style="color:red; font-family:cursive">rojo y cursiva</span>|
| Alinear al centro   | `<p style="text-align:center">Etiqueta centrada</p>` centra el texto en la pantalla |

<p class="note">
<strong>Nota:</strong> Usar el carácter <code>\</code> antes de <code>#</code>, <code>*</code>, <code>_</code>, y <code>\</code> para evitar que los efectos de diseño especial se activen con estos caracteres.
</p>