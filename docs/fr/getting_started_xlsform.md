# Débuter avec XLSForm

<iframe src="https://www.youtube.com/embed/xpeBCy9p1Ys?si=tP_3G2vMnRC1OgWS&cc_lang_pref=fr&hl=fr" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Lors de la création de formulaires d'enquête avec KoboToolbox, vous pouvez construire votre formulaire avec l'[interface de création de formulaires KoboToolbox (KoboToolbox Formbuilder)](https://support.kobotoolbox.org/formbuilder.html) ou en utilisant XLSForm. XLSForm est très efficace pour créer des formulaires de base et avancés dans un format convivial.

<p class="note">
  Pour plus d'informations sur XLSForm, consultez <a class="reference" href="https://support.kobotoolbox.org/edit_forms_excel.html">Introduction à XLSForm</a>. Pour une introduction complète au développement de formulaires en utilisant XLSForm, nous recommandons <a class="reference" href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">le cours en ligne à votre rythme XLSForm Fundamentals de KoboToolbox Academy</a>.
</p>

Cet article explique comment configurer un XLSForm en utilisant Microsoft Excel ou d'autres tableurs, notamment :

- Configurer la structure de base de votre XLSForm
- Ajouter des questions et des choix d'options
- Ajouter des paramètres de formulaire et des colonnes optionnelles
- Importer et prévisualiser votre XLSForm dans KoboToolbox

<p class="note">
  <b>Remarque :</b> Certaines fonctionnalités XLSForm ne sont actuellement pas disponibles dans l'interface de création de formulaires, mais les formulaires KoboToolbox peuvent être téléchargés, modifiés en XLSForm et <a class="reference" href="https://support.kobotoolbox.org/xlsform_with_kobotoolbox.html">importés à nouveau dans KoboToolbox</a>.
</p>

## Configurer un XLSForm

Pour configurer la structure de base d'un XLSForm :

1. Créez un classeur dans votre tableur préféré.
2. Créez trois feuilles de calcul : **survey**, **choices** et **settings**.
   - Les noms des feuilles de calcul doivent être en lettres minuscules uniquement.
3. Dans la feuille de calcul **survey**, créez trois colonnes avec les en-têtes : `type`, `name` et `label`.
4. Dans la feuille de calcul **choices**, créez trois colonnes avec les en-têtes : `list_name`, `name` et `label`.
5. La feuille de calcul **settings** est optionnelle. Elle peut être utilisée pour inclure des spécifications et des personnalisations supplémentaires du formulaire.
   - Par exemple : `form_title`, `style` et `default_language`.

<p class="note">
Pour débuter avec XLSForm, téléchargez un exemple d'XLSForm <a class="reference" href="https://support.kobotoolbox.org/_static/files/getting_started_xlsform/sample_xlsform.xlsx">ici</a>.
</p>

### Colonnes obligatoires dans XLSForm

Les colonnes suivantes sont obligatoires dans XLSForm :

**Feuille de calcul survey**

| Nom de colonne | Description |
| --- | --- |
| type | Définit le type de question (par exemple, text, integer, select_one) |
| name | Définit un nom court et unique pour faire référence à chaque question |
| label | Définit le texte de la question tel qu'il sera affiché dans le formulaire |

**Feuille de calcul choices**

| Nom de colonne | Description |
| --- | --- |
| list_name | Définit l'identifiant unique pour une liste de choix d'options |
| name | Définit un nom court et unique pour faire référence à chaque choix d'option |
| label | Définit le texte du choix tel qu'il sera affiché dans le formulaire |

## Ajouter des questions

Dans XLSForm, les questions sont ajoutées dans la feuille de calcul **survey**. Pour ajouter des questions dans XLSForm :

1. Dans la colonne `type` de la feuille de calcul `survey`, saisissez le [type de question](https://support.kobotoolbox.org/question_types_xls.html) de la question que vous souhaitez ajouter.
2. Dans la colonne `name`, saisissez un nom utilisé pour identifier la question.
   - Chaque question doit avoir un nom unique et ne peut pas contenir d'espaces ou de symboles (sauf les traits de soulignement).
3. Dans la colonne `label`, saisissez le texte de la question tel qu'il doit être affiché dans le formulaire lors de la collecte de données.

**Feuille de calcul survey**

| type | name | label |
| :--- | :--- | :--- |
| text | yourname | Quel est votre nom ? |
| survey |

4. Si vous ajoutez des **questions de type select** (`select_one`, `select_multiple` ou `rank`) : dans la colonne `type`, après le type de question, ajoutez un espace et saisissez le nom de la liste de choix.
   - Le nom de la liste de choix est défini ultérieurement dans la feuille de calcul `choices` en tant que `list_name`.

**Feuille de calcul survey**

| type | name | label |
| :--- | :--- | :--- |
| select_one sex | baby_sex | Quel est le sexe de votre bébé ? |
| survey |

<p class="note">
Pour en savoir plus sur les types de questions dans XLSForm, consultez <a class="reference" href="https://support.kobotoolbox.org/question_types_xls.html">Types de questions dans XLSForm</a>.
</p>

## Ajouter des choix d'options

Pour les questions de type select, les choix d'options sont ajoutés dans la feuille de calcul **choices**. Pour ajouter des choix d'options dans XLSForm :

1. Dans la colonne `list_name` de la feuille de calcul `choices`, saisissez le nom de la **liste de choix d'options**.
   - Le `list_name` est un identifiant unique pour une liste de choix d'options. Il doit correspondre au nom de liste saisi dans la colonne `type` de la feuille de calcul `survey`.
2. Dans la colonne `name`, ajoutez un nom court pour chaque choix d'option.
   - Chaque choix au sein d'une liste doit avoir un `name` unique, qui ne peut pas contenir d'espaces ou de symboles (sauf les traits de soulignement).
3. Dans la colonne `label`, saisissez le texte du choix tel qu'il doit être affiché dans le formulaire lors de la collecte de données.

**Feuille de calcul choices**

| list_name | name | label |
| :--- | :--- | :--- |
| sex | male | Masculin |
| sex | female | Féminin |
| choices |

<p class="note">
Pour en savoir plus sur la gestion des choix d'options dans XLSForm, consultez <a class="reference" href="https://support.kobotoolbox.org/option_choices_xls.html">Gestion des choix d'options dans XLSForm</a>.
</p>

## Ajouter des paramètres

Il existe de nombreux paramètres optionnels qui peuvent être ajoutés à la feuille de calcul **settings** dans XLSForm.

Les paramètres de formulaire courants incluent :

| Paramètre | Description |
| --- | --- |
| form_title | Titre affiché en haut du formulaire |
| default_language | Langue par défaut du formulaire |
| style | Thèmes pour les formulaires web Enketo |
| version | ID de version du formulaire |

Par exemple, pour ajouter un titre de formulaire :

1. Ajoutez une colonne dans la feuille de calcul settings nommée `form_title`.
2. Saisissez le titre du formulaire dans la colonne `form_title`.

<p class="note">
<b>Remarque :</b> Tous les paramètres de formulaire sont optionnels. Si vous ne définissez pas de titre de formulaire dans votre XLSForm, le nom du fichier Excel sera utilisé comme nom de projet dans KoboToolbox par défaut. Cela peut être modifié dans KoboToolbox.
</p>

**Feuille de calcul settings**

| form_title |
| :--- |
| Débuter avec <br> XLSForm |
| settings |

<p class="note">
Pour en savoir plus sur la feuille de calcul settings dans XLSForm, consultez <a class="reference" href="https://support.kobotoolbox.org/form_settings_xls.html">Paramètres de formulaire dans XLSForm</a>.
</p>

## Ajouter des colonnes optionnelles à la feuille de calcul survey

Pour personnaliser davantage votre XLSForm, vous pouvez ajouter des colonnes optionnelles pour configurer la logique du formulaire, les options de questions et les paramètres avancés. Les colonnes optionnelles courantes incluent :

| Nom de colonne | Description |
| --- | --- |
| hint | Indice de question |
| guidance_hint | Instructions supplémentaires |
| required | Option pour rendre une question obligatoire |
| relevant | Conditions de branchement conditionnel pour la question |
| constraint | Critères de validation pour la question |
| constraint_message | Message d'erreur lorsque les critères de validation ne sont pas respectés |
| appearance | Options pour l'affichage des questions |
| choice_filter | Critères pour la sélection en cascade |
| parameters | Paramètres pour des types de questions spécifiques |
| calculation | Expression mathématique pour la question de calcul |
| default | Réponse par défaut pour une question |

<p class="note">
Pour en savoir plus sur les colonnes optionnelles dans XLSForm, consultez <a class="reference" href="https://support.kobotoolbox.org/question_options_xls.html">Utilisation des options de questions dans XLSForm</a>, <a class="reference" href="https://support.kobotoolbox.org/appearances_xls.html">Apparences de questions dans XLSForm</a> et <a class="reference" href="https://support.kobotoolbox.org/form_logic_xls.html">Introduction à la logique de formulaire dans XLSForm</a>.
</p>

## Importer et prévisualiser votre XLSForm dans KoboToolbox

Une fois que vous avez terminé de développer votre XLSForm, vous pouvez l'importer et le prévisualiser dans KoboToolbox :

1. Accédez à la page d'accueil **Projet** dans KoboToolbox et cliquez sur **NOUVEAU**.
2. Sélectionnez **Importer un XLSForm** et importez votre fichier XLSForm.
3. Saisissez les détails du projet et cliquez sur **CRÉER UN PROJET**.
4. Cliquez sur le bouton <i class="k-icon k-icon-view"></i> **Aperçu**.

Si votre XLSForm contient une erreur, un message d'erreur apparaîtra, indiquant généralement la ligne, la question ou l'expression exacte où se trouve le problème. Après avoir corrigé l'erreur dans votre XLSForm, vous devrez importer à nouveau le fichier.

<p class="note">
Pour apprendre comment télécharger un XLSForm depuis KoboToolbox, importer votre XLSForm via une URL et utiliser KoboToolbox pour valider et tester votre XLSForm, consultez <a class="reference" href="https://support.kobotoolbox.org/xlsform_with_kobotoolbox.html">Utilisation d'XLSForm avec KoboToolbox</a>.
</p>