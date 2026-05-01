# Opciones avanzadas para la exportación de datos

Las opciones avanzadas brindan mayor control y flexibilidad al descargar y exportar tus datos. Este artículo te guiará a través de la personalización de tus exportaciones de datos, desde la selección de campos de datos y el manejo de varios tipos de preguntas hasta el establecimiento de parámetros para diferentes necesidades analíticas.

<p class="note">
    Para obtener más información sobre la descarga de datos, incluida una descripción general de los tipos de exportación y los formatos disponibles, consulta <a href="https://support.kobotoolbox.org/es/export_download.html?highlight=export">Exportar y descargar datos.</a>
</p>

## Opciones de exportación para preguntas de selección múltiple

La opción **Exporta preguntas Seleccionar varias como...** te permite elegir cómo exportar datos de preguntas **Seleccionar varias** (también llamadas `select_multiple`). Puedes elegir exportarlas como:

| **Opción de exportación**    | **Descripción**                                |
| :----------------- | :------------------------------------ |
| Columnas individuales y separadas &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;              | Esta configuración predeterminada exporta una columna con todas las opciones seleccionadas de las preguntas <strong>Seleccionar varias</strong>, más columnas individuales para cada respuesta, como se muestra a continuación.<br> ![Cómo seleccionar varias columnas](images/advanced_export/select_many_columns.png) |
| Columnas separadas  | Cada respuesta a las preguntas <strong>Seleccionar varias</strong> se exportará en columnas separadas.|
| Columna individual   | Las respuestas a las preguntas <strong>Seleccionar varias</strong> se exportarán en una sola columna.            |


<p class="note">
  <strong>Nota:</strong> En las columnas separadas, un valor de '1' indica que la opción fue seleccionada, mientras que '0' significa que el/la encuestado/a no eligió esa opción.
</p>

## Seleccionar campos de datos para exportar

Las opciones de exportación avanzadas te permiten refinar tu descarga de datos al incluir datos de todas las versiones del formulario o seleccionar preguntas específicas para exportar.

| **Configuración de Exportar**    | **Descripción**                                |
| :----------------- | :------------------------------------ |
| Incluye campos de las […] versiones &emsp;&emsp;&emsp;&emsp;&emsp;&emsp; | De forma predeterminada, esta opción está marcada. Esto te permite descargar datos de todas las versiones del formulario, incluidas las preguntas o opciones eliminadas. Si no está marcada, solo se descargarán los datos de la última versión del formulario implementado. |
| Seleccionar las preguntas que se exportarán | Para exportar datos de preguntas específicas, habilita esta opción y selecciona las preguntas que deseas incluir. |
| Rango de datos | Para exportar datos enviados dentro de un rango de fechas específico, habilita esta opción y selecciona las fechas de inicio y/o finalización. Los filtros de fecha se basan en el tiempo de envío y utilizan la zona horaria UTC. Los datos enviados en las fechas de <strong>inicio</strong> y <strong>finalización</strong> se incluyen en las exportaciones. |

![Cómo seleccionar campos de datos](images/advanced_export/select_data_fields.png)

## Opciones adicionales de formato de datos

KoboToolbox ofrece opciones adicionales de formato de datos para personalizar aún más tus exportaciones, como incluir nombres de grupos en los encabezados, almacenar respuestas de fecha y número como texto o incluir URL de archivos multimedia.

| **Configuración de Exportar**    | **Descripción**                                |
| :----------------- | :------------------------------------ |
| Incluir grupos en los encabezados | Elige esta opción para agregar nombres de grupos a cada encabezado de pregunta, como se muestra en el ejemplo a continuación. ![Incluir grupos en los encabezados](images/advanced_export/group_headers2.png) | 
| Almacenar las respuestas de fechas y números como texto &emsp;&emsp;&emsp;&emsp;&emsp;&emsp; | De forma predeterminada, las preguntas <strong>Fecha, Fecha y hora, Número</strong> y <strong>Decimal</strong> se guardan con sus tipos de datos correspondientes cuando se exportan a XLS. Marca esta opción si prefieres exportarlas como texto.<br><br><strong>Nota:</strong> Los formatos de tiempo de Excel no admiten datos de zona horaria; por lo tanto, cualquier dato de zona horaria en el valor de respuesta se eliminará durante la exportación. Para conservar esta información, marca la opción de exportar fechas como valores de texto. |
| Incluir URL de archivos multimedia | Si tu formulario recolectó archivos multimedia (fotos, audio, videos o archivos), marca esta opción para asegurarte de que tu archivo exportado incluya enlaces a estos archivos multimedia. |

## Guardar configuraciones de exportación

Puedes guardar tus configuraciones de exportación definidas para uso futuro o para generar un enlace de [exportación sincrónica](https://support.kobotoolbox.org/es/synchronous_exports.html) para software como PowerBI o Excel.

| **Configuración de Exportar** | **Descripción**                                |
| :-------------------- | :------------------------------------ |
| Guardar selección como... &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;| Marca esta opción e ingresa un nombre para tu configuración de exportación. Cuando hagas clic en <strong>EXPORTAR</strong>, estas configuraciones se guardarán y el nombre aparecerá en el cuadro <strong>Aplicar configuración de exportación guardada</strong>. | 

Para usar configuraciones de exportación guardadas, haz clic en el menú desplegable en **Aplicar configuración de exportación guardada** y selecciona la configuración de exportación nombrada de tu elección.