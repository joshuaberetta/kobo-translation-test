# Bloquear cuestionarios para la biblioteca usando XLSForms

La [Biblioteca de KoboToolbox](https://support.kobotoolbox.org/es/question_library.html) te permite almacenar y gestionar plantillas, preguntas y bloques para reutilizarlos en múltiples proyectos. Las plantillas de formularios en la **Biblioteca** se pueden compartir con los/as miembros del equipo para garantizar un diseño de formulario consistente y reducir la duplicación de esfuerzos.

El **bloqueo de biblioteca** amplía esto al permitirte controlar cómo se pueden editar las plantillas una vez que se utilizan para crear nuevos proyectos. Con el bloqueo, puedes especificar qué preguntas, grupos o configuraciones a nivel de formulario se pueden cambiar. Esto es especialmente útil para equipos grandes que trabajan desde una plantilla compartida, donde ciertos elementos deben permanecer fijos mientras que otros pueden adaptarse a las necesidades locales.

Este artículo explica cómo funciona el bloqueo de biblioteca, los tipos de restricciones que puedes aplicar, cómo configurarlas en XLSForm y cómo cargar XLSForms bloqueados en KoboToolbox.

<p class="note">
<strong>Nota:</strong> El bloqueo de biblioteca no está disponible actualmente en el editor de formularios de KoboToolbox (Formbuilder). Para usar esta función, debes implementarla a través de XLSForm y luego cargar tu XLSForm en KoboToolbox. 
<br><br>
Para obtener más información sobre cómo descargar y editar tu formulario como XLSForm, consulta <a href="https://support.kobotoolbox.org/es/xlsform_with_kobotoolbox.html">Usar XLSForm con KoboToolbox</a>.    
</p>

## Introducción al bloqueo de biblioteca

El bloqueo de biblioteca controla cuánto de un formulario **se puede editar** cuando se crea un proyecto a partir de una plantilla de la Biblioteca. Las restricciones se definen en tu XLSForm antes de cargar el formulario.

Cuando creas una plantilla bloqueada y la compartes a través de tu Biblioteca:
- Los/as usuarios/as pueden hacer ajustes locales donde las restricciones lo permitan.
- Los elementos bloqueados aparecen **atenuados** en el Formbuilder.
- Un mensaje encima del formulario indica qué restricciones están activas.

El bloqueo de biblioteca es independiente de los [permisos del proyecto](https://support.kobotoolbox.org/es/managing_permissions.html), que controlan lo que diferentes usuarios/as pueden hacer dentro de un proyecto implementado.

<p class="note">
<strong>Nota:</strong> Las restricciones de bloqueo de biblioteca se aplican solo en el <strong>Formbuilder</strong> cuando se crea un proyecto a partir de una plantilla bloqueada. Si el XLSForm se descarga y se edita en una hoja de cálculo, las restricciones no impedirán los cambios. Sin embargo, las configuraciones de bloqueo incorrectas o no válidas pueden causar errores cuando el formulario se vuelve a cargar.
</p>

El bloqueo de biblioteca se configura en tres hojas de trabajo de XLSForm:
- **hoja survey:** Para aplicar restricciones a preguntas y grupos específicos.
- **hoja settings:** Para aplicar restricciones a nivel de formulario y establecer la opción `kobo--lock_all`.
- **hoja kobo--locking-profiles:** Para definir perfiles que agrupan restricciones relacionadas. 

Juntas, estas hojas de trabajo te permiten definir qué partes de un formulario permanecen fijas y qué partes se pueden editar cuando la plantilla se usa para crear nuevos proyectos.

## Tipos de restricciones

El bloqueo de biblioteca admite restricciones en tres niveles: **pregunta**, **grupo** y **formulario**. Las restricciones definen qué se puede y qué no se puede editar cuando se crea un proyecto a partir de una plantilla bloqueada.

Además, se puede usar una configuración global (`kobo--lock_all`) para bloquear todo el formulario.

### Restricciones a nivel de pregunta

Las restricciones a nivel de pregunta se aplican a preguntas individuales. Puedes aplicar las siguientes restricciones a las preguntas en tu XLSForm:
| Restricción              | Descripción                                                                      |
|:------------------------------|:---------------------------------------------------------------------------------------------------------------|
| <code>choice_add</code>                 | Impide agregar nuevas opciones a una pregunta de **selección**.                                                             |
| <code>choice_delete</code>              | Impide eliminar opciones existentes en una pregunta de **selección**.                                                      |
| <code>choice_value_edit</code>          | Impide editar el nombre de una opción (o valor XML).                                                                |
| <code>choice_label_edit</code>          | Impide editar la etiqueta de una opción.                                                                              |
| <code>choice_order_edit</code>          | Impide reordenar opciones en una pregunta de **selección**.                                                             |
| <code>question_delete</code>            | Impide eliminar una pregunta.                                                                                 |
| <code>question_label_edit</code>        | Impide editar la etiqueta o sugerencia de una pregunta.                                                                    |
| <code>question_settings_edit</code>     | Impide editar la configuración de la pregunta, incluido el nombre de la pregunta. Esto no incluye la lógica de omisión ni los criterios de validación. |
| <code>question_skip_logic_edit</code>   | Impide editar las condiciones de lógica de omisión.                                                                       |
| <code>question_validation_edit</code>   | Impide editar los criterios de validación.                         |

### Restricciones a nivel de grupo

Las restricciones a nivel de grupo se aplican a [grupos de preguntas](https://support.kobotoolbox.org/es/grouping_questions_xls.html). Puedes aplicar las siguientes restricciones a los grupos en tu XLSForm:

| Nombre | Descripción |
|:------|:-------------|
| <code>group_delete</code> | Impide eliminar un grupo. |
| <code>group_split</code> | Impide desagrupar preguntas. |
| <code>group_label_edit</code> | Impide editar la etiqueta del grupo. |
| <code>group_question_add</code> | Impide agregar o clonar preguntas dentro de un grupo. |
| <code>group_question_delete</code> | Impide eliminar preguntas de dentro de un grupo. |
| <code>group_question_order_edit</code> | Impide reordenar preguntas dentro de un grupo. |
| <code>group_settings_edit</code> | Impide editar la configuración del grupo, incluido el nombre del grupo. Esto no incluye la lógica de omisión. |
| <code>group_skip_logic_edit</code> | Impide editar la lógica de omisión de un grupo. |

### Restricciones a nivel de formulario

Las restricciones a nivel de formulario se aplican a todo el formulario. Puedes aplicar las siguientes restricciones a tu XLSForm:
| Nombre | Descripción |
|:------|:-------------|
| <code>form_appearance</code> | Impide cambios en el [tema](https://support.kobotoolbox.org/es/form_style_xls.html) del formulario. |
| <code>form_replace</code> | Impide reemplazar el formulario en KoboToolbox usando la opción <i class="k-icon k-icon-replace"></i> **Reemplazar formulario**. |
| <code>group_add</code> | Impide crear nuevos grupos. |
| <code>question_add</code> | Impide agregar o clonar preguntas en un grupo. |
| <code>question_order_edit</code> | Impide reordenar preguntas. |
| <code>language_edit</code> | Impide editar traducciones. |
| <code>form_meta_edit</code> | Impide editar preguntas de [metadatos](https://support.kobotoolbox.org/es/metadata_xls.html). |

### Bloquear un formulario completo

La configuración `kobo--lock_all` se puede agregar a la **hoja settings** de tu XLSForm.
- Si se configura como **TRUE**, todo el formulario se bloquea y todas las restricciones granulares se vuelven redundantes.
- Si se configura como **FALSE** (o se omite), solo se aplican las restricciones definidas en tus perfiles de bloqueo.

**hoja settings**

|   kobo--lock_all       |
|:----------------- |
|   TRUE  |

### Definir perfiles de bloqueo

Los perfiles de bloqueo son **conjuntos de restricciones** que se pueden aplicar a preguntas, grupos o todo el formulario. Se definen en la **hoja kobo--locking-profiles** del XLSForm, y luego se aplican en las hojas **survey** y **settings**. Puedes crear tantos perfiles como necesites.

Para definir perfiles de bloqueo en tu XLSForm:
1. Crea una nueva hoja de trabajo llamada **kobo--locking-profiles.**
2. Agrega una **columna restriction**, que puede incluir cualquier restricción de las tablas anteriores.
3. Crea una columna por **perfil** (por ejemplo, `profile_1`, `profile_2`). 
4. En la celda correspondiente a una **restricción** y un **perfil**, incluye la palabra clave `locked` para asignar una restricción a un perfil.

**hoja kobo--locking-profiles**

| restriction         | profile_1 | profile_2 | profile_3 |
|:-------------------|:----------|:----------|:----------|
| choice_add          | locked    | locked    |           |
| choice_delete       |           | locked    |           |
| choice_value_edit   | locked    | locked    |           |
| choice_label_edit   |           | locked    |           |
| choice_order_edit   |           | locked    |           |
| question_delete     | locked    | locked    |           |
| form_appearance     |           |           | locked    |

### Aplicar perfiles en la hoja survey

Una vez que hayas definido los perfiles de bloqueo en la **hoja kobo--locking-profiles**, puedes aplicar estos perfiles a preguntas y grupos específicos. Para aplicar perfiles en la **hoja survey**:

1. Crea una columna llamada **kobo--locking-profile** en la **hoja survey**
2. Para cada pregunta o grupo que desees restringir, define el perfil de bloqueo en la columna `kobo--locking-profile`.

**hoja survey**

| type                     | name    | label              | kobo--locking-profile |
|:-------------------------|:--------|:------------------|:--------------------|
| select_one country        | country | Selecciona tu país | profile_1           |
| select_one city           | city    | Selecciona tu ciudad   | profile_2           |

### Aplicar perfiles en la hoja settings

Además de aplicar perfiles a preguntas y grupos en la **hoja survey**, también puedes aplicar un perfil con restricciones a nivel de formulario en la **hoja settings**.

Para aplicar un perfil a la **hoja settings**:
1. Crea una columna **kobo--locking-profile** en la **hoja settings**.
2. Especifica el perfil que deseas aplicar.

**hoja settings**

| kobo--locking-profile |
|:---------------------|
| profile_3            |

<p class="note">
<strong>Nota:</strong> Las restricciones no se pueden aplicar en la <strong>hoja choices</strong>. Todas las restricciones relacionadas con opciones se definen a nivel de pregunta o grupo en la <strong>hoja survey</strong>.
</p>

## Usar plantillas bloqueadas en KoboToolbox

Una vez que hayas creado y cargado un XLSForm bloqueado como plantilla, puedes usarlo para crear nuevos proyectos en KoboToolbox.

### Importar un XLSForm bloqueado a tu Biblioteca

Para importar un XLSForm bloqueado a tu Biblioteca:
1. Ve a tu <i class="k-icon k-icon-library"></i> **Biblioteca** desde la barra de menú izquierda en KoboToolbox.
2. Haz clic en **NUEVO**, luego selecciona **Cargar**.
3. Carga tu archivo XLSForm y selecciona **Cargar como plantilla.**

![Cargar plantilla](images/library_locking/upload_template.png)

La plantilla aparecerá en tu Biblioteca con un <i class="k-icon k-icon-template-locked"></i> **símbolo de candado**, mostrando que contiene restricciones.

### Crear un proyecto a partir de una plantilla bloqueada

1. Ve a la página de inicio de **Proyectos**.
2. Haz clic en **NUEVO**, luego selecciona **Usar una plantilla.**
3. Elige la plantilla bloqueada que deseas usar.
4. Continúa creando tu proyecto como de costumbre.

![Usar plantilla](images/library_locking/use_template.png)

Cuando abras el proyecto en el Formbuilder:
- Aparecerá un mensaje encima de la primera pregunta resumiendo las restricciones.
- Las preguntas, grupos o configuraciones a nivel de formulario bloqueados aparecerán **atenuados.**
- Cada pregunta bloqueada muestra qué perfil se ha aplicado en su **Configuración > Funciones bloqueadas.**

![Biblioteca bloqueada](images/library_locking/locked.png)

## Solución de problemas

<details>
  <summary><strong>Recomendaciones para la solución de problemas</strong></summary>
  Si el bloqueo de biblioteca no funciona como se esperaba, intenta lo siguiente:
    <ul>
  <li>Asegúrate de que el formulario se cargó como una <strong>Plantilla en la Biblioteca.</strong></li>
  <li>Verifica la <strong>hoja settings</strong> en tu XLSForm. Si <code>kobo--lock_all</code> está configurado como <code>true</code>, todo el formulario estará bloqueado.</li>
  <li>Verifica que todos los nombres de restricción en la <strong>hoja kobo--locking-profiles</strong> sean válidos. Solo se admiten nombres de restricción predefinidos.</li>
  <li>Asegúrate de que la columna <code>kobo--locking-profile</code> exista en la <strong>hoja survey</strong> o <strong>settings</strong> y que los nombres de perfil coincidan con los definidos en la <strong>hoja kobo--locking-profiles</strong>.</li>
</ul>
</details>

<br>

<details>
  <summary><strong>Advertencias y limitaciones</strong></summary>
  <ul>
  <li>Las restricciones se aplican solo en el <strong>Formbuilder.</strong> Si el XLSForm se descarga y se edita directamente en una hoja de cálculo, las restricciones no impiden los cambios.</li>
  <li>Las restricciones se aplican solo a los proyectos creados a partir de plantillas bloqueadas. Las plantillas y encuestas en la Biblioteca siguen siendo editables.</li>
  <li>Solo las encuestas y plantillas admiten bloqueo. Si cargas un XLSForm bloqueado como pregunta o bloque, el bloqueo se ignora.</li>
  <li>Algunos editores de hojas de cálculo convierten automáticamente dos guiones simples <code>--</code> en un guión largo (—). Usa siempre dos guiones simples en nombres como <code>kobo--locking-profiles</code>.</li>
</ul>

</details>