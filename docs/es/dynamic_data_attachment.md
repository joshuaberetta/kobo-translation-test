# Conexión dinámica de proyectos usando XLSForms

La conexión dinámica te permite usar datos de un **proyecto primario** dentro de **proyectos secundarios**, simplificando el manejo de la recolección de datos longitudinales. Este artículo explica cómo conectar dinámicamente datos entre proyectos de KoboToolbox.

<p class="note">
    <strong>Nota:</strong> La conexión dinámica de proyectos funciona de manera similar a la función <a href="https://support.kobotoolbox.org/pull_data_kobotoolbox.html"><code>pulldata()</code></a>, pero elimina la necesidad de archivos CSV separados, ya que los datos del proyecto primario conectado sirven como fuente de datos.
</p>

Puedes recuperar varias **respuestas sin multimedia** de un proyecto primario y realizar cálculos sobre estos datos conectados en un proyecto secundario. Esto puede ser útil para recuperar datos de línea de base, información de contacto o registros de salud en estudios de cohorte, o para confirmar o verificar datos recolectados previamente.

Recomendamos usar [XLSForm](https://support.kobotoolbox.org/edit_forms_excel.html) para configurar la conexión dinámica de proyectos. Para ejemplos de proyectos primarios y secundarios, descarga los archivos de muestra [aquí](https://support.kobotoolbox.org/_static/files/dynamic_data_attachment/parent.xlsx) y [aquí](https://support.kobotoolbox.org/_static/files/dynamic_data_attachment/child.xlsx).

## Conectar proyectos dinámicamente en XLSForm

Conectar proyectos dinámicamente requiere un **proyecto primario** y al menos un **proyecto secundario**. El **proyecto primario** no requiere modificación respecto a un XLSForm normal. Sin embargo, configurar el/los **proyecto(s) secundario(s)** implica los siguientes pasos:
1. En la hoja de trabajo `survey` de tu XLSForm, agrega una fila y configura el tipo de pregunta como `xml-external`.
2. En la columna `name`, proporciona un nombre corto para el formulario primario. Este nombre puede consistir en caracteres del alfabeto latino, guiones bajos y números.

**hoja survey**

| type | name     | label              |
| :--- | :------- | :----------------- |
| xml-external | parent |
| survey | 


3. A lo largo del formulario, puedes recuperar valores del proyecto primario creando una nueva pregunta e incluyendo la expresión apropiada en la columna `calculation` (ver tabla [abajo](https://support.kobotoolbox.org/dynamic_data_attachment.html#calculation-syntax-for-dynamic-data-attachments)). Puedes usar los siguientes tipos de pregunta para recuperar datos:
    - Utiliza un tipo de pregunta **calculate** (cálculo) para recuperar y almacenar valores para uso futuro dentro del formulario o conjunto de datos (por ejemplo, para cálculos o etiquetas de preguntas dinámicas).
    - Utiliza tipos de pregunta **text** (texto), **integer** (número), **decimal**, **select_one** (seleccionar una) o **select_multiple** (seleccionar varias) para incluir valores recuperados como respuestas predeterminadas en campos editables. Los datos editados en el proyecto secundario no cambiarán los datos originales en el proyecto primario.
  
**hoja survey**
      
| type | name     | label              | calculation |
| :--- | :------- | :----------------- | :----------------- |
| xml-external | parent |               |              |
| text | participant_id | ¿Cuál es el ID del/la participante? |  |
| integer | age | Confirma la edad del/la participante | instance('parent')/root/data[enrollment_id = current()/../participant_id]/age |
| survey | 

<p class="note">
   <strong>Nota:</strong> 
    Para mostrar datos conectados sin permitir que los/as usuarios/as editen el campo, usa una pregunta <strong>calculate</strong> (cálculo) seguida de una pregunta <strong>note</strong> (nota) que muestre el valor calculado. Alternativamente, usa preguntas <strong>text</strong> (texto), <strong>integer</strong> (número), <strong>decimal</strong>, <strong>select_one</strong> (seleccionar una) o <strong>select_multiple</strong> (seleccionar varias) con la columna <code>read_only</code> configurada como <code>TRUE</code>.
</p>

## Sintaxis de cálculo para la conexión dinámica de proyectos

En la columna `calculation` de la fila donde se recuperarán los datos conectados, incluye una de las expresiones de la tabla a continuación. Estas expresiones se llaman **XPaths**.

Para cada expresión en la tabla a continuación:

- `parent` es el nombre único asignado al **formulario primario** (por ejemplo, en la pregunta `xml-external` del **formulario secundario**).
- `parent_question` se refiere al `name` (nombre) de una pregunta del **formulario primario**.
- `child_question` se refiere al `name` (nombre) de una pregunta del **formulario secundario**.
- `parent_index_question` es la pregunta identificadora del **formulario primario** que lo conecta con el **formulario secundario** (por ejemplo, ID único, nombre de organización).
- `child_index_question` es la pregunta identificadora del **formulario secundario** que lo conecta con el **formulario primario** (por ejemplo, ID único, nombre de organización).
- `parent_group` se refiere al `name` (nombre) del grupo en el **formulario primario** en el que se encuentra la `parent_question`.
- `parent_index_group` se refiere al `name` (nombre) del grupo en el **formulario primario** en el que se encuentra la `parent_index_question`.

| **XPath**    | **Descripción**                                |
| :----------------- | :--------------------------------------------- |
| `count(instance('parent')/root/data)` | Devuelve el número total de filas en el proyecto primario. |
| `count(instance('parent')/root/ data[parent_group/parent_question])`      | Devuelve el número total de filas en el proyecto primario donde `parent_question` (en `parent_group`) no está vacía. |
| `count(instance('parent')/root/ data[parent_group/parent_question= current()/../child_question]` | Devuelve el recuento total de instancias donde el valor de `parent_question` (en `parent_group`) en el proyecto primario es igual al valor de `child_question` en el proyecto secundario. |
| `instance('parent')/root/ data[parent_index_group/parent_index_question= current()/../child_index_question]/parent_group/ parent_question` | Devuelve el valor de `parent_question` (en `parent_group`) del proyecto primario donde `child_index_question` en el proyecto secundario es igual a `parent_index_question` en el proyecto primario. |
| `instance('parent')/root/ data[parent_index_group/parent_index_question= current()/../child_index_question][position()= 1]/parent_group/parent_question` | Igual que arriba, pero especifica que solo se deben devolver datos de la primera instancia de `parent_index_question`, usando el argumento `[position() = 1]`. Se usa en caso de posibles duplicados en el formulario primario. |
| `sum(instance('parent')/root/ data/parent_group/parent_question)` | Devuelve la suma de valores de `parent_question` (en `parent_group`) del proyecto primario. Ten en cuenta que `parent_question` debe ser numérica. |
| `max(instance('parent')/root/ data/parent_group/parent_question)`         | Devuelve el valor máximo ingresado en `parent_question` (en `parent_group`) del proyecto primario. Ten en cuenta que `parent_question` debe ser numérica.     |
| `min(instance('parent')/root/ data/parent_group/parent_question)`      | Devuelve el valor mínimo ingresado en `parent_question` (en `parent_group`) del proyecto primario. Ten en cuenta que `parent_question` debe ser numérica.     |   


<p class="note">
    <strong>Nota:</strong> Si la pregunta primaria no está incluida en ningún grupo, omite <code>parent_group</code> de la expresión.
</p>

## Configurar proyectos para la conexión dinámica

Una vez que tus XLSForms estén configurados, inicia sesión en tu cuenta de KoboToolbox y sigue estos pasos:

1. Carga e implementa el **proyecto primario**, si aún no está implementado. Asegúrate de que el proyecto primario tenga al menos un envío.
2. Habilita el uso compartido de datos para el proyecto primario: 
    - En la ventana **CONFIGURACIÓN > Conectar proyectos** del proyecto primario, activa el interruptor **Compartir datos** (deshabilitado por defecto) y haz clic en **CONFIRMAR Y CONTINUAR** en la ventana de confirmación. 
    - Todos los datos se comparten por defecto, pero puedes restringir variables específicas para compartir con proyectos secundarios haciendo clic en "Seleccionar preguntas específicas para compartir".

<p class="note">
    <strong>Nota:</strong> Si los proyectos tienen diferentes propietarios/as, el/la propietario/a del proyecto primario debe <a href="https://support.kobotoolbox.org/managing_permissions.html">compartir el proyecto</a> con el/la propietario/a del proyecto secundario. Los permisos mínimos requeridos para que la conexión dinámica de proyectos funcione son <strong>Ver formulario</strong> y <strong>Ver envíos</strong>. Ten en cuenta que esto permite a los/as administradores/as del proyecto secundario ver todos los datos del proyecto primario.
</p>

3. Carga e implementa el **proyecto secundario**.
4. Conecta el proyecto secundario al proyecto primario: 
    - En la ventana **CONFIGURACIÓN > Conectar proyectos** del proyecto secundario, haz clic en "Seleccionar un proyecto diferente desde el cual importar datos". Un menú desplegable te permitirá seleccionar un proyecto primario para conectar. 
    - Renombra el proyecto primario conectado con el nombre de la pregunta `xml-external` definido en el XLSForm y haz clic en **IMPORTAR**. 
    - Luego puedes seleccionar preguntas específicas del proyecto primario para compartir con el proyecto secundario, o seleccionar todas las preguntas.
5. Si agregas nuevos campos al formulario primario y deseas usarlos en el proyecto secundario, vuelve a importar el proyecto primario en la configuración del proyecto secundario.

<p class="note">
    <strong>Nota:</strong> Los formularios solo se pueden conectar entre sí si están en el mismo servidor de KoboToolbox.
</p>

<iframe src="https://www.youtube.com/embed/pBqEsFlxqE4?si=6BPiDgOzO4LPO7zv" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


## Conectar dinámicamente un formulario consigo mismo

Es posible que un proyecto primario y secundario sean el mismo proyecto. Los pasos son los mismos que los descritos anteriormente. Ejemplos de casos de uso incluyen: 

- **Monitoreo diario**: Si un formulario se usa para encuestar a la misma persona a lo largo del tiempo, puedes conectarlo consigo mismo para contar envíos previos. Esto puede permitirte mostrar un mensaje (por ejemplo, "el monitoreo está completo") después de un cierto número de entradas o informar al/la encuestador/a del número de formularios enviados, como se muestra en el ejemplo a continuación.

**hoja survey**

| type | name     | label              | calculation |
| :--- | :------- | :----------------- | :----------------- |
| xml-external | monitoring |               |              |
| text | participant_id | ¿Cuál es el ID del/la participante? |  |
| calculate | count |  | count(instance('monitoring')/root/ data[monitoring/participant_id = current()/../participant_id]) |
| note | monitoring_note | Este/a participante ha sido encuestado/a ${count} veces. | |
| survey | 

- **Formulario de registro**: Al conectar un formulario de registro consigo mismo, puedes verificar si un/a usuario/a ya ha sido registrado/a. Esto puede permitirte generar un mensaje de error o agregar una restricción si ya está registrado/a, evitando registros duplicados, como se muestra en el ejemplo a continuación.

**hoja survey**

| type | name     | label              | calculation | relevant | 
| :--- | :------- | :----------------- | :----------------- | :------------ |
| xml-external | registration |               |              | |
| text | customer_id | ¿Cuál es el número de ID del/la cliente? |  | | 
| calculate | count |  | count(instance('registration')/root/ data[registration/customer_id = current()/../customer_id]) | |
| note | already_registered | Este/a cliente ya está registrado/a. Por favor cierra este formulario. | | ${count} > 0 |
| survey | 

## Recolectar y manejar datos con conexión dinámica

Los datos para proyectos conectados dinámicamente se pueden recolectar usando la [aplicación Android KoboCollect](https://support.kobotoolbox.org/kobocollect_on_android_latest.html) o [formularios web de Enketo](https://support.kobotoolbox.org/data_through_webforms.html).

Al recolectar datos, ten en cuenta lo siguiente:

- El proyecto primario debe tener al menos un envío para que el proyecto secundario funcione correctamente.
- Al recolectar datos en línea, hay un retraso de cinco minutos en la sincronización de nuevos datos del proyecto primario con el proyecto secundario.
- En modo sin conexión, descarga frecuentemente el proyecto secundario para asegurar la sincronización de datos con el proyecto primario.

<p class="note">
    <strong>Nota:</strong> Puedes <a href="https://support.kobotoolbox.org/kobocollect_settings.html#form-management-settings">configurar la aplicación Android KoboCollect</a> para actualizar automáticamente los datos del proyecto primario cuando haya una conexión a internet disponible. Ve a <strong>Ajustes > Manejo de formularios > Modo de actualización de formularios en blanco</strong> y selecciona <strong>Solo formularios descargados previamente</strong> o <strong>Coincidir exactamente con el servidor</strong>. Puedes configurar la frecuencia de descarga automática para que ocurra cada 15 minutos, cada hora, cada seis horas o cada 24 horas. Ten en cuenta que habilitar esta configuración puede aumentar el consumo de batería.
</p>

## Solución de problemas

<details>
<summary><strong>Error o fallo al conectar formularios</strong></summary>
La conexión dinámica de proyectos no puede conectarse a un proyecto primario vacío. Agrega al menos un envío al proyecto primario primero, luego conecta los formularios nuevamente.
</details>

<br>

<details>
<summary><strong>Los datos primarios no se muestran en el formulario secundario</strong></summary>
Verifica que la sintaxis de cálculo en el formulario secundario sea correcta y que las preguntas relevantes estén compartidas en ambos proyectos. Si tu pregunta primaria está en un grupo de preguntas, asegúrate de incluir el nombre del grupo en la expresión XPath. Ten en cuenta que los nuevos datos del proyecto primario tardan hasta cinco minutos en sincronizarse cuando estás en línea. Si agregas nuevos campos al formulario primario y deseas usarlos en el proyecto secundario, abre la configuración del proyecto secundario, vuelve a importar el proyecto primario y vuelve a implementar.
</details>

<br>

<details>
<summary><strong>El formulario secundario carga lentamente</strong></summary>
Las conexiones dinámicas de proyectos grandes pueden ralentizar la carga del formulario. Comparte solo las preguntas que el formulario secundario necesita en lugar de la lista completa de preguntas, luego vuelve a implementar e intenta nuevamente.
</details>

<br>

<details>
<summary><strong>Los datos dinámicos no se actualizan en KoboCollect</strong></summary>
Si estás usando KoboCollect y recolectando datos sin conexión, los datos primero deben enviarse al proyecto primario y luego descargarse a tu dispositivo de recolección de datos para que la conexión dinámica de proyectos funcione. Ambos pasos requieren una conexión a internet. Descargar datos primarios es similar a descargar una nueva versión de un formulario, y la aplicación KoboCollect se puede configurar para <a href="https://support.kobotoolbox.org/kobocollect_settings.html#form-management-settings">descargar automáticamente nuevos datos</a> con una frecuencia establecida. No se recomienda depender de la conexión dinámica de proyectos para datos recolectados sin conexión en un corto período de tiempo.
</details>

<br>

<details>
<summary><strong>La conexión dinámica de proyectos no funciona dentro de grupos de preguntas</strong></summary>
Para extraer datos dinámicos de un formulario primario a un formulario secundario con grupos de preguntas, asegúrate de que la pregunta índice (por ejemplo, el número de identificación) en el formulario secundario esté en el mismo grupo que el cálculo para los datos dinámicos. Consulta los archivos de muestra <a href="https://community.kobotoolbox.org/uploads/short-url/z5RpC1M3wj9716z9qQ8pWx9Pb4V.xlsx">Ronda 1 (Dentro de grupos).xlsx</a> y <a href="https://community.kobotoolbox.org/uploads/short-url/8JZvWJcrCxzKBllQYglRyAVyk03.xlsx">Ronda 2 (Dentro de grupos).xlsx</a> para un ejemplo de conexión dinámica de proyectos dentro de grupos.
</details>

<br>

<details>
<summary><strong>Error al evaluar campos en KoboCollect</strong></summary>
Si tu formulario primario contiene envíos duplicados, puedes recibir un mensaje de error en KoboCollect que indica "Error al evaluar el campo / Evaluación XPath: tipo no coincide / Este campo se repite". Para resolver este problema y extraer datos solo del primer envío que contiene un valor de índice específico, usa el argumento <code>[position()=1]</code>, como se muestra a continuación:
<br><br>
<code>instance('parent')/root/data[parent_index_group/parent_index_question = current()/../child_index_question][position()=1]/parent_group/parent_question</code>

</details>