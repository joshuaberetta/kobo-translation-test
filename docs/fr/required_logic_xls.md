# Ajouter une logique de réponse obligatoire dans XLSForm

La logique de réponse obligatoire vous permet de rendre une question obligatoire si des conditions spécifiques sont remplies. Par exemple, vous pouvez exiger un numéro de téléphone uniquement si les répondant(e)s acceptent d'être recontacté(e)s à l'avenir. Cette option offre plus de contrôle que de simplement marquer une question comme toujours obligatoire ou toujours facultative.

<p class="note">
  Pour en savoir plus sur les questions obligatoires et comment personnaliser le message affiché aux répondant(e)s lorsqu'ils ou elles laissent une question obligatoire sans réponse, consultez <a href="https://support.kobotoolbox.org/question_options_xls.html#required-questions">Utiliser les options de question dans XLSForm</a>.
</p>

Cet article explique comment ajouter des conditions de logique de réponse obligatoire dans XLSForm, y compris rendre une question obligatoire selon qu'une autre question a été répondue ou non.

<p class="note">
  <strong>Remarque :</strong> Cet article se concentre sur l'ajout de logique de réponse obligatoire dans <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">XLSForm</a>. Pour en savoir plus sur l'ajout de logique de réponse obligatoire dans l'interface de création de formulaires KoboToolbox (KoboToolbox Formbuilder), consultez <a href="https://support.kobotoolbox.org/question_options.html?highlight=custom+logic#mandatory-response">Utiliser les options de question</a>.
  <br><br>
  Pour une pratique concrète de la logique de réponse obligatoire dans XLSForm, consultez le <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">Cours sur les fondamentaux XLSForm</a> de KoboToolbox Academy.
</p>

## Ajouter des conditions de logique de réponse obligatoire

La logique de réponse obligatoire utilise le <a href="https://support.kobotoolbox.org/form_logic_xls.html#question-referencing">référencement de questions</a> pour rendre des questions obligatoires en fonction des réponses précédentes. La question utilisée pour définir la logique de réponse obligatoire est appelée la **question de référence.**

Pour ajouter une logique de réponse obligatoire dans XLSForm :
1. Ajoutez une colonne **required** à la feuille `survey`. 
2. Dans la ligne de la question pour laquelle vous souhaitez définir la logique de réponse obligatoire, saisissez la condition qui doit être remplie **pour que la question soit obligatoire.**

**Feuille survey**

| type         | name      | label                                                                     | required           |
|:--------------|:-----------|:--------------------------------------------------------------------------|:------------------|
| select_one yn | recontact  | Acceptez-vous d'être recontacté(e) pour une autre étude à l'avenir ?    |                    |
| text          | email      | Quelle est votre adresse e-mail ?                                        | ${recontact} = 'yes' |

Si un(e) répondant(e) ne répond pas à une question obligatoire, il ou elle ne pourra pas passer à la page suivante du formulaire ni le soumettre.

### Formater les conditions de logique de réponse obligatoire

Le format de la condition de logique de réponse obligatoire diffère selon le **type** de la question de référence, comme détaillé dans le tableau ci-dessous.

| Type de question de référence | Condition de logique de réponse obligatoire | Exemple |
|:-------------------------|:--------------------|:---------|
| select_one | `${question_de_référence} = 'nom_du_choix'` | `${consent} = 'yes'` |
| select_multiple | `selected(${question_de_référence}, 'nom_du_choix')` | `selected(${reasons}, 'other')` |
| integer | `${question_de_référence}` suivi d'un opérateur logique (>, <, =) et d'un nombre (ou d'une référence à une autre question) | `${age} >= 18` |
| date | `${question_de_référence}` suivi d'un opérateur logique (>, <, =) et de `date('AAAA-MM-JJ')` | `${dob} >= date('1975-01-01')` |

<p class="note">
Pour en savoir plus sur la construction d'expressions de logique de formulaire dans XLSForm, consultez <a href="https://support.kobotoolbox.org/form_logic_xls.html">Introduction à la logique de formulaire dans XLSForm</a>.
</p>

## Ajouter une logique de réponse obligatoire selon qu'une question a été répondue ou non

En plus de définir une logique de réponse obligatoire pour une réponse spécifique, vous pouvez également la baser sur le fait qu'une question a été répondue ou laissée vide. Cela est utile lorsque vous souhaitez vous assurer qu'au moins une des deux questions est obligatoire.

Les questions sans réponse sont traitées comme des chaînes vides, notées par deux apostrophes simples `''`. Les conditions de logique de réponse obligatoire suivantes peuvent être utilisées :

| Condition de logique de réponse obligatoire | Description |
|:---------------------------|:-------------|
| `${question_de_référence} != ''` | Rendre obligatoire uniquement si `question_de_référence` a été répondue (non vide). |
| `${question_de_référence} = ''`  | Rendre obligatoire uniquement si `question_de_référence` n'a pas été répondue (vide). |

**Feuille survey**

| type  | name    | label                                               | required     |
|:------|:--------|:----------------------------------------------------|:-------------|
| note  | contact | Veuillez fournir votre numéro de téléphone ou votre adresse e-mail ci-dessous. |              |
| text  | phone   | Numéro de téléphone                                 |              |
| text  | email   | Adresse e-mail                                      | ${phone} = '' |