# Apparences de questions dans XLSForm

Les apparences de questions vous permettent de personnaliser la façon dont les questions sont affichées dans le formulaire et le type de réponses qu'elles collectent. Cet article explique comment ajouter des apparences de questions dans XLSForm et répertorie les apparences courantes par type de question.

Il est important de noter que certaines apparences ne fonctionnent que dans les [formulaires web Enketo](https://support.kobotoolbox.org/enketo.html), tandis que d'autres ne sont prises en charge que dans [KoboCollect](https://support.kobotoolbox.org/kobocollect_on_android_latest.html). Tenez compte de votre méthode de collecte de données lors de la sélection des apparences.

<p class="note">
  <b>Remarque :</b> Cet article se concentre sur la définition des apparences de questions dans <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">XLSForm</a>. Pour en savoir plus sur la définition des apparences dans l'interface de création de formulaires KoboToolbox (KoboToolbox Formbuilder), consultez la documentation <a href="https://support.kobotoolbox.org/using-formbuilder.html">Utiliser l'interface de création de formulaires</a>.
<br><br>
Pour une pratique concrète des apparences de questions dans XLSForm, consultez le <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">cours Fondamentaux XLSForm</a> de KoboToolbox Academy.
</p>

## Ajouter des apparences de questions

Pour ajouter des apparences de questions dans XLSForm :
1. Dans la feuille `survey`, ajoutez une colonne **appearance**.
2. Saisissez le nom de l'apparence dans la colonne `appearance`. Assurez-vous d'utiliser l'orthographe et la ponctuation exactes du nom de l'apparence.
3. Certaines apparences peuvent être combinées et appliquées à la même question. Combinez les apparences en les saisissant dans la même cellule et en les séparant par un espace.

**Feuille survey**

| type | name | label | appearance |
| :--- | :--- | :--- | :--- |
| text | description | Décrivez le projet. | multiline |
| select_one country_list | country | Dans quel pays ce projet se déroule-t-il ? | autocomplete minimal |
| survey |


## Apparences de questions disponibles dans XLSForm
Les tableaux ci-dessous répertorient les apparences de questions courantes par type de question et indiquent lesquelles sont prises en charge dans les formulaires web Enketo et KoboCollect.

### Types de questions de sélection
Les questions de sélection permettent aux répondant(e)s de [choisir parmi des options prédéfinies](https://support.kobotoolbox.org/question_types_xls.html#select-question-types).

| Apparence | Description | Compatibilité |
| :--- | :--- | :--- |
| `minimal` | Affiche les choix dans un menu déroulant. | Enketo et KoboCollect |
| `compact` | Affiche les choix côte à côte avec un espacement minimal et sans cases de choix. | Enketo et KoboCollect |
| `label` | Affiche les libellés de choix sans les cases de choix. | Enketo et KoboCollect |
| `list-nolabel` | Affiche les cases de choix de réponse sans les libellés. | Enketo et KoboCollect |
| `autocomplete` | Ajoute une barre de recherche en haut de la liste d'options. | Enketo et KoboCollect (à combiner avec l'apparence minimal) |
| `horizontal` | Affiche les choix de réponse horizontalement en colonnes. | Enketo uniquement |
| `horizontal-compact` | Affiche les choix de réponse horizontalement, avec un espacement minimal et sans cases de choix. | Enketo uniquement |
| `likert` | Affiche les choix de réponse sous forme d'échelle de Likert (`select_one` uniquement). | Enketo et KoboCollect  |
| `quick` | Fait avancer automatiquement le formulaire à la question suivante après la sélection d'une réponse (`select_one` uniquement). | KoboCollect uniquement |
| `quickcompact` | Affiche les choix côte à côte avec un espacement minimal et sans cases de choix, et fait avancer automatiquement à la question suivante après la sélection d'une réponse (`select_one` uniquement). | KoboCollect uniquement |
| `columns` | Affiche les choix disponibles en 2, 3, 4 ou 5 colonnes selon la taille de l'écran. | Enketo et KoboCollect |
| `columns-pack` | Affiche les choix disponibles avec autant que possible sur une seule ligne. | Enketo et KoboCollect |
| `columns-n` | Affiche les choix disponibles dans le nombre spécifié (n) de colonnes. | Enketo et KoboCollect |
| `map` | Affiche une carte pour sélectionner des options. Nécessite de <a href="https://support.kobotoolbox.org/select_from_map_xls.html">définir des coordonnées GPS</a> dans la feuille `choices` (`select_one` uniquement). | KoboCollect uniquement |
| `quick map` | Affiche une carte pour sélectionner des options, en enregistrant automatiquement le premier emplacement sélectionné sans afficher d'informations supplémentaires. Nécessite de <a href="https://support.kobotoolbox.org/select_from_map_xls.html">définir des coordonnées GPS</a> dans la feuille `choices` (`select_one` uniquement). | KoboCollect uniquement |

<p class="note">
  <b>Remarque :</b> Les apparences pour les questions <code>select_one</code> et <code>select_multiple</code> peuvent également être utilisées pour les questions <a href="https://support.kobotoolbox.org/select_from_file_xls.html">de sélection à partir d'un fichier</a>.
</p>

### Types de questions entier et décimale
Les questions numériques sont utilisées pour [collecter des nombres entiers ou des nombres décimaux](https://support.kobotoolbox.org/question_types_xls.html#numeric-question-types).

| Apparence | Description | Compatibilité |
| :--- | :--- | :--- |
| `thousands-sep` | Formate les grands nombres en utilisant une virgule comme séparateur de milliers. | Enketo et KoboCollect |
| `bearing` | Enregistre une lecture de boussole en degrés (`decimal` uniquement). | KoboCollect uniquement  |
| `counter` | Affiche des boutons pour augmenter et diminuer les chiffres (`integer` uniquement). | KoboCollect uniquement |


### Type de question intervalle
Les questions d'intervalle sont utilisées pour [sélectionner des valeurs dans une plage spécifiée](https://support.kobotoolbox.org/question_types_xls.html#numeric-question-types).

| Apparence | Description | Compatibilité |
| :--- | :--- | :--- |
| `vertical` | Change l'orientation de la ligne numérique en une ligne verticale. | Enketo et KoboCollect |
| `picker` | Dans KoboCollect, affiche un sélecteur rotatif contextuel pour sélectionner des valeurs. Dans Enketo, affiche un menu déroulant. | Enketo et KoboCollect |
| `rating` | Affiche des étoiles au lieu d'une ligne numérique. | Enketo et KoboCollect |
| `distress` | Affiche un thermomètre au lieu d'une ligne numérique. | Enketo et KoboCollect  |


### Type de question texte
Les questions de texte permettent aux utilisatrices et utilisateurs de [collecter des réponses ouvertes](https://support.kobotoolbox.org/question_types_xls.html#text-and-note-question-types).

| Apparence | Description | Compatibilité |
| :--- | :--- | :--- |
| `numbers` | Affiche un clavier numérique au lieu d'un clavier de texte (par exemple, pour collecter des numéros de téléphone). | KoboCollect uniquement |
| `multiline` | Affiche une zone de texte multiligne pour des réponses textuelles plus longues. | Enketo et KoboCollect |
| `url` | Affiche une URL cliquable sous le texte de la question et rend la question en lecture seule. Nécessite de saisir une URL dans la colonne `default` de la question, ou dans la colonne `calculation` si l'URL inclut des valeurs dynamiques. Fonctionne également avec les questions `note`. | Enketo et KoboCollect |
| `masked` | Masque le texte saisi par le ou la répondant(e) (par exemple, un mot de passe ou des informations confidentielles). | KoboCollect uniquement |


### Type de question date
Les questions de date sont utilisées pour [capturer des dates de calendrier spécifiques](https://support.kobotoolbox.org/question_types_xls.html#date-and-time-question-types).

| Apparence | Description | Compatibilité |
| :--- | :--- | :--- |
| `month-year` | Capture un mois et une année. | Enketo et KoboCollect |
| `year` | Capture uniquement une année. | Enketo et KoboCollect |
| `no-calendar` | Affiche un sélecteur rotatif pour sélectionner le jour, le mois et l'année, au lieu du sélecteur de style calendrier par défaut. | KoboCollect uniquement |
| `coptic` | Affiche le calendrier copte. | KoboCollect uniquement |
| `ethiopian` | Affiche le calendrier éthiopien. | KoboCollect uniquement |
| `islamic` | Affiche le calendrier islamique. | KoboCollect uniquement  |
| `bikram-sambat` | Affiche le calendrier Bikram Sambat. | KoboCollect uniquement |
| `myanmar` | Affiche le calendrier birman. | KoboCollect uniquement |
| `persian` | Affiche le calendrier persan. | KoboCollect uniquement |
| `buddhist` | Affiche le calendrier bouddhiste. | KoboCollect uniquement |


### Types de questions GPS
Les questions GPS sont utilisées pour [capturer les coordonnées géographiques](https://support.kobotoolbox.org/question_types_xls.html#gps-question-types) d'un emplacement, d'un chemin ou d'une zone directement dans vos formulaires.

| Apparence | Description | Compatibilité |
| :--- | :--- | :--- |
| `maps` | Affiche une carte permettant aux utilisatrices et utilisateurs de visualiser l'emplacement qui est automatiquement enregistré (`geopoint` uniquement). | KoboCollect uniquement (inclus dans l'apparence Enketo par défaut)  |
| `placement-map` | Permet la sélection manuelle d'un emplacement sur une carte (`geopoint` uniquement). | KoboCollect uniquement (inclus dans l'apparence Enketo par défaut)  |
| `hide-input` | Affiche une carte plus grande et masque les autres champs de saisie (latitude, longitude, altitude, précision). | Enketo uniquement |


### Questions de photographie
Les questions de photographie permettent aux utilisatrices et utilisateurs de [télécharger ou enregistrer des images](https://support.kobotoolbox.org/question_types_xls.html#media-question-types) directement dans leurs formulaires.

| Apparence | Description | Compatibilité |
| :--- | :--- | :--- |
| `signature` | Permet aux utilisatrices et utilisateurs de dessiner leur signature. | Enketo et KoboCollect |
| `draw` | Permet aux utilisatrices et utilisateurs de faire des croquis ou de créer des dessins. | Enketo et KoboCollect |
| `annotate` | Permet aux utilisatrices et utilisateurs d'annoter une image en dessinant ou en écrivant dessus. | Enketo et KoboCollect |
| `new` | Invite les utilisatrices et utilisateurs à prendre une nouvelle photo à l'aide de l'appareil photo de l'appareil (pas de téléchargement de fichier). | KoboCollect uniquement |
| `new-front` | Invite les utilisatrices et utilisateurs à prendre une nouvelle photo à l'aide de l'appareil photo frontal de l'appareil. | KoboCollect uniquement |


### Questions de code-barres
Les questions de code-barres permettent aux utilisatrices et utilisateurs de [scanner un code QR](https://support.kobotoolbox.org/question_types_xls.html#media-question-types) à l'aide de l'appareil photo de l'appareil dans KoboCollect.

| Apparence | Description | Compatibilité |
| :--- | :--- | :--- |
| `hidden-answer` | Masque la valeur du code-barres scanné. | KoboCollect uniquement |