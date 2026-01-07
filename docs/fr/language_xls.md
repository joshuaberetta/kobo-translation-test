# Ajouter des traductions dans un XLSForm

L'ajout de traductions à un formulaire permet aux utilisateurs de basculer vers leur langue préférée pendant la collecte de données sans créer de formulaires distincts. Un nombre illimité de traductions peut être ajouté. [KoboCollect](https://support.kobotoolbox.org/kobocollect_on_android_latest.html) et les [formulaires web Enketo](https://support.kobotoolbox.org/enketo.html) prennent en charge les traductions de formulaires.

La plupart des éléments affichés dans le formulaire peuvent être traduits, tels que les **libellés de questions**, les **indices**, les **libellés de choix**, les **messages de contrainte** et les **messages d'obligation**. Les éléments utilisés pour la structure du formulaire, comme les noms de questions, les noms de choix et les noms de listes, ne peuvent pas être traduits et doivent rester dans la langue utilisée pour le développement du formulaire et l'analyse des données.

Lorsque votre formulaire comprend plusieurs traductions, KoboCollect et Enketo afficheront un sélecteur de langue dans le **coin supérieur droit du formulaire**, permettant aux répondants de choisir leur langue préférée.

<p class="note">
  <strong>Remarque :</strong> L'ajout de traductions dans un XLSForm est plus rapide et plus efficace que <a href="https://support.kobotoolbox.org/language_dashboard.html">l'utilisation de l'interface de création de formulaires (Formbuilder)</a>, en particulier pour les formulaires plus longs. Pour savoir comment télécharger votre formulaire au format XLSForm afin d'ajouter des traductions, consultez <a href="xlsform_with_kobotoolbox.html">Utiliser un XLSForm avec KoboToolbox</a>.
<br><br>
Pour une pratique concrète de l'ajout de traductions dans un XLSForm, consultez le <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">cours XLSForm Fundamentals</a> de la KoboToolbox Academy.
</p>

## Codes de langue dans un XLSForm

Lorsque vous faites référence à différentes langues dans un XLSForm, vous devrez utiliser le format `langue (code)` dans vos en-têtes de colonnes. Par exemple, la référence linguistique pour l'anglais est `English (en)` et la référence linguistique pour le français est `French (fr)`. Chaque traduction doit utiliser le même nom de langue et le même code de manière cohérente dans tout votre formulaire.

Les codes de langue se trouvent dans le <a href="https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry">registre des sous-étiquettes de langue IANA</a>. Sur le site web de l'IANA, la **Description** fait référence au nom de la langue, et le **Subtag** fait référence au code de langue (par exemple, **Description:** French, **Subtag:** fr).

## Définir la langue par défaut du formulaire

Pour ajouter des traductions à un XLSForm, définissez d'abord la langue par défaut. Il s'agit de la langue dans laquelle le formulaire s'ouvrira par défaut.

Pour définir la langue par défaut de votre formulaire :
1. Dans la feuille de calcul `settings`, ajoutez une colonne **default_language**.
2. Dans la colonne `default_language`, saisissez la langue par défaut en utilisant le format **langue (code)**.
    - Par exemple : `English (en)`.

**Feuille de calcul settings**

| default_language |
| :---------------- |
| English (en)      |
| settings |

Pour configurer la feuille de calcul `survey` :

1. Renommez la colonne **label** en utilisant le format **label::langue (code)**.
    - Par exemple : `label::English (en)`.
2. Si votre formulaire comprend des colonnes `hint`, `required_message`, `constraint_message` ou `media` dans la feuille de calcul `survey`, renommez les colonnes existantes en utilisant le format **nom_colonne::langue (code)**.
    - Par exemple : `hint::English (en)`.

**Feuille de calcul survey**

| type | name | label::English (en) | hint::English (en) |
| :--- | :--- | :------------------ | :----------------- |
| integer | age | How old are you? | In years |
| select_one yn | student | Are you currently a student? | |
| survey |

Enfin, pour configurer la feuille de calcul `choices`, renommez la colonne **label** en utilisant le format **label::langue (code)**.

**Feuille de calcul choices**

| list_name | name | label::English (en) |
| :--------- | :--- | :------------------ |
| yn | yes | Yes |
| yn | no | No |
| choices |

## Ajouter des traductions

Une fois que vous avez défini votre langue par défaut, vous pouvez ajouter des traductions pour chaque élément visible de votre formulaire. Vous pouvez ajouter autant de colonnes de traduction que vous le souhaitez.

<p class="note">
  <strong>Remarque :</strong> Si vous omettez le texte d'un élément traduit, il apparaîtra comme un champ vide sur le formulaire.
</p>

Pour ajouter des traductions à la feuille de calcul `survey` :
1. Ajoutez une nouvelle colonne **label** pour chaque langue de traduction en utilisant le format **label::langue (code)**.
    - Par exemple : `label::Spanish (es)`.
2. Si votre formulaire comprend des colonnes `hint`, `required_message`, `constraint_message` ou `media` dans la feuille de calcul `survey`, configurez les colonnes de traduction correspondantes en utilisant le format **nom_colonne::langue (code)**.
    - Par exemple : `hint::French (fr)` ou `required_message::Chichewa (ny)`.
3. Saisissez les traductions de tous les éléments du formulaire dans les colonnes correspondantes.

<p class="note">
  Pour en savoir plus sur la gestion des fichiers multimédias dans les formulaires traduits, consultez <a href="https://support.kobotoolbox.org/media.html#adding-media-to-translations">Ajouter des médias aux traductions</a>.
</p>

**Feuille de calcul survey**

| type | name | label::English (en) | label::Chichewa (ny) | hint::English (en) | hint::Chichewa (ny) |
| :--- | :--- | :------------------ | :------------------- | :----------------- | :------------------ |
| integer | age | How old are you? | Muli ndi zaka zingati? | In years | M'zaka |
| select_one yn | student | Are you currently a student? | Kodi panopa ndinu wophunzira? | | |
| survey |

Pour ajouter des traductions à la feuille de calcul `choices` :
1. Ajoutez une nouvelle colonne **label** pour chaque langue de traduction en utilisant le format **label::langue (code)**.
    - Par exemple : `label::Spanish (es)`.
2. Saisissez la traduction de chaque libellé de choix dans la colonne de traduction correspondante.
3. Si votre feuille de calcul `choices` comprend des colonnes de médias, configurez les colonnes de traduction correspondantes en utilisant le format **nom_colonne::langue (code)**.

<p class="note">
  <strong>Remarque :</strong> Pour en savoir plus sur la gestion des fichiers multimédias dans les formulaires traduits, consultez <a href="https://support.kobotoolbox.org/media.html#adding-media-to-translations">Ajouter des médias aux traductions</a>.
</p>

**Feuille de calcul choices**

| list_name | name | label::English (en) | label::Chichewa (ny) |
| :--------- | :--- | :------------------ | :------------------- |
| yn | yes | Yes | Inde |
| yn | no | No | Ayi |
| choices |

## Directives pour les traductions

### Utiliser les fonctionnalités du tableur pour les traductions en masse

XLSForm facilite la traduction d'éléments de formulaire en masse, au lieu de saisir les traductions une par une. Par exemple, vous pouvez copier une colonne entière dans un système de traduction pour une traduction en masse, puis coller la colonne dans votre XLSForm. Si vous utilisez Google Sheets pour créer votre XLSForm, vous pouvez utiliser la formule `GOOGLETRANSLATE()` pour automatiser le processus de traduction.

Les traductions automatiques doivent toujours être examinées et validées par un locuteur courant pour garantir l'exactitude, la pertinence culturelle et le contexte approprié. Cette étape permet de maintenir la qualité et la fiabilité de votre contenu traduit.

### Traduire vers des écritures non latines

Les écritures non latines telles que l'arabe, le cyrillique, le tamoul, le népalais ou l'hindi sont entièrement prises en charge dans KoboToolbox et peuvent être utilisées pour les langues par défaut ou les traductions.

<p class="note">
  <strong>Remarque :</strong> Il est recommandé d'utiliser uniquement des caractères latins pour les <strong>noms</strong> de questions et de choix, car les écritures non latines peuvent provoquer des erreurs ou des problèmes de compatibilité lors de l'exportation de données ou du travail avec un XLSForm, mais les <strong>libellés</strong> de questions et de choix peuvent utiliser en toute sécurité n'importe quelle écriture.
</p>

Lors de l'ajout de traductions dans des écritures non latines, il est essentiel d'**utiliser des caractères Unicode appropriés**. Unicode garantit que le texte est correctement affiché et compris sur tous les appareils et plateformes.

Pour saisir du texte Unicode, vous n'avez pas besoin d'installer de polices spéciales. Au lieu de cela, configurez le clavier de votre système sur la langue ou l'écriture appropriée et tapez comme vous le feriez normalement. Évitez d'utiliser des pseudo-polices (c'est-à-dire des polices spéciales qui imitent visuellement des écritures non latines en réaffectant des caractères latins), car elles ne sont pas compatibles avec KoboToolbox et peuvent causer de graves problèmes d'affichage et d'intégrité des données. Si vous utilisez Windows et avez besoin d'aide pour configurer le clavier de votre système, consultez la [documentation Microsoft](https://support.microsoft.com/en-us/windows/manage-the-language-and-keyboard-input-layout-settings-in-windows-12a10cb4-8626-9b77-0ccb-5013e0c7c7a2).

## Traduire des écritures de droite à gauche

Lors de l'ajout d'une langue qui utilise une écriture de droite à gauche (RTL), comme l'arabe, l'hébreu ou l'ourdou, il est important d'**utiliser le code de langue correct** et de s'assurer que le **premier texte visible dans la traduction** (par exemple, un libellé de question, un indice ou une note) est écrit dans la langue RTL. Cela garantira que la mise en page du formulaire ne revient pas par défaut au formatage de gauche à droite (LTR).

De plus, lors de l'incorporation de références de questions dans les libellés de questions utilisant des écritures RTL, veuillez noter que la syntaxe de référence de question est inversée (c'est-à-dire `{nom_question}$`).

**Feuille de calcul survey**

| type | name | label::English (en) | label::Arabic (ar) |
| :--- | :--- | :------------------ | :----------------- |
| begin\_group | profile | Respondent profile | ملف المستجيب |
| text | name | Respondent's name | اسم المدعى عليه |
| integer | age | How old is ${name}? | ؟{name}$ كم عمرك |
| end\_group | | | |
| survey |