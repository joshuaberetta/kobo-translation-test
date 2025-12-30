# Utiliser XLSForm avec KoboToolbox

XLSForm s'intègre facilement avec KoboToolbox pour créer, prévisualiser, modifier et déployer des formulaires de collecte de données. Par exemple, vous pouvez commencer à créer un formulaire dans l'interface de création de formulaires KoboToolbox (KoboToolbox Formbuilder), puis le télécharger en tant que XLSForm pour une personnalisation plus poussée. Cela fournit une base structurée, utile pour les nouveaux projets ou les utilisatrices et utilisateurs ayant moins d'expérience en création de formulaires.

Une fois personnalisés, les formulaires créés dans XLSForm peuvent être importés dans KoboToolbox pour révision, modification et déploiement.

Cet article couvre les sujets suivants :
-   Télécharger un XLSForm depuis KoboToolbox
-   Importer et prévisualiser un XLSForm dans KoboToolbox
-   Remplacer un formulaire existant par un XLSForm
-   Importer un XLSForm via URL
-   Tester et valider votre XLSForm

## Télécharger un XLSForm depuis KoboToolbox

Lorsque vous travaillez dans KoboToolbox, vous pouvez avoir besoin de télécharger votre formulaire en tant que XLSForm pour apporter des modifications plus efficacement, comme dupliquer de nombreuses questions, modifier de grandes listes d'options, ajouter des traductions ou utiliser des fonctionnalités avancées non disponibles dans l'interface de création de formulaires. De plus, télécharger votre formulaire en tant que XLSForm vous permet de créer des formulaires hors ligne, de les partager sous forme de fichiers `.xlsx` pour la collaboration et la gestion des versions, et de les partager avec l'équipe d'assistance KoboToolbox ou sur le Forum communautaire pour demander de l'aide.

Tout formulaire créé à l'aide de l'interface de création de formulaires KoboToolbox peut être téléchargé en tant que fichier XLSForm :

1.  Accédez à la page **FORMULAIRE** de votre projet dans KoboToolbox.
2.  Cliquez sur l'icône <i class="k-icon k-icon-more"></i> **Plus d'actions**.
3.  Sélectionnez <i class="k-icon k-icon-xls-file"></i> **Télécharger XLS**.

![Menu Télécharger XLS](images/xlsform_with_kobotoolbox/download_xls.png)

## Importer un XLSForm dans KoboToolbox
Vous pouvez également avoir besoin de créer un nouveau projet à partir d'un XLSForm que vous avez créé de toutes pièces ou qui a été partagé avec vous.

Pour importer et prévisualiser un XLSForm dans un nouveau projet dans KoboToolbox :

1.  Accédez à la page d'accueil **Projets** dans KoboToolbox et cliquez sur **NOUVEAU**.
2.  Sélectionnez **Importer un XLSForm** et importez votre fichier Excel.
3.  Saisissez les détails du projet et cliquez sur **Créer un projet**.
4.  Cliquez sur le bouton <i class="k-icon k-icon-view"></i> **Aperçu** pour prévisualiser votre formulaire.

![Boîte de dialogue Importer un XLSForm](images/xlsform_with_kobotoolbox/upload_xls.png)

## Remplacer un formulaire par un XLSForm
Une fois qu'un projet a été créé, vous pouvez remplacer n'importe quel formulaire existant par un XLSForm mis à jour :

1.  Accédez à la page **FORMULAIRE** de votre projet dans KoboToolbox.
2.  Cliquez sur <i class="k-icon k-icon-replace"></i> **Remplacer le formulaire** dans le coin supérieur droit.
3.  Sélectionnez **Importer un XLSForm** et importez votre fichier Excel.

![Boîte de dialogue Remplacer la source du formulaire](images/xlsform_with_kobotoolbox/replace_form.png)

## Importer un XLSForm via URL
Si vous utilisez Google Sheets ou stockez le fichier dans Dropbox, vous pouvez importer un XLSForm via une URL. L'URL doit être accessible publiquement et doit lancer un téléchargement de fichier lorsqu'elle est ouverte dans un navigateur pour que l'importation fonctionne. Les XLSForms peuvent également être importés depuis des logiciels similaires, tels qu'Excel Web et OneDrive.

<details><summary><strong>Récupérer un lien depuis Google Sheets</strong></summary>

Pour obtenir l'URL correcte pour une feuille de calcul Google Sheets :

1.  Cliquez sur **Fichier > Partager > Publier sur le Web**.
2.  Dans le menu déroulant **Page Web**, sélectionnez **Microsoft Excel (.xlsx)**. Conservez **Document entier** sélectionné dans le premier menu déroulant.
3.  Cliquez sur **Publier**.
4.  Copiez le lien du document résultant.

<p class="note"> 
Pour plus d'informations, consultez la <a href="https://support.google.com/docs/answer/183965?hl=en&co=GENIE.Platform%3DDesktop">documentation Google Sheets</a>.
</p>

</details>

<br>

<details><summary><strong>Récupérer un lien depuis Dropbox</strong></summary>
    
Pour obtenir l'URL correcte pour une feuille de calcul stockée dans Dropbox :

1.  Copiez le lien du fichier dans Dropbox en cliquant sur <i class="k-icon k-icon-link"></i> **Copier le lien**.
2.  À la fin du lien, remplacez le suffixe ``dl=0`` par ``dl=1``. Ce sera l'URL à importer dans KoboToolbox.
    
</details>

<br>

Une fois que vous avez récupéré l'URL du fichier, vous pouvez importer votre XLSForm dans KoboToolbox :

1.  Accédez à la page d'accueil **Projets** dans KoboToolbox et cliquez sur **NOUVEAU**.
2.  Sélectionnez **Importer un XLSForm via URL**.
3.  Collez votre URL et cliquez sur **Importer**.
4.  Saisissez les détails du projet et cliquez sur **Créer un projet**.

![Boîte de dialogue Importer un XLSForm via URL](images/xlsform_with_kobotoolbox/import_via_url.png)

<p class="note">
    <b>Remarque :</b> Les modifications apportées à un fichier dans Dropbox ou Google Sheets ne se mettent pas automatiquement à jour dans KoboToolbox. Vous devez réimporter le XLSForm via URL et redéployer les modifications du formulaire.
</p>

## Tester et valider votre XLSForm
Valider, prévisualiser et tester votre XLSForm est essentiel pour garantir son intégrité structurelle, sa fonctionnalité et l'expérience utilisateur. Chacune de ces étapes aide à identifier les erreurs ou problèmes qui pourraient empêcher le formulaire de fonctionner comme prévu.

| Étape | Description |
| :--- | :--- |
| Validation | Cela implique d'importer le formulaire et de vérifier les erreurs (par exemple, fautes d'orthographe ou de majuscules, expressions de logique de formulaire incorrectes, référencement de questions incorrect, libellés manquants). Les messages d'erreur de formulaire apparaissent généralement lors de l'importation, du déploiement ou de l'ouverture d'un formulaire. |
| Prévisualisation | Cela vous permet de visualiser le formulaire tel qu'il sera affiché aux répondant(e)s et de vérifier que tous les éléments fonctionnent correctement avant le déploiement (par exemple, mise en page du formulaire, libellés des questions et des choix). |
| Test | Cela implique de saisir des données pour tester la fonctionnalité du formulaire (par exemple, vérifier les apparences des questions, les options de choix et la logique du formulaire). Les tests peuvent être effectués en mode **APERÇU** avant le déploiement. |

Valider et tester continuellement votre XLSForm au fur et à mesure que vous apportez des modifications simplifiera le dépannage et aidera à identifier la cause de tout problème. Il est crucial de vous assurer que votre formulaire fonctionne comme prévu avant de lancer la collecte de données.

Plusieurs outils sont disponibles pour tester votre XLSForm, notamment la plateforme KoboToolbox, [l'application Android KoboCollect](https://play.google.com/store/apps/details?id=org.koboc.collect.android) et [XLSForm Online d'ODK](https://getodk.org/xlsform/). Lors de la prévisualisation et du test de votre formulaire, utilisez la même plateforme que celle que vous utiliserez pour la collecte de données : [formulaires web Enketo](https://support.kobotoolbox.org/enketo.html), [KoboCollect](https://support.kobotoolbox.org/kobocollect_on_android_latest.html), ou les deux.

<p class="note">
Pour en savoir plus sur la configuration de KoboCollect pour prévisualiser et tester vos formulaires, consultez <a href="https://support.kobotoolbox.org/kobocollect_on_android_latest.html">Se lancer avec KoboCollect</a>.
</p>

## Dépannage

<details>
<summary><strong>Message d'erreur lors de l'importation, de la prévisualisation ou du déploiement d'un XLSForm</strong></summary>
    
Si votre XLSForm contient une erreur, un message d'erreur apparaîtra, indiquant généralement la ligne, la question ou l'expression exacte où se trouve le problème. Après avoir corrigé l'erreur dans votre feuille de calcul, vous devrez importer à nouveau le fichier.


| **Messages d'erreur courants** | **Explication courante** |
| :--- | :--- |
| `The survey sheet is either empty or missing important column headers.` | Les en-têtes de colonnes obligatoires sont manquants ou mal orthographiés. |
| `The survey element named 'name' has no label or hint.` | L'une des questions de votre formulaire n'a pas de libellé de question. |
| `FormLogicError: Could not evaluate: [expression], message: The string did not match the expected pattern.` | Une expression de logique de formulaire contient des erreurs, telles qu'une syntaxe de référencement de question incorrecte ou une parenthèse manquante. |
| `unable to deploy ODK Validate Errors: >> XForm is invalid` | Une expression de logique de formulaire contient des erreurs, telles qu'une syntaxe de référencement de question incorrecte ou une parenthèse manquante. |
| `There has been a problem trying to replace ${question with the XPath to the survey element named 'question'. There is no survey element with this name.` | Vous faites référence à une question dans votre formulaire qui n'existe pas ou qui est mal orthographiée. Assurez-vous d'utiliser le nom de question **exact** dans vos expressions de logique de formulaire. |
| `list_name` | La liste d'options pour une question n'a pas été définie, ou il y a une faute de frappe dans le `list_name` (nom de la liste). |
| `Choice names must be unique for each choice list. If this is intentional, use the setting 'allow_choice_duplicates'.` | Des noms de choix en double ont été utilisés dans la même liste d'options. Supprimez le(s) nom(s) de choix en double, ou autorisez les choix en double dans vos <a href="https://support.kobotoolbox.org/form_settings_xls.html">paramètres de formulaire</a>. |
| `Unmatched begin statement: group (group)` | Un groupe de questions n'a pas sa ligne `end_group` correspondante. |
| `Can't find external_file.csv` | Une <a href="https://support.kobotoolbox.org/pull_data_kobotoolbox.html">pièce jointe externe</a> liée à votre formulaire (par exemple, lors de l'utilisation de `pulldata()`) n'a pas été importée dans KoboToolbox. |
| `Can't find survey.xml` | Les <a href="https://support.kobotoolbox.org/dynamic_data_attachment.html">pièces jointes de données dynamiques</a> n'ont pas été correctement configurées dans les paramètres de votre projet. |
</details>

<br>

<details>
<summary><strong>Erreur lors de la tentative d'importation d'un XLSForm via URL</strong></summary>
<br>
Vérifiez que l'URL que vous utilisez est correcte. Lorsqu'elle est chargée dans un navigateur, l'URL doit lancer un téléchargement de fichier, et non ouvrir une page web.
</details>

<br>

<details>
<summary><strong>L'importation via URL ne charge pas la version non déployée</strong></summary>
<br>
Si vous avez importé un lien et que vous ne voyez pas la nouvelle version du formulaire, actualisez votre navigateur.
</details>