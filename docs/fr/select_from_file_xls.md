# Sélectionner des options à partir d'un fichier externe

Les questions **Sélection à partir d'un fichier** vous permettent d'utiliser une liste d'options de choix stockée dans un fichier externe au lieu de les définir directement dans votre formulaire. Il existe deux types : `select_one_from_file` pour sélectionner un **choix unique**, et `select_multiple_from_file` pour sélectionner **plusieurs choix**.

L'utilisation d'un fichier séparé pour votre liste de choix facilite la gestion de longues listes, leur réutilisation dans plusieurs formulaires et la mise à jour des options si nécessaire. Les formats de fichiers pris en charge incluent CSV, XML et GeoJSON.

Cet article explique comment formater votre fichier externe, configurer votre XLSForm pour utiliser des questions de **sélection à partir d'un fichier**, et téléverser votre fichier externe vers KoboToolbox.

<p class="note">
<strong>Remarque :</strong> Cet article se concentre sur l'ajout de questions de sélection à partir d'un fichier dans <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">XLSForm</a>. Pour en savoir plus sur l'ajout de questions de sélection à partir d'un fichier dans l'interface de création de formulaires KoboToolbox (KoboToolbox Formbuilder), consultez <a href="https://support.kobotoolbox.org/external_file.html">Type de question Sélection unique ou multiple à partir d'un fichier externe</a>.
<br><br>
  Pour une pratique concrète des questions de sélection à partir d'un fichier dans XLSForm, consultez le <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">Cours sur les fondamentaux XLSForm</a> de KoboToolbox Academy.
</p>

## Formatage des listes de choix externes

Pour commencer, créez votre liste de choix dans un fichier externe séparé. La structure requise de ce fichier dépend du format que vous choisissez (CSV, XML ou GeoJSON). Utilisez un fichier séparé pour chaque liste de choix.

<p class="note">
  Pour en savoir plus sur le formatage des fichiers XML ou GeoJSON, consultez la documentation <a href="https://xlsform.org/en/#multiple-choice-from-file">XLSForm</a> et <a href="https://docs.getodk.org/form-datasets/#building-selects-from-geojson-files">ODK</a>. Les fichiers GeoJSON sont principalement utilisés pour <a href="https://support.kobotoolbox.org/select_from_map_xls.html">sélectionner des options à partir d'une carte</a>.
</p>

Pour les fichiers CSV, la structure est similaire à la feuille de calcul choices dans un XLSForm. Elle doit inclure les colonnes `name` (nom de l'élément) et `label` (libellé), mais la colonne `list_name` (nom de la liste) n'est pas nécessaire.

**Fichier CSV externe**

| name    | label     |
|:--------|:----------|
| option1 | Option 1  |
| option2 | Option 2  |
| option3 | Option 3  |

Si votre fichier utilise des noms différents pour le nom et le libellé du choix, vous pouvez le spécifier dans votre XLSForm (voir les instructions [ci-dessous](https://support.kobotoolbox.org/select_from_file_xls.html#configuring-choice-name-and-label-columns)).

<p class="note">
<strong>Remarque :</strong> Utilisez des noms de fichiers courts et simples pour vos fichiers externes, en évitant les espaces ou les caractères spéciaux. Le nom du fichier sera utilisé dans votre XLSForm pour lier les questions à leurs listes de choix. Si vous utilisez plusieurs fichiers externes, assurez-vous que chacun porte un nom unique, même s'ils utilisent des types de fichiers différents.
</p>

## Configuration de votre XLSForm

Pour ajouter une question de sélection à partir d'un fichier à votre XLSForm :
1. Dans la colonne `type` de la feuille de calcul `survey`, saisissez le type de question de sélection à partir d'un fichier (`select_one_from_file` ou `select_multiple_from_file`).
2. Dans la même cellule, au lieu du `list_name` (nom de la liste) des choix, ajoutez un espace simple et le nom du fichier externe, y compris l'extension du fichier.
    - Par exemple : `select_one_from_file households.csv`

**Feuille de calcul survey**

| type                     | name | label           |
|:-------------------------|:-----|:----------------|
| select_one_from_file households.csv | hh   | Sélectionner un ménage |

### Configuration des colonnes de nom et de libellé des choix

Si votre fichier externe utilise des noms de colonnes différents au lieu de `name` et `label` :
1. Ajoutez une colonne **parameters** à la feuille de calcul `survey`
2. Dans la ligne de la question de sélection à partir d'un fichier, spécifiez les noms personnalisés avec les paramètres `value` et `label`.
    - `value` représente le **nom** du choix.
    - `label` représente le **libellé** du choix.

**Feuille de calcul survey**

| type                     | name | label            | parameters                   |
|:-------------------------|:-----|:-----------------|:-----------------------------|
| select_one_from_file households.csv | hh   | Sélectionner un ménage | value=housenum label=housename |

## Téléversement du fichier externe vers KoboToolbox

Lors du téléversement de votre XLSForm vers KoboToolbox, vous devez également téléverser le fichier externe qui contient votre liste de choix :
1. Dans KoboToolbox, accédez à la page **PARAMÈTRES** du projet.
2. Dans l'onglet **Médias**, téléversez le fichier externe. Assurez-vous que le nom du fichier correspond exactement au nom de fichier spécifié dans le XLSForm.

Pour mettre à jour votre liste de choix, modifiez le fichier externe selon vos besoins, téléversez-le à nouveau vers KoboToolbox et redéployez votre formulaire.

![Téléverser un média](images/select_from_file_xls/upload_media.png)

## Dépannage

<details>
  <summary><strong>Listes de choix traduites</strong></summary>
  Les questions de sélection à partir d'un fichier ne prennent actuellement pas en charge les <a href="https://support.kobotoolbox.org/language_xls.html">listes de choix traduites</a>. Votre fichier de choix externe ne peut inclure qu'une seule colonne <code>label</code>. Toute colonne <code>label</code> traduite supplémentaire sera ignorée dans Enketo ou provoquera une erreur dans KoboCollect. Pour les formulaires qui incluent des traductions, utilisez plutôt des listes de choix internes, ou configurez plusieurs questions de <strong>sélection à partir d'un fichier</strong> en utilisant un branchement conditionnel pour extraire des fichiers différents selon la langue du formulaire.
</details>