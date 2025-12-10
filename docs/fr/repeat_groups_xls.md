# Groupes répétés dans XLSForm

Les groupes répétés dans XLSForm vous permettent de poser le même ensemble de questions plusieurs fois au sein d'un formulaire. Cela est particulièrement utile lors de la collecte d'informations similaires sur plusieurs personnes, objets ou événements.

Par exemple, si vous recueillez des détails sur chaque membre d'un ménage, vous pouvez utiliser un groupe répété pour poser les mêmes questions démographiques pour chaque individu.

Cet article couvre les sujets suivants :
- Créer un groupe répété
- Définir le nombre de répétitions pour limiter le nombre de répétitions
- Compter le nombre de répétitions au sein d'un groupe répété
- Récupérer des valeurs à partir de groupes répétés

<p class="note"> 
<strong>Remarque :</strong> Cet article se concentre sur les groupes répétés dans <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">XLSForm</a>. Pour en savoir plus sur les groupes répétés dans l'interface de création de formulaires KoboToolbox (KoboToolbox Formbuilder) et pour prévisualiser les groupes répétés en action, consultez <a href="https://support.kobotoolbox.org/group_repeat.html">Regrouper des questions et répéter des groupes</a>.
</p>

## Créer un groupe répété

Pour créer un groupe répété dans XLSForm :

1. Dans la colonne `type` de la feuille survey, saisissez **begin_repeat** pour indiquer le début du groupe répété.
2. Dans la colonne `name` de la ligne **begin_repeat**, saisissez l'identifiant unique du groupe.
3. Dans la colonne `label`, saisissez le titre du groupe tel que vous souhaitez qu'il apparaisse dans le formulaire. Le libellé est facultatif et peut être laissé vide.
4. Saisissez chaque question du groupe dans sa propre ligne, comme vous le feriez normalement.
5. Dans une nouvelle ligne après les questions répétées, saisissez **end_repeat** dans la colonne `type` pour indiquer la fin du groupe répété.
    - Dans la ligne **end_repeat**, laissez les colonnes `name` et `label` vides.

**feuille survey**

| type | name | label |
| :--- | :--- | :--- |
| **begin_repeat** | household_members | Membres du ménage |
| text | name | Quel est le nom de la personne ? |
| integer | age | Quel âge a-t-elle ? |
| select_one yn | married | Est-elle mariée ? |
| **end_repeat** | | |
| survey |

Les groupes répétés fonctionnent de manière similaire aux groupes de questions. Avec les groupes répétés, vous pouvez :

- Utiliser l'apparence **field-list** pour [afficher toutes les questions](https://support.kobotoolbox.org/grouping_questions_xls.html#appearance-settings-for-question-groups) sur la même page.
- Ajouter une [logique de saut](https://support.kobotoolbox.org/grouping_questions_xls.html#applying-skip-logic-to-question-groups) aux groupes répétés dans la colonne **relevance**.
- Créer des groupes répétés **imbriqués**, où un groupe répété est ajouté [à l'intérieur d'un autre](https://support.kobotoolbox.org/grouping_questions_xls.html#nested-groups).

<p class="note">
  <strong>Remarque :</strong> L'ajout de groupes répétés à votre formulaire crée une structure de données différente par rapport aux variables ou groupes standard. Lorsque vous téléchargez vos données au format .xlsx, vous trouverez une feuille distincte pour chaque groupe répété. Pour plus d'informations sur l'exportation et l'utilisation des données de groupes répétés, consultez <a href="https://support.kobotoolbox.org/managing_repeat_groups.html">Gérer les données de groupes répétés</a>.
</p>

## Définir le nombre de répétitions

Par défaut, les groupes répétés peuvent être répétés autant de fois que nécessaire. Pour limiter le nombre de fois qu'un groupe répété est répété dans le formulaire, vous pouvez définir un nombre de répétitions. Le **nombre de répétitions** peut être soit un nombre fixe, soit déterminé dynamiquement en fonction d'une réponse précédente.

Pour définir un nombre fixe de répétitions :

1. Ajoutez une colonne **repeat_count** dans la feuille `survey`.
2. Saisissez un nombre dans la colonne **repeat_count**.

**feuille survey**

| type | name | label | repeat_count |
| :--- | :--- | :--- | :--- |
| begin_repeat | participant_profile | Profil du participant | 3 |
| text | name | Nom | |
| select_one gender | gender | Genre | |
| integer | age | Âge | |
| end_repeat | | | |
| survey |

Pour déterminer dynamiquement le nombre de répétitions en fonction d'une réponse précédente :

1. Ajoutez une colonne **repeat_count** dans la feuille `survey`.
2. Saisissez la référence de la question dans la colonne **repeat_count**.
    - La question référencée doit être de type `integer`.

**feuille survey**

| type | name | label | repeat_count |
| :--- | :--- | :--- | :--- |
| integer | participants | Nombre total de participants à la formation | |
| begin_repeat | participant_profile | Profil du participant | ${participants} |
| text | name | Nom | |
| select_one gender | gender | Genre | |
| integer | age | Âge | |
| end_repeat | | | |
| survey |

<p class="note">
  <strong>Remarque :</strong> Dans la colonne <strong>repeat_count</strong>, vous pouvez également inclure des instructions conditionnelles avancées pour déterminer si les répétitions se poursuivront. Pour plus d'informations, consultez la <a href="https://docs.getodk.org/form-logic/#repeating-as-long-as-a-condition-is-met">documentation ODK</a>.
</p>

## Compter le nombre de répétitions à l'intérieur d'un groupe répété

Lorsque vous utilisez des groupes répétés, vous pouvez avoir besoin d'un champ qui compte combien de fois le groupe a été répété. Cela peut être utile pour des calculs ou la logique du formulaire. Par exemple, vous pouvez appliquer une logique de saut après une répétition spécifique ou inclure dynamiquement le numéro de répétition dans le libellé d'une question (par exemple, Enfant 1, Enfant 2).

Pour compter combien de fois un groupe répété a été répété :
1. Ajoutez une question **calculate** à l'intérieur du groupe répété.
2. Saisissez `position(..)` dans la colonne **calculation**.

Cette variable stocke l'index de répétition actuel. Vous pouvez l'utiliser dans la logique du formulaire ou pour créer des libellés de questions dynamiques.

**feuille survey**

| type | name | label | calculation | relevance |
| :--- | :--- | :--- | :--- | :--- |
| begin_repeat | profile | Profil du participant | | |
| calculate | number | | **position(..)** | |
| note | instructions | Répondez aux questions ci-dessous pour chaque participant(e). | | **${number} = 1** |
| text | name | Nom du participant **${number}** | | |
| select_one gender | gender | Genre du participant **${number}** | | |
| integer | age | Âge du participant **${number}** | | |
| end_repeat | | | | |
| survey |

## Compter le nombre total de répétitions d'un groupe répété

Vous pouvez également ajouter une question distincte en dehors du groupe répété pour compter le nombre total de répétitions. Cela est utile, par exemple, pour confirmer le nombre de participants ou d'enfants répertoriés dans le groupe répété.

Pour compter combien de fois un groupe répété a été rempli :
1. Ajoutez une question **calculate** après le groupe répété.
2. Dans la colonne **calculation**, saisissez `count(${repeat_group_name})`, où `repeat_group_name` est le nom du groupe répété.

Cette variable stocke le nombre total de répétitions du groupe. Vous pouvez l'utiliser dans des calculs ou pour créer des libellés de questions dynamiques dans votre formulaire.

**feuille survey**

| type | name | label | calculation |
| :--- | :--- | :--- | :--- |
| begin_repeat | children | Liste des enfants | |
| text | name | Nom | |
| select_one gender | gender | Genre | |
| integer | age | Âge | |
| end_repeat | | | |
| calculate | count_children | | **count(${children})** |
| acknowledge | confirm_children | Confirmez qu'il y a **${count_children}** enfants dans le ménage. | |
| survey |

## Récupérer des valeurs à partir de groupes répétés

Les formulaires avancés utilisent souvent le [référencement de questions](https://support.kobotoolbox.org/form_logic_xls.html#question-referencing) pour inclure des réponses de questions précédentes dans les libellés de questions, les calculs ou la logique de saut. Vous pouvez également utiliser le référencement de questions **au sein de groupes répétés** ou pour faire référence à des données répétées ailleurs dans votre formulaire.

Au sein d'un groupe répété, vous pouvez référencer une réponse d'une autre question dans la même répétition en utilisant le référencement de questions, comme indiqué ci-dessous.

**feuille survey**

| type | name | label |
| :--- | :--- | :--- |
| begin_repeat | children | Liste des enfants |
| text | name | Quel est le nom de l'enfant ? |
| integer | age | Quel âge a ${name} ? |
| select_one gender | married | Quel est le genre de ${name} ? |
| end_repeat | | |
| survey |

En dehors d'un groupe répété, vous pouvez récupérer des données du groupe répété pour les utiliser dans la logique du formulaire ou les libellés de questions :

1. Ajoutez une question **calculate** après votre groupe répété.
2. Incluez l'une des formules listées ci-dessous dans la colonne **calculation**.
3. La question **calculate** stocke la valeur récupérée, que vous pouvez ensuite utiliser dans la logique du formulaire ou les libellés de questions.

**Formules pour récupérer des données à partir de groupes répétés**

| Formule | Description |
| :--- | :--- |
| `max(${question-name})` | Récupère la valeur maximale saisie pour une question dans le groupe répété. |
| `min(${question-name})` | Récupère la valeur minimale saisie pour une question dans le groupe répété. |
| `sum(${question-name})` | Calcule la somme des valeurs numériques saisies pour une question dans le groupe répété. |
| `join('; ', ${question-name})` | Liste toutes les réponses à une question donnée à l'intérieur d'un groupe répété, séparées par un point-virgule. |
| `indexed-repeat(${question-name}, ${repeat-name}, n)` | Récupère la valeur de `${question-name}`, dans le groupe répété appelé `${repeat-name}`, dans la n<sup>ième</sup> répétition. |

**feuille survey**

| type | name | label | calculation |
| :--- | :--- | :--- | :--- |
| begin_repeat | children | Liste des enfants | |
| text | name | Nom | |
| select_one gender | gender | Genre | |
| integer | age | Âge | |
| end_repeat | | | |
| calculate | max_age | | **max(${age})** |
| acknowledge | confirm_age | Confirmez que l'enfant le plus âgé du ménage a **${max_age}** ans. | |
| survey |