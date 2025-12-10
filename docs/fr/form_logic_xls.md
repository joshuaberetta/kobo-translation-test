# Introduction à la logique de formulaire dans XLSForm

La logique de formulaire contrôle le flux et le comportement de votre formulaire en fonction des réponses aux questions précédentes. Elle vous permet de créer des formulaires dynamiques qui s'adaptent aux entrées de l'utilisateur. Par exemple, vous pouvez utiliser la logique de formulaire pour afficher des questions spécifiques uniquement lorsqu'elles sont pertinentes, valider des réponses ou effectuer des calculs automatiquement.

Les principaux types de logique de formulaire comprennent :
- **Branchement conditionnel :** Contrôle quand les questions sont affichées ou masquées en fonction des réponses précédentes.
- **Contraintes :** Valident les réponses pour s'assurer qu'elles respectent des règles ou des critères définis.
- **Filtres de choix :** Affichent uniquement les options de réponse pertinentes en fonction des réponses antérieures.
- **Calculs :** Génèrent automatiquement des valeurs à l'aide d'expressions mathématiques ou logiques.
- **Logique de réponse obligatoire :** Définit quand une question doit être répondue.

La logique de formulaire est construite à l'aide d'**expressions**, qui combinent des **références de questions**, des **opérateurs**, des **fonctions** et des **constantes**. L'expression est évaluée comme VRAI ou FAUX pour contrôler le comportement du formulaire.

<p class="note">
  Cet article présente les composants de base de la logique de formulaire dans <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">XLSForm</a>, y compris le référencement de questions, les opérateurs et les fonctions. Pour en savoir plus sur chaque type de logique de formulaire, consultez les articles d'aide sur le <a href="https://support.kobotoolbox.org/skip_logic_xls.html">branchement conditionnel</a>, la <a href="https://support.kobotoolbox.org/required_logic_xls.html">logique de réponse obligatoire</a>, les <a href="https://support.kobotoolbox.org/constraints_xls.html">contraintes</a>, les <a href="https://support.kobotoolbox.org/choice_filters_xls.html">filtres de choix</a> et les <a href="https://support.kobotoolbox.org/calculations_xls.html">calculs</a> dans XLSForm.
</p>

## Référencement de questions

Le référencement de questions vous permet d'incorporer la réponse à une question précédente dans le libellé ou la logique d'une question ultérieure. Le référencement de questions est fréquemment utilisé dans les formulaires avancés :

- **Dans les libellés ou indices de questions :** Par exemple, vous pouvez inclure le nom de l'enfant d'un(e) répondant(e) dans des questions ultérieures concernant son enfant.
- **Dans la logique de formulaire :** Par exemple, vous pouvez afficher ou masquer une question en fonction d'une réponse précédente, ou valider une réponse en la comparant avec une réponse antérieure.

Le référencement de questions utilise le format **${nom_question}**, où `nom_question` est remplacé par le nom unique de la question référencée.

Si une référence de question contient une erreur d'orthographe ou est autrement incorrecte, un message d'erreur apparaîtra lors de la prévisualisation ou de la soumission du formulaire.

<p class="note">
  <strong>Remarque :</strong> Lors du référencement d'une question dans sa propre logique (c'est-à-dire dans sa propre ligne), un point <code>.</code> peut être utilisé comme raccourci.
</p>

**Feuille survey**

| type     | name            | label                                                                 | constraint              |
|:-----------|:-----------------|:------------------------------------------------------------------------|:--------------------------|
| integer   | household_size  | Combien de personnes vivent dans votre ménage ?                        |                          |
| integer   | total_under18   | Parmi les ${household_size} personnes, combien ont moins de 18 ans ? | . < ${household_size}    |
| survey | 

## Opérateurs mathématiques et de comparaison

Les **opérateurs mathématiques** sont utilisés pour effectuer des calculs arithmétiques en utilisant des valeurs numériques dans le formulaire. Les opérateurs mathématiques dans XLSForm comprennent :

| Opérateur | Description                     |
|:-----------|:---------------------------------|
| `+`       | Addition                        |
| `-`       | Soustraction                    |
| `*`       | Multiplication                  |
| `div`     | Division                        |
| `mod`     | Modulo (reste d'une division)   |

Les **opérateurs de comparaison** sont utilisés pour comparer des valeurs. Les opérateurs de comparaison dans XLSForm comprennent :

| Opérateur | Description                  |
|:-----------|:------------------------------|
| `=`       | Égal à                       |
| `>`       | Supérieur à                  |
| `<`       | Inférieur à                  |
| `>=`      | Supérieur ou égal à          |
| `<=`      | Inférieur ou égal à          |
| `!=`      | Différent de                 |

## Combinaison de conditions à l'aide d'opérateurs logiques

Les **opérateurs logiques** peuvent être utilisés dans XLSForm pour combiner plusieurs conditions. Les opérateurs logiques dans XLSForm comprennent :
- **and** (toutes les conditions doivent être remplies)
- **or** (au moins une des conditions doit être remplie)
- **not** (la ou les conditions ne doivent pas être remplies)

**Feuille survey**

| type     | name           | label                                | constraint                         |
|:-----------|:----------------|:--------------------------------------|:------------------------------------|
| integer   | household_size | Combien de personnes vivent dans votre ménage ? |                                    |
| integer   | total_under18  | Combien ont moins de 18 ans ?        | . < ${household_size} <strong>and</strong> . >= 0   |
| survey |

## Fonctions

Les fonctions sont des opérations prédéfinies utilisées pour effectuer des calculs ou manipuler des données dans XLSForm. Les fonctions rendent les calculs et la logique de formulaire plus efficaces en effectuant automatiquement des tâches complexes comme l'arrondi de valeurs, le calcul de puissances ou l'extraction de la date actuelle.

<p class="note">
Pour une liste complète des fonctions dans XLSForm, consultez <a href="https://support.kobotoolbox.org/functions_xls.html">Utilisation des fonctions dans XLSForm</a>.
</p>

## Regex

Une expression régulière (regex) est un modèle de recherche utilisé pour faire correspondre des caractères spécifiques dans une chaîne de caractères. Elle est largement utilisée pour valider, rechercher, extraire et restreindre du texte dans la plupart des langages de programmation, y compris dans KoboToolbox.

Les regex peuvent être utilisées dans les **contraintes** pour contrôler la longueur et les caractères saisis dans une question (par exemple, limiter la saisie d'un numéro de téléphone à exactement 10 chiffres, contrôler le format des numéros d'identification ou vérifier la validité d'une adresse e-mail). Elles peuvent également être utilisées dans les **calculs** et d'autres logiques de formulaire.

Dans KoboToolbox, les expressions régulières sont évaluées à l'aide de la fonction `regex(., ' ')`, où la regex est saisie entre apostrophes et le point `.` représente la question actuelle. `regex(., ' ')` renvoie VRAI si l'expression régulière est satisfaite, et FAUX dans le cas contraire.

<p class="note">
  Pour en savoir plus sur l'utilisation des regex dans KoboToolbox, consultez <a href="https://support.kobotoolbox.org/restrict_responses.html">Restriction des réponses textuelles avec des expressions régulières</a>.
</p>