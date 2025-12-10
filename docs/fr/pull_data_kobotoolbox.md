# Extraire des données d'un fichier CSV externe

La fonction `pulldata()` dans XLSForm vous permet de récupérer dynamiquement des informations d'un fichier CSV externe lors du remplissage d'un formulaire. Cela vous permet de référencer des ensembles de données existants et d'extraire automatiquement des détails connexes, évitant ainsi aux enquêteurs de ressaisir les mêmes informations.

Par exemple, vous pouvez utiliser `pulldata()` pour :
- **Remplir automatiquement des informations connexes :** Lorsqu'un ID, un code ou une clé est saisi, récupérer automatiquement les détails associés tels qu'un nom, une catégorie ou une description.
- **Précharger des données de référence :** Charger des informations à partir de fichiers externes afin que les enquêteurs n'aient qu'à collecter des données nouvelles ou mises à jour.

L'utilisation de `pulldata()` permet de réduire les erreurs, de gagner du temps lors de la collecte de données et de garantir que les formulaires restent cohérents avec les ensembles de données de référence externes. Cette fonction est prise en charge à la fois dans <a href="https://support.kobotoolbox.org/kobocollect_on_android_latest.html">l'application Android KoboCollect</a> et dans les <a href="https://support.kobotoolbox.org/enketo.html">formulaires web Enketo</a>. Nous recommandons d'utiliser <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">XLSForm</a> pour configurer la fonction `pulldata()`.

Cet article couvre les étapes suivantes pour extraire des données d'un fichier CSV externe :
- Configuration de votre fichier CSV externe
- Configuration de votre XLSForm
- Téléchargement de votre fichier CSV externe vers KoboToolbox

## Configuration de votre fichier CSV externe

Pour utiliser `pulldata()`, préparez d'abord un fichier CSV externe contenant les données de référence que vous souhaitez récupérer. Chaque ligne doit représenter un enregistrement unique (par exemple, un participant, un lieu ou un élément) et le fichier doit inclure au moins deux colonnes. Une colonne doit contenir la **variable d'index** qui correspond aux valeurs saisies dans votre formulaire.

La **variable d'index** agit comme la [clé primaire](https://en.wikipedia.org/wiki/Primary_key) qui relie votre XLSForm au fichier CSV externe. Il doit s'agir d'un identifiant unique qui existe dans les deux fichiers, tel qu'un ID de participant, un nom de district ou un autre code correspondant.

Les colonnes restantes peuvent inclure tous les détails supplémentaires que vous souhaitez récupérer, tels que des noms, des catégories ou des descriptions. Assurez-vous que le fichier CSV est propre, formaté de manière cohérente et enregistré avec l'extension `.csv`.

**Exemple : eligibility.csv**

| ID           | status          | 
|:-----------  |:----------------|
| AH784N       | eligible        |
| DB839K       | ineligible      | 
| SH849T       | eligible        |

## Configuration de votre XLSForm

Une fois que vous avez configuré votre fichier CSV externe, configurez votre XLSForm de la manière suivante :

1. Assurez-vous que votre XLSForm inclut une question qui sert de **variable d'index**.
2. Ajoutez un champ `calculate` à votre questionnaire. Donnez un `name` au champ.
3. Dans la colonne `calculation`, utilisez la fonction **pulldata()** pour spécifier quel champ du CSV extraire. Utilisez la syntaxe suivante : `pulldata('csv','pull_from', 'csv_index', '${survey_index}')`.	
    - `csv` est le nom du fichier CSV, sans l'extension.
    - `pull_from` fait référence à la colonne de votre fichier CSV qui contient les données que vous souhaitez importer dans votre formulaire.
    - `csv_index` est la colonne de votre fichier CSV qui contient la **variable d'index**.
    - `survey_index` est le nom de la question dans votre questionnaire qui contient la **variable d'index**.
  
  **Feuille survey**

  | type      | name               | label                                      | calculation |
|:-----------|:------------------|:-------------------------------------------|:-------------|
| text       | respondent_id      | ID du répondant                            |              |
| calculate  | eligibility_status |                                            | pulldata('eligibility', 'status', 'ID', 'respondent_id') |
| note       | eligibility_note    | Le répondant est ${eligibility_status} pour l'étude. |              |
| survey | 

Dans l'exemple ci-dessus, le calcul récupère la valeur de la colonne `status` du fichier `eligibility.csv`, dans la ligne où l'`ID` du CSV correspond à l'ID saisi dans la question `respondent_id` de votre formulaire.

<p class="note">
<strong>Remarque :</strong> Après avoir utilisé la fonction <code>pulldata()</code> pour récupérer des données CSV externes, vous pouvez référencer ce champ dans les conditions de branchement conditionnel, les contraintes et les libellés suivants, comme n'importe quel autre champ ou calcul.
</p>

## Téléchargement de votre fichier CSV externe vers KoboToolbox

La dernière étape pour lier votre fichier CSV externe à votre formulaire consiste à télécharger le fichier vers KoboToolbox. Pour ce faire :
1. Accédez aux **PARAMÈTRES** de votre projet et ouvrez l'onglet **Médias**.
2. Téléchargez le(s) fichier(s) CSV avec le nom exact que vous avez utilisé dans votre XLSForm.
3. Déployez ou redéployez le formulaire.

![Télécharger un média](images/pull_data_kobotoolbox/upload_media.png) 

## Dépannage

<details>
  <summary><strong>Les polices non anglaises ou les caractères spéciaux ne s'affichent pas correctement</strong></summary>
  Enregistrez votre fichier CSV au <strong>format UTF-8</strong>. Cela garantit que les appareils Android peuvent afficher correctement le texte non anglais ou les caractères spéciaux.
</details>

<br>

<details>
  <summary><strong>Les valeurs numériques ne fonctionnent pas comme prévu</strong></summary>
  Toutes les données extraites d'un fichier CSV sont traitées comme du texte. Pour utiliser ces valeurs comme des nombres, appliquez les <a href="https://support.kobotoolbox.org/functions_xls.html">fonctions</a> <code>int()</code> ou <code>number()</code> à la valeur récupérée dans votre XLSForm.
</details>

<br>

<details>
  <summary><strong>Protection des données sensibles</strong></summary>
  Si votre CSV contient des informations sensibles que vous ne souhaitez pas télécharger sur le serveur, téléchargez un fichier CSV vide avec votre formulaire. Ensuite, remplacez-le manuellement sur chaque appareil par le véritable fichier CSV. Cette approche ne fonctionne qu'avec l'application KoboCollect.
</details>

<br>

<details>
  <summary><strong>Chargement lent du formulaire avec des fichiers volumineux</strong></summary>
  Si vous utilisez des fichiers CSV très volumineux, vous pouvez rencontrer un chargement lent du formulaire dans KoboCollect. Pour résoudre ce problème, nous recommandons d'utiliser la colonne <a href="https://support.kobotoolbox.org/question_options_xls.html#additional-question-options">trigger</a> pour extraire les données du fichier externe une seule fois, plutôt que de manière récurrente en arrière-plan.
</details>

<br>

<details>
  <summary><strong>Extraction de dates à partir de fichiers CSV externes</strong></summary>
  Si vous stockez des dates dans un fichier CSV externe et souhaitez les extraire dans un formulaire, assurez-vous qu'elles sont au format AAAA-MM-JJ. Si vous modifiez votre CSV dans Excel, ajoutez une apostrophe <code>'</code> devant la date pour éviter le formatage automatique des dates dans Excel.
</details>

<br>

<details>
  <summary><strong>L'extraction de données ne fonctionne pas correctement</strong></summary>
  Si la fonctionnalité pulldata() ne fonctionne pas correctement, essayez ce qui suit :
  <ul>
  <li>Renommez votre fichier CSV pour supprimer les traits de soulignement ou les symboles spéciaux.</li>
  <li>Vérifiez que votre fichier CSV est correctement configuré avec une variable par colonne (voir la publication sur le <a href="https://community.kobotoolbox.org/t/pulldata-is-not-working-on-kobocollect-android/6462/39">Forum communautaire</a>).</li>
  <li>Vérifiez que vous utilisez l'orthographe exacte pour les noms de fichiers et les noms de colonnes.</li>
  <li>Vérifiez que les cellules de votre fichier CSV ne contiennent pas d'espaces supplémentaires avant ou après la valeur.</li>
</ul>
</details>

<br>