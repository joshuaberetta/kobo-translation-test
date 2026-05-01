# Groupes et groupes répétés dans le Formbuilder

<iframe src="https://www.youtube.com/embed/nmPACLvYnUI?si=mkUi9RBLNHObj9ei" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Grouper des questions permet d'organiser les questions liées en sections, d'ajouter de la structure à votre formulaire et de faciliter la navigation. Par exemple, toutes les questions démographiques peuvent être regroupées dans une seule section du formulaire.

Les utilisateur(rice)s peuvent avoir besoin de grouper des questions pour diverses raisons :
-   **Structurer le questionnaire :** Les questions ayant des thèmes ou des attributs communs peuvent être regroupées dans une seule section.
-   **Afficher un ensemble de questions par page :** Les questions groupées peuvent être affichées sur des pages ou des écrans séparés lors de la collecte de données.
-   **Sauter un groupe de questions :** Une logique de saut peut être ajoutée à l'ensemble du groupe au lieu de l'ajouter à chaque question individuelle.
-   **Créer une série :** Les groupes de questions peuvent être répétés, par exemple pour des enquêtes auprès des ménages ou le suivi d'indicateurs.

Cet article explique comment créer et gérer des groupes de questions et des [groupes répétés](#répéter-un-groupe-de-questions) dans l'interface de création de formulaires KoboToolbox (KoboToolbox Formbuilder).

## Créer et gérer des groupes de questions

Le Formbuilder facilite le regroupement de questions, l'ajout de questions aux groupes, la suppression de questions des groupes et la réorganisation des questions au sein d'un groupe.

### Grouper un ensemble de questions

Pour créer un groupe de questions, suivez les étapes ci-dessous :

1. Rédigez un ensemble de questions que vous souhaitez regrouper.
2. Sélectionnez les questions en utilisant la touche **CTRL** (Windows) ou la touche **Command** (Mac).
3. Cliquez sur <i class="k-icon-group"></i> **Créer un groupe avec les questions sélectionnées** dans la barre de menu en haut à gauche.

![image](/images/group_repeat/grouping_questions.png)

Votre nouveau groupe apparaîtra dans un cadre ombré, le distinguant des questions standard. Vous pouvez également modifier le libellé du groupe, qui s'affichera en haut du groupe dans le formulaire.

<p class="note">
    <b>Remarque :</b> Vous pouvez également créer une seule question, sélectionner la question et cliquer sur <b>Créer un groupe</b>. Ensuite, vous pouvez ajouter d'autres questions dans le groupe, comme indiqué ci-dessous.
</p>

### Ajouter des questions dans un groupe

Placez votre souris n'importe où à l'intérieur du groupe où vous souhaitez ajouter une nouvelle question. Cliquez sur un <i class="k-icon-plus"></i> **signe** à l'intérieur du groupe pour ajouter une nouvelle question.

<p class="note">
    <b>Remarque :</b> Si vous cliquez sur le <i class="k-icon-plus"> </i><b>signe</b> situé à l'extérieur du groupe, vous ajouterez une question en dehors du groupe.
</p>

Vous pouvez également glisser-déposer n'importe quelle question existante dans un groupe de questions.

### Retirer des questions d'un groupe

Pour retirer une question d'un groupe tout en la conservant dans le formulaire, sélectionnez la question et faites-la glisser en dehors du groupe.

Pour supprimer définitivement une question du formulaire, cliquez sur <i class="k-icon-trash"></i> **Supprimer la question** dans le menu de la question à droite, puis cliquez sur **OK**.

### Réorganiser une question dans un groupe

Vous pouvez réorganiser les questions au sein d'un groupe en sélectionnant la question et en la faisant glisser vers la position souhaitée (vers le haut ou vers le bas).

### Supprimer un groupe de questions
Si vous n'avez plus besoin d'un groupe de questions, vous pouvez soit les dégrouper, soit supprimer l'ensemble du groupe. Pour ce faire, cliquez sur le bouton <i class="k-icon-trash"></i> **Supprimer** dans l'en-tête du groupe.

Une boîte de dialogue apparaîtra vous demandant de confirmer si vous souhaitez diviser le groupe ou tout supprimer.

- Cliquez sur **DÉGROUPER** pour supprimer le groupe tout en conservant les questions dans le formulaire.
- Cliquez sur **TOUT SUPPRIMER** pour supprimer à la fois le groupe et toutes ses questions.

### Sous-groupes

Un groupe de questions peut être créé ou placé à l'intérieur d'un autre groupe. C'est ce qu'on appelle des **sous-groupes**. Les [groupes répétés](#répéter-un-groupe-de-questions) peuvent également être imbriqués.

---

## Paramètres des groupes de questions

Après avoir créé un groupe de questions, vous pouvez personnaliser son comportement et son apparence. Par exemple, vous pouvez afficher toutes les questions du groupe sur le même écran, appliquer une logique de saut à l'ensemble du groupe ou configurer le groupe pour qu'il se répète.

### Afficher les questions groupées sur le même écran

Dans KoboCollect, les questions apparaissent une à la fois par défaut. Dans les formulaires web Enketo, toutes les questions apparaissent sur le même écran.

Pour afficher les questions par groupe sur le même écran lors de la collecte de données, cliquez sur l'icône <i class="k-icon-settings"></i> **Paramètres** à droite du nom du groupe. Ensuite, sous **Apparence (avancée)**, sélectionnez **field-list** (Afficher toutes les questions de ce groupe sur le même écran).

<p class="note">
    <b>Remarque :</b> Si vous prévoyez de collecter des données à l'aide de formulaires web Enketo, vous devrez également activer le thème <b>Pages multiples</b> dans le menu <b>Style du formulaire</b> (<b>Mise en page &amp; Paramètres</b>). Pour plus d'informations sur les styles de formulaires web Enketo, consultez l'article <a href="../fr/alternative_enketo.html">Styliser vos formulaires web dans le Formbuilder</a>.
</p>

### Sauter un groupe de questions
Pour sauter un groupe de questions, assurez-vous d'avoir au moins une question de contrôle positionnée avant les questions groupées. Cliquez sur l'icône <i class="k-icon-settings"></i> **Paramètres** pour la question groupée, puis sélectionnez **Branchement conditionnel** et configurez les conditions de logique de saut comme vous le feriez pour une question individuelle.

<p class="note">
    Pour en savoir plus sur l'ajout de conditions de logique de saut, consultez l'article <a href="../fr/skip_logic.html">Ajouter une logique de saut dans le Formbuilder</a>.
</p>

### Répéter un groupe de questions
Un groupe répété permet à un ensemble de questions de recevoir plusieurs réponses au sein d'un formulaire. Par exemple, dans une enquête auprès des ménages, vous pourriez utiliser un groupe répété pour collecter le nom, l'âge, le sexe et le niveau d'éducation de chaque membre du ménage.

Pour créer un groupe de questions :
1. Créez toutes les questions que vous souhaitez inclure, puis regroupez-les.
2. Dans les <i class="k-icon-settings"></i> **Paramètres** du groupe, activez l'option **Répéter ce groupe si nécessaire**.

![image](/images/group_repeat/repeating_groups.png)

Lors de la collecte de données, les enquêteur(rice)s pourront saisir des réponses pour ces questions groupées autant de fois que nécessaire.

<p class="note">
    <b>Remarque :</b> L'ajout de groupes répétés à votre formulaire crée une structure de données différente par rapport aux variables ou groupes standard. Lorsque vous téléchargez vos données au format .xlsx, vous trouverez un onglet séparé pour chaque groupe répété. Pour plus d'informations sur l'exportation et l'utilisation des données de groupes répétés, consultez l'article <a href="../fr/managing_repeat_groups.html">Gestion des données de groupes répétés</a>.
</p>

### Paramètres avancés pour les groupes répétés
Des paramètres et fonctionnalités supplémentaires pour les groupes répétés sont disponibles via XLSForm, mais pas directement dans le Formbuilder. Ceux-ci incluent la définition d'un nombre fixe ou dynamique de répétitions, et l'utilisation d'informations provenant de groupes répétés ailleurs dans votre formulaire.

<p class="note">
    Pour plus d'informations sur les paramètres avancés pour les groupes répétés, consultez l'article <a href="../fr/repeat_groups_xls.html">Groupes répétés dans XLSForm</a>.
</p>