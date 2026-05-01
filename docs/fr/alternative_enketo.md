# Utiliser des styles alternatifs pour les formulaires web Enketo

Les formulaires web Enketo peuvent être personnalisés dans la façon dont vos questions sont présentées.
Deux styles alternatifs peuvent être sélectionnés et même combinés :
**Pages multiples** et **Thème de grille**.

Le mode **Pages multiples** affiche une question à la fois par écran, ou un [groupe
de questions](group_repeat.md) configuré pour s'afficher sur le même écran. C'est la même façon dont
KoboCollect fonctionne.

Le **Thème de grille** est un affichage alternatif des questions conçu pour être plus compact
et plus proche des formulaires papier où l'espace est souvent une préoccupation majeure. theme-grid
permet d'afficher plusieurs questions par ligne et s'adapte de manière flexible en cas de logique de saut
faisant apparaître ou disparaître une nouvelle question. Pour afficher plusieurs questions
sur une ligne, elles doivent faire partie d'un groupe, qui par défaut affiche jusqu'à quatre
questions côte à côte. Ce thème peut être personnalisé en définissant le
nombre de questions à inclure dans chaque ligne via le champ apparence des
paramètres de chaque question. Pour plus de détails,
[consultez cet article](https://blog.enketo.org/gorgeous-grid).

Il est également possible d'utiliser à la fois **Pages multiples** et **Thème de grille** ensemble.
Vous pouvez définir ces styles via l'interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)** :

![image](/images/alternative_enketo/multiple_grid.gif)

Si vous créez votre projet d'enquête via XLSForm, vous pouvez faire de même
en définissant le thème dans la colonne `style` de l'onglet `settings` :

**onglet settings**

| form_title        | style |
| :---------------- | :---- |
| Formulaire thématisé | pages |
| settings          |       |

## Styles disponibles dans XLSForm :

| Thème XLSForm                        | Description                                                    |
| :----------------------------------- | :------------------------------------------------------------- |
| (laisser vide)                       | Par défaut – page simple                                       |
| `theme-grid no-text-transform`       | Thème de grille                                                |
| `theme-grid`                         | Thème de grille avec les titres en lettres MAJUSCULES         |
| `pages`                              | Pages multiples                                                |
| `theme-grid pages no-text-transform` | Thème de grille + pages multiples                              |
| `theme-grid pages`                   | Thème de grille + pages multiples + titres en lettres MAJUSCULES |