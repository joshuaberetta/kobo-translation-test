# Ajouter une logique de saut à un tableau de questions

Dans la plupart des cas, vous pouvez ajouter une logique de saut à n'importe quel type de question comme indiqué dans l'article d'aide **[Ajouter une logique de saut dans le Formbuilder](skip_logic.md)**. Cependant, lorsque vous travaillez dans l'interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)**, l'ajout d'une logique de saut à un tableau de questions n'est pas encore possible. À la place, un XLSForm peut être utilisé pour mettre en œuvre une logique de saut pour ce type de question. Cet article d'aide illustre comment vous pouvez ajouter une logique de saut à un tableau de questions en utilisant XLSForm.

Si vous avez consulté l'article d'aide **[Ajouter une matrice de questions avec le Formbuilder](matrix_response.md)**, vous savez déjà qu'il existe 2 approches pour créer un tableau de questions dans KoboToolbox : l'_approche Formbuilder_ et l'_approche `kobo--matrix_list`_. Cet article d'aide donne un aperçu des étapes nécessaires pour ajouter une logique de saut à un tableau de questions en utilisant l'une ou l'autre de ces approches.

## L'approche Formbuilder :

Cette approche fonctionne avec **Enketo**, également connu sous le nom de **formulaires web**, en utilisant le **thème de grille**. Elle peut ne pas fonctionner comme prévu si vous ignorez les paramètres du **thème de grille** comme indiqué dans l'article d'aide **[Styliser vos formulaires web dans le Formbuilder](alternative_enketo.md)**.

Suivez les étapes décrites ci-dessous pour ajouter une logique de saut à un tableau de questions en utilisant l'approche Formbuilder.

**Étape 1 :** Créer un tableau de questions dans le Formbuilder :

La première étape consiste à créer un tableau de questions dans le Formbuilder comme indiqué dans l'article d'aide **[Ajouter une matrice de questions avec le Formbuilder](matrix_response.md)**. Ajoutez simplement des lignes et des colonnes avec les variables pour lesquelles vous avez l'intention de collecter des données.

**Étape 2 :** Télécharger le formulaire en tant que XLSForm :

Une fois le tableau de questions prêt, **SAUVEGARDEZ** le formulaire puis [téléchargez-le en tant que XLSForm](getting_started_xlsform.md#downloading-an-xlsform-from-kobotoolbox).

**Étape 3 :** Ajouter l'en-tête de colonne relevant et la logique de saut à votre XLSForm :

Ouvrez maintenant le XLSForm puis ajoutez l'en-tête de colonne `relevant` au XLSForm. Une fois que vous avez l'en-tête de colonne `relevant`, vous pourrez ajouter une logique de saut à toutes les questions selon vos besoins.

Pour améliorer la façon dont les tableaux de questions sont affichés lors de la réponse, il est conseillé d'ajouter une question de type `note` (surlignée en jaune dans l'image ci-dessous) puis d'y inclure une logique de saut selon les besoins. Ceci est entièrement facultatif car cela affectera simplement le formatage du tableau de questions. La différence entre _utiliser_ et _ne pas utiliser_ la question de type `note` est illustrée ci-dessous dans **Étape 6 : Collecter des données**.

![XLSForm approche Formbuilder](images/adding_skip_to_matrix/formbuilder_xlsform.png)

**Étape 4 :** Remplacer le XLSForm :

Importez et remplacez votre XLSForm dans le projet existant, ou créez un nouveau projet (si nécessaire).

**Étape 5 :** Déployer le formulaire :

Une fois que vous avez remplacé le XLSForm (ou importé le XLSForm en tant que nouveau projet), vous devrez déployer votre formulaire.

**Étape 6 :** Collecter des données :

Après avoir déployé le formulaire, vous pouvez aller dans **onglet FORMULAIRE>Collecte de données>OUVRIR** pour commencer à collecter des données avec le formulaire web.

**Écran de saisie de données tel qu'il apparaît dans Enketo (formulaire web) : _lorsque rien n'est saisi_.**

![Formulaire Enketo vide approche Formbuilder](images/adding_skip_to_matrix/formbuilder_enketo_form_empty.png)

**Écran de saisie de données tel qu'il apparaît dans Enketo (formulaire web) avec la question de type `note` ajoutée : _lorsque le tableau de questions est rempli_.**

![Formulaire Enketo rempli approche Formbuilder](images/adding_skip_to_matrix/formbuilder_enketo_form_filled_no_issue.png)

Comme vous pouvez le voir dans l'image ci-dessus, le format du tableau de questions n'a pas été déformé. C'est ainsi que le tableau sera affiché lorsque vous utilisez la question de type `note` qui a été surlignée dans l'image partagée précédemment.

**Écran de saisie de données tel qu'il apparaît dans Enketo (formulaire web) sans la question de type `note` ajoutée : _lorsque le tableau de questions est rempli_.**

![Formulaire Enketo rempli approche Formbuilder](images/adding_skip_to_matrix/formbuilder_enketo_form_filled_with_issue.png)

Dans ce cas, le format du tableau de questions a été déformé. C'est le tableau qui sera affiché lorsque la question de type `note` n'est pas utilisée.

<p class="note">
  Vous pouvez accéder au XLSForm
  <a
    download
    class="reference"
    href="./_static/files/adding_skip_to_matrix/adding_skip_to_a_matrix_question.xls"
    >ici</a
  >
  qui a été utilisé pour cette approche
  <em
    >(ajouter une logique de saut à un tableau de questions en utilisant l'approche Formbuilder)</em
  >.
</p>

## Approche `kobo--matrix_list` :

Tout comme avec l'approche Formbuilder, cette méthode d'ajout de logique de saut avec un XLSForm fonctionne avec **Enketo** en utilisant le **thème de grille**.

Suivez les étapes ci-dessous pour ajouter une logique de saut à un tableau de questions avec un XLSForm en utilisant l'approche `kobo--matrix_list`.

**Étape 1 :** Créer un tableau de questions dans le XLSForm :

Créez un tableau de questions dans le XLSForm, comme indiqué dans l'article d'aide **[Ajouter une matrice de questions avec le Formbuilder](matrix_response.md)**.

**Étape 2 :** Ajouter l'en-tête de colonne `relevant` et la logique de saut à votre XLSForm :

Une fois le tableau de questions prêt, vous devez ajouter l'en-tête de colonne `relevant`. Vous pouvez maintenant ajouter une logique de saut à toutes les questions sous l'en-tête de colonne `relevant`.

![XLSForm approche kobo_matrix](images/adding_skip_to_matrix/kobo_matrix_xlsform.png)

**Étape 3 :** Importer le XLSForm :

Si votre XLSForm est prêt, importez-le en tant que nouveau projet.

**Étape 4 :** Déployer le formulaire :

Une fois que vous avez importé le XLSForm, vous devrez déployer votre formulaire.

**Étape 5 :** Collecter des données :

Vous pouvez maintenant aller dans **onglet FORMULAIRE>Collecte de données>OUVRIR** pour commencer à collecter des données.

**Écran de saisie de données tel qu'il apparaît dans Enketo (formulaire web) : _lorsque rien n'est saisi_.**

![Formulaire Enketo vide approche kobo_matrix](images/adding_skip_to_matrix/kobo_matrix_enketo_form_empty.png)

**Écran de saisie de données tel qu'il apparaît dans Enketo (formulaire web) : _lorsque le tableau de questions est rempli_.**

![Formulaire Enketo rempli approche kobo_matrix](images/adding_skip_to_matrix/kobo_matrix_enketo_form_filled.png)

Comme vous pouvez le voir dans la deuxième image, le format du tableau de questions a été déformé. Dans l'approche `kobo--matrix_list`, vous n'avez pas la possibilité de corriger le tableau comme vous l'aviez avec l'approche Formbuilder.

<p class="note">
  Vous pouvez accéder au XLSForm
  <a
    download
    class="reference"
    href="./_static/files/adding_skip_to_matrix/adding_skip_to_a_matrix_question_kobo_matrix.xls"
    >ici</a
  >
  qui a été utilisé pour cette approche
  <em
    >(ajouter une logique de saut à un tableau de questions en utilisant l'approche
    <code>kobo--matrix_list</code>)</em
  >.
</p>