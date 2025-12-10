# Utiliser les options de question dans XLSForm

Lors de la conception d'un formulaire dans XLSForm, vous pouvez personnaliser les questions en ajoutant des indices, en définissant des apparences, en rendant une question obligatoire, et plus encore. Pour ce faire, vous pouvez ajouter de nouvelles colonnes dans la feuille de calcul **survey** de votre XLSForm. Ces colonnes peuvent être ajoutées n'importe où dans la feuille de calcul, à condition que le nom de la colonne soit tapé exactement comme requis.

Cet article couvre les options de question les plus courantes et comment les ajouter à votre XLSForm, y compris les indices de question, les questions obligatoires, les réponses par défaut et les paramètres de question.

<p class="note">
  <strong>Note :</strong> Cet article se concentre sur la définition des options de question dans <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">XLSForm</a>. Pour en savoir plus sur les options de question dans l'interface de création de formulaires KoboToolbox (KoboToolbox Formbuilder), consultez <a href="https://support.kobotoolbox.org/question_options.html">Utiliser les options de question</a>.
<br><br>
Pour une pratique concrète des options de question dans XLSForm, consultez le <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">Cours Fondamentaux XLSForm</a> de KoboToolbox Academy.
</p>

## Indices de question

Les **indices de question** vous permettent d'ajouter des instructions ou des informations supplémentaires à votre formulaire. Il existe deux types d'indices que vous pouvez ajouter dans XLSForm :
- Les **indices de base** sont utilisés pour fournir des informations supplémentaires aux répondant(e)s ou aux enquêteurs directement dans le formulaire. Ils sont toujours visibles et affichés sous le libellé de la question.
- Les **instructions supplémentaires** sont utilisées pour fournir des informations supplémentaires pendant le développement du formulaire, la formation des enquêteurs ou la collecte de données. Elles ne sont pas affichées par défaut.

### Ajouter des indices de question dans XLSForm

Pour ajouter un **indice de base** dans XLSForm :
1. Ajoutez une colonne **hint** à la feuille de calcul `survey`.
2. Dans la même ligne que votre question, saisissez le texte qui doit être affiché comme indice pour cette question.

Pour ajouter des **instructions supplémentaires** dans XLSForm :
1. Ajoutez une colonne **guidance_hint** à la feuille de calcul `survey`.
2. Dans la même ligne que votre question, saisissez le texte qui doit être inclus comme instructions supplémentaires.

**Feuille de calcul survey**

| type | name | label | hint | guidance_hint |
| :--- | :--- | :--- | :--- | :--- |
| integer | height | Quelle est votre taille ? | En centimètres | Si le/la répondant(e) ne connaît pas sa taille, saisissez 0 |
| survey |

<p class="note">
<strong>Note :</strong> Les indices de question peuvent également être traduits en plusieurs langues. Pour plus d'informations sur la traduction des formulaires, consultez <a class="reference" href="https://support.kobotoolbox.org/language_xls.html">Ajouter des traductions dans XLSForm</a>.
</p>

### Afficher les instructions supplémentaires dans KoboCollect

Dans les formulaires web Enketo, les instructions supplémentaires apparaissent dans une section pliable **Plus de détails**. Dans KoboCollect, elles sont masquées par défaut, mais vous pouvez [modifier les paramètres de votre projet](https://support.kobotoolbox.org/kobocollect_settings.html#form-management-settings) pour toujours les afficher ou les afficher dans une section pliable.

Pour afficher les instructions supplémentaires dans KoboCollect, suivez les étapes ci-dessous :
1. Appuyez sur l'**icône Projet** dans le coin supérieur droit de votre écran.
2. Appuyez sur **Paramètres**.
3. Sous **Gestion de formulaires**, sélectionnez **Afficher les instructions pour les questions**.
4. Choisissez une option d'affichage : **Non**, **Oui - toujours affiché**, ou **Oui - réduit**.

<p class="note">
<strong>Note :</strong> Les instructions supplémentaires sont toujours affichées dans les formulaires imprimés.
</p>

## Questions obligatoires

Par défaut, les questions d'un formulaire sont facultatives. Définir une question comme **obligatoire** rend obligatoire pour le/la répondant(e) d'y répondre. Cela peut être utile pour garantir que les soumissions sont complètes et éviter les données manquantes.

<p class="note">
<strong>Note :</strong> Les conditions de branchement conditionnel ont la priorité sur les paramètres <strong>obligatoires</strong>, ce qui signifie que si une question obligatoire est masquée par un branchement conditionnel, il n'est plus obligatoire d'y répondre.
</p>

Pour définir une question comme obligatoire dans XLSForm :
1. Ajoutez une colonne `required` à la feuille de calcul `survey`.
2. Dans la colonne `required`, saisissez l'un des éléments suivants : **TRUE**, **true**, ou **yes**.
3. Pour les questions facultatives, laissez la colonne `required` vide ou saisissez l'un des éléments suivants : **FALSE**, **false**, ou **no**.

Si un(e) répondant(e) ne répond pas à une question obligatoire, il/elle ne pourra pas passer à la page suivante ou soumettre le formulaire. Le message obligatoire par défaut « Ce champ est obligatoire » sera affiché.

<p class="note">
<strong>Note :</strong> Seules les questions qui nécessitent une saisie doivent être marquées comme obligatoires dans votre XLSForm. Si les questions de type <code>note</code> sont marquées comme obligatoires, vous ne pourrez pas continuer ou soumettre le formulaire.
</p>

### Modifier le message obligatoire par défaut

Vous pouvez modifier le message obligatoire par défaut dans votre XLSForm en suivant les étapes ci-dessous :

1. Ajoutez une colonne **required_message** à la feuille de calcul `survey`.
2. Saisissez le texte que vous souhaitez afficher lorsque les utilisatrices et utilisateurs laissent une question obligatoire vide.

**Feuille de calcul survey**

| type | name | label | required | required_message |
| :--- | :--- | :--- | :--- | :--- |
| select_one education | education_level | Quel est le niveau d'études le plus élevé que vous avez terminé ? | TRUE | |
| integer | age | Quel est votre âge ? | TRUE | Veuillez répondre à cette question avant de continuer. |
| survey |

<p class="note">
<strong>Note :</strong> Une logique de formulaire personnalisée peut être utilisée pour rendre une question obligatoire ou facultative en fonction d'une réponse précédente. Pour en savoir plus sur la logique obligatoire basée sur des conditions, consultez <a class="reference" href="https://support.kobotoolbox.org/required_logic_xls.html">Ajouter une logique obligatoire dans XLSForm</a>.
</p>

## Réponses par défaut

Une **réponse par défaut** remplit une question avec une réponse prédéfinie basée sur une réponse courante ou attendue. La réponse par défaut peut être fixe ou [déterminée dynamiquement](https://support.kobotoolbox.org/question_options_xls.html#setting-dynamic-default-responses) en fonction de la réponse à une question précédente.

La réponse par défaut sera enregistrée comme réponse finale lorsque le formulaire sera soumis **sauf si elle est modifiée par le/la répondant(e)** pendant la collecte de données. Pour empêcher les répondant(e)s de modifier une réponse par défaut, ajoutez une colonne **read-only** et définissez-la sur **TRUE**.

<p class="note">
<strong>Note :</strong> Bien que les réponses par défaut puissent rendre la collecte de données plus efficace en préremplissant le formulaire avec des réponses attendues ou courantes, elles risquent également d'introduire des biais ou des erreurs dans les données, et doivent être utilisées avec prudence.
</p>

Pour définir une réponse par défaut fixe dans XLSForm :
1. Ajoutez une colonne **default** à la feuille de calcul `survey`.
2. Saisissez la réponse par défaut, en suivant le [format approprié](https://support.kobotoolbox.org/question_options_xls.html#default-response-format) pour le type de question.

**Feuille de calcul survey**

| type | name | label | default |
| :--- | :--- | :--- | :--- |
| text | name | Quel est votre nom ? | Jean Dupont |
| integer | age | Quel est votre âge ? | 50 |
| select_one marital_options | marital_status | Quel est votre état civil ? | married |
| select_multiple income_options | income_sources | Quelles sont vos sources de revenus ? | formal_work farm_business |
| date | dob | Quand êtes-vous né(e) ? | 1990-03-25 |
| date | interview_date | Quand cet entretien a-t-il été mené ? | today() |
| survey |

### Format de réponse par défaut

Le format de la réponse par défaut dépend du type de question et des données collectées :

| Type de question | Format de réponse par défaut |
| :--- | :--- |
| integer | Chiffre |
| text | Texte (sans guillemets) |
| select_one | **name** du choix (tel que défini dans la feuille de calcul choices) |
| select_multiple | **name(s)** du/des choix, séparés par un **espace** s'il y en a plusieurs |
| date | Date au format AAAA-MM-JJ. Si nécessaire, préfixez la date avec une apostrophe (') dans Excel pour éviter d'éventuels problèmes de formatage. |

### Définir des réponses par défaut dynamiques

Les réponses par défaut saisies dans le champ `default` doivent être des valeurs fixes. Pour définir une **réponse par défaut dynamique** basée sur une réponse précédente, utilisez les colonnes **calculation** et **trigger** au lieu de la colonne `default` :
1. Dans la colonne `calculation`, saisissez la **référence à la question** qui remplira dynamiquement la réponse par défaut.
2. Dans la colonne `trigger`, saisissez la question qui activera le calcul.
    - En règle générale, il s'agirait de la même question référencée dans la colonne `calculation`, de sorte que toute modification de la question déclencheur mettra également à jour la réponse par défaut.

**Feuille de calcul survey**

| type | name | label | calculation | trigger |
| :--- | :--- | :--- | :--- | :--- |
| text | hh_name | Nom du chef de ménage | | |
| text | phone | Numéro de téléphone du ménage | | |
| text | phone_name | Nom du propriétaire du téléphone | ${hh_name} | ${hh_name} |
| survey |

## Paramètres de question

Les paramètres de question dans XLSForm vous permettent d'affiner le comportement de vos questions au-delà des paramètres de base.

Pour ajouter des paramètres de question dans XLSForm :
1. Ajoutez une colonne **parameters** à la feuille de calcul `survey`.
2. Saisissez le [paramètre](https://support.kobotoolbox.org/question_options_xls.html#common-question-parameters) approprié pour votre type de question.
3. Certains paramètres peuvent être combinés et appliqués à la même question. Combinez les paramètres en les saisissant dans la même cellule et en les séparant par un espace.

**Feuille de calcul survey**

| type | name | label | parameters |
| :--- | :--- | :--- | :--- |
| select_one reasons | reasons | Veuillez sélectionner toutes les raisons qui s'appliquent. | randomize=true |
| range | phone | Veuillez sélectionner un chiffre entre 1 et 5. | start=1 end=5 step=1 |
| survey |

### Paramètres de question courants

Différents types de questions dans `XLSForm` ont différents paramètres. Les paramètres les plus courants sont :

| Paramètre | Type de question | Description |
| :--- | :--- | :--- |
| randomize=true | rank, select_one, select_multiple | Randomise l'ordre des choix d'options |
| start=1 end=5 step=1 | range | Définit la valeur minimale, la valeur maximale et l'intervalle entre les chiffres |
| capture-accuracy=20 | geopoint | Spécifie la précision GPS minimale acceptable (en mètres) pour capturer automatiquement une localisation |
| warning-accuracy=50 | geopoint | Déclenche un message d'avertissement si la précision GPS n'est pas dans le seuil de précision spécifié |
| max-pixels=480 | image | Limite les pixels maximum pour une photo, afin de réduire la taille du fichier image et d'améliorer la vitesse de téléchargement |
| quality=low | audio | Capture un enregistrement audio de qualité inférieure |
| quality=voice-only | audio | Capture l'enregistrement audio de la qualité la plus basse |

## Options de question supplémentaires

Les XLSForms peuvent inclure des colonnes supplémentaires dans la feuille de calcul survey pour des formulaires et des fonctionnalités plus avancés. Quelques-unes sont énumérées ci-dessous.

| Colonne XLSForm | Description |
| :--- | :--- |
| read_only | Si `yes` est saisi dans le champ `read_only`, la question ne peut pas être modifiée par le/la répondant(e). Les champs `read_only` peuvent être combinés avec les champs `default` ou `calculation` pour afficher des informations au/à la répondant(e). |
| trigger | La colonne trigger peut être utilisée pour exécuter un calcul uniquement lorsque la réponse à une autre question visible dans le formulaire est modifiée. Pour plus d'informations, consultez la <a href="https://xlsform.org/en/#trigger">documentation XLSForm</a>. |
| body::accept | Pour limiter les types de fichiers acceptés pour les questions de type `file`, spécifiez les extensions de fichier dans la colonne `body::accept`, séparées par une virgule (par exemple, .pdf, .doc). |

D'autres colonnes peuvent également être ajoutées pour incorporer une logique de formulaire dans votre XLSForm.

<p class="note">
    Pour en savoir plus sur l'ajout de logique de formulaire, consultez <a href="https://support.kobotoolbox.org/skip_logic_xls.html">Ajouter un branchement conditionnel dans XLSForm</a>, <a href="https://support.kobotoolbox.org/constraints_xls.html">Ajouter des contraintes dans XLSForm</a>, <a href="https://support.kobotoolbox.org/required_logic_xls.html">Ajouter une logique obligatoire dans XLSForm</a>, <a href="https://support.kobotoolbox.org/choice_filters_xls.html">Ajouter des filtres de choix dans XLSForm</a>, et <a href="https://support.kobotoolbox.org/calculations_xls.html">Ajouter des calculs dans XLSForm</a>.
</p>