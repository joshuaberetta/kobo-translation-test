# Ajouter une logique d'obligation conditionnelle dans un XLSForm

La logique d'obligation conditionnelle vous permet de rendre une question obligatoire si des conditions spécifiques sont remplies. Par exemple, vous pouvez exiger un numéro de téléphone uniquement si les répondant(e)s acceptent d'être recontacté(e)s à l'avenir. Cette option offre plus de contrôle que de simplement marquer une question comme toujours obligatoire ou toujours facultative.

<p class="note">
  Pour en savoir plus sur les questions obligatoires et comment personnaliser le message affiché aux répondant(e)s lorsqu'ils laissent une question obligatoire sans réponse, consultez <a href="https://support.kobotoolbox.org/fr/question_options_xls.html#required-questions">Utiliser les options de question dans un XLSForm</a>.
</p>

Cet article explique comment ajouter des conditions de logique d'obligation conditionnelle dans un XLSForm, notamment comment rendre une question obligatoire selon qu'une autre question a été répondue ou non.

<p class="note">
  <strong>Remarque :</strong> Cet article se concentre sur l'ajout de logique d'obligation conditionnelle dans un <a href="https://support.kobotoolbox.org/fr/getting_started_xlsform.html">XLSForm</a>. Pour en savoir plus sur l'ajout de logique d'obligation conditionnelle dans l'interface de création de formulaires KoboToolbox (KoboToolbox Formbuilder), consultez <a href="https://support.kobotoolbox.org/fr/question_options.html?highlight=custom+logic#mandatory-response">Utiliser les options de question</a>.
  <br><br>
  Pour un apprentissage pratique de la logique d'obligation conditionnelle dans un XLSForm, consultez le <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">cours XLSForm Fundamentals</a> de la KoboToolbox Academy.
</p>

## Ajouter des conditions de logique d'obligation conditionnelle

La logique d'obligation conditionnelle utilise le <a href="https://support.kobotoolbox.org/fr/form_logic_xls.html#question-referencing">référencement de questions</a> pour rendre des questions obligatoires en fonction de réponses précédentes. La question utilisée pour définir la logique d'obligation conditionnelle est appelée la **question de référence.**

Pour ajouter une logique d'obligation conditionnelle dans un XLSForm :
1. Ajoutez une colonne **required** à la feuille de calcul `survey`. 
2. Dans la ligne de la question pour laquelle vous souhaitez définir la logique d'obligation conditionnelle, saisissez la condition qui doit être remplie **pour que la question soit obligatoire.**

**feuille de calcul survey**

| type         | name      | label                                                                     | required           |
|:--------------|:-----------|:--------------------------------------------------------------------------|:------------------|
| select_one yn | recontact  | Acceptez-vous d'être recontacté(e) pour une autre étude à l'avenir ?    |                    |
| text          | email      | Quelle est votre adresse e-mail ?                                               | ${recontact} = 'yes' |

Si un(e) répondant(e) ne répond pas à une question obligatoire, il ou elle ne pourra pas passer à la page suivante du formulaire ni le soumettre.

### Formater les conditions de logique d'obligation conditionnelle

Le format de la condition de logique d'obligation conditionnelle diffère selon le **type** de la question de référence, comme détaillé dans le tableau ci-dessous.

| Type de question de référence | Condition de logique d'obligation conditionnelle | Exemple |
|:-------------------------|:--------------------|:---------|
| select_one | `${question_référence} = 'nom_choix'` | `${consent} = 'yes'` |
| select_multiple | `selected(${question_référence}, 'nom_choix')` | `selected(${reasons}, 'other')` |
| integer | `${question_référence}` suivi d'un opérateur logique (>, <, =) et d'un nombre (ou d'une référence à une autre question) | `${age} >= 18` |
| date | `${question_référence}` suivi d'un opérateur logique (>, <, =) et de `date('AAAA-MM-JJ')` | `${dob} >= date('1975-01-01')` |

<p class="note">
Pour en savoir plus sur la construction d'expressions de logique de formulaire dans un XLSForm, consultez <a href="https://support.kobotoolbox.org/fr/form_logic_xls.html">Introduction à la logique de formulaire dans un XLSForm</a>.
</p>

## Ajouter une logique d'obligation conditionnelle selon qu'une question a été répondue

En plus de définir une logique d'obligation conditionnelle pour une réponse spécifique, vous pouvez également la baser sur le fait qu'une question a été répondue ou laissée vide. Cela est utile lorsque vous souhaitez vous assurer qu'au moins une des deux questions est obligatoire.

Les questions sans réponse sont traitées comme des chaînes vides, notées par deux apostrophes simples `''`. Les conditions de logique d'obligation conditionnelle suivantes peuvent être utilisées :

| Condition de logique d'obligation conditionnelle | Description |
|:---------------------------|:-------------|
| `${question_référence} != ''` | Rendre obligatoire uniquement si `question_référence` a été répondue (non vide). |
| `${question_référence} = ''`  | Rendre obligatoire uniquement si `question_référence` n'a pas été répondue (vide). |

**feuille de calcul survey**

| type  | name    | label                                               | required     |
|:------|:--------|:----------------------------------------------------|:-------------|
| note  | contact | Veuillez fournir votre numéro de téléphone ou votre adresse e-mail ci-dessous. |              |
| text  | phone   | Numéro de téléphone                                        |              |
| text  | email   | Adresse e-mail                                       | ${phone} = '' |