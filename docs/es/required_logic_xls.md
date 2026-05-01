# Añadir lógica de obligación en un XLSForm

La lógica de obligación te permite hacer que una pregunta sea obligatoria si se cumplen condiciones específicas. Por ejemplo, puedes requerir una pregunta de número de teléfono solo si los/as encuestados/as aceptan ser contactados/as en el futuro. Esta opción proporciona más control que simplemente marcar una pregunta como siempre obligatoria o siempre opcional.

<p class="note">
  Para aprender más sobre preguntas obligatorias y cómo personalizar el mensaje que se muestra a los/as encuestados/as cuando dejan una pregunta obligatoria sin responder, consulta <a href="https://support.kobotoolbox.org/es/question_options_xls.html#required-questions">Usar opciones de preguntas en XLSForm</a>.
</p>

Este artículo explica cómo añadir condiciones de lógica de obligación en XLSForm, incluyendo hacer que una pregunta sea obligatoria según si otra pregunta fue respondida.

<p class="note">
  <strong>Nota:</strong> Este artículo se enfoca en añadir lógica de obligación en <a href="https://support.kobotoolbox.org/es/getting_started_xlsform.html">XLSForm</a>. Para aprender sobre cómo añadir lógica de obligación en el editor de formularios de KoboToolbox (Formbuilder), consulta <a href="https://support.kobotoolbox.org/es/question_options.html?highlight=custom+logic#mandatory-response">Usar las opciones de preguntas</a>.
  <br><br>
  Para práctica con lógica de obligación en XLSForm, consulta el <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">Curso XLSForm Fundamentals</a> de la KoboToolbox Academy.
</p>

## Añadir condiciones de lógica de obligación

La lógica de obligación utiliza <a href="https://support.kobotoolbox.org/es/form_logic_xls.html#question-referencing">referencia a preguntas</a> para hacer que las preguntas sean obligatorias según respuestas anteriores. La pregunta utilizada para definir la lógica de obligación se denomina **pregunta de referencia.**

Para añadir lógica de obligación en XLSForm:
1. Añadir una columna **required** a la **hoja survey**.
2. En la fila de la pregunta para la cual deseas configurar la lógica de obligación, ingresa la condición que debe cumplirse para **que la pregunta sea obligatoria.**

**hoja survey**

| type         | name      | label                                                                     | required           |
|:--------------|:-----------|:--------------------------------------------------------------------------|:------------------|
| select_one yn | recontact  | ¿Aceptas ser contactado/a nuevamente para otro estudio en el futuro?    |                    |
| text          | email      | ¿Cuál es tu dirección de correo electrónico?                                               | ${recontact} = 'yes' |

Si un/a encuestado/a no responde una pregunta obligatoria, no podrá continuar a la siguiente página del formulario ni enviarlo.

### Formato de las condiciones de lógica de obligación

El formato de la condición de lógica de obligación diferirá según el **tipo** de la pregunta de referencia, como se detalla en la tabla a continuación.

| Tipo de pregunta de referencia | Condición de lógica de obligación | Ejemplo |
|:-------------------------|:--------------------|:---------|
| select_one | `${pregunta_de_referencia} = 'nombre_de_opción'` | `${consent} = 'yes'` |
| select_multiple | `selected(${pregunta_de_referencia}, 'nombre_de_opción')` | `selected(${reasons}, 'other')` |
| integer | `${pregunta_de_referencia}` seguido de un operador lógico (>, <, =) y un número (o una referencia a otra pregunta) | `${age} >= 18` |
| date | `${pregunta_de_referencia}` seguido de un operador lógico (>, <, =) y `date('YYYY-MM-DD')` | `${dob} >= date('1975-01-01')` |

<p class="note">
Para aprender más sobre cómo construir expresiones de lógica de formularios en XLSForm, consulta <a href="https://support.kobotoolbox.org/es/form_logic_xls.html">Introducción a la lógica de formularios en XLSForm</a>.
</p>

## Añadir lógica de obligación según si una pregunta fue respondida

Además de configurar lógica de obligación para una respuesta específica, también puedes basarla en si una pregunta fue respondida o dejada en blanco. Esto es útil cuando deseas asegurar que al menos una de dos preguntas sea obligatoria.

Las preguntas sin responder se tratan como cadenas vacías, anotadas como dos apóstrofes simples `''`. Se pueden usar las siguientes condiciones de lógica de obligación:

| Condición de lógica de obligación | Descripción |
|:---------------------------|:-------------|
| `${pregunta_de_referencia} != ''` | Requerir solo si `pregunta_de_referencia` es respondida (no está en blanco). |
| `${pregunta_de_referencia} = ''`  | Requerir solo si `pregunta_de_referencia` no es respondida (está en blanco). |

**hoja survey**

| type  | name    | label                                               | required     |
|:------|:--------|:----------------------------------------------------|:-------------|
| note  | contact | Por favor proporciona tu número de teléfono o dirección de correo electrónico a continuación. |              |
| text  | phone   | Número de teléfono                                        |              |
| text  | email   | Dirección de correo electrónico                                       | ${phone} = '' |