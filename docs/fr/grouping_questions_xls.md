# Regrouper des questions dans XLSForm

Le regroupement de questions dans XLSForm permet d'organiser le contenu connexe en sections claires et structurées, améliorant ainsi la mise en page et la navigation du formulaire. Par exemple, vous pouvez regrouper toutes les questions démographiques dans une seule section.

XLSForm facilite la création de groupes et de [groupes imbriqués](https://support.kobotoolbox.org/grouping_questions_xls.html#nested-groups), et l'application de [branchement conditionnel](https://support.kobotoolbox.org/grouping_questions_xls.html#applying-skip-logic-to-question-groups) à des groupes entiers de questions. Le branchement conditionnel au niveau du groupe simplifie l'expérience du répondant en n'affichant que les sections pertinentes en fonction des réponses précédentes.

Cet article couvre les sujets suivants :

- Créer des groupes de questions et des groupes imbriqués dans XLSForm
- Afficher toutes les questions regroupées sur une seule page
- Ajouter un branchement conditionnel aux groupes de questions

<p class="note">
<strong>Remarque :</strong> Cet article se concentre sur le regroupement de questions dans <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">XLSForm</a>. Pour en savoir plus sur le regroupement de questions dans l'interface de création de formulaires KoboToolbox (KoboToolbox Formbuilder), consultez <a href="https://support.kobotoolbox.org/group_repeat.html">Regrouper des questions et répéter des groupes</a>.
</p>

## Créer un groupe de questions

Pour créer un groupe de questions dans XLSForm :

1.  Dans la colonne `type` de la feuille `survey`, saisissez **begin_group** pour indiquer le début du groupe.
2.  Dans la colonne `name` de la ligne **begin_group**, saisissez l'identifiant unique du groupe.
3.  Dans la colonne `label`, saisissez le titre du groupe tel que vous souhaitez qu'il apparaisse dans le formulaire. Le libellé est facultatif et peut être laissé vide.
4.  Saisissez chaque question du groupe dans sa propre ligne, comme vous le feriez normalement.
5.  Dans une nouvelle ligne après les questions regroupées, saisissez **end_group** dans la colonne `type` pour indiquer la fin du groupe.
    - Dans la ligne **end_group**, laissez les colonnes `name` et `label` vides.

**Feuille survey**

| type | name | label |
| :--- | :--- | :--- |
| **begin_group** | personal_info | Section A : Informations personnelles |
| text | name | Quel est votre nom ? |
| integer | age | Quel âge avez-vous ? |
| select_one yn | married | Êtes-vous marié(e) ? |
| **end_group** | | |
| survey |

### Groupes imbriqués

Les groupes imbriqués sont des groupes de questions à l'intérieur d'un autre groupe de questions. Les groupes imbriqués peuvent être utilisés pour créer une structure hiérarchique au sein de votre XLSForm. Par exemple, vous pouvez inclure un groupe de questions sur un enfant à l'intérieur d'un groupe plus large de questions sur le ménage.

Lors de la création de plusieurs groupes, assurez-vous que chaque ligne `begin_group` a une ligne `end_group` correspondante. Si le nombre de lignes `begin_group` ne correspond pas au nombre de lignes `end_group`, le formulaire générera une erreur, l'empêchant de fonctionner correctement lors de l'aperçu ou du déploiement.

**Feuille survey**

| type | name | label |
| :--- | :--- | :--- |
| **begin_group** | personal_info | Section A : Informations personnelles |
| text | name | Quel est votre nom ? |
| integer | age | Quel âge avez-vous ? |
| select_one yn | married | Êtes-vous marié(e) ? |
| **begin_group** | education | Éducation |
| select_one yn | student | Êtes-vous actuellement étudiant(e) ? |
| select_one edu | education_level | Quel est le niveau d'études le plus élevé que vous avez terminé ? |
| **end_group** | | |
| **end_group** | | |
| survey |

### Groupes répétés

Dans XLSForm, les groupes de questions peuvent être répétés pour collecter le même ensemble de réponses plusieurs fois au sein d'un formulaire. Cela est utile lors de la collecte d'informations similaires sur plusieurs personnes, éléments ou événements. Les groupes répétés sont appelés **groupes répétés**.

<p class="note">
  Pour en savoir plus sur la configuration de groupes répétés de questions dans XLSForm, consultez <a href="https://support.kobotoolbox.org/repeat_groups_xls.html">Groupes répétés dans XLSForm</a>.
</p>

## Paramètres d'apparence pour les groupes de questions

Une raison courante de regrouper des questions est de les afficher ensemble sur une seule page. Vous pouvez ajuster les paramètres d'apparence du groupe pour contrôler la façon dont les questions regroupées sont affichées lors de la collecte de données. Les étapes varient selon que vous utilisez [KoboCollect](https://support.kobotoolbox.org/kobocollect_on_android_latest.html) ou [Enketo](https://support.kobotoolbox.org/enketo.html).

<p class="note">
<strong>Remarque :</strong> Les paramètres d'apparence pour afficher les groupes sur une seule page fonctionnent à la fois pour les groupes de questions et les <a href="https://support.kobotoolbox.org/repeat_groups_xls.html">groupes répétés</a>.
</p>

### Utiliser KoboCollect pour collecter des données

Par défaut, KoboCollect affiche chaque question sur un écran séparé. Les utilisatrices et utilisateurs doivent passer manuellement d'une question à l'autre.

Pour **afficher toutes les questions regroupées sur le même écran** dans KoboCollect :
1.  Dans la feuille `survey`, ajoutez une colonne **appearance**.
2.  Dans la colonne `appearance`, saisissez **field-list** dans la ligne `begin_group`.
    * Chaque groupe de questions apparaîtra maintenant sur sa propre page.

**Feuille survey**

| type | name | label | appearance |
| :--- | :--- | :--- | :--- |
| begin_group | personal_info | Section A : Informations personnelles | **field-list** |
| text | name | Quel est votre nom ? | |
| integer | age | Quel âge avez-vous ? | |
| select_one yn | married | Êtes-vous marié(e) ? | |
| end_group | | | |
| survey |

### Utiliser les formulaires web Enketo pour collecter des données

Par défaut, les formulaires web Enketo affichent toutes les questions sur une seule page.

Pour afficher chaque groupe de questions sur sa propre page dans les formulaires web Enketo :
1.  Dans la feuille `settings`, ajoutez une colonne **style**.
2.  Dans la deuxième cellule de la colonne `style`, saisissez **pages**.
    * Cela applique le [thème](https://support.kobotoolbox.org/form_style_xls.html) **pages** à votre formulaire web Enketo, le divisant en pages séparées similaires à KoboCollect.

**Feuille settings**

| style |
| :--- |
| pages |
| settings |

3.  Dans la feuille `survey`, ajoutez une colonne **appearance**.
4.  Dans la colonne `appearance`, saisissez **field-list** dans la ligne `begin_group`.
    * Chaque groupe de questions apparaîtra maintenant sur sa propre page.

**Feuille survey**

| type | name | label | appearance |
| :--- | :--- | :--- | :--- |
| begin_group | personal_info | Section A : Informations personnelles | **field-list** |
| text | name | Quel est votre nom ? | |
| integer | age | Quel âge avez-vous ? | |
| select_one yn | married | Êtes-vous marié(e) ? | |
| end_group | | | |
| survey |


## Appliquer un branchement conditionnel aux groupes de questions

L'application d'un branchement conditionnel aux groupes de questions garantit que seules les sections pertinentes apparaissent en fonction des réponses antérieures. Par exemple, dans une enquête sur les ménages, vous pouvez utiliser un branchement conditionnel pour afficher un groupe de questions pour le chef de ménage uniquement lorsqu'une question précédente identifie le répondant comme tel. Cela rend le formulaire plus facile à naviguer et plus réactif aux entrées de l'utilisateur ou de l'utilisatrice.

Pour [appliquer un branchement conditionnel](https://support.kobotoolbox.org/skip_logic_xls.html) aux groupes de questions dans XLSForm, utilisez la même approche que pour les questions individuelles :
1.  Ajoutez une colonne **relevant** à votre feuille `survey`.
2.  Dans la colonne `relevant` pour la ligne `begin_group`, saisissez la condition qui détermine quand le groupe doit être affiché.
3.  Si la condition est remplie, le groupe entier sera affiché. Sinon, le groupe sera masqué.

Cela permet de contrôler le flux de votre formulaire afin que seules les sections pertinentes apparaissent en fonction des réponses antérieures, rendant le formulaire plus rationalisé et réactif aux entrées de l'utilisateur ou de l'utilisatrice.

<p class="note">
<strong>Remarque :</strong> Le branchement conditionnel peut être appliqué à la fois aux groupes de questions et aux <a href="https://support.kobotoolbox.org/repeat_groups_xls.html">groupes répétés</a>. Pour en savoir plus sur le branchement conditionnel dans XLSForm, consultez <a href="https://support.kobotoolbox.org/skip_logic_xls.html">Ajouter un branchement conditionnel dans XLSForm</a>.
</p>