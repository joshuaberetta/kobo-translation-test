# Question de type calcul

Certains formulaires avancés peuvent nécessiter qu'un calcul interne soit effectué dans le cadre du formulaire (plutôt qu'après, lors de l'analyse). Cela peut être fait en ajoutant un calcul et en écrivant l'expression mathématique dans le champ du libellé de la question.

![image](/images/calculate_questions/calculation.gif)

Une expression mathématique peut être aussi simple que `5 + 1`, mais elle inclurait très probablement une référence à une autre question.

Pour référencer d'autres questions dans votre question de calcul, vous devez attribuer des noms fixes aux autres questions via les paramètres de la question, tels que `girls` ou `income`. Lorsque vous référencez ces questions, vous devez toujours utiliser le nom de question unique (et non le libellé) - `${girls}` ou `${income}`

Par exemple, si vous souhaitez convertir la réponse à une question sur le revenu d'une personne dans une autre devise (comme les francs rwandais en dollars américains), vous devez écrire `${income} div 688`.

Vous pouvez également utiliser la réponse à cette question de calcul à d'autres fins, comme construire votre logique de saut (par exemple, ne poser une question de suivi qu'au-dessus d'un certain seuil de revenu) ou en l'affichant dans une note ([voir ici](responses_inside_question.md) pour obtenir de l'aide sur la façon d'afficher la réponse à une question dans le libellé d'une autre question).

## Liste des fonctions disponibles

Il existe de nombreuses options différentes disponibles, telles que la fonction round() (par exemple, `round(${int_1} div ${int_2}, 1)` arrondira le résultat d'une division à une seule décimale). Pour une liste de certaines des nombreuses expressions mathématiques qui peuvent être utilisées dans ce champ, veuillez consulter les [spécifications XForm sur les fonctions de calcul](https://docs.getodk.org/form-operators-functions/) pour le contexte technique de toutes les fonctions disponibles dans KoboToolbox et les XLSForms. Pour une utilisation avancée des calculs dans KoboToolbox, veuillez vous référer à [cet article](advanced_calculate.md).

## Liste des opérateurs mathématiques disponibles

| Opérateur              | Description                      |
| :--------------------- | :------------------------------- |
| `+`                    | Addition                         |
| `-`                    | Soustraction                     |
| `*`                    | Multiplication                   |
| `div`                  | Division                         |
| `=`                    | Égal                             |
| `!=`                   | Différent de                     |
| `<`                    | Inférieur à                      |
| `<=`                   | Inférieur ou égal à              |
| `>`                    | Supérieur à                      |
| `>=`                   | Supérieur ou égal à              |
| `or`                   | Ou                               |
| `and`                  | Et                               |
| `mod`                  | Modulo (reste de la division)    |
| `pow([base], [power])` | Puissance / exposant             |