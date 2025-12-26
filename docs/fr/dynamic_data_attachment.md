# Pièces jointes de données dynamiques

Le lien dynamique vous permet d'utiliser les données d'un **projet principal** dans des **projets secondaires**, simplifiant ainsi la gestion de la collecte de données longitudinales. Cet article explique comment lier dynamiquement des données entre des projets KoboToolbox.

<p class="note">
    <strong>Remarque :</strong> Les pièces jointes de données dynamiques fonctionnent de manière similaire à la fonction <a href="https://support.kobotoolbox.org/pull_data_kobotoolbox.html"><code>pulldata()</code></a> mais éliminent le besoin de fichiers CSV séparés, puisque les données d'un projet principal lié servent de source de données.
</p>

Vous pouvez récupérer diverses **réponses (hors fichiers média)** d'un projet principal et effectuer des calculs sur ces données liées dans un projet secondaire. Cela peut être utile pour récupérer des données de référence, des informations de contact ou des dossiers médicaux dans des études de cohorte, ou pour confirmer ou vérifier des données collectées précédemment.

Nous recommandons d'utiliser [XLSForm](https://support.kobotoolbox.org/edit_forms_excel.html) pour configurer les pièces jointes de données dynamiques. Pour des exemples de projets principaux et secondaires, téléchargez des fichiers exemples [ici](https://support.kobotoolbox.org/_static/files/dynamic_data_attachment/parent.xlsx) et [ici](https://support.kobotoolbox.org/_static/files/dynamic_data_attachment/child.xlsx).

## Lier dynamiquement des projets dans XLSForm

Lier dynamiquement des projets nécessite un **projet principal** et au moins un **projet secondaire**. Le **projet principal** ne nécessite aucune modification par rapport à un XLSForm normal. Cependant, la configuration du ou des **projets secondaires** implique les étapes suivantes :
1. Dans la feuille de calcul `survey` de votre XLSForm, ajoutez une ligne et définissez le type de question sur `xml-external`.
2. Dans la colonne `name`, fournissez un nom court pour le formulaire principal. Ce nom peut être composé de caractères de l'alphabet latin, de traits de soulignement et de chiffres.

**feuille de calcul survey**

| type | name     | label              |
| :--- | :------- | :----------------- |
| xml-external | parent |
| survey | 


3. Tout au long du formulaire, vous pouvez récupérer des valeurs du projet principal en créant une nouvelle question et en incluant l'expression appropriée dans la colonne `calculation` (voir le tableau [ci-dessous](https://support.kobotoolbox.org/dynamic_data_attachment.html#calculation-syntax-for-dynamic-data-attachments)). Vous pouvez utiliser les types de questions suivants pour récupérer des données :
    - Utilisez un type de question **calculate** pour récupérer et stocker des valeurs pour une utilisation future dans le formulaire ou l'ensemble de données (par exemple, pour des calculs ou des libellés de questions dynamiques).
    - Utilisez les types de questions **text**, **integer**, **decimal**, **select_one** ou **select_multiple** pour inclure les valeurs récupérées comme réponses par défaut dans des champs modifiables. Les données modifiées dans le projet secondaire ne modifieront pas les données d'origine dans le projet principal.
  
**feuille de calcul survey**
      
| type | name     | label              | calculation |
| :--- | :------- | :----------------- | :----------------- |
| xml-external | parent |               |              |
| text | participant_id | Quel est l'identifiant du participant ? |  |
| integer | age | Confirmez l'âge du participant | instance('parent')/root/data[enrollment_id = current()/../participant_id]/age |
| survey | 

<p class="note">
   <strong>Remarque :</strong> 
    Pour afficher des données liées sans permettre aux utilisateurs de modifier le champ, utilisez une question <strong>calculate</strong> suivie d'une question <strong>note</strong> qui affiche la valeur calculée. Alternativement, utilisez des questions <strong>text</strong>, <strong>integer</strong>, <strong>decimal</strong>, <strong>select_one</strong> ou <strong>select_multiple</strong> avec la colonne <code>read_only</code> définie sur <code>TRUE</code>.
</p>

## Syntaxe de calcul pour les pièces jointes de données dynamiques

Dans la colonne `calculation` de la ligne où les données liées seront récupérées, incluez l'une des expressions du tableau ci-dessous. Ces expressions sont appelées **XPaths**.

Pour chaque expression dans le tableau ci-dessous :

- `parent` est le nom unique attribué au **formulaire principal** (par exemple, dans la question `xml-external` du **formulaire secondaire**).
- `parent_question` fait référence au `name` d'une question du **formulaire principal**.
- `child_question` fait référence au `name` d'une question du **formulaire secondaire**.
- `parent_index_question` est la question d'identification du **formulaire principal** qui le relie au **formulaire secondaire** (par exemple, identifiant unique, nom d'organisation).
- `child_index_question` est la question d'identification du **formulaire secondaire** qui le relie au **formulaire principal** (par exemple, identifiant unique, nom d'organisation).
- `parent_group` fait référence au `name` du groupe dans le **formulaire principal** dans lequel se trouve la `parent_question`.
- `parent_index_group` fait référence au `name` du groupe dans le **formulaire principal** dans lequel se trouve la `parent_index_question`.

| **XPath**    | **Description**                                |
| :----------------- | :--------------------------------------------- |
| `count(instance('parent')/root/data)` | Renvoie le nombre total de lignes dans le projet principal. |
| `count(instance('parent')/root/ data[parent_group/parent_question])`      | Renvoie le nombre total de lignes dans le projet principal où `parent_question` (dans `parent_group`) n'est pas vide. |
| `count(instance('parent')/root/ data[parent_group/parent_question= current()/../child_question]` | Renvoie le nombre total d'instances où la valeur de `parent_question` (dans `parent_group`) dans le projet principal est égale à la valeur de `child_question` dans le projet secondaire. |
| `instance('parent')/root/ data[parent_index_group/parent_index_question= current()/../child_index_question]/parent_group/ parent_question` | Renvoie la valeur de `parent_question` (dans `parent_group`) du projet principal où `child_index_question` dans le projet secondaire est égale à `parent_index_question` dans le projet principal. |
| `instance('parent')/root/ data[parent_index_group/parent_index_question= current()/../child_index_question][position()= 1]/parent_group/parent_question` | Identique à ce qui précède, mais spécifie que seules les données de la première instance de `parent_index_question` doivent être renvoyées, en utilisant l'argument `[position() = 1]`. Utilisé en cas de doublons possibles dans le formulaire principal. |
| `sum(instance('parent')/root/ data/parent_group/parent_question)` | Renvoie la somme des valeurs de `parent_question` (dans `parent_group`) du projet principal. Notez que `parent_question` doit être numérique. |
| `max(instance('parent')/root/ data/parent_group/parent_question)`         | Renvoie la valeur maximale saisie dans `parent_question` (dans `parent_group`) du projet principal. Notez que `parent_question` doit être numérique.     |
| `min(instance('parent')/root/ data/parent_group/parent_question)`      | Renvoie la valeur minimale saisie dans `parent_question` (dans `parent_group`) du projet principal. Notez que `parent_question` doit être numérique.     |   


<p class="note">
    <strong>Remarque :</strong> Si la question principale n'est incluse dans aucun groupe, omettez <code>parent_group</code> de l'expression.
</p>

## Configuration des projets pour le lien dynamique

Une fois vos XLSForms configurés, connectez-vous à votre compte KoboToolbox et suivez ces étapes :

1. Envoyez et déployez le **projet principal**, s'il n'est pas déjà déployé. Assurez-vous que le projet principal a au moins une soumission.
2. Activez le partage de données pour le projet principal : 
    - Dans l'onglet **PARAMÈTRES > Connecter des projets** du projet principal, activez le bouton **Partage de données** (désactivé par défaut) et cliquez sur **RECONNAÎTRE ET CONTINUER** dans la fenêtre de confirmation. 
    - Toutes les données sont partagées par défaut, mais vous pouvez restreindre des variables spécifiques à partager avec les projets secondaires en cliquant sur « Sélectionner des questions spécifiques à partager ».

<p class="note">
    <strong>Remarque :</strong> Si les projets ont des propriétaires différents, le propriétaire du projet principal doit <a href="https://support.kobotoolbox.org/managing_permissions.html">partager le projet</a> avec le propriétaire du projet secondaire. Les autorisations minimales requises pour que les pièces jointes de données dynamiques fonctionnent sont <strong>Voir le formulaire</strong> et <strong>Voir les soumissions</strong>. Notez que cela permet aux administrateurs du projet secondaire de voir toutes les données du projet principal.
</p>

3. Envoyez et déployez le **projet secondaire**.
4. Connectez le projet secondaire au projet principal : 
    - Dans l'onglet **PARAMÈTRES > Connecter des projets** du projet secondaire, cliquez sur « Sélectionner un projet différent pour importer des données ». Un menu déroulant vous permettra de sélectionner un projet principal à lier. 
    - Renommez le projet principal lié avec le nom de question `xml-external` défini dans le XLSForm et cliquez sur **IMPORTER**. 
    - Vous pouvez ensuite sélectionner des questions spécifiques du projet principal à partager avec le projet secondaire, ou sélectionner toutes les questions.
5. Si vous ajoutez de nouveaux champs au formulaire principal et souhaitez les utiliser dans le projet secondaire, réimportez le projet principal dans les paramètres du projet secondaire.

<p class="note">
    <strong>Remarque :</strong> Les formulaires ne peuvent être liés ensemble que s'ils se trouvent sur le même serveur KoboToolbox.
</p>

<iframe src="https://www.youtube.com/embed/pBqEsFlxqE4?si=6BPiDgOzO4LPO7zv&cc_lang_pref=fr&hl=fr" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


## Lier dynamiquement un formulaire à lui-même

Il est possible qu'un projet principal et un projet secondaire soient le même projet. Les étapes sont les mêmes que celles décrites ci-dessus. Voici des exemples de cas d'utilisation : 

- **Suivi quotidien** : Si un formulaire est utilisé pour enquêter sur la même personne au fil du temps, vous pouvez le lier à lui-même pour compter les soumissions précédentes. Cela peut permettre d'afficher un message (par exemple, « le suivi est terminé ») après un certain nombre d'entrées ou d'informer l'enquêteur du nombre de formulaires soumis, comme indiqué dans l'exemple ci-dessous.

**feuille de calcul survey**

| type | name     | label              | calculation |
| :--- | :------- | :----------------- | :----------------- |
| xml-external | monitoring |               |              |
| text | participant_id | Quel est l'identifiant du participant ? |  |
| calculate | count |  | count(instance('monitoring')/root/ data[monitoring/participant_id = current()/../participant_id]) |
| note | monitoring_note | Ce participant a été enquêté ${count} fois. | |
| survey | 

- **Formulaire d'inscription** : En liant un formulaire d'inscription à lui-même, vous pouvez vérifier si un utilisateur a déjà été inscrit. Cela peut permettre de générer un message d'erreur ou d'ajouter une contrainte s'il est déjà inscrit, empêchant ainsi les inscriptions en double, comme indiqué dans l'exemple ci-dessous.

**feuille de calcul survey**

| type | name     | label              | calculation | relevant | 
| :--- | :------- | :----------------- | :----------------- | :------------ |
| xml-external | registration |               |              | |
| text | customer_id | Quel est le numéro d'identification du client ? |  | | 
| calculate | count |  | count(instance('registration')/root/ data[registration/customer_id = current()/../customer_id]) | |
| note | already_registered | Ce client est déjà inscrit. Veuillez fermer ce formulaire. | | ${count} > 0 |
| survey | 

## Collecte et gestion de données avec le lien dynamique

Les données pour les projets liés dynamiquement peuvent être collectées à l'aide de [l'application Android KoboCollect](https://support.kobotoolbox.org/kobocollect_on_android_latest.html) ou des [formulaires web Enketo](https://support.kobotoolbox.org/data_through_webforms.html).

Lors de la collecte de données, notez ce qui suit :

- Le projet principal doit avoir au moins une soumission pour que le projet secondaire fonctionne correctement.
- Lors de la collecte de données en ligne, il y a un délai de cinq minutes pour la synchronisation des nouvelles données du projet principal avec le projet secondaire.
- En mode hors ligne, téléchargez fréquemment le projet secondaire pour assurer la synchronisation des données avec le projet principal.

<p class="note">
    <strong>Remarque :</strong> Vous pouvez <a href="https://support.kobotoolbox.org/kobocollect_settings.html#form-management-settings">configurer l'application Android KoboCollect</a> pour mettre à jour automatiquement les données du projet principal lorsqu'une connexion Internet est disponible. Allez dans <strong>Paramètres > Gestion de formulaires > Mode de mise à jour des formulaires vierges</strong> et sélectionnez soit <strong>Formulaires téléchargés précédemment uniquement</strong> soit <strong>Correspondance exacte avec le serveur</strong>. Vous pouvez définir la fréquence de téléchargement automatique toutes les 15 minutes, toutes les heures, toutes les six heures ou toutes les 24 heures. Notez que l'activation de ce paramètre peut augmenter la consommation de la batterie.
</p>

## Dépannage

<details>
<summary><strong>Erreur ou plantage lors de la liaison des formulaires</strong></summary>
Les pièces jointes de données dynamiques ne peuvent pas se connecter à un projet principal vide. Ajoutez d'abord au moins une soumission au projet principal, puis reliez à nouveau les formulaires.
</details>

<br>

<details>
<summary><strong>Les données du projet principal ne s'affichent pas dans le formulaire secondaire</strong></summary>
Vérifiez que la syntaxe de calcul dans le formulaire secondaire est correcte et que les questions pertinentes sont partagées dans les deux projets. Si votre question principale se trouve dans un groupe de questions, assurez-vous d'inclure le nom du groupe dans l'expression XPath. Notez que les nouvelles données du projet principal prennent jusqu'à cinq minutes pour se synchroniser lorsque vous êtes en ligne. Si vous ajoutez de nouveaux champs au formulaire principal et souhaitez les utiliser dans le projet secondaire, ouvrez les paramètres du projet secondaire, réimportez le projet principal et redéployez.
</details>

<br>

<details>
<summary><strong>Le formulaire secondaire se charge lentement</strong></summary>
Les grandes pièces jointes de données dynamiques peuvent ralentir le chargement du formulaire. Partagez uniquement les questions dont le formulaire secondaire a besoin au lieu de la liste complète des questions, puis redéployez et réessayez.
</details>

<br>

<details>
<summary><strong>Les données dynamiques ne se rafraîchissent pas dans KoboCollect</strong></summary>
Si vous utilisez KoboCollect et collectez des données hors ligne, les données doivent d'abord être soumises au projet principal, puis téléchargées sur votre appareil de collecte de données pour que la pièce jointe de données dynamiques fonctionne. Les deux étapes nécessitent une connexion Internet. Le téléchargement des données du projet principal est similaire au téléchargement d'une nouvelle version d'un formulaire, et l'application KoboCollect peut être configurée pour <a href="https://support.kobotoolbox.org/kobocollect_settings.html#form-management-settings">télécharger automatiquement de nouvelles données</a> à une fréquence définie. Il n'est pas recommandé de s'appuyer sur les pièces jointes de données dynamiques pour les données collectées hors ligne dans un court laps de temps.
</details>

<br>

<details>
<summary><strong>La pièce jointe de données dynamiques ne fonctionne pas à l'intérieur des groupes de questions</strong></summary>
Pour extraire des données dynamiques d'un formulaire principal vers un formulaire secondaire avec des groupes de questions, assurez-vous que la question d'index (par exemple, le numéro d'identification) dans le formulaire secondaire se trouve dans le même groupe que le calcul pour les données dynamiques. Consultez les fichiers exemples <a href="https://community.kobotoolbox.org/uploads/short-url/z5RpC1M3wj9716z9qQ8pWx9Pb4V.xlsx">Round 1 (Within Groups).xlsx</a> et <a href="https://community.kobotoolbox.org/uploads/short-url/8JZvWJcrCxzKBllQYglRyAVyk03.xlsx">Round 2 (Within Groups).xlsx</a> pour un exemple de pièces jointes de données dynamiques au sein de groupes.
</details>

<br>

<details>
<summary><strong>Erreur d'évaluation des champs dans KoboCollect</strong></summary>
Si votre formulaire principal contient des soumissions en double, vous pouvez recevoir un message d'erreur dans KoboCollect indiquant « Erreur d'évaluation du champ / évaluation XPath : incompatibilité de type / Ce champ est répété. » Pour résoudre ce problème et extraire des données uniquement de la première soumission contenant une valeur d'index spécifique, utilisez l'argument <code>[position()=1]</code>, comme ci-dessous :
<br><br>
<code>instance('parent')/root/data[parent_index_group/parent_index_question = current()/../child_index_question][position()=1]/parent_group/parent_question</code>

</details>