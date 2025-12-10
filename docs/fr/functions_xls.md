# Utiliser des fonctions dans XLSForm

Les fonctions sont des opérations prédéfinies utilisées pour effectuer des calculs ou manipuler des données dans XLSForm. Elles sont essentielles pour automatiser des tâches et obtenir des informations clés dans vos formulaires, vous permettant de calculer des indicateurs de projet, de créer des systèmes de notation et de gérer les dates efficacement.

Cet article répertorie les fonctions courantes utilisées dans XLSForm, y compris les fonctions pour manipuler des nombres, des chaînes de caractères, des dates et des points GPS.

<p class="note">
  Pour en savoir plus sur la logique de formulaire dans XLSForm, consultez <a href="https://support.kobotoolbox.org/form_logic_xls.html">Introduction à la logique de formulaire dans XLSForm</a>. Pour en savoir plus sur les fonctions spécifiquement utilisées dans les groupes répétés, consultez <a href="https://support.kobotoolbox.org/repeat_groups_xls.html">Groupes répétés dans XLSForm</a>.
</p>

## Fonctions couramment utilisées dans XLSForm

Les fonctions suivantes sont parmi les plus fréquemment utilisées dans XLSForm. Elles aident à contrôler le comportement du formulaire, à gérer les réponses et à effectuer des calculs de base ou des opérations logiques entre les questions. Ces fonctions peuvent être appliquées dans les calculs, les contraintes, les conditions de pertinence et d'autres expressions tout au long de votre formulaire.

| Fonction | Description |
|:-----------|:-------------|
| `if(expression, then, else)` | Si l'expression est VRAIE, renvoie `then`. Sinon, renvoie `else`. |
| `selected(${nom_question}, nom_option)` | Utilisée pour déterminer si un choix spécifique a été sélectionné dans une question `select_multiple`. |
| `random()` | Renvoie un nombre aléatoire entre 0,0 (inclus) et 1,0 (exclus). |
| `count-selected(${nom_question})` | Renvoie le nombre d'options sélectionnées dans une question `select_multiple`. |
| `coalesce(${question1}, ${question2})` | Renvoie la première valeur non vide des deux arguments. Renvoie une chaîne vide si les deux sont vides ou inexistants. |
| `jr:choice-name(nom_choix, '${nom_question}')` | Renvoie la valeur du libellé, dans la langue active, associée au `nom_choix` dans la liste de choix pour une question de type sélection. Pour récupérer le libellé de la réponse sélectionnée, utilisez `jr:choice-name(${nom_question}, '${nom_question}')`. |
| `selected-at(${nom_question}, n)` | Renvoie le choix sélectionné dans une question `select_multiple` à la position **n+1**. Par exemple, `selected-at(${nom_question}, 2)` renvoie le troisième choix sélectionné dans une question `select_multiple`. |
| `once(expression)` | Évalue une expression une seule fois (par exemple, pour s'assurer qu'un nombre aléatoire n'est généré qu'une seule fois, ou pour stocker la première valeur saisie pour une question même si la réponse est modifiée ultérieurement). |
| `instance('nom_liste')/root/item[name = ${question}]/nom_colonne` | Récupère une valeur de la feuille de choix. Recherche la liste de choix nommée `nom_liste`, trouve la ligne où le `name` du choix correspond à la réponse à `${question}`, et renvoie la valeur de la colonne spécifiée comme `nom_colonne`. |

## Fonctions pour manipuler des nombres

Les fonctions suivantes sont utilisées pour effectuer des opérations mathématiques ou transformer des valeurs numériques dans XLSForm. Elles peuvent vous aider à calculer, arrondir ou convertir des nombres, ainsi qu'à appliquer des expressions mathématiques plus avancées si nécessaire.

| Fonction | Description |
|:---------|:------------|
| `int(nombre)` | Transforme un nombre décimal en entier sans arrondir. |
| `round(nombre, places)` | Arrondit une valeur décimale à un nombre prédéterminé de décimales. |
| `pow(nombre, puissance)` | Calcule la puissance d'un nombre. |
| `number(x)` | Convertit x (une chaîne de caractères ou une expression booléenne) en valeur numérique. |
| `log(nombre)` <br> `log10(nombre)` | Renvoie le logarithme naturel ou le logarithme en base 10 d'un nombre. |
| `abs(nombre)` | Renvoie la valeur absolue d'un nombre. |
| `sin(nombre)` <br> `asin(nombre)` <br> `cos(nombre)` <br> `acos(nombre)` <br> `tan(nombre)` <br> `atan(nombre)` | Renvoie le sinus/arc sinus, le cosinus/arc cosinus, ou la tangente/arc tangente d'un nombre. |
| `sqrt(nombre)` | Renvoie la racine carrée d'un nombre. |
| `exp(x)` <br> `exp10(x)` | Renvoie e^x ou 10^x. |
| `pi()` | Renvoie une approximation de la constante mathématique π. |

<p class="note">
  <strong>Remarque :</strong> À l'intérieur de ces fonctions, des constantes ou des <a href="https://support.kobotoolbox.org/form_logic_xls.html#question-referencing">références de questions</a> peuvent être incluses.
</p>

## Fonctions pour manipuler des chaînes de caractères

Les fonctions suivantes sont utilisées pour créer, modifier ou analyser des chaînes de texte dans XLSForm. Elles sont utiles pour combiner du texte, vérifier des motifs ou des caractères spécifiques, et nettoyer ou formater les saisies de texte.

| Fonction | Description |
|:---------|:------------|
| `concat()` | Concatène un ou plusieurs arguments (séparés par des virgules) en une seule chaîne de caractères. |
| `regex(chaîne, expression)` | Renvoie `TRUE` si la chaîne correspond exactement et complètement à une <a href="https://support.kobotoolbox.org/restrict_responses.html">expression régulière</a>. |
| `contains(chaîne, sous-chaîne)` | Renvoie `TRUE` si la chaîne contient la sous-chaîne. |
| `starts-with(chaîne, sous-chaîne)` | Renvoie `TRUE` si la chaîne commence par la sous-chaîne. |
| `ends-with(chaîne, sous-chaîne)` | Renvoie `TRUE` si la chaîne se termine par la sous-chaîne. |
| `substr(chaîne, début[, fin])` | Renvoie la sous-chaîne de `chaîne` commençant à l'index début et s'étendant jusqu'à (mais n'incluant pas) l'index fin (ou jusqu'à la fin de `chaîne`, si fin n'est pas fourni). |
| `substring-before(chaîne, cible)` | Renvoie la sous-chaîne de `chaîne` avant la première occurrence de la sous-chaîne cible. Si la cible n'est pas trouvée, ou si `chaîne` commence par la sous-chaîne cible, cela renverra une chaîne vide. |
| `substring-after(chaîne, cible)` | Renvoie la sous-chaîne de `chaîne` après la première occurrence de la sous-chaîne cible. Si la cible n'est pas trouvée, cela renverra une chaîne vide. |
| `translate(chaîne, caractères_source, caractères_cible)` | Renvoie une copie de chaîne, où chaque occurrence d'un caractère dans `caractères_source` est remplacée par le caractère correspondant dans `caractères_cible` (par exemple, remplacer toutes les lettres minuscules par des lettres majuscules). <br><br> <strong>Remarque :</strong> Si `caractères_source` est plus long que `caractères_cible`, chaque occurrence d'un caractère dans `caractères_source` qui n'a pas de caractère correspondant dans `caractères_cible` sera supprimée. |
| `string-length(chaîne)` | Renvoie le nombre de caractères dans `chaîne` (par exemple, pour ajouter une limite de mots à une question de texte). |
| `normalize-space(chaîne)` | Renvoie une chaîne dans laquelle tous les espaces de début et de fin dans la chaîne sont supprimés, et les séquences d'espaces sont remplacées par un seul espace. |

## Fonctions pour manipuler des dates

Les fonctions suivantes sont utilisées pour enregistrer, formater et calculer des valeurs de date et d'heure dans XLSForm. Elles peuvent aider à capturer la date ou l'heure actuelle, convertir du texte en format de date, ou afficher des dates et des heures dans un format spécifique.

| Fonction | Description |
|:---------|:------------|
| `today()` | Renvoie la date actuelle sans composante horaire. |
| `now()` | Renvoie la date et l'heure actuelles au format ISO 8601, y compris le fuseau horaire. |
| `date('AAAA-MM-JJ')` | Force les dates dans le format de date correct (en particulier pour les dates antérieures à 1970). |
| `format-date(date, format)` | Renvoie `date` sous forme de chaîne formatée comme défini par <code>format</code>. Les formats courants incluent : <ul><li><code>%Y</code> : année à 4 chiffres</li><li><code>%y</code> : année à 2 chiffres</li><li><code>%m</code> : mois avec zéro initial</li><li><code>%n</code> : mois numérique</li><li><code>%b</code> : mois en texte court (jan, fév, mar…)</li><li><code>%d</code> : jour du mois avec zéro initial</li><li><code>%e</code> : jour du mois</li><li><code>%a</code> : jour en texte court (dim, lun, mar…).</li></ul> |
| `format-date-time(datetime, format)` | Renvoie `datetime` sous forme de chaîne formatée comme défini par <code>format</code>. Les formats courants incluent : <ul><li><code>%H</code> : heure avec zéro initial (format 24h)</li><li><code>%h</code> : heure (format 24h)</li><li><code>%M</code> : minute avec zéro initial</li><li><code>%S</code> : seconde avec zéro initial</li><li><code>%3</code> : millisecondes avec zéro initial.</li></ul> |

## Fonctions pour manipuler des données GPS

Les fonctions suivantes sont utilisées pour travailler avec des données géographiques collectées via des questions GPS dans XLSForm. Elles peuvent calculer des distances, des périmètres ou des surfaces en fonction des réponses geopoint, geotrace ou geoshape.

| Fonction | Description |
|:---------|:------------|
| `area(${geoshape})` | Renvoie la surface, en mètres carrés, d'une valeur `geoshape`. |
| `distance(geo)` | Renvoie la distance, en mètres, soit : <ul><li>du périmètre d'une valeur `geoshape`</li><li>de la longueur d'une valeur `geotrace`</li><li>d'une liste de geopoints spécifiés sous forme de chaînes de caractères ou de références à d'autres champs (y compris des groupes répétés), séparés par des virgules</li></ul> |
| `geofence(${geopoint}, ${geoshape})` | Renvoie `TRUE` si le `${geopoint}` spécifié est à l'intérieur du `${geoshape}` spécifié, `FALSE` sinon. Pris en charge uniquement dans KoboCollect. |