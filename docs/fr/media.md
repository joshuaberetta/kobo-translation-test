# Ajouter des médias à un XLSForm

<iframe src="https://www.youtube.com/embed/7TrVmKIuCa8?si=QCr1IzvDXaASEZg7&cc_lang_pref=fr&hl=fr" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

KoboToolbox vous permet d'ajouter des médias, notamment des **images**, des **fichiers audio** et des **vidéos**, aux notes, questions et choix de votre formulaire. L'ajout de médias peut augmenter l'engagement des utilisateur(rice)s et rendre les formulaires plus accessibles pour les utilisateur(rice)s ayant une déficience visuelle ou des difficultés de lecture.

Les médias au sein du formulaire fonctionnent avec [KoboCollect](../fr/kobocollect_on_android_latest.md) et les [formulaires web Enketo](../fr/enketo.md). Les types de fichiers multimédias suivants sont actuellement pris en charge :

| Média | Fichiers |
| :--- | :--- |
| Image | jpeg, png, svg |
| Audio | aac, aacp, flac, mp3, mp4, mpeg, ogg, wav, webm, x-m4a, x-wav |
| Vidéo | 3gpp, avi, flv, mov, mp4, ogg, quicktime (qtff), webm, wmv |

Cet article couvre les sujets suivants :
- Ajouter des médias aux questions d'enquête
- Ajouter des médias aux choix de réponse
- Ajouter des médias aux traductions de formulaires
- Importer des fichiers multimédias dans KoboToolbox

<p class="note">
    <strong>Note :</strong> L'interface de création de formulaires KoboToolbox <strong>(KoboToolbox Formbuilder)</strong> ne prend pas actuellement en charge l'ajout de fichiers multimédias dans vos formulaires. Pour ajouter des médias, vous devrez utiliser XLSForm puis importer votre XLSForm dans KoboToolbox. Pour en savoir plus sur le téléchargement et la modification de votre formulaire en tant que XLSForm, consultez l'article <a href="../fr/xlsform_with_kobotoolbox.md">Utiliser XLSForm avec KoboToolbox</a>.
<br><br>
Pour une pratique concrète de l'ajout de médias dans XLSForm, consultez le <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">cours XLSForm Fundamentals</a> de la KoboToolbox Academy.
</p>

## Ajouter des médias aux questions dans XLSForm

Pour ajouter des fichiers multimédias aux questions ou aux notes dans votre XLSForm :
1. Ajoutez une nouvelle question dans **l'onglet survey**, en spécifiant le **type**, le **name** et le **label** (facultatif).
    - Utilisez une question de type **note** si vous souhaitez afficher le fichier multimédia sans collecter de données (par exemple, un logo d'organisation ou une vidéo d'introduction).
    - L'ajout d'un libellé est facultatif lors de l'inclusion d'un fichier multimédia.
2. Ajoutez une colonne pour le média que vous souhaitez inclure. Nommez-la `image`, `video` ou `audio`, selon le type de média.
3. Dans la colonne du média, dans la ligne de la question que vous avez ajoutée, saisissez le nom exact du fichier multimédia **y compris l'extension**.
    - Par exemple : `logo.png` ou `intro.mp4`.

**onglet survey**

| type | name | label | image |
| :--- | :--- | :--- | :--- |
| text | Q1 | Avec vos propres mots, comment décririez-vous l'image ci-dessus ? | q1.png |
| survey |

<p class="note">
    <strong>Note :</strong> Auparavant, le format <code>media::file_type</code> était utilisé pour les noms de colonnes de médias (par exemple, <code>media::image</code>, <code>media::video</code>, <code>media::audio</code>). Le format simplifié utilisant uniquement le type de média sans le préfixe <code>media::</code> est désormais plus couramment adopté (par exemple, <code>image</code>, <code>video</code>, <code>audio</code>).
</p>

### Importer des fichiers multimédias dans KoboToolbox

Pour importer les fichiers multimédias dans KoboToolbox :
1. Accédez à votre [compte KoboToolbox](https://www.kobotoolbox.org/sign-up/).
2. Dans votre projet KoboToolbox, accédez à **PARAMÈTRES > Médias**.
3. Importez les fichiers multimédias que vous avez ajoutés à votre XLSForm, en vous assurant que le nom du fichier est exactement le même.
4. Déployez ou redéployez votre formulaire pour voir les changements de médias.

![Importer des fichiers multimédias](images/media/upload_media.png)

## Ajouter des médias aux choix dans XLSForm

Pour ajouter des fichiers multimédias aux choix de réponse dans votre XLSForm :
1. Ajoutez une [question à choix multiple](../fr/question_types_xls.md#questions-à-choix-multiple) dans **l'onglet survey**.
2. Dans **l'onglet choices**, ajoutez un **list_name**, un **name** et un **label** (facultatif) pour vos choix.
    - L'ajout d'un libellé est facultatif lors de l'inclusion d'un fichier multimédia. Si vous souhaitez utiliser les fichiers multimédias comme libellés d'options, omettez le texte du libellé.
3. Ajoutez une colonne pour le média que vous souhaitez inclure. Nommez-la `image`, `video` ou `audio`, selon le type de média.
4. Dans la colonne du média, dans la ligne des choix que vous avez ajoutés, saisissez le nom du fichier multimédia **y compris l'extension**.
    - Par exemple : `goat.png` ou `fish.png`

**onglet survey**

| name | type | label |
| :--- | :--- | :--- |
| select_one animals | animals | Lequel de ces animaux est votre préféré ? |
| survey |

**onglet choices**

| list_name | name | label | image |
| :--- | :--- | :--- | :--- |
| animals | goats | Chèvres | goat.png |
| animals | cows | Vaches | cow.png |
| animals | chicken | Poulets | chicken.png |
| animals | pigs | Cochons | pig.png |
| animals | fish | Poissons | fish.png |
| choices |

### Importer des fichiers multimédias dans KoboToolbox

Pour importer les fichiers multimédias dans KoboToolbox :
1. Accédez à votre [compte KoboToolbox](https://www.kobotoolbox.org/sign-up/).
2. Dans votre projet KoboToolbox, accédez à **PARAMÈTRES > Médias**.
3. Importez les fichiers multimédias que vous avez ajoutés à votre XLSForm, en vous assurant que le nom du fichier est exactement le même.
4. Déployez ou redéployez votre formulaire pour voir les changements de médias.

## Ajouter des médias aux traductions

Dans les XLSForms qui sont [traduits en plusieurs langues](../fr/language_xls.md), vous pouvez inclure différents fichiers multimédias pour chaque langue en ajoutant de nouvelles colonnes **image**, **audio** ou **video**.

Pour ajouter des fichiers multimédias pour différentes langues dans votre onglet survey :

1. Renommez vos colonnes de médias en utilisant le format **type_média::langue (code)**, où `type_média` est le type de fichier multimédia et `langue` est la langue par défaut.
    - Par exemple : `image::English (en)`
2. Ajoutez une nouvelle colonne de média pour chaque langue de traduction en utilisant le format **type_média::langue (code)**.
    - Par exemple : `audio::Spanish (es)`
3. Dans la colonne de média pour chaque langue, saisissez le nom du fichier multimédia que vous souhaitez inclure, y compris l'extension.
    - Pour utiliser le même fichier multimédia pour chaque langue, saisissez le même nom de fichier que celui de la colonne de langue par défaut.

<p class="note">
    <strong>Note :</strong> Si un fichier multimédia n'est pas répertorié dans une colonne de traduction, il ne sera pas affiché pour cette langue.
</p>

**onglet survey**

| type | name | label | video::English (en) | video::Chichewa (ny) |
| :--- | :--- | :--- | :--- | :--- |
| note | intro | Avant de répondre au formulaire, regardez la vidéo ci-dessous : | intro.mp4 | intro_ny.mp4 |
| survey |

### Importer des fichiers multimédias dans KoboToolbox

Pour importer les fichiers multimédias traduits dans KoboToolbox :
1. Accédez à votre [compte KoboToolbox](https://www.kobotoolbox.org/sign-up/).
2. Dans votre projet KoboToolbox, accédez à **PARAMÈTRES > Médias**.
3. Importez les fichiers multimédias que vous avez ajoutés à votre XLSForm, en vous assurant que le nom du fichier est exactement le même.
4. Déployez ou redéployez votre formulaire pour voir les changements de médias.

<p class="note">
    <strong>Note :</strong> Pour en savoir plus sur la gestion des traductions dans XLSForm, consultez l'article <a href="../fr/language_xls.md">Ajouter des traductions dans XLSForm</a>.
</p>

## Résolution de problèmes

<details>
<summary><strong>Erreur lors du déploiement ou de l'affichage du formulaire</strong></summary>
Si vous rencontrez une erreur lors du déploiement ou de l'affichage de votre formulaire, vérifiez les points suivants :
    <ul>
      <li>Le fichier multimédia a été importé dans KoboToolbox dans l'onglet <strong>Médias</strong> de la page <strong>PARAMÈTRES</strong>.</li>
      <li>Le nom du fichier dans votre XLSForm correspond exactement au nom et à l'extension du fichier multimédia.</li>
    </ul>
</details>

<br>

<details>
<summary><strong>Les fichiers multimédias n'apparaissent pas dans le formulaire déployé</strong></summary>
Si les fichiers multimédias n'apparaissent pas dans votre formulaire déployé, vérifiez les points suivants :
    <ul>
      <li>Le fichier multimédia a été importé dans KoboToolbox dans l'onglet <strong>Médias</strong> de la page <strong>PARAMÈTRES</strong>.</li>
      <li>Le nom du fichier dans votre XLSForm correspond exactement au nom et à l'extension du fichier multimédia.</li>
      <li>Le formulaire a été <strong>redéployé</strong> depuis que vous avez importé les fichiers multimédias.</li>
      <li>Vous avez inclus des fichiers multimédias pour chaque traduction du formulaire, le cas échéant.</li>
    </ul>
</details>

<br>

<details>
<summary><strong>Modifier la taille d'un fichier multimédia</strong></summary>
Pour contrôler la taille des images affichées dans vos questions ou choix, vous devez importer des fichiers multimédias avec les dimensions souhaitées. Notez que l'utilisation de fichiers très volumineux peut augmenter les temps de chargement dans les formulaires Enketo.
</details>

<br>

<details>
<summary><strong>Le formulaire met beaucoup de temps à se charger</strong></summary>
Les formulaires Enketo se chargeront lentement si vos fichiers multimédias sont volumineux. Réduisez la taille des fichiers image, vidéo ou audio avant de les importer sur le serveur pour améliorer les temps de chargement.
</details>

<br>

<details>
<summary><strong>Modifier l'alignement des fichiers multimédias</strong></summary>
Les médias dans les formulaires KoboToolbox sont centrés par défaut, et un alignement personnalisé (à gauche ou à droite) n'est pas possible.
</details>

<br>

<details>
<summary><strong>Les fichiers GIF animés ne sont pas pris en charge</strong></summary>
Les fichiers GIF animés ne sont actuellement pas pris en charge par les formulaires web Enketo ni par l'application Android KoboCollect.
</details>

<br>

<details>
<summary><strong>Impossible d'importer un fichier multimédia</strong></summary>
La taille maximale pour les importations de médias est de 100 Mo. Les fichiers dépassant cette limite doivent être réduits en taille avant l'importation.
</details>