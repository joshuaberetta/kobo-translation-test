# Tipos de preguntas "Seleccionar una" y "Seleccionar varias"

Cuando tienes una pregunta categórica con una lista de opciones predefinidas para que los/as encuestados/as elijan, debes elegir el tipo de pregunta "Seleccionar una" o "Seleccionar varias" en KoboToolbox. El tipo de pregunta "Seleccionar una", también conocido como pregunta de "respuesta única", significa que el/la encuestado/a solo puede seleccionar una única respuesta de una lista de opciones. De manera similar, el tipo de pregunta "Seleccionar varias" también se conoce como pregunta de "respuesta múltiple" donde el/la encuestado/a puede seleccionar múltiples respuestas de una lista de opciones.

Los tipos de preguntas "Seleccionar una" y "Seleccionar varias" pueden ser mejores opciones para mantener la calidad de los datos cuando la pregunta tiene un alcance limitado y definido. Esto se debe a que, a diferencia de la naturaleza abierta del tipo de pregunta "Texto", los dos tipos de preguntas de selección limitan al usuario a las opciones listadas.

## Cuándo usarlos

Usa el tipo de pregunta "Seleccionar una" cuando una pregunta tiene una lista de opciones y el/la encuestado/a está limitado/a a solo una opción de la lista. Los ejemplos incluyen estado civil, sexo o religión.

Usa el tipo de pregunta "Seleccionar varias" si hay una lista de opciones y el/la encuestado/a puede considerar apropiado seleccionar más de una opción. Los ejemplos incluyen fuentes de ingresos del hogar o una lista de activos del hogar.

## Configurar la pregunta y las opciones

Sigue los mismos pasos para configurar una pregunta "Seleccionar una" o "Seleccionar varias":

-   En el editor de formularios de KoboToolbox (Formbuilder), click en el botón <i class="k-icon k-icon-plus"></i> para agregar una nueva pregunta.
-   Escribe la etiqueta de la pregunta, por ejemplo, "¿Cuál es tu estado civil?". Luego click en **+ Add Question** (o presiona **Enter**).
-   Elige el tipo de pregunta ("Seleccionar una" o "Seleccionar varias")
-   Escribe las etiquetas de respuesta donde dice "Option 1", "Option 2". Agrega más opciones si es necesario.

<p class="note">
  Puedes reordenar tu lista de opciones haciendo click y arrastrando cada elemento a una nueva posición en la lista.
</p>

Click en el ícono de papelera <i class="k-icon k-icon-trash"></i> a la izquierda de la etiqueta de la opción para eliminarla.

## Traducir etiquetas de preguntas y opciones

Para traducir preguntas de tipo selección y sus etiquetas a otros idiomas a través de la interfaz de usuario de KoboToolbox, consulta el artículo de ayuda [Agregar otro idioma en el panel del proyecto](language_dashboard.md), o [aquí](language_xls.md) si estás creando tu formulario usando XLSForm.

## Valores XML

Al configurar las respuestas de las preguntas "Seleccionar una" y "Seleccionar varias", tienes la opción de especificar los valores XML o dejar que KoboToolbox los genere automáticamente.

<p class="note">
  Se recomienda encarecidamente que especifiques valores XML para <strong>todas las preguntas y opciones</strong> antes de desplegar tu formulario, <em>especialmente</em> si las etiquetas están en idiomas con caracteres no latinos como chino, árabe o nepalí.
</p>

Los valores XML son los valores que se guardan en el envío cuando un usuario elige la respuesta, no la etiqueta. En el editor de formularios, escribe los valores donde dice "AUTOMATIC" como se muestra a continuación.

![XML Values](/images/select_one_and_select_many/xml_values.png)

Las opciones predefinidas para las preguntas "Seleccionar una" y "Seleccionar varias" a veces pueden ser insuficientes al recolectar datos. Es posible incluir la opción de una respuesta de texto en ese caso, como se describe en nuestro artículo de ayuda [Respuestas "Otras" especificadas por el usuario para preguntas de opción múltiple](user_specified_other.md).

## Cómo se muestran por defecto en formularios web y KoboCollect

![Comparison of select one and select many on Enketo and KoboCollect](/images/select_one_and_select_many/select_one_select_many_comparison.png)

Puedes diferenciar fácilmente entre una pregunta "Seleccionar una" y "Seleccionar varias" en un formulario de entrada de datos. La pregunta "Seleccionar una" tiene opciones con un botón de radio (aparece un punto sólido después de seleccionar un elemento) mientras que la pregunta "Seleccionar varias" tiene opciones con una casilla de verificación cuadrada (aparecen marcas de verificación después de seleccionar elementos).

## Opciones de exportación

Al exportar preguntas "Seleccionar varias", puedes elegir entre exportar todas las respuestas seleccionadas en una sola columna o tener las opciones en columnas separadas o ambas. Lee más sobre exportar y descargar datos en [este artículo de ayuda](export_download.md).

## Aspectos avanzados

Al agregar preguntas "Seleccionar una" y "Seleccionar varias", puedes elegir entre una amplia gama de aspectos. Los aspectos cambian la forma en que se muestra la pregunta en los formularios web o KoboCollect.

![Appearances](/images/select_one_and_select_many/appearances.png)

<p class="note">
  La opción "other" te proporciona un espacio donde puedes escribir un aspecto diferente que no se muestra en la lista.
</p>

La siguiente tabla muestra los diferentes aspectos disponibles y cómo se muestran tanto en los formularios web como en KoboCollect.

![Appearances](/images/select_one_and_select_many/select_one_select_many_table.png)

<p class="note">
  Los aspectos "quick", "likert" y "quickcompact" solo son aplicables a preguntas "Seleccionar una".
</p>