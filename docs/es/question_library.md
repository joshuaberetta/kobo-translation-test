# Uso de La biblioteca de preguntas

## Agregar preguntas a tu biblioteca

Las preguntas que se han agregado previamente a tu biblioteca se pueden añadir a cualquier otro formulario arrastrándolas y soltándolas desde la barra lateral de La biblioteca de preguntas dentro del editor de formularios de KoboToolbox (Formbuilder).

Para acceder a la barra lateral de La biblioteca de preguntas, haz click en el botón **Añadir desde la biblioteca** en la esquina superior derecha de la barra de herramientas del editor de formularios.

![image](/images/question_library/library.jpg)

Si es necesario, puedes buscar la pregunta que estás buscando utilizando la función de búsqueda para buscar por palabra clave o etiqueta.

Para añadir la pregunta a tu formulario, **arrástrala y suéltala** en la posición deseada. Una pregunta se puede añadir varias veces si es necesario, por ejemplo, cuando se reutiliza una escala específica para diferentes preguntas.

## Administrar preguntas en tu biblioteca

La biblioteca de preguntas te permite guardar y reutilizar preguntas de uso frecuente.

Para administrar La biblioteca de preguntas, haz click en el botón del menú de la biblioteca en la barra lateral superior izquierda. De forma predeterminada, la biblioteca mostrará todas tus preguntas. Puedes **ver** o editar cada pregunta individual haciendo click en la etiqueta de la colección.

Para **clonar** o **descargar** la colección, coloca el cursor sobre la etiqueta de la colección y los íconos aparecerán en el lado derecho.

También puedes **añadir nuevas preguntas** desde dentro de la biblioteca. Solo haz click en **Nuevo** y podrás crear una nueva pregunta que se guarda en la biblioteca.

Para **eliminar preguntas** en tu biblioteca, simplemente haz click en **Eliminar** después de hacer click en el ícono **Más acciones**.

![image](/images/question_library/delete.jpg)

## Importar colecciones

Además de crear colecciones en la interfaz, también puedes importar grandes conjuntos de preguntas y bloques desde Excel, basados en el formato estándar XLSForm. Los/as usuarios/as avanzados/as encontrarán más práctico comenzar desde XLSForms existentes que copiar el contenido de preguntas existentes en la herramienta uno por uno.

![image](/images/question_library/import_collection.png)

De forma predeterminada, cada archivo XLS se importará como una nueva colección. Si tu archivo solo contiene una pregunta o un bloque, se importará solo esa pregunta o ese bloque en lugar de crear una colección. El nombre de la colección se toma del nombre del archivo (se permiten duplicados de colecciones existentes). Pero es fácil cambiar el nombre de la colección después de importarla: solo haz click en el nombre de la colección en la barra lateral izquierda y luego haz click en el ícono de configuración.

Usa <a download class="reference" href="./_static/files/question_library/collection_import_sample.xlsx">este archivo de Excel como plantilla</a>.
El archivo generalmente sigue el formato XLSForm. Hay algunas diferencias:

* La hoja principal que contiene las preguntas debe llamarse **library** al cargar múltiples bloques.
* (Opcional) Los bloques de preguntas deben definirse en la columna adicional llamada **block**, escribiendo el mismo título de bloque en cada fila de la tabla que debe incluirse en el bloque. La etiqueta del bloque no tiene limitaciones en términos de caracteres, pero debe tener exactamente la misma ortografía para evitar dividir el bloque ('Household questions' es diferente de 'household questions'). Usa un título de bloque que facilite identificar el contenido más adelante.
* Cualquier fila en la hoja de plantilla que no tenga un valor en la columna block se importará como una pregunta separada.
* (Opcional) Define cualquier etiqueta para la pregunta o bloque añadiendo una columna **tag:[nombre de tu etiqueta]** para cada etiqueta, luego escribe '1' en cada fila que deba usar la etiqueta. En el caso de bloques, es suficiente escribir '1' en cualquiera de las filas del bloque sin importar cuál. Es suficiente marcar una de las preguntas en el bloque, aunque no importa si se etiquetan varias preguntas.

Algunas otras sugerencias:

* Puedes incluir grupos en bloques. Solo asegúrate de que la línea 'begin group' tenga un ID de 'name' único (como en todos los XLSForms) y que la apertura (begin group) y el cierre (end group) estén incluidos en el bloque. Añadir el nombre del bloque como etiqueta del grupo podría ser una buena idea para que veas la etiqueta del bloque después de importarlo al editor de formularios.
* Puedes incluir lógica de omisión y reglas de validación dentro de los bloques que importas. Eso es muy útil al importar bloques completos de preguntas en nuevos borradores de formularios sin tener que reconstruir estas configuraciones avanzadas.
* Puedes añadir múltiples idiomas a las etiquetas de preguntas y respuestas con la sintaxis habitual de XLSForm (label::English (en), label::Español (es), etc.)