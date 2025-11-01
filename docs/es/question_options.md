# Uso de las opciones de pregunta

Después de añadir una pregunta, hay muchas personalizaciones diferentes que puedes hacer usando las opciones de pregunta. Para acceder a la pantalla de opciones de pregunta de una pregunta, haz click en su botón <i class="k-icon k-icon-settings"></i> Ajustes.

![Opciones de pregunta](/images/question_options/options2.png)

## Nombre de columna de datos

El **Nombre de columna de datos** es el identificador único (ID) de tu pregunta.

Este campo es obligatorio para cada pregunta. Solo se permiten letras, números y guiones bajos en este campo, y el campo debe comenzar con una letra o un guión bajo. Puedes ingresar lo que quieras, como `what_is_your_name` o `age`.

El Nombre de columna de datos es importante porque se usa en los encabezados de columna de tablas y hojas de cálculo después de que tus datos hayan sido recolectados. Si quieres que tu hoja de cálculo siga una convención de nomenclatura específica, debes especificar el nombre para cada una de tus preguntas antes de desplegar el formulario como un proyecto de recolección de datos.

## Sugerencia adicional (opcional)

Las **Sugerencias adicionales** son instrucciones extra que puedes añadir a tus preguntas como notas. Por defecto en los formularios web de Enketo, las sugerencias adicionales se muestran bajo un acordeón que puede expandirse y contraerse como se muestra a continuación.

![Sugerencia adicional en formularios web de Enketo](/images/question_options/guidance_hint_enketo.gif)

En [KoboCollect](https://support.kobotoolbox.org/kobocollect_on_android_latest.html), las sugerencias adicionales no se muestran por defecto. Puedes [elegir cómo deben mostrarse las sugerencias adicionales](https://support.kobotoolbox.org/kobocollect_settings.html#form-management-settings) en tus formularios yendo a Ajustes -> Manejo de formularios -> Mostrar sugerencias para preguntas. Aquí tienes 3 opciones: No, Sí - siempre mostrado y Sí - siempre contraído.

![Sugerencia adicional en KoboCollect](/images/question_options/guidance_hint_kobocollect.gif)

Las sugerencias adicionales pueden usarse como notas internas cuando colaboras con otras personas en el desarrollo del formulario. También puedes mostrarlas en impresiones o instrucciones extra durante la capacitación para encuestadores/as.

## Respuesta obligatoria

Este ajuste te permite especificar si la pregunta debe ser respondida en todo momento o no. En XLSForm, esto se llama `required`.

En KoboToolbox, hay tres opciones para respuesta obligatoria:

1. Sí - La pregunta debe ser respondida en todo momento. Si no se proporciona una respuesta, el/la usuario/a no podrá pasar a la siguiente pregunta o guardar el formulario.
2. No - La pregunta no es obligatoria y por lo tanto puede omitirse manualmente.
3. Lógica personalizada - Puedes definir lógica usando código XLSForm que definirá cuándo la pregunta será obligatoria. Por ejemplo, si estableces la siguiente lógica personalizada `${age} > 18`, la pregunta será obligatoria cuando una pregunta anterior con el nombre de columna de datos `age` sea mayor que 18.

## Respuesta predeterminada (opcional)

Esto permite especificar una respuesta predeterminada que el/la entrevistador/a puede aceptar o cambiar.

En la mayoría de los estudios esto no sería recomendable ya que podría crear un sesgo accidental, pero puede ser útil para preguntas de fecha u hora donde las respuestas tienden a estar alrededor de un cierto punto conocido.

Para preguntas de <i class="k-icon k-icon-qt-date"></i> Fecha, la respuesta predeterminada debe escribirse en el formato `YYYY-MM-DD` por ejemplo `1974-12-31`).

Para preguntas de <i class="k-icon k-icon-qt-select-one"></i> Seleccionar una o <i class="k-icon k-icon-qt-select-many"></i> Seleccionar varias, la respuesta debe escribirse usando el Valor único (valor xml) - no la etiqueta (por ejemplo, `first_grade` en lugar de `First grade`).

## Aspecto (opcional)

Este ajuste avanzado permite mostrar la pregunta de una manera modificada. Ciertas opciones de aspecto solo estarán disponibles dependiendo del [Tipo de pregunta](question_types.md).

Para una lista completa de valores de aspecto, visita [la documentación de aspectos de ODK](http://xlsform.org/en/#appearance).

![Opciones de aspecto de pregunta](/images/question_options/appearance.png)