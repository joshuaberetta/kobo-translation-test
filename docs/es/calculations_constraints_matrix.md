# Agregar cálculos y restricciones en una pregunta de matriz

<a href="https://github.com/kobotoolbox/docs/blob/aaabdac8ec257d3157ec2ab2ceae65130e8c12d4/source/calculations_constraints_matrix.md" class="reference">14
Apr 2022</a>

Cuando trabajas en el editor de formularios de KoboToolbox (Formbuilder), es sencillo
[agregar cálculos](calculate_questions.md) o
[restricciones](validation_criteria.md) a casi cualquier tipo de pregunta. Si bien el
editor de formularios actualmente no admite agregar estas funcionalidades a una
pregunta de matriz, puedes usar XLSForm para hacerlo. Los pasos que se enumeran a continuación en este
artículo de ayuda ilustrarán cómo puedes agregar cálculos y restricciones a una
pregunta de matriz usando XLSForm.

## Configurar la pregunta y los campos

**Paso 1: Crea una pregunta de matriz en el editor de formularios**

El primer paso es crear una pregunta de matriz en el editor de formularios (como se describe en
el artículo de ayuda [Tipo de respuesta de matriz de preguntas](matrix_response.md)). Simplemente
agrega filas y columnas con las variables necesarias para la recolección de datos.

**Paso 2: Descarga el formulario como XLSForm**

Una vez que se haya creado la pregunta de matriz, **GUARDA** el formulario y
[descárgalo como XLSForm](getting_started_xlsform.md#downloading-an-xlsform-from-kobotoolbox).

**Paso 3: Agrega lógica a la pregunta de matriz**

Abre el XLSForm y agrega los encabezados de columna `calculation`, `constraint` y `constraint_message`. Con estos encabezados de columna, podrás agregar las expresiones de _total de columna_ y _total de fila_ bajo el encabezado de columna `calculation`. También
puedes agregar _restricciones_ apropiadas bajo el encabezado de columna `constraint` y
_mensajes de restricción_ bajo el encabezado `constraint_message` según sea necesario.

Además, también puedes optar por agregar un encabezado de columna `read_only` para restringir
que los/as encuestadores/as editen las respuestas mientras recolectan datos de ciertas
preguntas (por ejemplo, el _total de fila_ y _total de columna_ que se
calculan).

![Survey Tab](images/calculations_constraints_matrix/survey_tab.png)

<p class="note">
  En la imagen de arriba, puedes notar que las entradas de <code>name</code> son
  más cortas. En este ejemplo, se han renombrado de las generadas automáticamente
  en el editor de formularios para capturar la captura de pantalla completa de la pestaña survey. Si
  decides renombrar las tuyas, asegúrate de usar tus nuevos nombres de variable en los
  encabezados de columna <code>calculation</code> y <code>constraint</code>. Si el
  formulario ya ha sido desplegado y se han recolectado datos, se recomienda
  que <em>no</em> renombres las variables existentes.
</p>

**Paso 4: Reemplaza el formulario**

Carga y reemplaza tu XLSForm dentro del proyecto existente, o crea un nuevo
proyecto (si es necesario).

**Paso 5: Despliega el formulario**

**Paso 6: Recolecta datos**

Después de desplegar el formulario, puedes ir a **FORMULARIO>Recolectar datos>ABRIR** para comenzar
a recolectar datos con el formulario web.

## Ver el resultado

Las siguientes imágenes ilustran cómo se verá y funcionará el formulario en el
formulario web Enketo después de haber seguido los pasos anteriores:

**No se ingresan datos:**

![Enketo Nothing Entered](images/calculations_constraints_matrix/enketo_nothing_entered.png)

**Se comete un error de entrada:**

![Enketo Wrong Inputs Entered](images/calculations_constraints_matrix/enketo_wrong_inputs_entered.png)

Aquí verás que solo hay cinco miembros totales del hogar. Si un/a
encuestador/a ingresa 6 para el número de hombres (0-14 años), la restricción
mostrará un mensaje de error.

**Sin errores de entrada:**

![Enketo Correct Inputs Entered](images/calculations_constraints_matrix/enketo_correct_inputs_entered.png)

Aquí, cuando ingresas valores en una tabla de matriz, las filas y columnas se
calculan automáticamente.

<p class="note">
  Puedes descargar el XLSForm que se usó para este artículo
  <a
    download
    class="reference"
    href="./_static/files/calculations_constraints_matrix/calculations_constraints_matrix.xlsx"
    >aquí</a
  >.
</p>

## Solución de problemas

-   La pregunta de matriz solo funciona con **formularios web Enketo**. No es
    compatible con la **aplicación de Android de KoboCollect**.

-   La tabla de matriz aparecerá distorsionada si no configuras el diseño en
    **Grid-theme**. Para obtener más detalles sobre las apariencias de formularios web, puedes consultar
    [Usar estilos alternativos de formularios web Enketo](alternative_enketo.md).