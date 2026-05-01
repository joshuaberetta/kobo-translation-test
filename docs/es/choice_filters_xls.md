# Agregar filtros de selección a un XLSForm

Los filtros de selección crean formularios dinámicos donde las opciones en una pregunta dependen de la respuesta a una pregunta anterior. Esto agiliza la recolección de datos al presentar solo las opciones relevantes, mejorando la eficiencia y precisión de la encuesta.

Los filtros de selección se pueden usar para varias aplicaciones, incluyendo:
- **Listas jerárquicas**, como continentes y países, donde la lista de países depende del continente seleccionado (también conocido como **selección en cascada**).
- **Eliminar una o múltiples opciones de una lista** si son irrelevantes para un/a encuestado/a según sus respuestas anteriores.
- **Reutilizar una lista de opciones** en XLSForm para múltiples preguntas, donde la lista varía ligeramente de una pregunta a otra.
- Reutilizar una lista de opciones de una pregunta anterior, incluyendo **solo las opciones que fueron seleccionadas por el/la encuestado/a.**

Este artículo explica cómo agregar filtros de selección en XLSForm e incluye ejemplos para diferentes casos de uso. Los filtros de selección se definen en la columna `choice_filter` de la hoja de trabajo `survey`, y se operacionalizan en la hoja de trabajo `choices`.

<p class="note">
<strong>Nota:</strong> Este artículo se enfoca en agregar filtros de selección en <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">XLSForm</a>. Para aprender sobre cómo agregar preguntas de selección en cascada en el editor de formularios de KoboToolbox, consulta <a href="https://support.kobotoolbox.org/cascading_select.html">Agregar preguntas de selección en cascada en el Formbuilder</a>.
<br><br>
Para práctica con filtros de selección en XLSForm, consulta el <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">curso XLSForm Fundamentals</a> de la KoboToolbox Academy.
</p>

## Agregar filtros de selección estáticos

Los **filtros de selección estáticos** aplican las mismas condiciones de filtrado para todos/as los/as encuestados/as. Al usar filtros de selección estáticos, una lista de opciones se filtra, pero no varía según las respuestas anteriores. Esto puede ser útil cuando quieres reutilizar una lista de opciones en múltiples preguntas de tu formulario con variaciones menores, sin duplicar la lista de opciones múltiples veces en tu hoja de trabajo `choices`.

Para agregar filtros de selección estáticos en XLSForm:
1. Añade una pregunta `select_one` o `select_multiple` a tu XLSForm y [define tus opciones de respuesta](https://support.kobotoolbox.org/option_choices_xls.html) en la hoja de trabajo `choices`.
2. En la hoja de trabajo `choices`, añade una columna de filtro.
    - Puedes nombrar esta columna como quieras (ej., `q2`).
3. En la columna de filtro, escribe cualquier valor (ej., `yes`) junto a la(s) opción(es) que quieras incluir en la lista de opciones para tu pregunta.
    - Este valor actuará como el filtro. Puede ser cualquier palabra o número.
4. En la hoja de trabajo `survey`, añade una columna **choice_filter**. Esta columna contendrá la **expresión de filtro de selección** usada para filtrar las opciones de respuesta.
    - La expresión de filtro de selección en su forma más básica tendrá el formato: **filtro = 'valor'.**
    - Por ejemplo, `q2 = 'yes'` retendrá todas las opciones con **yes** en la columna `q2`.

### Ejemplo

En el ejemplo a continuación, la misma lista de opciones (`activities`) se usa para dos preguntas diferentes. Para la segunda pregunta, la lista se filtra para mostrar solo actividades al aire libre.

**hoja de trabajo survey**

| type             | name               | label                                                   | choice_filter   |
|:-----------------|:------------------|:--------------------------------------------------------|:----------------|
| select_one activities | activities        | ¿Qué actividades disfrutas hacer en tu tiempo libre?  |                 |
| select_one activities | outdoors_activities | ¿Cuáles de estas actividades al aire libre están disponibles en tu ciudad? | <strong>filter = 'outdoors'</strong> |
| survey | 

**hoja de trabajo choices**

| list_name  | name       | label                 | filter   |
|:-----------|:-----------|:--------------------|:---------|
| activities | reading    | Leer              |          |
| activities | swimming   | Nadar             | outdoors |
| activities | running    | Correr              | outdoors |
| activities | television | Ver televisión  |          |
| activities | hiking     | Hacer senderismo               | outdoors |
| choices | 

## Agregar filtros de selección dinámicos

Los filtros de selección también se pueden usar para filtrar una lista de opciones según una respuesta anterior. En este caso, tendrás una **pregunta primaria** con una correspondiente **lista primaria** de opciones, y una **pregunta secundaria** con una correspondiente **lista secundaria** de opciones. La lista de opciones para la pregunta secundaria se filtra según la respuesta a la pregunta primaria.

<p class="note">
Para un ejemplo de un XLSForm usando filtros de selección dinámicos, consulta este <a href="https://docs.google.com/spreadsheets/d/10gpBV6YaYGx1i367hyW-w1Ms9tkUQnCx0V8YsdwYxmk/edit?gid=0#gid=0">formulario de ejemplo</a>.
</p>

Para agregar filtros de selección dinámicos en XLSForm:
1. Añade la **pregunta primaria** y la **pregunta secundaria** a tu XLSForm y [define sus opciones de respuesta](https://support.kobotoolbox.org/option_choices_xls.html) en la hoja de trabajo `choices`.
    - Estas deben ser preguntas `select_one` o `select_multiple`.
2. En la hoja de trabajo `choices`, añade una columna de filtro.
    - Puede ser útil nombrar esta columna igual que la **pregunta primaria.**
3. En la columna de filtro, ingresa el **nombre de la opción** de la lista primaria a la que corresponde cada opción en la lista secundaria.
4. En la hoja de trabajo `survey`, añade una columna **choice_filter**. Esta columna contendrá la **expresión de filtro de selección** usada para filtrar las opciones de respuesta.
    - Si la pregunta primaria es `select_one`, la expresión de filtro de selección será `columna_de_filtro = ${nombre_de_la_pregunta}`, donde `nombre_de_la_pregunta` se refiere a la pregunta primaria.
    - Si la pregunta primaria es `select_multiple`, la expresión de filtro de selección será `selected(${nombre_de_la_pregunta}, columna_de_filtro)`.

Cuando un/a encuestado/a selecciona una opción en la pregunta primaria, la lista de opciones para la pregunta secundaria se filtrará para incluir solo las opciones correspondientes.

### Ejemplo

En el ejemplo a continuación, `continent` es la **pregunta primaria** y `country` es la **pregunta secundaria.** La lista de opciones para la pregunta `country` se filtrará según la respuesta a la pregunta `continent`.

**hoja de trabajo survey**

| type              | name      | label     | choice_filter        |
|:------------------|:---------|:----------|:--------------------|
| select_one continent | continent | Continente |                     |
| select_one country   | country   | País   | **continent = ${continent}** |
| survey | 

**hoja de trabajo choices**

| list_name  | name     | label   | continent |
|:-----------|:---------|:--------|:----------|
| continent  | africa   | África  |           |
| continent  | asia     | Asia    |           |
| country    | malawi   | Malawi  | africa    |
| country    | zambia   | Zambia  | africa    |
| country    | india    | India   | asia      |
| country    | pakistan | Pakistán| asia      |
| choices |

## Filtros de selección avanzados en XLSForm

Puedes crear filtros de selección más avanzados usando operadores lógicos, operadores matemáticos, funciones y expresiones regulares en tus expresiones de filtro de selección. Esto permite un filtrado de opciones altamente personalizado y preciso, adaptando el formulario a requisitos específicos de recolección de datos y características de los/as encuestados/as.

<p class="note">
<strong>Nota:</strong> En expresiones de filtro de selección avanzadas, la columna <code>name</code> de la hoja de trabajo <code>choices</code> puede usarse como una columna de filtro.
</p>

Ejemplos de expresiones de filtro de selección avanzadas en XLSForm incluyen:
| Filtro de selección | Descripción |
|:---------------|:------------|
| `selected(${pregunta_primaria}, name)` | Mostrar solo respuestas que fueron seleccionadas en una `pregunta_primaria` anterior. |
| `filter = 'outdoors' and include = 'yes'` | Combinar expresiones de filtro de selección para que ambas condiciones deban aplicarse para que la opción se muestre. |
| `name != 'none'` | Excluir la opción <strong>Ninguna</strong> de una lista de opciones. |
| `selected(${Q1}, name) or name='none'` | Incluir opciones seleccionadas en una pregunta anterior así como una opción <strong>Ninguna</strong> (incluso si no fue seleccionada previamente). |
| `filter=${Q1} or name='other'` | Incluir opciones basadas en una pregunta anterior así como una opción <strong>Otra</strong>. |
| `filter=${Q1} or always_include='yes'` | Incluir opciones basadas en una pregunta anterior así como un conjunto de opciones que siempre deben incluirse. |
| `filter <= ${product_count}` | Usar números en la columna de filtro en lugar de texto, y filtrar según un número de una pregunta o cálculo anterior. |
| `if(${relationship_status} = 'married', filter = 'married', filter = 'unmarried')` | Usar declaraciones if para mostrar condicionalmente opciones según los antecedentes del/de la encuestado/a. |

<p class="note">
  Para aprender más sobre cómo construir expresiones de lógica de formulario en XLSForm, consulta <a href="https://support.kobotoolbox.org/form_logic_xls.html">Introducción a la lógica de formularios en XLSForm</a>.
</p>

### Ejemplo
En el ejemplo a continuación, la lista de opciones subyacente para `Q1` y `Q2` es la misma, pero solo las opciones seleccionadas en `Q1` se mostrarán a los/as encuestados/as al responder `Q2`.

**hoja de trabajo survey**

| type               | name | label                                              | choice_filter            |
|:------------------|:-----|:--------------------------------------------------|:-------------------------|
| select_multiple item | Q1  | ¿Qué artículos del hogar posees actualmente?      |                          |
| select_multiple item | Q2  | ¿Cuáles de estos artículos considerarías actualizar en el futuro? | selected(${Q1}, name) |
| survey |

**hoja de trabajo choices**

| list_name | name      | label            |
|:----------|:----------|:----------------|
| item      | fridge    | Refrigerador    |
| item      | tv        | Televisión      |
| item      | fan       | Ventilador de techo     |
| item      | microwave | Horno microondas  |
| item      | radio     | Radio           |
| item      | bike      | Bicicleta         |
| item      | phone     | Teléfono móvil    |
| item      | laptop    | Computadora portátil |
| choices | 

En el formulario resultante, `Q2` mostrará solo las opciones elegidas en `Q1`, como se muestra a continuación.

![Filtros de selección](images/choice_filters_xls/choice_filters.png)

## Solución de problemas

<details>
  <summary><strong>El formulario se ralentiza o falla con listas muy largas</strong></summary>
  Las listas de opciones grandes que incluyen miles de filas pueden funcionar en vista previa pero fallar cuando se implementan. Esto sucede porque la vista previa del navegador puede manejar listas grandes, mientras que la aplicación móvil o el analizador XLS no pueden. Para solucionar esto, mueve las listas grandes a un archivo CSV externo y usa <a href="https://support.kobotoolbox.org/select_from_file_xls.html">preguntas select_from_file</a> con filtros de selección. Este enfoque se recomienda para listas con más de 3,000 opciones.
</details>

<br>

<details>
  <summary><strong>Nombres de opciones duplicados en una lista</strong></summary>
  Si tu lista de opciones incluye nombres de opciones duplicados (por ejemplo, si el mismo nombre de vecindario está presente en diferentes ciudades), <a href="https://support.kobotoolbox.org/form_settings_xls.html">habilita opciones duplicadas</a> en la hoja de trabajo <code>settings</code> configurando <code>allow_choice_duplicates</code> como <code>yes</code>.
</details>