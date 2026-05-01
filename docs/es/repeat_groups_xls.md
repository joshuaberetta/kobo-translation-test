# Grupos repetidos en XLSForm

Los grupos repetidos en XLSForm te permiten hacer el mismo conjunto de preguntas varias veces dentro de un formulario. Esto es especialmente útil cuando recolectas información similar sobre varias personas, artículos o eventos.

Por ejemplo, si estás recopilando detalles sobre cada miembro de un hogar, puedes usar un grupo de repetición para hacer las mismas preguntas demográficas para cada individuo.

Este artículo cubre los siguientes temas:
- Crear un grupo de repetición
- Establecer conteos de repetición para limitar el número de repeticiones
- Contar el número de repeticiones dentro de un grupo de repetición
- Recuperar valores de grupos de repetición

<p class="note"> 
<strong>Nota:</strong> Este artículo se enfoca en grupos de repetición en <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">XLSForm</a>. Para aprender sobre grupos de repetición en el editor de formularios de KoboToolbox (Formbuilder) y para previsualizar grupos de repetición en acción, consulta <a href="https://support.kobotoolbox.org/group_repeat.html">Agrupar preguntas y grupos de repetición</a>. 
</p>

## Crear un grupo de repetición

Para crear un grupo de repetición en XLSForm:

1. En la columna `type` de la **hoja survey**, ingresa **begin_repeat** para indicar el inicio del grupo de repetición.
2. En la columna `name` de la fila **begin_repeat**, ingresa el identificador único para el grupo.
3. En la columna `label`, ingresa el título del grupo como quieres que se muestre en el formulario. La etiqueta es opcional y puede dejarse en blanco.
4. Ingresa cada pregunta del grupo en su propia fila, como lo harías normalmente.
5. En una nueva fila después de las preguntas repetidas, ingresa **end_repeat** en la columna `type` para indicar el final del grupo de repetición.
    - En la fila **end_repeat**, deja las columnas `name` y `label` en blanco.

**hoja survey**

| type | name | label |
| :--- | :--- | :--- |
| **begin_repeat** | household_members | Miembros del hogar |
| text | name | ¿Cuál es el nombre de la persona? |
| integer | age | ¿Cuántos años tiene? |
| select_one yn | married | ¿Está casado/a? |
| **end_repeat** | | |
| survey |

Los grupos de repetición funcionan de manera similar a los grupos de preguntas. Con los grupos de repetición, puedes:

- Usar la apariencia **field-list** para [mostrar todas las preguntas](https://support.kobotoolbox.org/grouping_questions_xls.html#appearance-settings-for-question-groups) en la misma página.
- Agregar [lógica de omisión](https://support.kobotoolbox.org/grouping_questions_xls.html#applying-skip-logic-to-question-groups) a grupos de repetición en la columna **relevant**.
- Crear grupos de repetición **anidados**, donde un grupo de repetición se agrega [dentro de otro](https://support.kobotoolbox.org/grouping_questions_xls.html#nested-groups).

<p class="note">
  <strong>Nota:</strong> Agregar grupos de repetición a tu formulario crea una estructura de datos diferente en comparación con variables o grupos estándar. Cuando descargues tus datos en formato .xlsx, encontrarás una hoja separada para cada grupo de repetición. Para más información sobre cómo exportar y usar datos de grupos de repetición, consulta <a href="https://support.kobotoolbox.org/managing_repeat_groups.html">Gestión de datos de grupos repetidos</a>.
</p>

## Establecer conteos de repetición

Por defecto, los grupos de repetición pueden repetirse tantas veces como sea necesario. Para limitar el número de veces que un grupo de repetición se repite en el formulario, puedes establecer un conteo de repetición. El **conteo de repetición** puede ser un número fijo o determinarse dinámicamente según una respuesta anterior.

Para establecer un número fijo de repeticiones:

1. Añade una columna **repeat_count** en la **hoja survey**.
2. Ingresa un número en la columna **repeat_count**.

**hoja survey**

| type | name | label | repeat_count |
| :--- | :--- | :--- | :--- |
| begin_repeat | participant_profile | Perfil del/de la participante | 3 |
| text | name | Nombre | |
| select_one gender | gender | Género | |
| integer | age | Edad | |
| end_repeat | | | |
| survey |

Para determinar dinámicamente el número de repeticiones según una respuesta anterior:

1. Añade una columna **repeat_count** en la **hoja survey**.
2. Ingresa la referencia de la pregunta en la columna **repeat_count**.
    - La pregunta referenciada debe ser de tipo `integer`.

**hoja survey**

| type | name | label | repeat_count |
| :--- | :--- | :--- | :--- |
| integer | participants | Número total de participantes en la capacitación | |
| begin_repeat | participant_profile | Perfil del/de la participante | ${participants} |
| text | name | Nombre | |
| select_one gender | gender | Género | |
| integer | age | Edad | |
| end_repeat | | | |
| survey |

<p class="note">
  <strong>Nota:</strong> Dentro de la columna <strong>repeat_count</strong>, también puedes incluir declaraciones condicionales avanzadas para determinar si las repeticiones continuarán. Para más información, consulta la <a href="https://docs.getodk.org/form-logic/#repeating-as-long-as-a-condition-is-met">documentación de ODK</a>. 
</p>

## Contar el número de repeticiones dentro de un grupo de repetición

Cuando usas grupos de repetición, puedes necesitar un campo que cuente cuántas veces se ha repetido el grupo. Esto puede ser útil para cálculos o lógica del formulario. Por ejemplo, puedes aplicar lógica de omisión después de una repetición específica o incluir dinámicamente el número de repetición en una etiqueta de pregunta (ej. Niño/a 1, Niño/a 2).

Para contar cuántas veces se ha repetido un grupo de repetición:
1. Añade una pregunta de tipo **calculate** dentro del grupo de repetición.
2. Ingresa `position(..)` en la columna **calculation**.

Esta variable almacena el índice de repetición actual. Puedes usarla en la lógica del formulario o para crear etiquetas de preguntas dinámicas.

**hoja survey**

| type | name | label | calculation | relevant |
| :--- | :--- | :--- | :--- | :--- |
| begin_repeat | profile | Perfil del/de la participante | | |
| calculate | number | | **position(..)** | |
| note | instructions | Responde las preguntas a continuación para cada participante. | | **${number} = 1** |
| text | name | Nombre del/de la participante **${number}** | | |
| select_one gender | gender | Género del/de la participante **${number}** | | |
| integer | age | Edad del/de la participante **${number}** | | |
| end_repeat | | | | |
| survey |

## Contar el número total de repeticiones de un grupo de repetición

También puedes agregar una pregunta separada fuera del grupo de repetición para contar el número total de repeticiones. Esto es útil, por ejemplo, para confirmar el número de participantes o niños/as listados/as en el grupo de repetición.

Para contar cuántas veces se completó un grupo de repetición:
1. Añade una pregunta de tipo **calculate** después del grupo de repetición.
2. En la columna **calculation**, ingresa `count(${repeat_group_name})`, donde `repeat_group_name` es el nombre del grupo de repetición.

Esta variable almacena el número total de repeticiones del grupo. Puedes usarla en cálculos o para crear etiquetas de preguntas dinámicas en tu formulario.

**hoja survey**

| type | name | label | calculation |
| :--- | :--- | :--- | :--- |
| begin_repeat | children | Lista de niños/as | |
| text | name | Nombre | |
| select_one gender | gender | Género | |
| integer | age | Edad | |
| end_repeat | | | |
| calculate | count_children | | **count(${children})** |
| acknowledge | confirm_children | Confirma que hay **${count_children}** niños/as en el hogar. | |
| survey |

## Recuperar valores de grupos de repetición

Los formularios avanzados a menudo usan [referencia a preguntas](https://support.kobotoolbox.org/form_logic_xls.html#question-referencing) para incluir respuestas de preguntas anteriores en etiquetas de preguntas, cálculos o lógica de omisión. También puedes usar referencia a preguntas **dentro de grupos de repetición** o para referirte a datos repetidos en otra parte de tu formulario.

Dentro de un grupo de repetición, puedes referenciar una respuesta de otra pregunta en la misma repetición usando referencia a preguntas, como se muestra a continuación.

**hoja survey**

| type | name | label |
| :--- | :--- | :--- |
| begin_repeat | children | Lista de niños/as |
| text | name | ¿Cuál es el nombre del niño/de la niña? |
| integer | age | ¿Cuántos años tiene ${name}? |
| select_one gender | married | ¿Cuál es el género de ${name}? |
| end_repeat | | |
| survey |

Fuera de un grupo de repetición, puedes recuperar datos del grupo de repetición para usarlos en la lógica del formulario o en etiquetas de preguntas:

1. Añade una pregunta de tipo **calculate** después de tu grupo de repetición.
2. Incluye una de las fórmulas listadas a continuación en la columna **calculation**.
3. La pregunta **calculate** almacena el valor recuperado, que luego puedes usar en la lógica del formulario o en etiquetas de preguntas.

**Fórmulas para recuperar datos de grupos de repetición**

| Fórmula | Descripción |
| :--- | :--- |
| `max(${question-name})` | Recupera el valor máximo ingresado para una pregunta en el grupo de repetición. |
| `min(${question-name})` | Recupera el valor mínimo ingresado para una pregunta en el grupo de repetición. |
| `sum(${question-name})` | Calcula la suma de valores numéricos ingresados para una pregunta en el grupo de repetición. |
| `join('; ', ${question-name})` | Lista todas las respuestas a una pregunta dada dentro de un grupo de repetición, separadas por punto y coma. |
| `indexed-repeat(${question-name}, ${repeat-name}, n)` | Recupera el valor para `${question-name}`, en el grupo de repetición llamado `${repeat-name}`, en la n<sup>ava</sup> repetición. |

**hoja survey**

| type | name | label | calculation |
| :--- | :--- | :--- | :--- |
| begin_repeat | children | Lista de niños/as | |
| text | name | Nombre | |
| select_one gender | gender | Género | |
| integer | age | Edad | |
| end_repeat | | | |
| calculate | max_age | | **max(${age})** |
| acknowledge | confirm_age | Confirma que el niño/la niña mayor en el hogar tiene **${max_age}** años. | |
| survey |