# Exportar y descargar tus datos

<iframe src="https://www.youtube.com/embed/bXzwvvnhj7U" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Cuando usas KoboToolbox, puedes descargar tus datos recolectados en varios formatos y personalizar la configuración de exportación. Este artículo explica cómo descargar tus datos recolectados, incluyendo una descripción general de los tipos de exportación y los formatos disponibles.

## Descargar tus datos

Para descargar tus datos:

1. Abre tu proyecto y navega a **DATOS > Descargas**.
2. Elige la configuración de exportación (se detalla a continuación).
3. Click en **EXPORTAR**. Esto generará una exportación que se mostrará en una tabla debajo de la configuración de exportación.
4. Click en **DESCARGAR** para descargar el archivo exportado.

![Ejemplo de exportación de datos](images/export_download/export.png)

<p class="note">
    <strong>Nota:</strong> Una exportación puede tardar desde unos segundos hasta varios minutos en generarse, dependiendo del número de envíos, el tamaño del formulario y la carga del servidor. Una vez creada, aparecerá en la sección <strong>Exportaciones</strong> de la página.
</p>

## Tipos de exportación

Puedes elegir entre los siguientes tipos de exportación:

| **Tipo de exportación**    | **Descripción**                                |
| :----------------- | :--------------------------------------------- |
| XLS               | Archivo de Microsoft Excel (formato .xlsx). Este tipo de archivo se recomienda cuando recolectas datos de grupos de repetición.                                  |
| CSV      | Archivo de valores separados por comas. Este tipo de archivo es ideal para importar a la mayoría de los programas de manejo de datos, incluyendo bases de datos.                                  |
| GeoJSON           | Este es un formato de intercambio de datos geoespaciales de estándar abierto, ideal para integrar con programas de SIG como ArcGIS.            |
| SPSS Labels           | Genera un archivo de sintaxis de SPSS que aplica etiquetas de preguntas y etiquetas de valores a las variables de datos de KoboToolbox importados en SPSS. Para más información, consulta <a href="https://support.kobotoolbox.org/converting_to_spss_and_stata.html">Convertir datos a SPSS y/o Stata</a>.         |
| GPS Coordinates (KML)               | Genera un archivo KML para trabajar con tus datos en programas de SIG, como Google Earth.                               |
| Media Attachments (ZIP)               |  Descarga un archivo ZIP que contiene todos los datos multimedia recolectados a través del formulario.                               |
| XLS (legacy)              | Genera un archivo .xlsx (Microsoft Excel) usando una interfaz heredada de KoboToolbox. Usa esta opción solo en caso de problemas ocasionales con las exportaciones estándar de XLS y CSV, ya que se eliminará en una actualización futura.                                  |
| CSV (legacy)               | Genera un archivo CSV usando una interfaz heredada de KoboToolbox. Usa esta opción solo en caso de problemas ocasionales con las exportaciones estándar de XLS y CSV, ya que se eliminará en una actualización futura.                                  |

## Formato de valores y encabezados

Cuando usas los formatos de exportación estándar (XLS, CSV, GeoJSON y SPSS Labels), puedes seleccionar el formato de tus valores de datos y encabezados:

| **Formato**    | **Descripción**                                |
| :----------------- | :--------------------------------------------- |
| Labels (default)               | El archivo exportado usa <strong>etiquetas de preguntas</strong> (texto de la pregunta) como encabezados de columna y <strong>etiquetas de opciones</strong> para las respuestas a preguntas de Seleccionar una y Seleccionar varias.                                  |
| XML values and headers      | El archivo exportado usa <strong>nombres de preguntas</strong> (nombres de columna de datos) como encabezados de columna y <strong>nombres de opciones</strong> (valores XML) para las respuestas. Esta configuración de exportación se recomienda para importar tus datos a programas de análisis de datos.                                  |
| Labels in any of the defined languages           | El archivo exportado usa <strong>etiquetas de preguntas y opciones</strong> en cualquiera de los idiomas configurados dentro del formulario.            |

## Opciones avanzadas

Además de personalizar los formatos de valores y encabezados, los formatos de exportación no heredados también ofrecen otras opciones de personalización dentro de la sección **Opciones avanzadas**. Para más información sobre las opciones avanzadas, consulta [Opciones avanzadas para exportar datos](https://support.kobotoolbox.org/advanced_export.html).

## Solución de problemas

<details>
    <summary><strong>Exportaciones atascadas en estado pendiente o fallidas</strong></summary>
    
El tiempo de exportación depende del número de envíos, la complejidad del formulario y la carga actual del servidor. Si las exportaciones permanecen en estado pendiente durante un período prolongado:
- Elimina las exportaciones atascadas haciendo click en el <i class="k-icon-trash"></i> <strong>ícono de papelera.</strong>
- Vuelve a intentar la exportación haciendo click en el botón <strong>EXPORTAR</strong> nuevamente.
- Evita crear múltiples exportaciones rápidamente, ya que esto puede sobrecargar el servidor y reducir el rendimiento para todos/as los/as usuarios/as.

<p class="note">
    <strong>Nota:</strong> Las exportaciones agotarán el tiempo de espera y se mostrarán como <strong>fallidas</strong> después de 30 minutos. Este límite a nivel del servidor puede requerir que filtres el número de envíos incluidos en la exportación para completarla dentro del tiempo permitido. Un ejemplo de cómo hacer esto se discute en el <a href="https://community.kobotoolbox.org/t/how-to-download-data-between-two-dates-from-date-to-date/25569/4">Foro de la comunidad</a>.
</p>

Si continúas experimentando problemas al exportar tus datos, por favor publica en el <a href="https://community.kobotoolbox.org/">Foro de la comunidad</a>.
</details>

<br>

<details>
    <summary><strong>Datos de grupos de repetición no encontrados</strong></summary>
Solo el <b>formato XLS</b> admite datos de grupos de repetición. Cada grupo de repetición se exportará <strong>como una hoja separada</strong> en el archivo exportado. Las descargas en CSV solo proporcionarán los datos principales, sin los datos de grupos de repetición. 
<br><br>
Para más información sobre cómo exportar y usar datos de grupos de repetición, consulta <a href="https://support.kobotoolbox.org/managing_repeat_groups.html">Manejo de datos de grupos de repetición</a>.    
</details>

<br>

<details>
    <summary><strong>Algunos datos no se están exportando</strong></summary>
    Si algunos de tus datos no se están exportando, verifica las <a href="https://support.kobotoolbox.org/advanced_export.html">opciones avanzadas</a>. Por ejemplo, asegúrate de que los datos de todas las versiones de tu formulario estén seleccionados para la exportación.
</details>

<br>

<details>
    <summary><strong>Descargar datos de diferentes versiones</strong></summary>
    Cuando descargues datos que incluyen múltiples versiones del formulario, puedes encontrar cambios en el formato de tus archivos de datos. 
</details>

<br>

<details>
    <summary><strong>Datos de zona horaria se pierden en la exportación</strong></summary>
    Los formatos de tiempo de Excel no admiten datos de zona horaria. Por lo tanto, cualquier dato de zona horaria en el valor de respuesta se eliminará durante la exportación XLS. Para conservar esta información, marca la opción de exportar fechas como valores de texto. 
<br><br>
Para más información sobre esta configuración, consulta <a href="https://support.kobotoolbox.org/advanced_export.html">Opciones avanzadas para exportar datos</a>.
</details>