# Ajouter des calculs dans XLSForm

Les calculs peuvent être utilisés dans votre formulaire pour dériver de nouvelles variables, construire une logique de formulaire avancée et afficher des résultats aux répondant(e)s pendant la collecte de données.

Les calculs sont traités au sein du formulaire, ce qui permet de gagner du temps lors de l'analyse des données. Les résultats sont stockés sous forme de nouvelles colonnes dans l'ensemble de données final et peuvent être utilisés tout au long du formulaire pour appliquer un [branchement conditionnel](https://support.kobotoolbox.org/skip_logic_xls.html), définir des [contraintes](https://support.kobotoolbox.org/constraints_xls.html) ou afficher du [contenu dynamique](https://support.kobotoolbox.org/form_logic_xls.html#question-referencing) dans les libellés de questions et les notes.

Cet article explique comment ajouter des calculs dans XLSForm, couvrant à la fois l'arithmétique de base et les expressions plus avancées.

<p class="note">
<strong>Remarque :</strong> Cet article se concentre sur l'ajout de calculs dans <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">XLSForm</a>. Pour en savoir plus sur l'ajout de calculs dans l'interface de création de formulaires KoboToolbox (KoboToolbox Formbuilder), consultez <a href="https://support.kobotoolbox.org/calculate_questions.html">Question de type Calcul</a>.
<br><br>
Pour une pratique concrète des calculs dans XLSForm, consultez le <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">Cours sur les fondamentaux XLSForm</a> de KoboToolbox Academy.
</p>

## Ajouter des calculs dans XLSForm

Les expressions de calcul sont construites en utilisant une combinaison de [références de questions](https://support.kobotoolbox.org/form_logic_xls.html#question-referencing), d'[opérateurs mathématiques](https://support.kobotoolbox.org/form_logic_xls.html#mathematical-and-comparison-operators), de [fonctions](https://support.kobotoolbox.org/functions_xls.html) et de constantes.

Pour ajouter un calcul dans votre XLSForm :
1. Dans la colonne `type` de la feuille `survey`, saisissez **calculate** pour ajouter une question de type `calculate`. 
2. Saisissez un `name` (nom de l'élément) pour la question `calculate`. 
    - Comme le calcul n'est pas affiché dans le formulaire, la question `calculate` ne nécessite pas de **label** (libellé).
3. Ajoutez une colonne **calculation** dans la feuille `survey`.
4. Dans la colonne `calculation`, saisissez l'**expression de calcul.** 
    - Les calculs peuvent aller de [calculs arithmétiques de base](https://support.kobotoolbox.org/calculations_xls.html#arithmetic-calculations) à des [calculs avancés](https://support.kobotoolbox.org/calculations_xls.html#advanced-calculations) utilisant des fonctions et des expressions régulières.
  
Pour faire référence au résultat du calcul dans le reste de votre formulaire (par exemple, dans une question de type note, un libellé de question ou une logique de formulaire), utilisez le format de [référencement de questions](https://support.kobotoolbox.org/form_logic_xls.html#question-referencing) **${question_name}**, où `question_name` est le **name** (nom de l'élément) de la question `calculate`.

**Feuille survey**

| type      | name          | label                          | calculation           |
|:----------|:--------------|:-------------------------------|:----------------------|
| integer   | bags          | Nombre total de sacs vendus    |                       |
| decimal   | price         | Prix par sac                   |                       |
| calculate | total_amount  |                                | ${bags} * ${price}    |
| note      | display_total | Le total est ${total_amount}   |                       |
| survey | 

## Calculs arithmétiques

Les calculs dans XLSForm peuvent aller de simples calculs arithmétiques à la dérivation avancée de variables.

Les calculs arithmétiques vous permettent d'effectuer des calculs de base en utilisant les **opérateurs** suivants :

| Opérateur | Description |
|:----------|:-------------|
| <strong>+</strong>   | Addition |
| <strong>-</strong>   | Soustraction |
| <strong>*</strong>   | Multiplication |
| <strong>div</strong> | Division |
| <strong>mod</strong> | Modulo (calcule le reste d'une division) |

Les calculs dans XLSForm suivent la règle **BODMAS** pour l'ordre des opérations mathématiques : **B**rackets (parenthèses), **O**rder of powers (ordre des puissances), **D**ivision, **M**ultiplication, **A**ddition et **S**ubtraction (soustraction). Cela signifie que les calculs entre parenthèses sont effectués en premier, suivis des puissances, puis des divisions, des multiplications, etc. L'utilisation correcte des parenthèses garantit que vos calculs fonctionnent comme prévu.

## Calculs avancés

Les calculs avancés dans XLSForm s'appuient souvent sur des **fonctions** et des **expressions régulières** pour rendre les calculs plus efficaces.
* Les **fonctions** sont des opérations prédéfinies utilisées pour effectuer automatiquement des tâches complexes comme arrondir des valeurs, calculer des puissances ou extraire la date actuelle.
* Les **expressions régulières (regex)** sont des modèles de recherche utilisés pour faire correspondre des caractères spécifiques dans une chaîne de texte.

<p class="note">
  Pour une liste complète des fonctions disponibles dans XLSForm, consultez <a href="https://support.kobotoolbox.org/functions_xls.html">Utiliser des fonctions dans XLSForm</a>. Pour en savoir plus sur les expressions régulières, consultez <a href="https://support.kobotoolbox.org/restrict_responses.html">Restreindre les réponses textuelles avec des expressions régulières</a>.
</p>

Voici des exemples de calculs plus avancés :

| Calcul | Description |
|:-------------|:-------------|
| `int((today()-${DOB}) div 365.25)` | Calculer l'âge à partir de la date de naissance. |
| `int(today()-${date})` | Calculer le nombre de jours depuis une date. |
| `format-date(${date}, '%b')` | Retourner uniquement le mois d'une date. |
| `concat(${first}, " ", ${middle}, " ", ${last})` | Créer une seule chaîne avec le nom complet d'un(e) répondant(e). |
| `jr:choice-name(${question1}, '${question1}')` | Retourner le libellé d'un choix, dans la langue actuelle, à partir de la liste de choix. |
| `translate(${full_name}, "ABCDEFGHIJKLMNOPQRSTUVWXYZ ", "abcdefghijklmnopqrstuvwxyz_")` | Convertir les lettres majuscules en minuscules et les espaces en traits de soulignement. |
| `substr(${question}, 1, 2)` | Conserver uniquement la 1ère lettre ou le 1er chiffre dans une chaîne. |
| `int(random()*10)` | Générer un nombre aléatoire entre 0 et 10. |
| `selected-at(${gps}, 0)` | Isoler la latitude des coordonnées GPS. |
| `selected-at(${gps}, 1)` | Isoler la longitude des coordonnées GPS. |
| `if(regex(${id}, '^ML-'), 'yes', 'no')` | Créer une variable binaire qui prend `yes` si l'identifiant du/de la répondant(e) commence par "ML-". |

### Définir des réponses par défaut dynamiques

Le champ `calculation` peut également être utilisé pour définir des **réponses par défaut dynamiques.** Les réponses par défaut dynamiques vous permettent d'afficher une réponse par défaut dans une question en fonction d'une réponse précédente.

Pour définir une réponse par défaut dynamique :
1. Dans la colonne `calculation`, saisissez la **référence à la question** qui remplira dynamiquement la réponse par défaut. 
2. Dans la colonne `trigger`, saisissez la question qui activera le calcul. 
    - En général, il s'agirait de la même question référencée dans la colonne `calculation`, de sorte que toute modification de la question déclencheur mettra également à jour la réponse par défaut.

**Feuille survey**

| type | name       | label                     | calculation | trigger     |
|:------|:-----------|:--------------------------|:-------------|:-------------|
| text  | hh_name    | Nom du chef de ménage     |             |              |
| text  | phone      | Numéro de téléphone du ménage |              |              |
| text  | phone_name | Nom du propriétaire du téléphone | ${hh_name}   | ${hh_name}   |
| survey | 

<p class="note">
<strong>Remarque :</strong> Si vous souhaitez empêcher les utilisatrices et utilisateurs de modifier le champ, définissez la colonne <code>read_only</code> sur <code>TRUE</code>.
</p>

## Dépannage

<details>
  <summary><strong>Recommandations de dépannage</strong></summary>
  Pour faciliter le dépannage, affichez les résultats des calculs dans une note pendant le développement de votre formulaire. Cela permet de déterminer si le calcul s'évalue correctement et facilite l'identification des problèmes. Vous pouvez également décomposer les longues expressions en plus petites et afficher le résultat de chacune pour identifier les problèmes.
</details>

<br>

<details>
  <summary><strong>Les calculs ne fonctionnent pas correctement</strong></summary>
  Si vos calculs ne fonctionnent pas, vérifiez les points suivants :
  <ul>
  <li><strong>Syntaxe :</strong> Toutes les parenthèses ouvertes sont fermées, des guillemets droits <code>'</code> sont utilisés, et des virgules sont incluses là où nécessaire.</li>
  <li><strong>Références :</strong> Les références de questions correspondent correctement au nom de l'élément, pas d'espaces ni de fautes de frappe, pas de références circulaires (c'est-à-dire que le calcul ne dépend pas de lui-même).</li>
  <li><strong>Types de données :</strong> Les calculs numériques et de chaînes ne sont pas combinés dans la même question, les types de données sont utilisés correctement.</li>
</ul>
</details>

<br>

<details>
  <summary><strong>Gérer les champs vides</strong></summary>
  Les questions sans réponse sont traitées comme des chaînes vides et ne seront pas automatiquement converties en zéro. Lorsqu'une valeur vide est utilisée dans un calcul, cela entraîne "Not a Number" (NaN). Pour convertir les valeurs vides en zéro pour les calculs, utilisez les <a href="https://support.kobotoolbox.org/functions_xls.html">fonctions</a> <code>coalesce()</code> ou <code>if()</code>. Par exemple :
  <ul>
  <li><code>coalesce(${potentially_empty_value}, 0)</code></li>
  <li><code>if(${potentially_empty_value}="", 0, ${potentially_empty_value})</code></li>
</ul>
  Une autre option consiste à définir des valeurs par défaut pour chacune des variables numériques à 0 dans la colonne <code>default</code>.
</details>

<br>

<details>
  <summary><strong>Les calculs continuent de changer dans le formulaire</strong></summary>
  Les expressions sont réévaluées au fur et à mesure qu'un(e) enquêteur(rice) progresse dans un formulaire. Ceci est particulièrement important pour les <a href="https://support.kobotoolbox.org/functions_xls.html">fonctions</a> non connectées aux champs du formulaire, telles que <code>random()</code> ou <code>now()</code>, car leurs valeurs peuvent changer dans ces conditions.
<br><br>
Les expressions sont réévaluées lorsque :
  <ul>
  <li>Un formulaire est ouvert</li>
  <li>La valeur de toute question dans le calcul change</li>
  <li>Un groupe répété est ajouté ou supprimé</li>
  <li>Un formulaire est sauvegardé ou finalisé</li>
</ul>
  Pour contrôler quand une expression est évaluée, définissez un <a href="https://support.kobotoolbox.org/question_options_xls.html#additional-question-options">déclencheur</a> pour l'évaluer uniquement lorsqu'une question donnée reçoit une réponse, ou utilisez la fonction <code>once()</code> pour vous assurer que l'expression n'est évaluée qu'une seule fois (par exemple, <code>once(random())</code> ou <code>once(today())</code>).
</details>