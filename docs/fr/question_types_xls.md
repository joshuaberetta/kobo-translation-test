# Types de questions dans XLSForm

Lorsque vous ajoutez des questions à un XLSForm, vous devrez choisir le **type de question** approprié. Le type de question dépendra du type d'information que vous souhaitez collecter : certains types de questions sont plus adaptés au texte, d'autres aux chiffres, aux dates ou aux choix multiples.

Le type de question dans XLSForm est saisi dans la colonne **type** de la feuille de calcul **survey**. Utilisez toujours l'orthographe exacte et respectez la casse. Vous pouvez ajouter des [apparences](https://support.kobotoolbox.org/appearances_xls.html) supplémentaires à la plupart des types de questions pour modifier leur affichage ou leur fonctionnalité.

<p class="note">
<strong>Remarque :</strong> Bien que XLSForm soit entièrement intégré dans KoboToolbox, certains types de questions ont des noms et des fonctionnalités différents dans l'<a href="https://support.kobotoolbox.org/formbuilder.html">interface de création de formulaires</a> par rapport à XLSForm.
</p>

Cet article couvre les types de questions disponibles dans XLSForm, y compris leurs descriptions et leurs équivalents dans l'interface de création de formulaires. Des liens sont fournis à la fin de chaque section pour plus d'informations sur les fonctionnalités des types de questions et les apparences lors de la collecte de données.

<p class="note">
Pour en savoir plus sur la création de formulaires dans XLSForm, consultez <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">Débuter avec XLSForm</a>.
</p>

### Types de questions de sélection

Les questions de sélection permettent aux répondant(e)s de choisir parmi des options prédéfinies. Pour les questions `select_one`, `select_multiple` et `rank`, les [choix d'options](https://support.kobotoolbox.org/option_choices_xls.html) sont définis dans la feuille de calcul **choices** de l'XLSForm.

| Type XLSForm | Description | Équivalent dans l'interface de création de formulaires |
| :--- | :--- | :--- |
| `select_one` | Permet aux répondant(e)s de sélectionner une option parmi une liste prédéfinie. | Choix unique |
| `select_multiple` | Permet aux répondant(e)s de sélectionner plusieurs options parmi une liste prédéfinie. | Choix multiple |
| `rank` | Permet aux répondant(e)s de classer des éléments ou des options dans une liste de choix. | Classement |
| `acknowledge` | Une case à cocher unique que les répondant(e)s peuvent sélectionner pour confirmer leur accord avec une déclaration. | Consentement |
| `select_one_from_file` | Permet aux répondant(e)s de sélectionner une option parmi une liste prédéfinie, stockée dans un fichier CSV externe. | Choix unique à partir d'un fichier externe |
| `select_multiple_from_file` | Permet aux répondant(e)s de sélectionner plusieurs options parmi une liste prédéfinie, stockée dans un fichier CSV externe. | Choix multiple à partir d'un fichier externe |


<p class="note">
Pour en savoir plus sur les types de questions de sélection dans KoboToolbox, consultez <a href="https://support.kobotoolbox.org/select_one_and_select_many.html">Types de questions Choix unique et Choix multiple</a>, <a href="https://support.kobotoolbox.org/rating_ranking.html">Types de questions Notation vs Classement</a>, <a href="https://support.kobotoolbox.org/acknowledge.html">Type de question Consentement</a>, et <a href="https://support.kobotoolbox.org/external_file.html">Types de questions Choix unique ou multiple à partir d'un fichier externe</a>.
</p>


### Types de questions numériques

Les questions numériques sont utilisées pour collecter des nombres entiers, des nombres décimaux ou des valeurs dans une plage spécifiée.

| Type XLSForm | Description | Équivalent dans l'interface de création de formulaires |
| :--- | :--- | :--- |
| `integer` | Permet aux répondant(e)s de saisir des nombres entiers. | Chiffre |
| `decimal` | Permet aux répondant(e)s de saisir des nombres pouvant contenir des décimales. | Décimale |
| `range` | Permet aux répondant(e)s de sélectionner une valeur numérique dans une plage spécifiée, limitée par des valeurs minimales et maximales, <a href="https://support.kobotoolbox.org/question_options_xls.html#question-parameters">configurées</a> dans la colonne **parameters**. | Intervalle |


<p class="note">
Pour en savoir plus sur les types de questions numériques dans KoboToolbox, consultez <a href="https://support.kobotoolbox.org/number_decimal_range.html">Types de questions Chiffre, Décimale et Intervalle</a>.
</p>


### Types de questions texte et note

Les questions texte sont utilisées pour collecter des réponses ouvertes, tandis que les questions note fournissent des informations ou donnent des instructions aux répondant(e)s.

| Type XLSForm | Description | Équivalent dans l'interface de création de formulaires |
| :--- | :--- | :--- |
| `text` | Fournit une zone de texte pour collecter des réponses ouvertes lorsque les choix ne peuvent pas être facilement prédéfinis, comme des noms, des opinions ou des descriptions détaillées. | Texte |
| `note` | Fournit des informations au/à la répondant(e) sans nécessiter de saisie, comme des instructions ou des explications. | Note |


<p class="note">
Pour en savoir plus sur les types de questions texte et note dans KoboToolbox, consultez <a href="https://support.kobotoolbox.org/text_and_note.html">Types de questions Texte et Note</a>.
</p>

### Types de questions média

Les questions média permettent aux répondant(e)s de télécharger ou d'enregistrer des images, des fichiers audio et vidéo, ou de scanner des codes-barres directement dans leurs formulaires.

| Type XLSForm | Description | Équivalent dans l'interface de création de formulaires |
| :--- | :--- | :--- |
| `image` | Permet aux répondant(e)s de télécharger des images ou de prendre des photos lors de l'utilisation de l'application KoboCollect. La qualité des fichiers image peut être <a href="https://support.kobotoolbox.org/question_options_xls.html#question-parameters">ajustée</a> dans la colonne **parameters**. | Photographie |
| `audio` | Permet aux répondant(e)s de télécharger un fichier audio ou d'enregistrer de l'audio en réponse à une question spécifique. La qualité des fichiers audio peut être <a href="https://support.kobotoolbox.org/question_options_xls.html#question-parameters">ajustée</a> dans la colonne **parameters**. | Audio |
| `video` | Permet aux répondant(e)s de télécharger des vidéos ou d'enregistrer des vidéos lors de l'utilisation de l'application KoboCollect. | Vidéo |
| `file` | Permet aux répondant(e)s de télécharger des fichiers, tels que des fichiers texte, des feuilles de calcul et des fichiers PDF. Les types de fichiers acceptés peuvent être <a href="https://support.kobotoolbox.org/question_options_xls.html#additional-question-options">restreints</a> en spécifiant les extensions de fichiers dans la colonne **body::accept** (par exemple, `.pdf, .docx`). | Fichier |
| `barcode` | Scanne un code QR pour collecter les informations intégrées à l'aide de la caméra de l'appareil dans KoboCollect. | Code-barres |
| `background-audio` | Collecte de l'audio en continu pendant que le formulaire est ouvert. L'enregistrement audio commence lorsque le formulaire est ouvert et se poursuit jusqu'à ce que le formulaire soit fermé. | Enregistrement audio d'arrière-plan |


<p class="note">
Pour en savoir plus sur les types de questions média dans KoboToolbox, consultez <a href="https://support.kobotoolbox.org/photo_audio_video_file.html">Types de questions média</a>, <a href="https://support.kobotoolbox.org/barcode_qrcode_questions.html">Type de question Code-barres/QR code</a>, et <a href="https://support.kobotoolbox.org/recording-interviews.html">Enregistrement d'entretiens à l'aide de l'enregistrement audio d'arrière-plan</a>.
</p>

### Types de questions GPS

Les questions GPS sont utilisées pour capturer les coordonnées géographiques d'un lieu, d'un chemin ou d'une zone directement dans vos formulaires.

| Type XLSForm | Description | Équivalent dans l'interface de création de formulaires |
| :--- | :--- | :--- |
| `geopoint` | Collecte un emplacement géographique unique, tel que les coordonnées d'une école, d'une clinique ou d'une maison spécifique. La précision par défaut et la précision d'avertissement peuvent être <a href="https://support.kobotoolbox.org/question_options_xls.html#question-parameters">configurées</a> dans la colonne **parameters**. | Position |
| `geotrace` | Enregistre plusieurs points GPS qui forment une ligne, par exemple pour suivre un chemin, tracer un itinéraire ou cartographier un drain. | Ligne |
| `geoshape` | Collecte des points qui forment une zone fermée, comme une parcelle de terrain ou un champ. | Zone |


<p class="note">
Pour en savoir plus sur les types de questions GPS dans KoboToolbox, consultez <a href="https://support.kobotoolbox.org/gps_questions.html">Types de questions GPS</a>.
</p>

### Types de questions date et heure

Les questions date et heure sont utilisées pour capturer des dates de calendrier spécifiques, des heures ou les deux dans une seule réponse.

| Type XLSForm | Description | Équivalent dans l'interface de création de formulaires |
| :--- | :--- | :--- |
| `date` | Capture une date de calendrier spécifique, généralement au format jour, mois et année. | Date |
| `time` | Capture une heure spécifique en heures et minutes. | Heure |
| `datetime` | Capture à la fois une date et une heure dans une seule réponse combinée. | Date et heure |


<p class="note">
Pour en savoir plus sur les questions date et heure dans KoboToolbox, consultez <a href="https://support.kobotoolbox.org/date_time.html">Types de questions Date et Heure</a>.
</p>

### Types de questions calcul et caché

Les questions calcul et caché sont utilisées pour effectuer des calculs automatiques dans un formulaire en fonction des réponses précédentes ou pour stocker des valeurs prédéfinies.

| Type XLSForm | Description | Équivalent dans l'interface de création de formulaires |
| :--- | :--- | :--- |
| `calculate` | Effectue automatiquement des calculs dans un formulaire en fonction des réponses aux questions précédentes. | Calcul |
| `hidden` | Stocke des valeurs prédéfinies qui ne sont pas visibles pour le/la répondant(e). La valeur est <a href="https://support.kobotoolbox.org/question_options_xls.html#default-responses">stockée</a> dans la colonne **default**. | Caché |

Pour en savoir plus sur les calculs dans l'interface de création de formulaires, consultez <a href="https://support.kobotoolbox.org/calculate_questions.html">Type de question Calcul</a>. Pour en savoir plus sur les calculs dans XLSForm, consultez <a href="https://support.kobotoolbox.org/calculations_xls.html">Ajouter des calculs dans XLSForm</a>.

<p class="note">
Pour une pratique concrète avec différents types de questions XLSForm, consultez le <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">Cours sur les fondamentaux XLSForm de KoboToolbox Academy</a>.
</p>