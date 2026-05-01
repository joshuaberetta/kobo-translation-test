# Agregar cálculos y restricciones a una matriz de preguntas

Cuando trabajas en el editor de formularios de KoboToolbox **(Formbuilder)**, es sencillo [agregar cálculos](calculate_questions.md) o [restricciones](validation_criteria.md) a casi cualquier tipo de pregunta. Si bien el Formbuilder actualmente no permite agregar estas funciones a una matriz de preguntas, puedes usar XLSForm para hacerlo. Los pasos que se enumeran a continuación en este artículo de ayuda ilustrarán cómo puedes agregar cálculos y restricciones a una matriz de preguntas usando XLSForm.

## Configurar la pregunta y los campos

**Paso 1: Crear una matriz de preguntas en el Formbuilder**

El primer paso es crear una matriz de preguntas en el Formbuilder (como se describe en el artículo de ayuda [Matriz de preguntas](matrix_response.md)). Simplemente agrega filas y columnas con las variables necesarias para la recolección de datos.

**Paso 2: Descargar el formulario como XLSForm**

Una vez que se haya creado la matriz de preguntas, **GUARDA** el formulario y [descárgalo como un XLSForm](getting_started_xlsform.md#downloading-an-xlsform-from-kobotoolbox).

**Paso 3: Agregar lógica a la matriz de preguntas**

Abre el XLSForm y agrega los encabezados de columna `calculation`, `constraint` y `constraint_message`. Con estos encabezados de columna, podrás agregar las expresiones de _total de columna_ y _total de fila_ bajo el encabezado de columna `calculation`. También puedes agregar las _restricciones_ apropiadas bajo el encabezado de columna `constraint` y el _mensaje de restricción_ bajo el encabezado `constraint_message` según sea necesario.

Además, también puedes optar por agregar un encabezado de columna `read_only` para restringir que los/as encuestadores/as editen las respuestas mientras recolectan datos de ciertas preguntas (por ejemplo, el _total de fila_ y el _total de columna_ que se calcula).

![Ventana Survey](images/calculations_constraints_matrix/survey_tab.png)

<p class="note">
  En la imagen de arriba, puedes notar que las entradas de <code>name</code> son más cortas. En este ejemplo, se han renombrado de las generadas automáticamente en el Formbuilder para capturar la captura de pantalla completa de la ventana survey. Si eliges renombrar las tuyas, asegúrate de usar tus nuevos nombres de variables en los encabezados de columna <code>calculation</code> y <code>constraint</code>. Si el formulario ya ha sido implementado y se han recolectado datos, se recomienda que <em>no</em> cambies el nombre de las variables existentes.
</p>

**Paso 4: Reemplazar el formulario**

Carga y reemplaza tu XLSForm dentro del proyecto existente, o crea un nuevo proyecto (si es necesario).

**Paso 5: Implementar el formulario**

**Paso 6: Recolectar datos**

Después de implementar el formulario, puedes ir a **FORMULARIO>Recolectar datos>ABRIR** para comenzar a recolectar datos con el formulario web.

## Ver el resultado

Las siguientes imágenes ilustran cómo se verá y funcionará el formulario en el formulario web de Enketo después de haber seguido los pasos anteriores:

**No se ingresaron datos:**

![Enketo sin datos ingresados](images/calculations_constraints_matrix/enketo_nothing_entered.png)

**Se cometió un error de entrada:**

![Enketo con entradas incorrectas ingresadas](images/calculations_constraints_matrix/enketo_wrong_inputs_entered.png)

Aquí verás que solo hay cinco miembros totales del hogar. Si un/a encuestador/a ingresa 6 para el número de hombres (0-14 años), la restricción mostrará un mensaje de error.

**Sin errores de entrada:**

![Enketo con entradas correctas ingresadas](images/calculations_constraints_matrix/enketo_correct_inputs_entered.png)

Aquí, cuando ingresas valores en una tabla de matriz, las filas y columnas se calculan automáticamente.

<p class="note">
  Puedes descargar el XLSForm que se utilizó para este artículo
  <a
    download
    class="reference"
    href="./_static/files/calculations_constraints_matrix/calculations_constraints_matrix.xlsx"
    >aquí</a
  >.
</p>

## Solución de problemas

-   La matriz de preguntas solo funciona con **formularios web de Enketo**. No es compatible con la **aplicación Android KoboCollect**.

-   La tabla de matriz aparecerá distorsionada si no configuras el diseño como **Tema de cuadrícula**. Para obtener más detalles sobre los aspectos de los formularios web, puedes consultar [Diseñar formularios web usando el Formbuilder](alternative_enketo.md).