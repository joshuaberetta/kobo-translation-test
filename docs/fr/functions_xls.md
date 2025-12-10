# Utiliser des fonctions dans XLSForm

Les fonctions sont des opérations prédéfinies utilisées pour effectuer des calculs ou manipuler des données dans XLSForm. Elles sont essentielles pour automatiser des tâches et obtenir des informations clés dans vos formulaires, vous permettant de calculer des indicateurs de projet, de créer des systèmes de notation et de gérer les dates efficacement.

Cet article répertorie les fonctions courantes utilisées dans XLSForm, y compris les fonctions pour manipuler les nombres, les chaînes de caractères, les dates et les points GPS.

<p class="note">
  Pour en savoir plus sur la logique de formulaire dans XLSForm, consultez <a href="https://support.kobotoolbox.org/form_logic_xls.html">Introduction à la logique de formulaire dans XLSForm</a>. Pour en savoir plus sur les fonctions spécifiquement utilisées dans les groupes répétés, consultez <a href="https://support.kobotoolbox.org/repeat_groups_xls.html">Groupes répétés dans XLSForm</a>.
</p>

## Fonctions couramment utilisées dans XLSForm

Les fonctions suivantes sont parmi les plus fréquemment utilisées dans XLSForm. Elles aident à contrôler le comportement du formulaire, à gérer les réponses et à effectuer des calculs de base ou des opérations logiques entre les questions. Ces fonctions peuvent être appliquées dans les calculs, les contraintes, les conditions de pertinence et d'autres expressions tout au long de votre formulaire.

| Fonction | Description |
|:-----------|:-------------|
| `if(expression, then, else)` | Si l'expression est VRAIE, renvoie `then`. Sinon, renvoie `else`. |
| `selected(${question_name}, option_name)` | Utilisée pour déterminer si un choix spécifique a été sélectionné dans une question `select_multiple`. |
| `random()` | Renvoie un nombre aléatoire entre 0,0 (inclus) et 1,0 (exclus). |
| `count-selected(${question_name})` | Renvoie le nombre d'options sélectionnées dans une question `select_multiple`. |
| `coalesce(${question1}, ${question2})` | Renvoie la première valeur non vide des deux arguments. Renvoie une chaîne vide si les deux sont vides ou inexistants. |
| `jr:choice-name(choice_name, '${question_name}')` | Renvoie la valeur du libellé, dans la langue active, associée au `choice_name` dans la liste de choix pour une question de type sélection. Pour récupérer le libellé de la réponse sélectionnée, utilisez `jr:choice-name(${question_name}, '${question_name}')`. |
| `selected-at(${question_name}, n)` | Renvoie le choix sélectionné dans une question `select_multiple` à la position **n+1**. Par exemple, `selected-at(${question_name}, 2)` renvoie le troisième choix sélectionné dans une question `select_multiple`. |
| `once(expression)` | Évalue une expression une seule fois (par exemple, pour s'assurer qu'un nombre aléatoire n'est généré qu'une seule fois, ou pour stocker la première valeur saisie pour une question même si la réponse est modifiée ultérieurement). |
| `instance('list_name')/root/item[name = ${question}]/column_name` | Récupère une valeur de la feuille de choix. Recherche la liste de choix nommée `list_name`, trouve la ligne où le `name` du choix correspond à la réponse à `${question}`, et renvoie la valeur de la colonne spécifiée comme `column_name`. |

## Fonctions pour manipuler les nombres

Les fonctions suivantes sont utilisées pour effectuer des opérations mathématiques ou transformer des valeurs numériques dans XLSForm. Elles peuvent vous aider à calculer, arrondir ou convertir des nombres, ainsi qu'à appliquer des expressions mathématiques plus avancées si nécessaire.

| Fonction | Description |
|:---------|:------------|
| `int(number)` | Transforme un nombre décimal en un entier sans arrondir. |
| `round(number, places)` | Arrondit une valeur décimale à un nombre prédéterminé de décimales. |
| `pow(number, power)` | Calcule la puissance d'un nombre. |
| `number(x)` | Convertit x (une chaîne de caractères ou une expression booléenne) en une valeur numérique. |
| `log(number)` <br> `log10(number)` | Renvoie le logarithme naturel ou le logarithme en base 10 d'un nombre. |
| `abs(number)` | Renvoie la valeur absolue d'un nombre. |
| `sin(number)` <br> `asin(number)` <br> `cos(number)` <br> `acos(number)` <br> `tan(number)` <br> `atan(number)` | Renvoie le sinus/arc sinus, le cosinus/arc cosinus, ou la tangente/arc tangente d'un nombre. |
| `sqrt(number)` | Renvoie la racine carrée d'un nombre. |
| `exp(x)` <br> `exp10(x)` | Renvoie e^x ou 10^x. |
| `pi()` | Renvoie une approximation de la constante mathématique π. |

<p class="note">
  <strong>Remarque :</strong> À l'intérieur de ces fonctions, des constantes ou des <a href="https://support.kobotoolbox.org/form_logic_xls.html#question-referencing">références de questions</a> peuvent être incluses.
</p>

## Fonctions pour manipuler les chaînes de caractères

Les fonctions suivantes sont utilisées pour créer, modifier ou analyser des chaînes de texte dans XLSForm. Elles sont utiles pour combiner du texte, vérifier des motifs ou des caractères spécifiques, et nettoyer ou formater les saisies de texte.

| Fonction | Description |
|:---------|:------------|
| `concat()` | Concatène un ou plusieurs arguments (séparés par des virgules) en une seule chaîne de caractères. |
| `regex(string, expression)` | Renvoie `TRUE` si la chaîne correspond exactement et complètement à une <a href="https://support.kobotoolbox.org/restrict_responses.html">expression régulière</a>. |
| `contains(string, substring)` | Renvoie `TRUE` si la chaîne contient la sous-chaîne. |
| `starts-with(string, substring)` | Renvoie `TRUE` si la chaîne commence par la sous-chaîne. |
| `ends-with(string, substring)` | Renvoie `TRUE` si la chaîne se termine par la sous-chaîne. |
| `substr(string, start[, end])` | Renvoie la sous-chaîne de `string` commençant à l'index start et s'étendant jusqu'à (mais n'incluant pas) l'index end (ou jusqu'à la fin de `string`, si end n'est pas fourni). |
| `substring-before(string, target)` | Renvoie la sous-chaîne de `string` avant la première occurrence de la sous-chaîne cible. Si la cible n'est pas trouvée, ou si `string` commence par la sous-chaîne cible, cela renverra une chaîne vide. |
| `substring-after(string, target)` | Renvoie la sous-chaîne de `string` après la première occurrence de la sous-chaîne cible. Si la cible n'est pas trouvée, cela renverra une chaîne vide. |
| `translate(string, fromchars, tochars)` | Renvoie une copie de string, où chaque occurrence d'un caractère dans `fromchars` est remplacée par le caractère correspondant dans `tochars` (par exemple, remplacer toutes les lettres minuscules par des lettres majuscules). <br><br> <strong>Remarque :</strong> Si `fromchars` est plus long que `tochars`, chaque occurrence d'un caractère dans `fromchars` qui n'a pas de caractère correspondant dans `tochars` sera supprimée. |
| `string-length(string)` | Renvoie le nombre de caractères dans `string` (par exemple, pour ajouter une limite de mots à une question de texte). |
| `normalize-space(string)` | Renvoie une chaîne dans laquelle tous les espaces de début et de fin dans la chaîne sont supprimés, et les séquences d'espaces sont remplacées par un seul espace. |

## Fonctions pour manipuler les dates

Les fonctions suivantes sont utilisées pour enregistrer, formater et calculer des valeurs de date et d'heure dans XLSForm. Elles peuvent aider à capturer la date ou l'heure actuelle, convertir du texte en format de date, ou afficher des dates et des heures dans un format spécifique.

| Fonction | Description |
|:---------|:------------|
| `today()` | Renvoie la date actuelle sans composante horaire. |
| `now()` | Renvoie la date et l'heure actuelles au format ISO 8601, y compris le fuseau horaire. |
| `date('YYYY-MM-DD')` | Force les dates dans le format de date correct (en particulier pour les dates antérieures à 1970). |
| `format-date(date, format)` | Renvoie `date` sous forme de chaîne formatée comme défini par <code>format</code>. Les formats courants incluent : <ul><li><code>%Y</code> : année à 4 chiffres</li><li><code>%y</code> : année à 2 chiffres</li><li><code>%m</code> : mois avec zéro initial</li><li><code>%n</code> : mois numérique</li><li><code>%b</code> : mois en texte abrégé (Jan, Feb, Mar…)</li><li><code>%d</code> : jour du mois avec zéro initial</li><li><code>%e</code> : jour du mois</li><li><code>%a</code> : jour en texte abrégé (Sun, Mon, Tue…).</li></ul> |
| `format-date-time(datetime, format)` | Renvoie `datetime` sous forme de chaîne formatée comme défini par <code>format</code>. Les formats courants incluent : <ul><li><code>%H</code> : heure avec zéro initial (format 24h)</li><li><code>%h</code> : heure (format 24h)</li><li><code>%M</code> : minute avec zéro initial</li><li><code>%S</code> : seconde avec zéro initial</li><li><code>%3</code> : millisecondes avec zéro initial.</li></ul> |

## Fonctions pour manipuler les données GPS

Les fonctions suivantes sont utilisées pour travailler avec des données géographiques collectées via des questions GPS dans XLSForm. Elles peuvent calculer des distances, des périmètres ou des surfaces en fonction des réponses geopoint, geotrace ou geoshape.

| Fonction | Description |
|:---------|:------------|
| `area(${geoshape})` | Renvoie la surface, en mètres carrés, d'une valeur `geoshape`. |
| `distance(geo)` | Renvoie la distance, en mètres, soit : <ul><li>du périmètre d'une valeur `geoshape`</li><li>de la longueur d'une valeur `geotrace`</li><li>d'une liste de geopoints spécifiés sous forme de chaînes de caractères ou de références à d'autres champs (y compris des groupes répétés), séparés par des virgules</li></ul> |
| `geofence(${geopoint}, ${geoshape})` | Renvoie `TRUE` si le `${geopoint}` spécifié se trouve à l'intérieur du `${geoshape}` spécifié, `FALSE` sinon. Pris en charge uniquement dans KoboCollect. |