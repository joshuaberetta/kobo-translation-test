# Type de question Consentement

Le type de question « Consentement » affiche une seule option, pour sélectionner « OK » sur le formulaire.

Vous pouvez utiliser le type « Consentement » pour les questions qui ne nécessitent que 2 états de réponse : répondu et non répondu, ou accepté et non accepté. Vous pourriez utiliser ce type de question avec un consentement éclairé dans votre formulaire d'enquête, ou comme moyen de vous assurer que la personne interrogée a lu et accepte les conditions, généralement décrites à l'aide d'un [type de question « Note »](question_types.md).

## Comment configurer la question

1. Dans l'interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)**, cliquez sur le bouton <i class="k-icon k-icon-plus"></i> pour ajouter une nouvelle question.
2. Saisissez le texte de la question. Par exemple, « Si vous acceptez de poursuivre l'enquête, cliquez sur OK. »
3. Cliquez sur « <i class="k-icon k-icon-plus"></i> AJOUTER UNE QUESTION » (ou appuyez sur la touche Entrée du clavier).
4. Choisissez le type de question « <i class="k-icon k-icon-qt-acknowledge"></i> Consentement ».

![Ajouter la question de consentement](images/acknowledge/acknowledge_adding.gif)

## Comment elle s'affiche dans les formulaires web et KoboCollect

La question « Consentement » affiche un seul bouton radio avec le libellé « OK » comme indiqué ci-dessous :

![Questions de consentement dans KoboCollect et Enketo](images/acknowledge/acknowledge.png)

## Utiliser la logique de saut et les critères de validation

Une question « Consentement » n'a que 2 états de réponse : un où la question a reçu une réponse, et un où elle n'en a pas reçu, c'est-à-dire que la valeur de réponse est soit « OK » soit _vide_.

![Questions de consentement dans la logique de saut](images/acknowledge/acknowledge_skip.gif)

Dans l'exemple ci-dessus, le groupe « Enquête » ne sera affiché que si la question « Consentement » a reçu une réponse (l'utilisateur(rice) a cliqué sur OK).

Ci-dessous se trouve la logique de formulaire équivalente dans la syntaxe XLSForm :

**onglet survey**

| type        | name    | label                                                    | relevant          |
| :---------- | :------ | :------------------------------------------------------- | :---------------- |
| acknowledge | consent | Si vous acceptez de poursuivre l'enquête, cliquez sur OK |                   |
| begin_group | survey  | Enquête                                                  | ${consent} = "OK" |
| text        | name    | Quel est votre nom ?                                     |                   |
| integer     | age     | Quel âge avez-vous ?                                     |                   |
| end_group   |         |                                                          |                   |

<p class="note">
  Vous pouvez télécharger l'exemple XLSForm
  <a
    download
    class="reference"
    href="./_static/files/acknowledge/acknowledge.xlsx"
    >ici <i class="k-icon k-icon-file-xls"></i></a
  >.
</p>