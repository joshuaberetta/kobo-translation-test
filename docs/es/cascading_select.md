# Añadir preguntas de selección en cascada en el editor de formularios de KoboToolbox (Formbuilder)

<iframe src="https://www.youtube.com/embed/JDDNmErhV7o?si=S2k3G0sadiFJursu" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Las preguntas de selección en cascada te permiten crear formularios dinámicos donde las opciones de una pregunta dependen de la respuesta a una pregunta anterior. Esta funcionalidad ayuda a optimizar la recolección de datos al presentar solo las opciones relevantes, mejorando la eficiencia y precisión de tus encuestas.

<p class="note">
  <strong>Nota:</strong> Este artículo se enfoca en preguntas básicas de selección en cascada usando el editor de formularios. Para aprender más sobre el uso de XLSForm para crear preguntas avanzadas de selección en cascada y añadir filtros de opciones, consulta la <a href="https://xlsform.org/en/#cascading-selects">documentación de XLSForm</a>.
</p>

## Preparar una tabla de opciones en cascada

Para importar preguntas de selección en cascada en el editor de formularios, primero debes preparar tu lista de opciones en Excel u otro programa de hojas de cálculo. Puedes usar esta <a href="https://docs.google.com/spreadsheets/d/1C_uDOkjjbv5Kx3lyOY7ORwM-muW6BKVzdaPMB1X8-2A/edit?gid=0#gid=0">Plantilla de importación en cascada</a> para comenzar.

La tabla de opciones debe incluir las siguientes columnas:
- **list_name (nombre de la lista):** Identificador único para la lista de opciones de una pregunta. Este también será el nombre de columna de datos para la pregunta creada.
- **name (nombre):** Identificador único para cada opción dentro de una lista.
- **label (etiqueta):** Texto que aparece en el formulario para cada opción.

<p class="note">
  <strong>Nota:</strong> Al definir un <strong>list_name (nombre de la lista)</strong> o un <strong>name (nombre)</strong>, no uses símbolos como guiones largos o signos de interrogación. Solo se pueden usar letras del alfabeto, guiones bajos y números.
</p>

A continuación, debes añadir una columna para cada **lista principal**, que es una lista que incluye una sublista dentro de ella. Por ejemplo, una **lista principal** de continentes podría incluir una **lista secundaria** de países.

Para cada elemento en la **lista secundaria**, indica en la columna de **lista principal** a qué elemento principal pertenece el elemento secundario. Por ejemplo, si el país en la lista secundaria es Malawi, entonces en la columna de continente, indica África. Para referirte a un elemento de la lista principal, usa el **nombre de la opción**, no la etiqueta de la opción.

![Muestra de selección en cascada](images/cascading_select/sample.png)

## Importar la tabla en el editor de formularios

Una vez que tu lista de opciones esté lista, puedes importarla en el editor de formularios siguiendo estos pasos:
1. Copia toda la tabla de opciones de tu hoja de cálculo.
2. En el editor de formularios, click en <i class="k-icon-cascading"></i> **Insertar selección en cascada**.
3. Pega la tabla copiada en el cuadro de texto y click en **Listo** para importar. Este proceso creará automáticamente nuevas preguntas en tu formulario.
    - Si hay errores de formato, la importación fallará. Corrige cualquier error y asegúrate de haber seguido las instrucciones de la plantilla.
4. Una vez importadas, puedes mover las preguntas dentro de tu formulario, cambiar las etiquetas de preguntas y opciones, e incluso eliminar opciones.
5. Para añadir más opciones a la lista en cascada, elimina las preguntas importadas existentes e importa una nueva lista desde tu hoja de cálculo actualizada, siguiendo el mismo proceso descrito anteriormente.

![Ejemplo de insertar selección en cascada](images/cascading_select/insert_cascading_select.png)

<p class="note">
  <strong>Nota:</strong> Si cambias la etiqueta de la pregunta en el editor de formularios, asegúrate de que el nombre de columna de datos en su configuración aún coincida con el <strong>list_name (nombre de la lista)</strong> de tu tabla de lista de opciones.
</p>

## Manejo avanzado de selección en cascada usando XLSForm

Para mayor flexibilidad en el manejo y actualización de tus preguntas de selección en cascada, especialmente si anticipas cambios frecuentes en tus listas de opciones, se recomienda usar XLSForm. Este método te permite modificar directamente tus listas de opciones, sin perder ningún cambio realizado en las etiquetas y configuraciones de las preguntas.

Para actualizar tus preguntas de selección en cascada usando XLSForm:
1. Descarga tu XLSForm saliendo del editor de formularios, haciendo click en <i class="k-icon-more"></i><strong>Más acciones</strong> en la ventana **FORMULARIO**, y seleccionando **Descargar XLS**.
2. Navega a la hoja de trabajo `choices` en el archivo descargado y modifica tu lista de opciones. Mantén el mismo enfoque y formato descrito anteriormente para preparar una tabla de opciones en cascada.
3. Vuelve a cargar el XLSForm actualizado a KoboToolbox haciendo click en **Reemplazar formulario** y cargando tu archivo modificado.

<p class="note">
    Para aprender más sobre cómo añadir preguntas de selección en cascada y usar filtros de opciones en XLSForm, consulta la <a href="https://xlsform.org/en/#cascading-selects">Documentación de XLSForm</a>. Para más información sobre el uso de XLSForm con KoboToolbox, consulta <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">Iniciar con XLSForm</a>. 
</p>

## Solución de problemas
<details>
<summary><strong>La lista de opciones en cascada está en blanco</strong></summary>
Si la lista de opciones para la pregunta secundaria está vacía, la lista secundaria no está encontrando una coincidencia en la lista principal. Verifica que los nombres de las opciones no contengan símbolos (solo letras, números o guiones bajos) y que cada opción principal tenga al menos una opción secundaria vinculada a ella.
</details>
<br>
<details>
<summary><strong>Las cascadas se rompen después de editar el formulario</strong></summary>
Renombrar una pregunta o editar listas de opciones puede cambiar el código de backend del cual depende la cascada. Al renombrar una pregunta, asegúrate de que el <strong>nombre de columna de datos</strong> permanezca igual que el <strong>list_name (nombre de la lista)</strong> correspondiente. Para ediciones grandes de listas de opciones, reconstruye la cascada desde cero o descarga el XLSForm, realiza tus cambios allí y vuelve a cargarlo.
</details>
<br>
<details>
<summary><strong>Selección en cascada desde una pregunta Seleccionar varias</strong></summary>
La funcionalidad de selección en cascada en el editor de formularios está diseñada solo para preguntas de tipo <strong>Seleccionar una</strong>. Construir una cascada que comience desde una pregunta de tipo <strong>Seleccionar varias</strong> requiere usar XLSForm. 
Para aprender más sobre selección en cascada avanzada usando XLSForm, consulta la <a href="https://xlsform.org/en/#cascading-selects">documentación de XLSForm</a>.
</details>
<br>
<details>
<summary><strong>No se puede encontrar el elemento de la encuesta</strong></summary>
Un error que indica que no se puede encontrar un elemento de la encuesta generalmente significa que el código interno no coincide con las expectativas de la cascada. Para solucionar esto, abre la configuración de la pregunta, localiza el <strong>nombre de columna de datos</strong> y reviértelo al valor original (que debe coincidir con el <strong>list_name (nombre de la lista)</strong> correspondiente) antes de volver a desplegar tu formulario.
</details>