# Agregar restricciones a un XLSForm

Las restricciones, también conocidas como criterios de validación, son un tipo de lógica de formulario utilizada para **restringir las respuestas aceptables a una pregunta en función de una condición predefinida**. Si no se cumple la condición de restricción, se muestra un mensaje de error personalizable que solicita al/a la usuario/a del formulario que ingrese una respuesta válida.

<p class="note">
  Para obtener más información sobre la lógica de formularios en XLSForm, consulta <a href="https://support.kobotoolbox.org/es/form_logic_xls.html">Introducción a la lógica de formularios en XLSForm</a>.
</p>

Este artículo cubre los siguientes temas:
- Agregar restricciones a preguntas en XLSForm
- Combinar múltiples condiciones de restricción
- Personalizar mensajes de error de restricción
- Restricciones avanzadas en XLSForm

<p class="note">
  <strong>Nota:</strong> Este artículo se centra en agregar restricciones en <a href="https://support.kobotoolbox.org/es/getting_started_xlsform.html">XLSForm</a>. Para obtener información sobre cómo agregar restricciones en el editor de formularios de KoboToolbox **(Formbuilder)**, consulta <a href="https://support.kobotoolbox.org/es/validation_criteria.html?highlight=limiting">Añadir criterios de validación en el Formbuilder</a>.
<br><br>
Para practicar con la adición de restricciones en XLSForm, consulta el <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">curso XLSForm Fundamentals</a> de la KoboToolbox Academy.
</p>

## Agregar una restricción

Las restricciones se construyen utilizando [referencias a preguntas](https://support.kobotoolbox.org/es/form_logic_xls.html#question-referencing), [operadores de comparación](https://support.kobotoolbox.org/es/form_logic_xls.html#mathematical-and-comparison-operators) y constantes. Las condiciones de restricción deben cumplirse para validar o enviar un formulario. De lo contrario, aparece un **mensaje de error** y se impide que los/as usuarios/as pasen a la siguiente página o envíen el formulario.

Para agregar restricciones en XLSForm:
1. Agrega una columna **constraint** a la hoja de trabajo `survey`.
2. En la columna `constraint`, define la condición que debe cumplirse **para que la respuesta sea válida.** 
    - Utiliza un punto `.` para hacer referencia a la pregunta en la fila donde estás agregando una restricción.
    - Utiliza un [operador de comparación](https://support.kobotoolbox.org/es/form_logic_xls.html#mathematical-and-comparison-operators), seguido de un valor de referencia, para construir una restricción simple. 
    - Por ejemplo, `. > 18` restringe una pregunta `integer` para aceptar solo valores mayores que 18.

**hoja survey**

| type     | name       | label                                | constraint       |
|:---------|:-----------|:-------------------------------------|:----------------|
| integer  | age        | ¿Cuál es tu edad?                    | . >= 18         |
| integer  | household  | ¿Cuántas personas viven en tu hogar? | . <= 30         |
| integer  | income     | De esas, ¿cuántas obtienen ingresos?  | . <= ${household} |

### Formato de los valores de referencia
El valor de referencia en una condición de restricción debe coincidir con el **tipo** de pregunta para la cual estás agregando una restricción. Los formatos de valores de referencia para los principales tipos de preguntas se enumeran a continuación: 

| Tipo de pregunta   | Formato del valor de referencia                                      | Ejemplo                      |
|:----------------|:-----------------------------------------------------------|:------------------------------|
| integer         | Número                                                      | `. > 35`                     |
| select_one      | Nombre de la opción (como se define en la hoja de trabajo choices) entre comillas | `. = 'yes'`                  |
| select_multiple | Nombre de la opción combinado con la <a href="https://support.kobotoolbox.org/es/functions_xls.html">función</a> `selected()`       | `selected(., 'chair')`       |
| date            | Fecha en el formato `date('YYYY-MM-DD')`                    | `. > date('2021-01-01')`    |
| text            | Texto entre comillas (rara vez se usa para restricciones)      | `. != 'Not applicable'`      |

<p class="note">
  Para obtener más información sobre cómo construir expresiones de lógica de formulario en XLSForm, consulta <a href="https://support.kobotoolbox.org/es/form_logic_xls.html">Introducción a la lógica de formularios en XLSForm</a>.
</p>

## Combinar múltiples condiciones de restricción
Se pueden combinar múltiples condiciones de restricción en una sola expresión para determinar si una respuesta es válida. Las condiciones se pueden combinar utilizando los operadores lógicos **and**, **or** y **not**:

- Utiliza **and** cuando todas las condiciones deben cumplirse para que una respuesta sea válida. 
    - Por ejemplo: <code>. > 18 <strong>and</strong> . < 65</code>
- Utiliza **or** cuando al menos una condición debe cumplirse para que una respuesta sea válida.
    - Por ejemplo: <code>. < 18 <strong>or</strong> ${student} = 'yes'</code>
- Utiliza **not** para indicar que una condición o conjunto de condiciones no deben cumplirse (por ejemplo, cuando dos condiciones no pueden ser verdaderas juntas para que una respuesta sea válida).
    - Por ejemplo: <code><strong>not</strong>(. < 18 <strong>and</strong> ${household_head} = 'yes')</code>

**hoja survey**

| type     | name   | label              | hint                                        | constraint                                               |
|:---------|:-------|:------------------|:--------------------------------------------|:---------------------------------------------------------|
| integer  | age    | ¿Cuál es tu edad? | Debe ser menor de 18 o mayor de 65 para participar | <code>. < 18 <strong>or</strong> . > 65</code>         |
| integer  | weight | ¿Cuánto pesas? | Debe estar entre 30 y 200 kg               | <code>. >= 30 <strong>and</strong> . <= 200</code>     |


## Personalizar mensajes de error de restricción

De forma predeterminada, cuando un valor de respuesta en el formulario no cumple con la condición de restricción, aparece un mensaje de error "Valor no permitido". Se recomienda personalizar este mensaje para informar a los/as usuarios/as por qué el valor no es válido, permitiéndoles corregir su entrada.

Para personalizar el mensaje de error de restricción:
1. Agrega una columna **constraint_message** a la hoja de trabajo `survey`.
2. En la columna `constraint_message`, ingresa el texto que deseas mostrar como mensaje de error cuando no se cumplan las condiciones de restricción.

**hoja survey**

| type    | name | label           | constraint | constraint_message     |
|:--------|:-----|:----------------|:-----------|:----------------------|
| integer | age  | ¿Cuál es tu edad? | . >= 18   | Debes ser mayor de 18. |

## Restricciones avanzadas en XLSForm

Más allá de las restricciones básicas, puedes personalizar las condiciones para garantizar la calidad de los datos y adaptarte a muchos escenarios de recolección de datos. Para construir condiciones de restricción más avanzadas en XLSForm:

- Utiliza paréntesis para combinar más de dos condiciones
- Utiliza [funciones](https://support.kobotoolbox.org/es/functions_xls.html) para mayor flexibilidad 
- Utiliza [expresiones regulares](https://support.kobotoolbox.org/es/restrict_responses.html) para restringir respuestas de texto
  
Ejemplos de criterios de validación más avanzados incluyen:

| Criterios | Descripción |
|:---------|:------------|
| <code>(. >= 18 and . < 130) or (. = 999)</code> | La respuesta debe estar entre 17 y 130 o ser igual a 999 (a menudo se usa para no respuesta) |
| <code>not(${in_university} = 'yes' and . < 16)</code> | Si la respuesta a `in_university` es 'yes', la respuesta actual debe ser mayor que 16. |
| <code>not(selected(., 'none') and count-selected(.)>1)</code> | La opción 'none' no se puede seleccionar si se selecciona cualquier otra respuesta en una pregunta `select_multiple`. |
| <code>. < today()</code> | La fecha ingresada debe ser anterior a la fecha de hoy. |
| <code>regex(., '^\d{2}$')</code> | La entrada está restringida a dos números (usando <a href="https://support.kobotoolbox.org/es/restrict_responses.html">expresiones regulares</a>). |