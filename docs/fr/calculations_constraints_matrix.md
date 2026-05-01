# Ajouter des calculs et des contraintes dans un tableau de questions

Lorsque vous travaillez dans l'interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)**, il est simple d'[ajouter des calculs](calculate_questions.md) ou des [contraintes](validation_criteria.md) à presque tous les types de questions. Bien que le Formbuilder ne prenne pas actuellement en charge l'ajout de ces fonctionnalités à un tableau de questions, vous pouvez utiliser XLSForm pour le faire. Les étapes énumérées ci-dessous dans cet article d'aide illustrent comment vous pouvez ajouter des calculs et des contraintes à un tableau de questions en utilisant XLSForm.

## Configuration de la question et des champs

**Étape 1 : Créer un tableau de questions dans le Formbuilder**

La première étape consiste à créer un tableau de questions dans le Formbuilder (comme indiqué dans l'article d'aide [Tableau de questions](matrix_response.md)). Ajoutez simplement des lignes et des colonnes avec les variables nécessaires pour la collecte de données.

**Étape 2 : Télécharger le formulaire en tant que XLSForm**

Une fois le tableau de questions créé, **ENREGISTREZ** le formulaire et [téléchargez-le en tant que XLSForm](getting_started_xlsform.md#downloading-an-xlsform-from-kobotoolbox).

**Étape 3 : Ajouter une logique au tableau de questions**

Ouvrez le XLSForm et ajoutez les en-têtes de colonnes `calculation`, `constraint` et `constraint_message`. Avec ces en-têtes de colonnes, vous pourrez ajouter les expressions de _total de colonne_ et _total de ligne_ sous l'en-tête de colonne `calculation`. Vous pouvez également ajouter des _contraintes_ appropriées sous l'en-tête de colonne `constraint` et un _message de contrainte_ sous l'en-tête `constraint_message` selon les besoins.

De plus, vous pouvez également choisir d'ajouter un en-tête de colonne `read_only` pour empêcher les enquêteur(rice)s de modifier les réponses lors de la collecte de données pour certaines questions (par exemple, le _total de ligne_ et le _total de colonne_ qui sont calculés).

![Onglet Survey](images/calculations_constraints_matrix/survey_tab.png)

<p class="note">
  Dans l'image ci-dessus, vous remarquerez peut-être que les entrées <code>name</code> sont plus courtes. Dans cet exemple, elles ont été renommées à partir de celles générées automatiquement dans le Formbuilder pour capturer la capture d'écran complète de l'onglet survey. Si vous choisissez de renommer les vôtres, assurez-vous d'utiliser vos nouveaux noms de variables dans les en-têtes de colonnes <code>calculation</code> et <code>constraint</code>. Si le formulaire a déjà été déployé et que des données ont été collectées, il est recommandé de <em>ne pas</em> renommer les variables existantes.
</p>

**Étape 4 : Remplacer le formulaire**

Importez et remplacez votre XLSForm dans le projet existant, ou créez un nouveau projet (si nécessaire).

**Étape 5 : Déployer le formulaire**

**Étape 6 : Collecter des données**

Après avoir déployé le formulaire, vous pouvez aller dans **FORMULAIRE>Collecter des données>OUVRIR** pour commencer à collecter des données avec le formulaire web.

## Visualisation du résultat

Les images suivantes illustrent comment le formulaire apparaîtra et fonctionnera dans le formulaire web Enketo après avoir suivi les étapes ci-dessus :

**Aucune donnée n'est saisie :**

![Enketo Rien de Saisi](images/calculations_constraints_matrix/enketo_nothing_entered.png)

**Une erreur de saisie est commise :**

![Enketo Mauvaises Saisies](images/calculations_constraints_matrix/enketo_wrong_inputs_entered.png)

Ici, vous verrez qu'il y a seulement cinq membres du ménage au total. Si un(e) enquêteur(rice) saisit 6 pour le nombre d'hommes (0-14 ans), la contrainte affichera un message d'erreur.

**Aucune erreur de saisie :**

![Enketo Saisies Correctes](images/calculations_constraints_matrix/enketo_correct_inputs_entered.png)

Ici, lorsque vous saisissez des valeurs dans un tableau, les lignes et les colonnes sont automatiquement calculées.

<p class="note">
  Vous pouvez télécharger le XLSForm qui a été utilisé pour cet article
  <a
    download
    class="reference"
    href="./_static/files/calculations_constraints_matrix/calculations_constraints_matrix.xlsx"
    >ici</a
  >.
</p>

## Résolution de problèmes

-   Le tableau de questions fonctionne uniquement avec les **formulaires web Enketo**. Il n'est pas pris en charge par l'**application Android KoboCollect**.

-   Le tableau apparaîtra déformé si vous ne définissez pas la mise en page sur **Thème de grille**. Pour plus de détails sur les apparences des formulaires web, vous pouvez consulter [Styliser vos formulaires web dans le Formbuilder](alternative_enketo.md).