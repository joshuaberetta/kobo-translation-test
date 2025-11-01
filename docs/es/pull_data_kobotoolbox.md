# Funcionalidad de extracción de datos en KoboToolbox

Esto se hace mejor en la versión xls del formulario.

-   En el lado de la encuesta del formulario, añade un campo de cálculo a tu encuesta.
-   Dale a ese campo el nombre que desees
-   Luego, en su columna de cálculo, llama a la función pulldata(), indicando
    qué campo extraer de qué fila de qué archivo .csv. Esto se puede lograr
    escribiendo lo siguiente
    `pulldata('nombredelcsv', 'encabezadodecolumnaparaextraerdatos', 'columnaparaverificarcoincidenciaTEXTO', 'TEXTOaVerificar'`

    ![image](/images/pull_data_kobotoolbox/xls.png)

-   Ten en cuenta que tu CSV debe tener al menos dos columnas y asegúrate de que la
    columnaparaverificarcoincidenciaTEXTO sea siempre la primera columna desde la izquierda
-   TEXTOaVerificar también puede ser referenciado desde una pregunta de campo anterior
    usando `${Pregunta}` como en el ejemplo anterior
-   Una vez que hayas terminado de actualizar el xls, necesitarás cargar tu formulario
    desde xls (no lo edites en el editor de formularios de KoboToolbox (Formbuilder)), luego cargarás tu CSV
    de la misma manera que cargarías tus imágenes.
-   Cuando despliegues tu archivo, el csv se descargará a los archivos multimedia

**Aspectos a tener en cuenta**

-   Esto funcionará tanto en la aplicación de Android de KoboCollect como en Enketo (formulario web).
-   Comprime un archivo .csv grande en un archivo .zip antes de cargarlo.
-   Guarda el archivo .csv en formato UTF-8 si los datos precargados contienen fuentes no inglesas
    o caracteres especiales, esto permite que tu dispositivo Android muestre el texto
    correctamente.
-   Los campos de datos extraídos de un archivo .csv se consideran cadenas de texto,
    por lo tanto, usa las funciones int() o number() para convertir un campo precargado
    en forma numérica.
-   Si el archivo .csv contiene datos sensibles que no deseas cargar al
    servidor, carga un archivo .csv en blanco como parte de tu formulario, luego reemplázalo
    con el archivo .csv real copiando manualmente el archivo en cada uno de tus dispositivos.
-   Si estás enfrentando mensajes de error al usar esta funcionalidad, intenta cambiar el nombre del archivo para eliminar guiones bajos o símbolos.