# Añadir otro idioma a tu XLSForm

Existen dos métodos para añadir múltiples idiomas a tu formulario. Puedes añadirlos y gestionarlos directamente a través del [Panel de Proyectos](language_dashboard.md) en línea o puedes añadirlos en un XLSForm y cargarlo a Kobo.

Aquí encontrarás instrucciones detalladas sobre cómo puedes añadir otro idioma a tu formulario:

-   Crea tu formulario en el idioma predeterminado. Este debe ser el idioma con el que la persona responsable de diseñar el cuestionario se sienta más cómoda. Cuando hayas terminado, o cuando se haya creado una parte del formulario, guárdalo. Regresarás al panel de proyectos del formulario Borrador.

-   Exporta el formulario a XLS.

-   Abre el archivo en Excel (Google Spreadsheet, Open Office Calc, etc., todos funcionarán) (Si estás en Excel, es posible que primero tengas que sacar el archivo de la Vista Protegida. [Ver aquí](https://support.office.com/en-us/article/what-is-protected-view-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653?ocmsassetID=HA010355931&CorrelationId=04b441d5-5c7c-441a-bbac-8f34b3071869&ui=en-US&rs=en-US&ad=US).) Tu hoja de cálculo tendrá tres hojas (mira las pequeñas pestañas en la parte inferior): **survey**, **choices**, **settings**. Permanece en la hoja **survey** por ahora.

-   Encuentra la columna llamada `label`. Aquí es donde se almacenan las etiquetas de tus preguntas originales. Inserta otra columna a la derecha de label. En el encabezado (primera fila) de esta nueva columna, escribe `label::idioma (código)`, por ejemplo `label::Français (fr)` o `label::English (en)`.

<p class="note">Puedes cambiar el tamaño de tus columnas, añadir colores o cambiar el tamaño de la fuente, nada de esto afectará tu formulario.</p>

-   Luego, si tienes sugerencias en tu formulario, lo mismo debe aplicarse a la columna `hint`, por ejemplo `hint::Français (fr)` o `hint::English (en)`.

**Hoja survey**

| type             | name           | label                          | relevant                  |
| :--------------- | :------------- | :----------------------------- | :------------------------ |
| text             | full_name      | What is your name?             |                           |
| select_one yesno | children_yesno | Do you have any children?      |                           |
| integer          | children_count | How many children do you have? | ${children_yesno} = 'yes' |
| survey |

-   Ahora añade tus traducciones para cada fila dentro de la columna `label::idioma (código)`. Cuando hayas terminado, asegúrate de no haber omitido ninguna pregunta (para cada campo que tenga texto dentro de la columna label debe haber texto dentro de la columna `label::idioma (código)`). Puedes encontrar los códigos oficiales de idioma de 2 caracteres (subetiquetas) [aquí](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry).

<p class="note">Consejo: Copia y pega la columna label original y luego realiza cambios a las traducciones para no dejar nada en blanco por accidente: Es mejor tener algo que se muestre en el idioma incorrecto que tener una pregunta en blanco en algún idioma. <em>Puedes repetir este paso y añadir tantos idiomas como desees, cada uno en sus columnas separadas y con un nombre diferente dentro de <code>label::idioma (código)</code>.</em></p>

**Hoja survey**

| type             | name           | label:English (en)             | label::Français (fr)           | relevant                  |
| :--------------- | :------------- | :----------------------------- | :----------------------------- | :------------------------ |
| text             | full_name      | What is your name?             | Quel est votre nom?            |                           |
| select_one yesno | children_yesno | Do you have any children?      | Avez-vous des enfants?         |                           |
| integer          | children_count | How many children do you have? | Combien des enfants avez-vous? | ${children_yesno} = 'yes' |
| survey |

-   Ahora cambia a la hoja **choices** de tu archivo, si tienes una.

-   En la hoja **choices** tienes otra columna llamada `label`. Repite los pasos 5 y 6. Asegúrate de usar exactamente la misma ortografía para `label::idioma (código)`. Por ejemplo, `label::Francais (fr)` y `label::Français (fr)` no son idénticos.

**Hoja choices**

| list_name | name | label::English (en) | label::Français (fr) |
| :-------- | :--- | :------------------ | :------------------- |
| yesno     | yes  | Yes                 | Oui                  |
| yesno     | no   | No                  | Non                  |
| choices |

-   En la hoja **settings**, debajo de `form_title` edita el texto del título de tu formulario a algo como "Mi formulario (inglés y francés)" para que puedas identificarlo fácilmente más tarde.

**Hoja settings**

| form_title                   |
| :--------------------------- |
| My form (English and French) |
| settings |

-   Guarda tu archivo y cierra Excel.

-   Regresa a KoboToolbox y click en **Reemplazar con XLS**, luego carga tu XLSForm actualizado. Elige el archivo que acabas de terminar de editar y click en **OK**.

-   Abre el formulario que acabas de cargar y click en **Vista previa del formulario**. En la parte superior, junto a **Elegir idioma**, click en el menú desplegable. Tendrá un predeterminado (tu idioma original) así como los nuevos idiomas que acabas de añadir.

## Traducir a escrituras tamil, nepalí, hindi, etc.

Al traducir a escrituras no latinas, como tamil, nepalí, hindi, etc., asegúrate de no usar una fuente pseudo. Al escribir en estos idiomas, asegúrate de usar únicamente los caracteres Unicode adecuados. Para escribir caracteres Unicode adecuados no tienes que instalar ninguna fuente en particular. En su lugar, tú (o tu traductor/a) necesitan configurar tu teclado para usar la escritura respectiva (tamil, nepalí, etc.) y luego escribir normalmente. La configuración correcta del teclado producirá las letras reales de la escritura en Unicode en lugar de algunos equivalentes fonéticos latinos. (Esta también sería la misma forma de escribir estos idiomas en un correo electrónico, KoboToolbox o cualquier otra aplicación web.

Para obtener ayuda sobre cómo añadir el teclado del sistema correcto, [consulta este enlace](https://support.microsoft.com/en-us/help/17424/windows-change-keyboard-layout) (solo Windows).

Las fuentes pseudo permiten escribir en estas escrituras y se usan comúnmente en muchos países, particularmente en el sur de Asia. Pero aunque funcionan en la computadora que tiene instalada una fuente específica, no funcionarán en ninguna otra computadora que no use esa fuente en particular. Esto se debe a que estas fuentes simplemente disfrazan caracteres y símbolos latinos regulares y los hacen aparecer en una forma diferente. Por ejemplo, al escribir "Hello" con la fuente pseudo nepalí 'Preeti', se verá así: हेल्लो. Pero lo que realmente está escrito allí siguen siendo las letras H e l l o. Para algunas personas que usan estas fuentes, que a menudo usan equivalentes fonéticos al inglés, puede ser más fácil. Otra razón por la que se usan ampliamente es que muchas computadoras solían no tener soporte para estas escrituras y, por lo tanto, necesitaban fuentes pseudo como un "truco". De cualquier manera, los caracteres Unicode son la mejor opción, y la única forma para usar en KoboToolbox.

## Traducir escrituras de derecha a izquierda

Al añadir un idioma que usa escritura de derecha a izquierda, es importante usar el código de idioma correcto, sin embargo, incluso si se usa el código correcto, si la primera pregunta, sugerencia o nota está escrita en una escritura de izquierda a derecha, el formulario formateará automáticamente el resto de la traducción a un formato de izquierda a derecha.