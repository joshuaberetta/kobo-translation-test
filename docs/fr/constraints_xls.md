# Ajouter des contraintes dans XLSForm

Les contraintes, également appelées critères de validation, sont un type de logique de formulaire utilisé pour **restreindre les réponses acceptables à une question en fonction d'une condition prédéfinie**. Si la condition de contrainte n'est pas remplie, un message d'erreur personnalisable s'affiche, invitant l'utilisatrice ou l'utilisateur du formulaire à saisir une réponse valide.

<p class="note">
  Pour en savoir plus sur la logique de formulaire dans XLSForm, consultez <a href="https://support.kobotoolbox.org/form_logic_xls.html">Introduction à la logique de formulaire dans XLSForm</a>.
</p>

Cet article couvre les sujets suivants :
- Ajouter des contraintes aux questions dans XLSForm
- Combiner plusieurs conditions de contrainte
- Personnaliser les messages d'erreur de contrainte
- Contraintes avancées dans XLSForm

<p class="note">
  <strong>Remarque :</strong> Cet article se concentre sur l'ajout de contraintes dans <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">XLSForm</a>. Pour en savoir plus sur l'ajout de contraintes dans l'interface de création de formulaires KoboToolbox (KoboToolbox Formbuilder), consultez <a href="https://support.kobotoolbox.org/validation_criteria.html?highlight=limiting">Ajouter des critères de validation dans l'interface de création de formulaires</a>.
<br><br>
Pour une pratique concrète de l'ajout de contraintes dans XLSForm, consultez le <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">Cours sur les fondamentaux XLSForm</a> de KoboToolbox Academy.
</p>

## Ajouter une contrainte

Les contraintes sont construites à l'aide de [références de questions](https://support.kobotoolbox.org/form_logic_xls.html#question-referencing), d'[opérateurs de comparaison](https://support.kobotoolbox.org/form_logic_xls.html#mathematical-and-comparison-operators) et de constantes. Les conditions de contrainte doivent être remplies pour valider ou soumettre un formulaire. Sinon, un **message d'erreur** apparaît et les utilisatrices et utilisateurs ne peuvent pas passer à la page suivante ou soumettre le formulaire.

Pour ajouter des contraintes dans XLSForm :
1. Ajoutez une colonne **constraint** à la feuille `survey`.
2. Dans la colonne `constraint`, définissez la condition qui doit être remplie **pour que la réponse soit valide.**
    - Utilisez un point `.` pour référencer la question dans la ligne où vous ajoutez une contrainte.
    - Utilisez un [opérateur de comparaison](https://support.kobotoolbox.org/form_logic_xls.html#mathematical-and-comparison-operators), suivi d'une valeur de référence, pour construire une contrainte simple.
    - Par exemple, `. > 18` restreint une question `integer` pour n'accepter que des valeurs supérieures à 18.

**Feuille survey**

| type     | name       | label                                | constraint       |
|:---------|:-----------|:-------------------------------------|:----------------|
| integer  | age        | Quel est votre âge ?                    | . >= 18         |
| integer  | household  | Combien de personnes vivent dans votre ménage ? | . <= 30         |
| integer  | income     | Parmi celles-ci, combien gagnent un revenu ?  | . <= ${household} |

### Formater les valeurs de référence
La valeur de référence dans une condition de contrainte doit correspondre au **type** de la question pour laquelle vous ajoutez une contrainte. Les formats de valeur de référence pour les principaux types de questions sont listés ci-dessous :

| Type de question   | Format de valeur de référence                                      | Exemple                      |
|:----------------|:-----------------------------------------------------------|:------------------------------|
| integer         | Nombre                                                      | `. > 35`                     |
| select_one      | Nom du choix (tel que défini dans la feuille choices) entre guillemets | `. = 'yes'`                  |
| select_multiple | Nom du choix combiné avec la <a href="https://support.kobotoolbox.org/functions_xls.html">fonction</a> `selected()`       | `selected(., 'chair')`       |
| date            | Date au format `date('YYYY-MM-DD')`                    | `. > date('2021-01-01')`    |
| text            | Texte entre guillemets (rarement utilisé pour les contraintes)      | `. != 'Not applicable'`      |

<p class="note">
  Pour en savoir plus sur la construction d'expressions de logique de formulaire dans XLSForm, consultez <a href="https://support.kobotoolbox.org/form_logic_xls.html">Introduction à la logique de formulaire dans XLSForm</a>.
</p>

## Combiner plusieurs conditions de contrainte
Plusieurs conditions de contrainte peuvent être combinées en une seule expression pour déterminer si une réponse est valide. Les conditions peuvent être combinées à l'aide des opérateurs logiques **and**, **or** et **not** :

- Utilisez **and** lorsque toutes les conditions doivent être remplies pour qu'une réponse soit valide.
    - Par exemple : <code>. > 18 <strong>and</strong> . < 65</code>
- Utilisez **or** lorsqu'au moins une condition doit être remplie pour qu'une réponse soit valide.
    - Par exemple : <code>. < 18 <strong>or</strong> ${student} = 'yes'</code>
- Utilisez **not** pour indiquer qu'une condition ou un ensemble de conditions ne doit pas être rempli (par exemple, lorsque deux conditions ne peuvent pas être vraies ensemble pour qu'une réponse soit valide).
    - Par exemple : <code><strong>not</strong>(. < 18 <strong>and</strong> ${household_head} = 'yes')</code>

**Feuille survey**

| type     | name   | label              | hint                                        | constraint                                               |
|:---------|:-------|:------------------|:--------------------------------------------|:---------------------------------------------------------|
| integer  | age    | Quel est votre âge ? | Doit être inférieur à 18 ou supérieur à 65 pour participer | <code>. < 18 <strong>or</strong> . > 65</code>         |
| integer  | weight | Combien pesez-vous ? | Doit être entre 30 et 200 kg               | <code>. >= 30 <strong>and</strong> . <= 200</code>     |


## Personnaliser les messages d'erreur de contrainte

Par défaut, lorsqu'une valeur de réponse dans le formulaire ne remplit pas la condition de contrainte, un message d'erreur « Valeur non autorisée » apparaît. Il est recommandé de personnaliser ce message pour informer les utilisatrices et utilisateurs de la raison pour laquelle la valeur est invalide, leur permettant ainsi de corriger leur saisie.

Pour personnaliser le message d'erreur de contrainte :
1. Ajoutez une colonne **constraint_message** à la feuille `survey`.
2. Dans la colonne `constraint_message`, saisissez le texte que vous souhaitez afficher comme message d'erreur lorsque les conditions de contrainte ne sont pas remplies.

**Feuille survey**

| type    | name | label           | constraint | constraint_message     |
|:--------|:-----|:----------------|:-----------|:----------------------|
| integer | age  | Quel est votre âge ? | . >= 18   | Doit être âgé(e) de plus de 18 ans. |

## Contraintes avancées dans XLSForm

Au-delà des contraintes de base, vous pouvez personnaliser les conditions pour garantir la qualité des données et vous adapter à de nombreux scénarios de collecte de données. Pour construire des conditions de contrainte plus avancées dans XLSForm :

- Utilisez des parenthèses pour combiner plus de deux conditions
- Utilisez des [fonctions](https://support.kobotoolbox.org/functions_xls.html) pour plus de flexibilité
- Utilisez des [expressions régulières](https://support.kobotoolbox.org/restrict_responses.html) pour restreindre les réponses textuelles
  
Voici des exemples de critères de validation plus avancés :

| Critère | Description |
|:---------|:------------|
| <code>(. >= 18 and . < 130) or (. = 999)</code> | La réponse doit être entre 17 et 130 ou être égale à 999 (souvent utilisé pour les non-réponses) |
| <code>not(${in_university} = 'yes' and . < 16)</code> | Si la réponse à `in_university` est 'yes', la réponse actuelle doit être supérieure à 16. |
| <code>not(selected(., 'none') and count-selected(.)>1)</code> | L'option 'none' ne peut pas être sélectionnée si une autre réponse dans une question `select_multiple` est sélectionnée. |
| <code>. < today()</code> | La date saisie doit être antérieure à la date du jour. |
| <code>regex(., '^\d{2}$')</code> | La saisie est limitée à deux chiffres (en utilisant des <a href="https://support.kobotoolbox.org/restrict_responses.html">expressions régulières</a>). |