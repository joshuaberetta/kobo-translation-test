# Verrouillage de bibliothèque avec XLSForm

[La bibliothèque KoboToolbox](https://support.kobotoolbox.org/question_library.html) vous permet de stocker et de gérer des modèles, des questions et des blocs pour les réutiliser dans plusieurs projets. Les modèles de formulaires dans **La bibliothèque** peuvent être partagés avec les membres de l'équipe pour garantir une conception de formulaire cohérente et réduire la duplication des efforts.

Le **verrouillage de bibliothèque** étend cette fonctionnalité en vous permettant de contrôler comment les modèles peuvent être modifiés une fois qu'ils sont utilisés pour créer de nouveaux projets. Avec le verrouillage, vous pouvez spécifier quelles questions, groupes ou paramètres au niveau du formulaire peuvent être modifiés. Cela est particulièrement utile pour les grandes équipes travaillant à partir d'un modèle partagé, où certains éléments doivent rester fixes tandis que d'autres peuvent être adaptés aux besoins locaux.

Cet article explique comment fonctionne le verrouillage de bibliothèque, les types de restrictions que vous pouvez appliquer, comment les configurer dans XLSForm et comment téléverser des XLSForms verrouillés dans KoboToolbox.

<p class="note">
<strong>Remarque :</strong> Le verrouillage de bibliothèque n'est actuellement pas pris en charge dans l'interface de création de formulaires KoboToolbox (KoboToolbox Formbuilder). Pour utiliser cette fonctionnalité, vous devez l'implémenter via XLSForm, puis téléverser votre XLSForm dans KoboToolbox.
<br><br>
Pour en savoir plus sur le téléchargement et la modification de votre formulaire en tant que XLSForm, consultez <a href="https://support.kobotoolbox.org/xlsform_with_kobotoolbox.html">Utiliser XLSForm avec KoboToolbox</a>.
</p>

## Introduction au verrouillage de bibliothèque

Le verrouillage de bibliothèque contrôle quelle partie d'un formulaire **peut être modifiée** lorsqu'un projet est créé à partir d'un modèle de La bibliothèque. Les restrictions sont définies dans votre XLSForm avant de téléverser le formulaire.

Lorsque vous créez un modèle verrouillé et le partagez via votre bibliothèque :
- Les utilisatrices et utilisateurs peuvent effectuer des ajustements locaux là où les restrictions le permettent.
- Les éléments verrouillés apparaissent **grisés** dans l'interface de création de formulaires.
- Un message au-dessus du formulaire indique quelles restrictions sont actives.

Le verrouillage de bibliothèque est distinct des [autorisations de projet](https://support.kobotoolbox.org/managing_permissions.html), qui contrôlent ce que différentes utilisatrices et différents utilisateurs peuvent faire à l'intérieur d'un projet déployé.

<p class="note">
<strong>Remarque :</strong> Les restrictions de verrouillage de bibliothèque s'appliquent uniquement dans <strong>l'interface de création de formulaires</strong> lorsqu'un projet est créé à partir d'un modèle verrouillé. Si le XLSForm est téléchargé et modifié dans un tableur, les restrictions n'empêcheront pas les modifications. Cependant, des configurations de verrouillage incorrectes ou invalides peuvent causer des erreurs lorsque le formulaire est retéléversé.
</p>

Le verrouillage de bibliothèque est configuré dans trois feuilles de calcul XLSForm :
- **Feuille survey :** Pour appliquer des restrictions à des questions et groupes spécifiques.
- **Feuille settings :** Pour appliquer des restrictions au niveau du formulaire et définir l'option `kobo--lock_all`.
- **Feuille kobo--locking-profiles :** Pour définir des profils qui regroupent des restrictions connexes.

Ensemble, ces feuilles de calcul vous permettent de définir quelles parties d'un formulaire restent fixes et quelles parties peuvent être modifiées lorsque le modèle est utilisé pour créer de nouveaux projets.

## Types de restrictions

Le verrouillage de bibliothèque prend en charge les restrictions à trois niveaux : **question**, **groupe** et **formulaire**. Les restrictions définissent ce qui peut et ne peut pas être modifié lorsqu'un projet est créé à partir d'un modèle verrouillé.

De plus, un paramètre global (`kobo--lock_all`) peut être utilisé pour verrouiller l'ensemble du formulaire.

### Restrictions au niveau des questions

Les restrictions au niveau des questions s'appliquent aux questions individuelles. Vous pouvez appliquer les restrictions suivantes aux questions dans votre XLSForm :

| Restriction              | Description                                                                      |
|:------------------------------|:---------------------------------------------------------------------------------------------------------------|
| <code>choice_add</code>                 | Empêche l'ajout de nouveaux choix à une question de type **select**.                                                             |
| <code>choice_delete</code>              | Empêche la suppression de choix existants dans une question de type **select**.                                                      |
| <code>choice_value_edit</code>          | Empêche la modification d'un nom de choix (ou valeur XML).                                                                |
| <code>choice_label_edit</code>          | Empêche la modification d'un libellé de choix.                                                                              |
| <code>choice_order_edit</code>          | Empêche la réorganisation des choix dans une question de type **select**.                                                             |
| <code>question_delete</code>            | Empêche la suppression d'une question.                                                                                 |
| <code>question_label_edit</code>        | Empêche la modification d'un libellé de question ou d'une indication.                                                                    |
| <code>question_settings_edit</code>     | Empêche la modification des paramètres de question, y compris le nom de la question. Cela n'inclut pas le branchement conditionnel ou les critères de validation. |
| <code>question_skip_logic_edit</code>   | Empêche la modification des conditions de branchement conditionnel.                                                                       |
| <code>question_validation_edit</code>   | Empêche la modification des critères de validation.                         |

### Restrictions au niveau des groupes

Les restrictions au niveau des groupes s'appliquent aux [groupes de questions](https://support.kobotoolbox.org/grouping_questions_xls.html). Vous pouvez appliquer les restrictions suivantes aux groupes dans votre XLSForm :

| Nom | Description |
|:------|:-------------|
| <code>group_delete</code> | Empêche la suppression d'un groupe. |
| <code>group_split</code> | Empêche le dégroupement de questions. |
| <code>group_label_edit</code> | Empêche la modification du libellé du groupe. |
| <code>group_question_add</code> | Empêche l'ajout ou le clonage de questions à l'intérieur d'un groupe. |
| <code>group_question_delete</code> | Empêche la suppression de questions à l'intérieur d'un groupe. |
| <code>group_question_order_edit</code> | Empêche la réorganisation des questions à l'intérieur d'un groupe. |
| <code>group_settings_edit</code> | Empêche la modification des paramètres du groupe, y compris le nom du groupe. Cela n'inclut pas le branchement conditionnel. |
| <code>group_skip_logic_edit</code> | Empêche la modification du branchement conditionnel pour un groupe. |

### Restrictions au niveau du formulaire

Les restrictions au niveau du formulaire s'appliquent à l'ensemble du formulaire. Vous pouvez appliquer les restrictions suivantes à votre XLSForm :

| Nom | Description |
|:------|:-------------|
| <code>form_appearance</code> | Empêche les modifications du [thème](https://support.kobotoolbox.org/form_style_xls.html) du formulaire. |
| <code>form_replace</code> | Empêche le remplacement du formulaire dans KoboToolbox en utilisant l'option <i class="k-icon k-icon-replace"></i> **Remplacer le formulaire**. |
| <code>group_add</code> | Empêche la création de nouveaux groupes. |
| <code>question_add</code> | Empêche l'ajout ou le clonage de questions dans un groupe. |
| <code>question_order_edit</code> | Empêche la réorganisation des questions. |
| <code>language_edit</code> | Empêche la modification des traductions. |
| <code>form_meta_edit</code> | Empêche la modification des questions de [métadonnées](https://support.kobotoolbox.org/metadata_xls.html). |

### Verrouillage d'un formulaire entier

Le paramètre `kobo--lock_all` peut être ajouté à la feuille **settings** de votre XLSForm.
- S'il est défini sur **TRUE**, l'ensemble du formulaire est verrouillé et toutes les restrictions granulaires deviennent redondantes.
- S'il est défini sur **FALSE** (ou omis), seules les restrictions définies dans vos profils de verrouillage sont appliquées.

**Feuille settings**

|   kobo--lock_all       |
|:----------------- |
|   TRUE  |

## Configuration du verrouillage de bibliothèque dans XLSForm

### Définition des profils de verrouillage

Les profils de verrouillage sont des **ensembles de restrictions** qui peuvent être appliqués aux questions, aux groupes ou à l'ensemble du formulaire. Ils sont définis dans la feuille **kobo--locking-profiles** du XLSForm, puis appliqués dans les feuilles **survey** et **settings**. Vous pouvez créer autant de profils que nécessaire.

Pour définir des profils de verrouillage dans votre XLSForm :
1. Créez une nouvelle feuille de calcul nommée **kobo--locking-profiles.**
2. Ajoutez une **colonne restriction**, qui peut inclure toutes les restrictions des tableaux ci-dessus.
3. Créez une colonne par **profil** (par exemple, `profile_1`, `profile_2`).
4. Dans la cellule correspondant à une **restriction** et à un **profil**, incluez le mot-clé `locked` pour attribuer une restriction à un profil.

**Feuille kobo--locking-profiles**

| restriction         | profile_1 | profile_2 | profile_3 |
|:-------------------|:----------|:----------|:----------|
| choice_add          | locked    | locked    |           |
| choice_delete       |           | locked    |           |
| choice_value_edit   | locked    | locked    |           |
| choice_label_edit   |           | locked    |           |
| choice_order_edit   |           | locked    |           |
| question_delete     | locked    | locked    |           |
| form_appearance     |           |           | locked    |

### Application des profils dans la feuille survey

Une fois que vous avez défini des profils de verrouillage dans la feuille **kobo--locking-profiles**, vous pouvez appliquer ces profils à des questions et groupes spécifiques. Pour appliquer des profils dans la feuille `survey` :

1. Créez une colonne nommée **kobo--locking-profile** dans la feuille `survey`
2. Pour chaque question ou groupe que vous souhaitez restreindre, définissez le profil de verrouillage dans la colonne `kobo--locking-profile`.

**Feuille survey**

| type                     | name    | label              | kobo--locking-profile |
|:-------------------------|:--------|:------------------|:--------------------|
| select_one country        | country | Sélectionnez votre pays | profile_1           |
| select_one city           | city    | Sélectionnez votre ville   | profile_2           |

### Application des profils dans la feuille settings

En plus d'appliquer des profils aux questions et groupes dans la feuille `survey`, vous pouvez également appliquer un profil avec des restrictions au niveau du formulaire dans la feuille `settings`.

Pour appliquer un profil à la feuille `settings` :
1. Créez une colonne **kobo--locking-profile** dans la feuille `settings`.
2. Spécifiez le profil que vous souhaitez appliquer.

**Feuille settings**

| kobo--locking-profile |
|:---------------------|
| profile_3            |

<p class="note">
<strong>Remarque :</strong> Les restrictions ne peuvent pas être appliquées dans la feuille <code>choices</code>. Toutes les restrictions liées aux choix sont définies au niveau de la question ou du groupe dans la feuille <code>survey</code>.
</p>

## Utilisation de modèles verrouillés dans KoboToolbox

Une fois que vous avez créé et téléversé un XLSForm verrouillé en tant que modèle, vous pouvez l'utiliser pour créer de nouveaux projets dans KoboToolbox.

### Importation d'un XLSForm verrouillé dans votre bibliothèque

Pour importer un XLSForm verrouillé dans votre bibliothèque :
1. Accédez à votre <i class="k-icon k-icon-library"></i> **Bibliothèque** depuis la barre de menu de gauche dans KoboToolbox.
2. Cliquez sur **NOUVEAU**, puis sélectionnez **Importer**.
3. Téléversez votre fichier XLSForm et sélectionnez **Importer en tant que modèle.**

![Téléverser un modèle](images/library_locking/upload_template.png)

Le modèle apparaîtra dans votre bibliothèque avec un <i class="k-icon k-icon-template-locked"></i> **symbole de cadenas**, indiquant qu'il contient des restrictions.

### Création d'un projet à partir d'un modèle verrouillé

1. Accédez à la page d'accueil **Projets**.
2. Cliquez sur **NOUVEAU**, puis sélectionnez **Utiliser un modèle.**
3. Choisissez le modèle verrouillé que vous souhaitez utiliser.
4. Continuez à créer votre projet comme d'habitude.

![Utiliser un modèle](images/library_locking/use_template.png)

Lorsque vous ouvrez le projet dans l'interface de création de formulaires :
- Un message apparaîtra au-dessus de la première question résumant les restrictions.
- Les questions, groupes ou paramètres au niveau du formulaire verrouillés apparaîtront **grisés.**
- Chaque question verrouillée indique quel profil a été appliqué dans ses **Paramètres > Fonctionnalités verrouillées.**

![Bibliothèque verrouillée](images/library_locking/locked.png)

## Dépannage

<details>
  <summary><strong>Recommandations de dépannage</strong></summary>
  Si le verrouillage de bibliothèque ne fonctionne pas comme prévu, essayez ce qui suit :
    <ul>
  <li>Assurez-vous que le formulaire a été téléversé en tant que <strong>Modèle dans La bibliothèque.</strong></li>
  <li>Vérifiez la feuille <strong>settings</strong> dans votre XLSForm. Si <code>kobo--lock_all</code> est défini sur <code>true</code>, l'ensemble du formulaire sera verrouillé.</li>
  <li>Vérifiez que tous les noms de restriction dans la feuille <code>kobo--locking-profiles</code> sont valides. Seuls les noms de restriction prédéfinis sont pris en charge.</li>
  <li>Assurez-vous que la colonne <code>kobo--locking-profile</code> existe dans la feuille <strong>survey</strong> ou <strong>settings</strong> et que les noms de profil correspondent à ceux définis dans la feuille <code>kobo--locking-profiles</code>.</li>
</ul>
</details>

<br>

<details>
  <summary><strong>Mises en garde et limitations</strong></summary>
  <ul>
  <li>Les restrictions sont appliquées uniquement dans <strong>l'interface de création de formulaires.</strong> Si le XLSForm est téléchargé et modifié directement dans un tableur, les restrictions n'empêchent pas les modifications.</li>
  <li>Les restrictions s'appliquent uniquement aux projets créés à partir de modèles verrouillés. Les modèles et formulaires dans La bibliothèque restent modifiables.</li>
  <li>Seuls les formulaires et les modèles prennent en charge le verrouillage. Si vous téléversez un XLSForm verrouillé en tant que question ou bloc, le verrouillage est ignoré.</li>
  <li>Certains éditeurs de tableur convertissent automatiquement deux tirets simples <code>--</code> en un tiret long (—). Utilisez toujours deux tirets simples dans les noms tels que <code>kobo--locking-profiles</code>.</li>
</ul>

</details>