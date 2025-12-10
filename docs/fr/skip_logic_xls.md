# Ajouter un branchement conditionnel dans XLSForm

Le branchement conditionnel, également connu sous le nom de logique de pertinence, vous permet de **déterminer quand une question ou un groupe de questions sera affiché** dans le formulaire en fonction d'une question précédente ou du résultat d'un calcul. Par exemple, vous pouvez l'utiliser pour poser des questions de suivi uniquement à un sous-ensemble de répondant(e)s, ou pour masquer des sections entières d'un formulaire si elles ne sont pas pertinentes.

<p class="note">
  Pour en savoir plus sur la logique de formulaire dans XLSForm, consultez <a href="https://support.kobotoolbox.org/form_logic_xls.html">Introduction à la logique de formulaire dans XLSForm</a>.
</p>

Cet article couvre les sujets suivants :
- Ajouter un branchement conditionnel à des questions individuelles
- Combiner plusieurs conditions de branchement conditionnel
- Ajouter un branchement conditionnel basé sur le fait qu'une question a été répondue ou non
- Ajouter un branchement conditionnel à des groupes de questions

<p class="note">
  <strong>Remarque :</strong> Cet article se concentre sur l'ajout de branchement conditionnel dans <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">XLSForm</a>. Pour en savoir plus sur l'ajout de branchement conditionnel dans l'interface de création de formulaires KoboToolbox (KoboToolbox Formbuilder), consultez <a href="https://support.kobotoolbox.org/skip_logic.html">Ajouter un branchement conditionnel dans l'interface de création de formulaires</a>.
    <br><br>
Pour une pratique concrète du branchement conditionnel dans XLSForm, consultez le <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">cours XLSForm Fundamentals</a> de KoboToolbox Academy.
</p>

## Ajouter des conditions de branchement conditionnel à des questions individuelles

Le branchement conditionnel utilise le [référencement de questions](https://support.kobotoolbox.org/form_logic_xls.html#question-referencing) pour n'afficher que les questions pertinentes pour le ou la répondant(e) en fonction des réponses précédentes. La question utilisée pour définir la logique de pertinence est appelée la **question de référence**.

Pour ajouter un branchement conditionnel dans XLSForm :
1. Ajoutez une colonne **relevant** à la feuille `survey`.
2. Dans la ligne de la question que vous souhaitez afficher ou masquer, saisissez la condition qui doit être remplie **pour que la question soit affichée.**

**Feuille survey**

| type         | name     | label             | relevant     |
|:--------------|:----------|:------------------|:--------------|
| integer       | age       | Quel âge avez-vous ?  |               |
| select_one yn | married   | Êtes-vous marié(e) ?  | ${age} > 18   |

Dans l'exemple ci-dessus, `${age}` est la question de référence, et la réponse à `${age}` doit être supérieure à 18 pour que la question « Êtes-vous marié(e) ? » soit affichée.

### Formater les conditions de branchement conditionnel

Le format de la condition de branchement conditionnel diffère selon le **type** de la question de référence, comme détaillé dans le tableau ci-dessous.

| Type de question de référence | Condition de branchement conditionnel | Exemple |
|:-------------------------|:--------------------|:---------|
| select_one | `${question_de_référence} = 'nom_du_choix'` | `${consentement} = 'oui'` |
| select_multiple | `selected(${question_de_référence}, 'nom_du_choix')` | `selected(${raisons}, 'autre')` |
| integer | `${question_de_référence}` suivi d'un opérateur logique (>, <, =) et d'un nombre (ou d'une référence à une autre question) | `${age} >= 18` |
| date | `${question_de_référence}` suivi d'un opérateur logique (>, <, =) et de `date('AAAA-MM-JJ')` | `${date_naissance} >= date('1975-01-01')` |

<p class="note">
  Pour en savoir plus sur la construction d'expressions de logique de formulaire dans XLSForm, consultez <a href="https://support.kobotoolbox.org/form_logic_xls.html">Introduction à la logique de formulaire dans XLSForm</a>.
</p>

## Combiner plusieurs conditions de branchement conditionnel

Plusieurs conditions de pertinence peuvent être combinées en une seule expression pour déterminer quand une question est affichée en fonction d'une réponse précédente. Les conditions peuvent être combinées à l'aide des opérateurs logiques **and**, **or** et **not** :

- Utilisez **and** lorsque toutes les conditions doivent être remplies pour qu'une question soit affichée.
    - Par exemple : <code>${age} > 18 <strong>and</strong> ${etudiant} = 'non'</code>
- Utilisez **or** lorsqu'au moins une condition doit être remplie pour qu'une question soit affichée.
    - Par exemple : <code>${age} < 18 <strong>or</strong> ${etudiant} = 'oui'</code>
- Utilisez **not** pour indiquer qu'une condition ou un ensemble de conditions ne doit pas être rempli (par exemple, lorsque deux conditions ne peuvent pas être vraies ensemble pour qu'une question soit affichée).
    - Par exemple : <code><strong>not</strong>(${age} > 18 <strong>and</strong> ${etudiant} = 'oui')</code>

**Feuille survey**

| type         | name     | label              | relevant                          |
|:--------------|:----------|:-------------------|:----------------------------------|
| integer       | age       | Quel est votre âge ?  |                                   |
| select_one yn | employe  | Êtes-vous employé(e) ?  | ${age} >= 16 <strong>and</strong> ${age} <= 75     |

## Ajouter un branchement conditionnel basé sur le fait qu'une question a été répondue ou non

En plus d'ajouter un branchement conditionnel basé sur une réponse spécifique, vous pouvez ajouter un branchement conditionnel basé sur le fait qu'une question a été répondue ou laissée vide. Cela peut être utile pour ajouter des questions de suivi, ou lors de l'utilisation de [questions de consentement](https://support.kobotoolbox.org/acknowledge.html) dans votre formulaire.

Les questions non répondues sont traitées comme des chaînes vides, notées par deux apostrophes simples `''`. Les conditions de branchement conditionnel suivantes peuvent être utilisées :

| Condition de branchement conditionnel | Description |
|:---------------------|:-------------|
| `${question_de_référence} != ''` | Afficher uniquement si `question_de_référence` est répondue (non vide). |
| `${question_de_référence} = ''` | Afficher uniquement si `question_de_référence` n'est pas répondue (vide). |

**Feuille survey**

| type         | name      | label                | relevant             |
|:--------------|:-----------|:---------------------|:---------------------|
| text          | pourquoi_rejoint | Pourquoi avez-vous rejoint ?    |                      |
| select_one yn | benefices   | Constatez-vous des bénéfices ? | ${pourquoi_rejoint} != '' |

## Ajouter des conditions de branchement conditionnel à des groupes de questions

Le branchement conditionnel peut être appliqué aux groupes de questions ainsi qu'aux questions individuelles. Appliquer un branchement conditionnel à un groupe affichera ou masquera toutes les questions de ce groupe en fonction des réponses précédentes.

Pour ajouter un branchement conditionnel à des groupes de questions :
1. Ajoutez une colonne **relevant** à la feuille `survey`.
2. Dans la ligne **begin_group** du groupe de questions que vous souhaitez afficher ou masquer, saisissez la condition qui doit être remplie **pour que le groupe soit affiché.**

**Feuille survey**

| type         | name        | label                                         | relevant            |
|:-------------|:------------|:---------------------------------------------|:-------------------|
| select_one yn | rejoint     | Avez-vous rejoint l'association ?                |                     |
| begin_group  | association | Participation à l'association                    | ${rejoint} = 'oui'  |
| date         | date_adhesion | Quand avez-vous rejoint l'association ?           |                     |
| select_one yn | vote      | Avez-vous déjà voté lors d'une élection pour l'association ? |                     |
| end_group    |             |                                              |                     |