# Manejo de datos de grupos de repetición

KoboToolbox te permite recolectar datos repetidos dentro de un formulario, por ejemplo, al realizar una encuesta de hogares donde se hacen las mismas preguntas a todos/as los/as miembros/as. Este artículo explica cómo visualizar, editar y exportar datos de grupos de repetición, y cómo vincular los datos de grupos de repetición con los datos principales.

<p class="note">
  Para obtener más información sobre cómo configurar grupos de repetición en tus formularios, consulta <a href="https://support.kobotoolbox.org/group_repeat.html">Agrupar preguntas y repetir grupos</a>.
</p>

## Visualizar y editar datos de grupos de repetición
Puedes visualizar los datos repetidos en la tabla de datos, que se encuentra en la vista de **Tabla** de la ventana **DATOS** en la interfaz del proyecto de KoboToolbox. Las respuestas a las preguntas repetidas aparecen en una sola columna por pregunta, con las respuestas separadas por una coma, como se muestra a continuación.

 ![image](/images/managing_repeat_groups/data_table.png) 

También puedes visualizar los datos completos de cualquier envío, incluida cada repetición de los grupos de repetición, haciendo click en el botón <i class="k-icon-view"></i>**Abrir** a la izquierda de cada envío.

Para editar los datos de grupos de repetición, haz click en el botón <i class="k-icon-edit"></i>**Editar**. Esto abrirá el formulario y te permitirá [editar los datos del formulario](https://support.kobotoolbox.org/howto_edit_single_submissions.html) antes de volver a enviar. Actualmente no se admite la [edición masiva](https://support.kobotoolbox.org/howto_edit_multiple_submissions.html) de datos de grupos de repetición.

<p class="note">
  <b>Nota</b>: Los datos de grupos de repetición no se pueden mostrar en las vistas de <b>Informes</b> o <b>Mapa</b> debido a la estructura de datos de los grupos de repetición.
</p>

## Exportar datos de grupos de repetición
Para exportar datos de un formulario con grupos de repetición, debes descargar tus datos en **formato XLS**. Cada grupo de repetición se exportará **como una hoja separada** en el archivo exportado. La descarga en CSV solo proporcionará datos de los datos principales.

![image](/images/managing_repeat_groups/download.png)

<p class="note"> 
    Para obtener más información sobre cómo exportar tus datos, consulta <a href="https://support.kobotoolbox.org/export_download.html">Exportar y descargar tus datos</a>.
</p>

## Vincular datos de grupos de repetición
En los archivos XLS exportados, los datos de grupos de repetición se almacenan **en una hoja separada**. La primera hoja del archivo XLS contiene los datos de respuesta principales, y los datos de cada grupo de repetición se almacenan en su propia hoja. Los grupos de repetición anidados también se almacenan en hojas separadas.

Los datos de los grupos de repetición se pueden vincular con los datos principales utilizando la columna **_index** de la hoja de datos principales y la columna **_parent_index** de la hoja de datos del grupo de repetición.

En el ejemplo a continuación, la primera hoja incluye una columna **_index**, en verde, que identifica el primer envío. La segunda hoja, que se muestra en la segunda imagen, contiene una columna **_parent_index**, también resaltada en verde, que se vincula con la primera hoja. En este ejemplo, ambas filas de los datos repetidos provienen del primer envío de datos.

![image](/images/managing_repeat_groups/main_data.png)

![image](/images/managing_repeat_groups/repeat_group_data.png)

<p class="note">
  <b>Nota</b>: La hoja de datos del grupo de repetición también incluye una <b>columna _index</b>. Esta columna se utiliza para vincular a <b>grupos de repetición anidados</b>, siguiendo la misma configuración descrita anteriormente, con el grupo de repetición como los datos principales y el grupo de repetición anidado como los datos vinculados.
</p>

Los datos de grupos de repetición se pueden combinar con los datos principales utilizando diferentes herramientas para el análisis de datos. Por ejemplo, en Excel y Power BI, puedes usar [Power Query](https://learn.microsoft.com/en-us/power-query/power-query-what-is-power-query) o [VLOOKUP()](https://support.microsoft.com/en-us/office/vlookup-function-0bbc8083-26fe-4963-8ab8-93a18ad188a1) para combinar datos. En SQL, R, SAS y otros lenguajes de manejo de bases de datos, puedes combinar los conjuntos de datos usando una [combinación izquierda](https://learn.microsoft.com/en-us/sql/relational-databases/performance/joins?view=sql-server-ver17).

<p class="note">
  Para obtener más información sobre cómo combinar datos de grupos de repetición usando Power Query, consulta <a href="https://support.kobotoolbox.org/merging_dataset_excel_power_query.html?highlight=power+query">Combinar datos individuales con datos de lista a través de Power Query en Excel</a>.<br><br>Para obtener más información sobre cómo combinar conjuntos de datos en R, consulta <a href="https://dplyr.tidyverse.org/reference/mutate-joins.html">Uniones de mutación</a>.
</p>