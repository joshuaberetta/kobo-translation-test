# Ajouter des filtres de choix dans XLSForm

Les filtres de choix créent des formulaires dynamiques où les options d'une question dépendent de la réponse à une question précédente. Cela rationalise la collecte de données en ne présentant que les choix pertinents, améliorant ainsi l'efficacité et la précision de l'enquête.

Les filtres de choix peuvent être utilisés pour diverses applications, notamment :
- **Listes hiérarchiques**, telles que les continents et les pays, où la liste des pays dépend du continent sélectionné (également connues sous le nom de **sélections en cascade**).
- **Supprimer une ou plusieurs options d'une liste** si elles ne sont pas pertinentes pour un répondant en fonction de ses réponses précédentes.
- **Réutiliser une liste d'options** dans XLSForm pour plusieurs questions, où la liste varie légèrement d'une question à l'autre.
- Réutiliser une liste d'options d'une question précédente, en incluant **uniquement les options qui ont été sélectionnées par le répondant.**

Cet article explique comment ajouter des filtres de choix dans XLSForm et inclut des exemples pour différents cas d'usage. Les filtres de choix sont définis dans la colonne `choice_filter` de la feuille `survey`, et opérationnalisés dans la feuille `choices`.

<p class="note">
<strong>Remarque :</strong> Cet article se concentre sur l'ajout de filtres de choix dans <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">XLSForm</a>. Pour en savoir plus sur l'ajout de questions de sélection en cascade dans l'interface de création de formulaires KoboToolbox (KoboToolbox Formbuilder), consultez <a href="https://support.kobotoolbox.org/cascading_select.html">Ajouter des questions de sélection en cascade dans l'interface de création de formulaires</a>.
<br><br>
Pour une pratique concrète des filtres de choix dans XLSForm, consultez le <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">Cours sur les fondamentaux XLSForm</a> de KoboToolbox Academy.
</p>

## Ajouter des filtres de choix statiques

Les **filtres de choix statiques** appliquent les mêmes conditions de filtrage pour tous les répondants. Lors de l'utilisation de filtres de choix statiques, une liste d'options est filtrée, mais elle ne varie pas en fonction des réponses précédentes. Cela peut être utile lorsque vous souhaitez réutiliser une liste d'options dans plusieurs questions de votre formulaire avec des variations mineures, sans dupliquer la liste de choix plusieurs fois dans votre feuille `choices`.

Pour ajouter des filtres de choix statiques dans XLSForm :
1. Ajoutez une question `select_one` ou `select_multiple` à votre XLSForm et [définissez vos options de choix](https://support.kobotoolbox.org/option_choices_xls.html) dans la feuille `choices`.
2. Dans la feuille `choices`, ajoutez une colonne de filtre.
    - Vous pouvez nommer cette colonne comme vous le souhaitez (par exemple, `q2`).
3. Dans la colonne de filtre, écrivez n'importe quelle valeur (par exemple, `yes`) à côté du ou des choix que vous souhaitez inclure dans la liste de choix pour votre question.
    - Cette valeur servira de filtre. Il peut s'agir de n'importe quel mot ou nombre.
4. Dans la feuille `survey`, ajoutez une colonne **choice_filter**. Cette colonne contiendra l'**expression de filtre de choix** utilisée pour filtrer les options de choix.
    - L'expression de filtre de choix dans sa forme la plus basique prendra le format : **filtre = 'valeur'.**
    - Par exemple, `q2 = 'yes'` conservera tous les choix avec **yes** dans la colonne `q2`.

### Exemple

Dans l'exemple ci-dessous, la même liste de choix (`activities`) est utilisée pour deux questions différentes. Pour la deuxième question, la liste est filtrée pour n'afficher que les activités de plein air.

**feuille survey**

| type             | name               | label                                                   | choice_filter   |
|:-----------------|:------------------|:--------------------------------------------------------|:----------------|
| select_one activities | activities        | Quelles activités aimez-vous faire pendant votre temps libre ?  |                 |
| select_one activities | outdoors_activities | Lesquelles de ces activités de plein air sont disponibles dans votre ville ? | <strong>filter = 'outdoors'</strong> |
| survey | 

**feuille choices**

| list_name  | name       | label                 | filter   |
|:-----------|:-----------|:--------------------|:---------|
| activities | reading    | Lecture              |          |
| activities | swimming   | Natation             | outdoors |
| activities | running    | Course à pied              | outdoors |
| activities | television | Regarder la télévision  |          |
| activities | hiking     | Randonnée               | outdoors |
| choices | 

## Ajouter des filtres de choix dynamiques

Les filtres de choix peuvent également être utilisés pour filtrer une liste de choix en fonction d'une réponse précédente. Dans ce cas, vous aurez une **question principale** avec une **liste principale** de choix correspondante, et une **question secondaire** avec une **liste secondaire** de choix correspondante. La liste de choix pour la question secondaire est filtrée en fonction de la réponse à la question principale.

<p class="note">
Pour un exemple d'XLSForm utilisant des filtres de choix dynamiques, consultez ce <a href="https://docs.google.com/spreadsheets/d/10gpBV6YaYGx1i367hyW-w1Ms9tkUQnCx0V8YsdwYxmk/edit?gid=0#gid=0">formulaire exemple</a>.
</p>

Pour ajouter des filtres de choix dynamiques dans XLSForm :
1. Ajoutez la **question principale** et la **question secondaire** à votre XLSForm et [définissez leurs options de choix](https://support.kobotoolbox.org/option_choices_xls.html) dans la feuille `choices`.
    - Il doit s'agir de questions `select_one` ou `select_multiple`.
2. Dans la feuille `choices`, ajoutez une colonne de filtre.
    - Il peut être utile de nommer cette colonne de la même manière que la **question principale.**
3. Dans la colonne de filtre, entrez le **nom du choix** de la liste principale auquel chaque option de la liste secondaire correspond.
4. Dans la feuille `survey`, ajoutez une colonne **choice_filter**. Cette colonne contiendra l'**expression de filtre de choix** utilisée pour filtrer les options de choix.
    - Si la question principale est `select_one`, l'expression de filtre de choix sera `filter_column = ${question_name}`, où `question_name` fait référence à la question principale.
    - Si la question principale est `select_multiple`, l'expression de filtre de choix sera `selected(${question_name}, filter_column)`.

Lorsqu'un répondant sélectionne une option dans la question principale, la liste de choix pour la question secondaire sera filtrée pour n'inclure que les choix correspondants.

### Exemple

Dans l'exemple ci-dessous, `continent` est la **question principale** et `country` est la **question secondaire.** La liste de choix pour la question `country` sera filtrée en fonction de la réponse à la question `continent`.

**feuille survey**

| type              | name      | label     | choice_filter        |
|:------------------|:---------|:----------|:--------------------|
| select_one continent | continent | Continent |                     |
| select_one country   | country   | Pays   | **continent = ${continent}** |
| survey | 

**feuille choices**

| list_name  | name     | label   | continent |
|:-----------|:---------|:--------|:----------|
| continent  | africa   | Afrique  |           |
| continent  | asia     | Asie     |           |
| country    | malawi   | Malawi  | africa    |
| country    | zambia   | Zambie  | africa    |
| country    | india    | Inde   | asia      |
| country    | pakistan | Pakistan| asia      |
| choices |

## Filtres de choix avancés dans XLSForm

Vous pouvez créer des filtres de choix plus avancés en utilisant des opérateurs logiques, des opérateurs mathématiques, des fonctions et des regex dans vos expressions de filtre de choix. Cela permet un filtrage hautement personnalisé et précis des options, adaptant le formulaire aux exigences spécifiques de collecte de données et aux caractéristiques des répondants.

<p class="note">
<strong>Remarque :</strong> Dans les expressions de filtre de choix avancées, la colonne <code>name</code> de la feuille <code>choices</code> peut être utilisée comme colonne de filtre.
</p>

Exemples d'expressions de filtre de choix avancées dans XLSForm :
| Filtre de choix | Description |
|:---------------|:------------|
| `selected(${parent_question}, name)` | Afficher uniquement les réponses qui ont été sélectionnées dans une `parent_question` précédente. |
| `filter = 'outdoors' and include = 'yes'` | Combiner des expressions de filtre de choix afin que les deux conditions doivent s'appliquer pour que le choix soit affiché. |
| `name != 'none'` | Exclure l'option <strong>Aucun</strong> d'une liste de choix. |
| `selected(${Q1}, name) or name='none'` | Inclure les choix sélectionnés dans une question précédente ainsi qu'une option <strong>Aucun</strong> (même si elle n'a pas été sélectionnée précédemment). |
| `filter=${Q1} or name='other'` | Inclure les choix basés sur une question précédente ainsi qu'une option <strong>Autre</strong>. |
| `filter=${Q1} or always_include='yes'` | Inclure les choix basés sur une question précédente ainsi qu'un ensemble d'options qui doivent toujours être incluses. |
| `filter <= ${product_count}` | Utiliser des nombres dans la colonne de filtre au lieu de texte, et filtrer en fonction d'un nombre provenant d'une question ou d'un calcul précédent. |
| `if(${relationship_status} = 'married', filter = 'married', filter = 'unmarried')` | Utiliser des instructions if pour afficher conditionnellement des choix en fonction du profil du répondant. |

<p class="note">
  Pour en savoir plus sur la construction d'expressions de logique de formulaire dans XLSForm, consultez <a href="https://support.kobotoolbox.org/form_logic_xls.html">Introduction à la logique de formulaire dans XLSForm</a>.
</p>

### Exemple
Dans l'exemple ci-dessous, la liste de choix sous-jacente pour `Q1` et `Q2` est la même, mais seules les options sélectionnées dans `Q1` seront affichées aux répondants lors de la réponse à `Q2`.

**feuille survey**

| type               | name | label                                              | choice_filter            |
|:------------------|:-----|:--------------------------------------------------|:-------------------------|
| select_multiple item | Q1  | Quels articles ménagers possédez-vous actuellement ?      |                          |
| select_multiple item | Q2  | Lesquels de ces articles envisageriez-vous de remplacer à l'avenir ? | selected(${Q1}, name) |
| survey |

**feuille choices**

| list_name | name      | label            |
|:----------|:----------|:----------------|
| item      | fridge    | Réfrigérateur    |
| item      | tv        | Télévision      |
| item      | fan       | Ventilateur de plafond     |
| item      | microwave | Four à micro-ondes  |
| item      | radio     | Radio           |
| item      | bike      | Bicyclette         |
| item      | phone     | Téléphone portable    |
| item      | laptop    | Ordinateur portable |
| choices | 

Dans le formulaire résultant, `Q2` n'affichera que les options choisies dans `Q1`, comme illustré ci-dessous.

![Filtres de choix](images/choice_filters_xls/choice_filters.png)

## Dépannage

<details>
  <summary><strong>Le formulaire ralentit ou plante avec de très longues listes</strong></summary>
  Les grandes listes de choix qui incluent des milliers de lignes peuvent fonctionner en aperçu mais échouer lors du déploiement. Cela se produit parce que l'aperçu du navigateur peut gérer de grandes listes, contrairement à l'application mobile ou à l'analyseur XLS. Pour résoudre ce problème, déplacez les grandes listes vers un fichier CSV externe et utilisez des <a href="https://support.kobotoolbox.org/select_from_file_xls.html">questions select_from_file</a> avec des filtres de choix. Cette approche est recommandée pour les listes comportant plus de 3 000 options.
</details>

<br>

<details>
  <summary><strong>Noms d'options en double dans une liste</strong></summary>
  Si votre liste de choix inclut des noms d'options en double (par exemple, si le même nom de quartier est présent dans différentes villes), <a href="https://support.kobotoolbox.org/form_settings_xls.html">activez les doublons de choix</a> dans la feuille <code>settings</code> en définissant <code>allow_choice_duplicates</code> sur <code>yes</code>.
</details>