# Añadir lógica de omisión en el Formbuilder

<iframe src="https://www.youtube.com/embed/uLSnoG0mqV4?si=63o4YeQUZWOsZmfF" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

La lógica de omisión, también conocida como ramificación o condiciones de relevancia, controla qué preguntas se muestran en un formulario. De forma predeterminada, todas las preguntas son visibles. La lógica de omisión determina bajo qué condición(es) debe aparecer una pregunta. Las condiciones de lógica de omisión siempre se aplican a la pregunta o grupo que debe ser condicionalmente visible.

<p class="note">
    <strong>Nota:</strong> Puedes aplicar lógica de omisión a <a href="group_repeat.html">grupos de preguntas</a> completos, así como a preguntas individuales. Esto puede simplificar la lógica del formulario y facilitar la gestión de cuestionarios complejos.
</p>

Hay dos métodos para añadir lógica de omisión en el Formbuilder: añadir una condición a través del **generador de lógica de omisión**, o ingresar manualmente la lógica de omisión en **código XLSForm**.

## Añadir una condición

Este primer método te permite usar el generador de lógica de omisión para añadir tus condiciones. Se recomienda para principiantes. Para añadir una condición de lógica de omisión, sigue estos pasos:

1. Abre la <i class="k-icon-settings"></i> **Configuración** en el menú lateral derecho de la pregunta o grupo que se mostrará condicionalmente.
2. Selecciona **Lógica de omisión** y haz click en **Añadir una condición**.
3. Selecciona la pregunta en el formulario que determinará si la pregunta actual se muestra o no.
4. Elige el operador lógico apropiado para tu condición (por ejemplo, >, =, !=).
5. En el campo **valor de respuesta**, selecciona o escribe la respuesta que se requiere para que se cumpla la condición.

La pregunta se mostrará solo cuando se cumpla la condición especificada.

Para añadir múltiples condiciones, añade tu primera condición y luego haz click en el botón **Añadir otra condición**. Cuando uses múltiples condiciones, especifica si al menos una de estas condiciones debe cumplirse o todas ellas.

<p class="note">
    <strong>Nota:</strong> Puedes eliminar condiciones de lógica de omisión haciendo click en el <i class="k-icon-trash"></i> icono de papelera.
</p>

## Ingresar manualmente la lógica de omisión en código XLSForm
Para usuarios/as avanzados/as, la lógica de omisión se puede ingresar directamente en código XLSForm. La estructura básica de las condiciones permanece sin cambios: necesitarás identificar la pregunta de control, elegir un operador lógico y escribir el valor de respuesta requerido.

Para ingresar manualmente la lógica de omisión en código XLSForm, sigue estos pasos:
1. Abre la <i class="k-icon-settings"></i> **Configuración** en el menú lateral derecho de la pregunta o grupo que se mostrará condicionalmente.
2. Selecciona **Lógica de omisión** y haz click en **Ingresar manualmente tu lógica de omisión en código XLSForm**.
3. Ingresa la condición en código XLSForm.

En código XLSForm, las preguntas se referencian por su **nombre de pregunta** (nombre de columna de datos) usando el formato `${nombre_pregunta}`. Por ejemplo, si P2 debe preguntarse solo si la respuesta a P1 es "Sí", la condición de lógica de omisión para P2 sería `${P1} = 'si'`.

<p class="note">
    Para más información sobre código XLSForm y operadores, consulta la <a href="https://xlsform.org/en/#relevant">documentación de XLSForm</a>.
</p>