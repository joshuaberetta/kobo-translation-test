# Agregar cálculos en XLSForm

Los cálculos se pueden utilizar dentro de tu formulario para derivar nuevas variables, construir lógica de formulario avanzada y mostrar resultados a los/as encuestados/as durante la recolección de datos.

Los cálculos se procesan dentro del formulario, lo que ayuda a ahorrar tiempo durante el análisis de datos. Los resultados se almacenan como nuevas columnas en el conjunto de datos final y se pueden utilizar en todo el formulario para aplicar [lógica de omisión](https://support.kobotoolbox.org/skip_logic_xls.html), establecer [restricciones](https://support.kobotoolbox.org/constraints_xls.html) o mostrar [contenido dinámico](https://support.kobotoolbox.org/form_logic_xls.html#question-referencing) en etiquetas de preguntas y notas.

Este artículo explica cómo agregar cálculos en XLSForm, cubriendo tanto aritmética básica como expresiones más avanzadas.

<p class="note">
<strong>Nota:</strong> Este artículo se centra en agregar cálculos en <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">XLSForm</a>. Para aprender sobre cómo agregar cálculos en el editor de formularios de KoboToolbox **(Formbuilder)**, consulta <a href="https://support.kobotoolbox.org/calculate_questions.html">Agregar cálculos con el Formbuilder</a>.
<br><br>
Para práctica práctica con cálculos en XLSForm, consulta el <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">curso XLSForm Fundamentals</a> de la KoboToolbox Academy.
</p>

## Agregar cálculos en XLSForm

Las expresiones de cálculo se construyen utilizando una combinación de [referencias a preguntas](https://support.kobotoolbox.org/form_logic_xls.html#question-referencing), [operadores matemáticos](https://support.kobotoolbox.org/form_logic_xls.html#mathematical-and-comparison-operators), [funciones](https://support.kobotoolbox.org/functions_xls.html) y constantes.

Para agregar un cálculo en tu XLSForm:
1. En la columna `type` de la hoja de trabajo `survey`, ingresa **calculate** para agregar un tipo de pregunta `calculate`. 
2. Ingresa un `name` para la pregunta `calculate`. 
    - Debido a que el cálculo no se muestra en el formulario, la pregunta `calculate` no requiere una **label**.
3. Añadir una columna **calculation** en la hoja de trabajo `survey`.
4. En la columna `calculation`, ingresa la **expresión de cálculo.** 
    - Los cálculos pueden variar desde [cálculos aritméticos básicos](https://support.kobotoolbox.org/calculations_xls.html#arithmetic-calculations) hasta [cálculos avanzados](https://support.kobotoolbox.org/calculations_xls.html#advanced-calculations) utilizando funciones y expresiones regulares.
  
Para hacer referencia al resultado del cálculo en el resto de tu formulario (por ejemplo, dentro de una pregunta de nota, etiqueta de pregunta o lógica de formulario), utiliza el formato de [referencia a preguntas](https://support.kobotoolbox.org/form_logic_xls.html#question-referencing) **${nombre_de_la_pregunta}**, donde `nombre_de_la_pregunta` es el **name** de la pregunta `calculate`.

**hoja de trabajo survey**

| type      | name          | label                          | calculation           |
|:----------|:--------------|:-------------------------------|:----------------------|
| integer   | bags          | Número total de bolsas vendidas |                       |
| decimal   | price         | Precio por bolsa                |                       |
| calculate | total_amount  |                                | ${bags} * ${price}    |
| note      | display_total | El total es ${total_amount}     |                       |

## Cálculos aritméticos

Los cálculos en XLSForm pueden variar desde cálculos aritméticos simples hasta la derivación avanzada de variables.

Los cálculos aritméticos te permiten realizar cálculos básicos utilizando los siguientes **operadores**:

| Operador | Descripción |
|:----------|:-------------|
| <strong>+</strong>   | Suma |
| <strong>-</strong>   | Resta |
| <strong>*</strong>   | Multiplicación |
| <strong>div</strong> | División |
| <strong>mod</strong> | Módulo (calcula el resto de una división) |

Los cálculos en XLSForm siguen la regla **BODMAS** para el orden de las operaciones matemáticas: **B**rackets (paréntesis), **O**rder of powers (orden de potencias), **D**ivision (división), **M**ultiplication (multiplicación), **A**ddition (suma) y **S**ubtraction (resta). Esto significa que los cálculos dentro de paréntesis se realizan primero, seguidos de potencias, luego divisiones, multiplicaciones, y así sucesivamente. Usar paréntesis correctamente asegura que tus cálculos funcionen como se espera. 

## Cálculos avanzados

Los cálculos avanzados en XLSForm a menudo dependen de **funciones** y **expresiones regulares** para hacer los cálculos más eficientes. 
* Las **funciones** son operaciones predefinidas utilizadas para realizar automáticamente tareas complejas como redondear valores, calcular potencias o extraer la fecha actual.
* Las **expresiones regulares (regex)** son patrones de búsqueda utilizados para coincidir con caracteres específicos dentro de una cadena de texto.

<p class="note">
  Para una lista completa de funciones disponibles en XLSForm, consulta <a href="https://support.kobotoolbox.org/functions_xls.html">Usar funciones en XLSForm</a>. Para aprender más sobre expresiones regulares, consulta <a href="https://support.kobotoolbox.org/restrict_responses.html">Usar expresiones regulares en XLSForm</a>.
</p>

Ejemplos de cálculos más avanzados incluyen:

| Cálculo | Descripción |
|:-------------|:-------------|
| `int((today()-${DOB}) div 365.25)` | Calcular edad a partir de la fecha de nacimiento. |
| `int(today()-${date})` | Calcular días desde una fecha. |
| `format-date(${date}, '%b')` | Devolver solo el mes de una fecha. |
| `concat(${first}, " ", ${middle}, " ", ${last})` | Crear una sola cadena con el nombre completo del/la encuestado/a. |
| `jr:choice-name(${question1}, '${question1}')` | Devolver la etiqueta de una opción, en el idioma actual, de la lista de opciones. |
| `translate(${full_name}, "ABCDEFGHIJKLMNOPQRSTUVWXYZ ", "abcdefghijklmnopqrstuvwxyz_")` | Convertir letras mayúsculas a minúsculas y espacios a guiones bajos. |
| `substr(${question}, 1, 2)` | Mantener solo la primera letra o número en una cadena. |
| `int(random()*10)` | Generar un número aleatorio entre 0 y 10. |
| `selected-at(${gps}, 0)` | Aislar latitud de coordenadas GPS. |
| `selected-at(${gps}, 1)` | Aislar longitud de coordenadas GPS. |
| `if(regex(${id}, '^ML-'), 'yes', 'no')` | Crear una variable binaria que toma `yes` si el ID del/la encuestado/a comienza con "ML-". |

### Establecer respuestas predeterminadas dinámicas

El campo `calculation` también se puede utilizar para establecer **respuestas predeterminadas dinámicas.** Las respuestas predeterminadas dinámicas te permiten mostrar una respuesta predeterminada dentro de una pregunta basada en una respuesta anterior. 

Para establecer una respuesta predeterminada dinámica:
1. En la columna `calculation`, ingresa la **referencia a la pregunta** que poblará dinámicamente la respuesta predeterminada. 
2. En la columna `trigger`, ingresa la pregunta que activará el cálculo. 
    - Típicamente, esta sería la misma pregunta referenciada en la columna `calculation`, de modo que cualquier cambio en la pregunta de activación también actualizará la respuesta predeterminada.

**hoja de trabajo survey**

| type | name       | label                     | calculation | trigger     |
|:------|:-----------|:--------------------------|:-------------|:-------------|
| text  | hh_name    | Nombre del jefe de hogar  |             |              |
| text  | phone      | Número de teléfono del hogar |              |              |
| text  | phone_name | Nombre del/la propietario/a del teléfono | ${hh_name}   | ${hh_name}   |

<p class="note">
<strong>Nota:</strong> Si deseas evitar que los/as usuarios/as editen el campo, configura la columna <code>read_only</code> como <code>TRUE</code>.
</p>

## Solución de problemas

<details>
  <summary><strong>Recomendaciones para la solución de problemas</strong></summary>
  Para facilitar la solución de problemas, muestra los resultados de los cálculos en una nota mientras desarrollas tu formulario. Esto ayuda a determinar si el cálculo se está evaluando correctamente y facilita la identificación de problemas. También puedes dividir expresiones largas en otras más pequeñas y mostrar el resultado de cada una para identificar problemas. 
</details>

<br>

<details>
  <summary><strong>Los cálculos no funcionan correctamente</strong></summary>
  Si tus cálculos no funcionan, verifica lo siguiente:
  <ul>
  <li><strong>Sintaxis:</strong> Todos los paréntesis abiertos están cerrados, se utilizan comillas rectas <code>'</code>, y se incluyen comas donde sea necesario.</li>
  <li><strong>Referencias:</strong> Las referencias a preguntas coinciden correctamente con el nombre de la pregunta, sin espacios ni errores tipográficos, sin referencias circulares (es decir, el cálculo no depende de sí mismo).</li>
  <li><strong>Tipos de datos:</strong> Los cálculos numéricos y de cadena no se combinan dentro de la misma pregunta, los tipos de datos se utilizan correctamente.</li>
</ul>
</details>

<br>

<details>
  <summary><strong>Manejo de campos vacíos</strong></summary>
  Las preguntas sin respuesta se tratan como cadenas vacías y no se convertirán automáticamente a cero. Cuando se utiliza un valor vacío en un cálculo, resulta en "Not a Number" (NaN). Para convertir valores vacíos a cero para cálculos, utiliza las <a href="https://support.kobotoolbox.org/functions_xls.html">funciones</a> <code>coalesce()</code> o <code>if()</code>. Por ejemplo:
  <ul>
  <li><code>coalesce(${potentially_empty_value}, 0)</code></li>
  <li><code>if(${potentially_empty_value}="", 0, ${potentially_empty_value})</code></li>
</ul>
  Otra opción es establecer valores predeterminados para cada una de las variables numéricas en 0 en la columna <code>default</code>.
</details>

<br>

<details>
  <summary><strong>Los cálculos siguen cambiando en el formulario</strong></summary>
  Las expresiones se reevalúan a medida que un/a encuestador/a avanza a través de un formulario. Esto es especialmente importante para <a href="https://support.kobotoolbox.org/functions_xls.html">funciones</a> no conectadas a campos en el formulario, como <code>random()</code> o <code>now()</code>, ya que sus valores pueden cambiar bajo estas condiciones.
<br><br>
Las expresiones se reevalúan cuando:
  <ul>
  <li>Se abre un formulario</li>
  <li>El valor de cualquier pregunta en el cálculo cambia</li>
  <li>Se agrega o elimina un grupo de repetición</li>
  <li>Se guarda o finaliza un formulario</li>
</ul>
  Para controlar cuándo se evalúa una expresión, establece un <a href="https://support.kobotoolbox.org/question_options_xls.html#additional-question-options">trigger</a> para evaluarla solo cuando se responda una pregunta determinada, o la función <code>once()</code> para asegurar que la expresión se evalúe solo una vez (por ejemplo, <code>once(random())</code> o <code>once(today())</code>).
</details>