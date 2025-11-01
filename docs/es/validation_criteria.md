# Añadir criterios de validación en el editor de formularios de KoboToolbox (Formbuilder)

<iframe src="https://www.youtube.com/embed/ya9usVpEo9Q?si=-rDzXcCRazcY0Bws" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

La lógica de validación, también conocida como criterios de validación o restricciones, define las condiciones para una respuesta aceptable a una pregunta. Esta funcionalidad ayuda a garantizar datos de alta calidad al prevenir respuestas accidentales o inválidas.

Los criterios de validación se pueden aplicar a cualquier tipo de pregunta. Por ejemplo, puedes usarlos para asegurar que un/a participante tenga más de cierta edad, que una fecha esté dentro de un rango específico, o que una entrada de texto coincida con un patrón determinado.

Existen dos métodos para añadir criterios de validación en el editor de formularios: añadir una condición a través del **generador de criterios de validación**, o ingresar manualmente la lógica de validación en **código XLSForm.**


## Añadir una condición

El generador de criterios de validación te permite añadir condiciones para preguntas de tipo **Texto**, **Número**, **Decimal** y **Fecha**. No es compatible con preguntas de tipo **Seleccionar una** o **Seleccionar varias**. Para usar el generador:
1. Abre <i class="k-icon-settings"></i> **Ajustes** en el menú lateral derecho de la pregunta.
2. Selecciona **Criterios de validación** y click en **Añadir una condición.**
3. Elige el operador lógico apropiado para tu condición (por ejemplo, >, =, !=).
4. En el campo **valor de respuesta**, selecciona o escribe el valor que se requiere para que la respuesta sea válida.

<p class="note">
    <strong>Nota:</strong> Para añadir criterios de validación a preguntas de tipo <strong>Fecha</strong>, el valor de respuesta debe estar en formato <code>AAAA-MM-DD</code>. Por ejemplo, para establecer un criterio de validación para que una fecha sea anterior al 1 de enero de 2021, usa <code>< 2021-01-01</code>.
</p>

Para añadir múltiples condiciones (por ejemplo, un valor mínimo y un valor máximo), añade tu primera condición, luego click en **Añadir otra condición.** Cuando uses múltiples condiciones, especifica si al menos una de estas condiciones debe cumplirse o todas ellas. Puedes eliminar condiciones haciendo click en el ícono de <i class="k-icon-trash"></i> papelera.

Si no se cumplen las condiciones de validación, la entrada no será aceptada durante la recolección de datos. Se mostrará un [mensaje de error](#mensaje-de-error).


## Ingresar manualmente la lógica de validación en código XLSForm
Para usuarios/as avanzados/as y para preguntas de tipo **Seleccionar una** o **Seleccionar varias**, los criterios de validación se pueden ingresar directamente en código XLSForm.

Para ingresar manualmente la lógica de validación en código XLSForm, sigue estos pasos:
1. Abre <i class="k-icon-settings"></i> **Ajustes** en el menú lateral derecho de la pregunta.
2. Selecciona **Criterios de validación** y click en **Ingresar manualmente tu lógica de validación en código XLSForm.**
3. Ingresa los criterios en código XLSForm.

En la sintaxis XLSForm, se usa un punto `.` para referirse a la pregunta actual, y `${nombre_pregunta}` se usa para referirse a otras preguntas. También necesitarás incluir el operador lógico relevante y el valor de respuesta.

### Ejemplos de criterios de validación

| Criterio             | Descripción                                  |
| :------------------- | :------------------------------------------- |
| `. > 17`             | La respuesta debe ser mayor que 17             |
| `. >= 17 and . <= 130` | La respuesta debe ser igual o estar entre 17 y 130          |
| `not(${en_universidad} = 'yes' and . < 16)` | No se puede proporcionar una respuesta menor a 16 si la respuesta a `en_universidad` es "Sí"|
| `not(selected(., 'none') and count-selected(.)>1)`| No se puede seleccionar "Ninguno" y otras opciones en una pregunta de Seleccionar varias |


<p class="note">
    Para más información sobre código XLSForm y operadores, consulta la <a href="https://xlsform.org/en/#constraints">documentación de XLSForm</a>.
</p>

## Mensaje de error
El **mensaje de error** es un mensaje opcional que el/la entrevistador/a o encuestado/a verá cuando se ingrese una respuesta inválida. Se puede configurar tanto usando el enfoque del **generador de criterios de validación** como el enfoque de **código XLSForm**, en la parte inferior del cuadro.

Si no se especifica ningún mensaje de error, el mensaje predeterminado es "Valor no permitido". Los mensajes de error personalizados típicamente especifican los criterios de validación para ayudar al/a la encuestado/a a corregir su respuesta (por ejemplo, "La edad debe ser mayor que 18").