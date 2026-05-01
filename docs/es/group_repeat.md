# Grupos y grupos de repetición en el Formbuilder

<iframe src="https://www.youtube.com/embed/nmPACLvYnUI?si=mkUi9RBLNHObj9ei" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Agrupar preguntas ayuda a organizar preguntas relacionadas en secciones, añade estructura a tu formulario y facilita la navegación. Por ejemplo, todas las preguntas demográficas pueden agruparse en una sección del formulario.

Los/as usuarios/as pueden necesitar agrupar preguntas por varias razones:
-   **Estructurar el cuestionario:** Las preguntas con temas o atributos comunes pueden agruparse en una sola sección.
-   **Mostrar un conjunto de preguntas por página:** Las preguntas agrupadas pueden mostrarse en páginas o pantallas separadas durante la recolección de datos.
-   **Omitir un grupo de preguntas:** La lógica de omisión puede añadirse a todo el grupo en lugar de añadirla a cada pregunta individual.
-   **Crear un grupo:** Los grupos de preguntas pueden repetirse, por ejemplo para encuestas de hogares o seguimiento de indicadores.

Este artículo explica cómo crear y gestionar grupos de preguntas y [grupos de repetición](#repetir-un-grupo-de-preguntas) en el editor de formularios de KoboToolbox (Formbuilder).

## Crear y gestionar grupos de preguntas

El Formbuilder facilita agrupar preguntas, añadir preguntas a grupos, eliminar preguntas de grupos y reordenar preguntas dentro de un grupo.

### Agrupar un conjunto de preguntas

Para crear un grupo de preguntas, sigue los pasos a continuación:

1. Crea un conjunto de preguntas que deseas agrupar.
2. Selecciona las preguntas usando la tecla **CTRL** (Windows) o la tecla **Command** (Mac).
3. Haz clic en <i class="k-icon-group"></i> **Crear grupo con las preguntas seleccionadas** en la barra de menú superior izquierda.

![image](/images/group_repeat/grouping_questions.png)

Tu nuevo grupo aparecerá dentro de un cuadro sombreado, distinguiéndolo de las preguntas estándar. También puedes cambiar la etiqueta del grupo, que se mostrará en la parte superior del grupo en el formulario.

<p class="note">
    <b>Nota:</b> Alternativamente, puedes crear una sola pregunta, seleccionarla y hacer clic en <b>Crear grupo</b>. Luego, puedes añadir más preguntas dentro del grupo, como se describe a continuación.
</p>

### Añadir preguntas dentro de un grupo

Coloca el cursor en cualquier lugar dentro del grupo donde deseas añadir una nueva pregunta. Haz clic en el <i class="k-icon-plus"></i> **signo** dentro del grupo para añadir una nueva pregunta.

<p class="note">
    <b>Nota:</b> Si haces clic en el <i class="k-icon-plus"> </i><b>signo</b> que se encuentra fuera del grupo, estarás añadiendo una pregunta fuera del grupo.
</p>

También puedes arrastrar y soltar cualquier pregunta existente dentro de un grupo de preguntas.

### Eliminar preguntas de un grupo

Para eliminar una pregunta de un grupo pero mantenerla en el formulario, selecciona la pregunta y arrástrala fuera del grupo.

Para eliminar permanentemente una pregunta del formulario, haz clic en <i class="k-icon-trash"></i> **Eliminar pregunta** desde el menú de la pregunta a la derecha, luego haz clic en **OK**.

### Reordenar una pregunta dentro de un grupo

Puedes reordenar preguntas dentro de un grupo seleccionando la pregunta y arrastrándola a la posición deseada (arriba o abajo).

### Eliminar un grupo de preguntas
Si ya no necesitas un grupo de preguntas, puedes desagruparlas o eliminar todo el grupo. Para hacer esto, haz clic en el botón <i class="k-icon-trash"></i> **Eliminar** del encabezado del grupo.

Aparecerá un cuadro de diálogo pidiéndote que confirmes si deseas dividir el grupo o eliminar todo.

- Haz clic en **DESAGRUPAR** para eliminar el grupo manteniendo las preguntas en el formulario.
- Haz clic en **ELIMINAR TODO** para eliminar tanto el grupo como todas sus preguntas.

### Subgrupos

Un grupo de preguntas puede crearse o colocarse dentro de otro grupo. Esto se conoce como **subgrupos**. Los [grupos de repetición](#repetir-un-grupo-de-preguntas) también pueden anidarse.

---

## Configuración de grupos de preguntas

Después de crear un grupo de preguntas, puedes personalizar su comportamiento y apariencia. Por ejemplo, puedes mostrar todas las preguntas del grupo en la misma pantalla, aplicar lógica de omisión a todo el grupo o configurar el grupo para que se repita.

### Mostrar preguntas agrupadas en la misma pantalla

En KoboCollect, las preguntas aparecen de una en una de forma predeterminada. En los formularios web de Enketo, todas las preguntas aparecen en la misma pantalla.

Para mostrar preguntas por grupo en la misma pantalla durante la recolección de datos, haz clic en el ícono <i class="k-icon-settings"></i> **Configuración** a la derecha del nombre del grupo. Luego, en **Aspecto (avanzado)**, selecciona **field-list** (Mostrar todas las preguntas de este grupo en la misma pantalla).

<p class="note">
    <b>Nota:</b> Si planeas recolectar datos usando formularios web de Enketo, también necesitarás habilitar el tema <b>Múltiples páginas</b> en el menú <b>Estilo del formulario</b> (<b>Diseño y configuración</b>). Para más información sobre estilos de formularios web de Enketo, consulta <a href="../es/alternative_enketo.html">Diseñar formularios web usando el Formbuilder</a>.
</p>

### Omitir un grupo de preguntas
Para omitir un grupo de preguntas, asegúrate de tener al menos una pregunta de control posicionada antes de las preguntas agrupadas. Haz clic en el ícono <i class="k-icon-settings"></i> **Configuración** del grupo de preguntas, luego selecciona **Lógica de omisión** y configura las condiciones de lógica de omisión como lo harías para una pregunta individual.

<p class="note">
    Para obtener más información sobre cómo añadir condiciones de lógica de omisión, consulta <a href="../es/skip_logic.html">Añadir lógica de salto al Formbuilder</a>.
</p>

### Repetir un grupo de preguntas
Un grupo de repetición permite que un conjunto de preguntas se responda varias veces dentro de un formulario. Por ejemplo, en una encuesta de hogares, podrías usar un grupo de repetición para recolectar el nombre, edad, género y nivel educativo de cada miembro del hogar.

Para crear un grupo de preguntas:
1. Crea todas las preguntas que deseas incluir, luego agrúpalas.
2. En la <i class="k-icon-settings"></i> **Configuración** del grupo, activa la opción **Repetir este grupo si es necesario**.

![image](/images/group_repeat/repeating_groups.png)

Durante la recolección de datos, los/as encuestadores/as podrán ingresar respuestas para estas preguntas agrupadas tantas veces como sea necesario.

<p class="note">
    <b>Nota:</b> Añadir grupos de repetición a tu formulario crea una estructura de datos diferente en comparación con variables o grupos estándar. Cuando descargues tus datos en formato .xlsx, encontrarás una hoja separada para cada grupo de repetición. Para más información sobre la exportación y uso de datos de grupos de repetición, consulta <a href="../es/managing_repeat_groups.html">Gestión de datos de grupos repetidos</a>.
</p>

### Configuración avanzada para grupos de repetición
Configuraciones y funcionalidades adicionales para grupos de repetición están disponibles a través de XLSForm, pero no directamente dentro del Formbuilder. Estas incluyen establecer un número fijo o dinámico de repeticiones, y usar información de grupos de repetición en otras partes de tu formulario.

<p class="note">
    Para más información sobre configuraciones avanzadas para grupos de repetición, consulta <a href="../es/repeat_groups_xls.html">Grupos repetidos en XLSForm</a>.
</p>