# Gérer les listes de choix dans XLSForm

XLSForm simplifie la création et la gestion des **listes de choix** pour les formulaires d'enquête. Cela est particulièrement utile pour les listes longues ou répétitives, telles que les noms de pays ou de villes. Les listes de choix sont définies pour les [questions](https://support.kobotoolbox.org/question_types_xls.html#select-question-types) de type `select_one`, `select_multiple` ou `rank`.

Cet article détaille comment définir et gérer les listes de choix dans XLSForm pour des formulaires complexes, y compris les bonnes pratiques pour définir les noms de choix.

<p class="note">
Pour en savoir plus sur la création de formulaires dans XLSForm, consultez <a href="getting_started_xlsform.html">Se lancer avec XLSForm</a>.
</p>

## Définir les listes de choix dans XLSForm

Les listes de choix sont définies dans la feuille `choices` de votre XLSForm. La feuille `choices` comprend trois colonnes obligatoires :

| Colonne | Description |
| :---------  | :--------  |
| `list_name` | Identifiant unique pour une liste de choix, qui relie la question dans la feuille `survey` à sa liste de choix dans la feuille `choices`. |
| `name` | Nom court et unique utilisé pour faire référence à chaque choix. |
| `label` | Texte du choix tel qu'il sera affiché dans le formulaire. |

Pour définir une liste de choix dans XLSForm :

1.  Dans la feuille `choices`, saisissez le **nom de la liste de choix** dans la colonne `list_name`.
2.  Saisissez un `name` court et un `label` pour chaque option, en utilisant le même `list_name` pour toutes les options de la liste.

**Feuille choices**

| list_name | name | label |
| :---------  | :---------  | :---------  |
| marital_options | single | Célibataire |
| marital_options | married | Marié(e) |
| marital_options | separated_divorced | Séparé(e)/Divorcé(e) |
| marital_options | widowed | Veuf/Veuve |
| choices |

3.  Dans la feuille `survey`, ajoutez votre question d'enquête. Dans la colonne `type`, saisissez le type de question suivi d'un espace simple, puis le `list_name` de votre liste de choix.
    - Une liste de choix peut être réutilisée dans plusieurs questions de la feuille `survey`.

**Feuille survey**

| type | name | label |
| :---------  | :---------  | :---------  |
| acknowledge | consent | Acceptez-vous de poursuivre l'entretien ? |
| select_one marital_options | marital_status | Quel est votre état civil ? |
| survey |

 
## Bonnes pratiques pour définir les noms de choix

Lorsque les données sont téléchargées au [format valeurs XML et en-têtes](https://support.kobotoolbox.org/export_download.html#value-and-header-format), chaque question apparaît comme sa propre variable ou colonne dans le jeu de données. Les valeurs à l'intérieur de chaque colonne sont les **noms de choix** définis dans votre feuille `choices`, plutôt que les libellés complets affichés aux répondant(e)s. Ce format est recommandé pour l'analyse, car il fournit des noms de variables courts et cohérents ainsi que des valeurs codées plus faciles à utiliser que les libellés complets des questions ou des options.

Lors de la définition des noms de choix :
- Utilisez uniquement des **lettres, des chiffres et des traits de soulignement**. Les espaces et les caractères spéciaux ne sont pas autorisés.
- Évitez les chaînes de texte très longues ou complexes, car ces valeurs apparaîtront dans votre jeu de données exporté et pourront être utilisées dans la [logique de formulaire](https://support.kobotoolbox.org/form_logic_xls.html).
- Gardez les noms **cohérents** d'une liste à l'autre pour faciliter l'analyse des données.
 

## Gérer les listes de choix dans XLSForm

### Réutiliser les listes de choix

L'utilisation de **`list_name`** dans XLSForm vous permet de **réutiliser facilement les listes de choix** dans plusieurs questions, éliminant ainsi le besoin de les saisir manuellement à nouveau. Par exemple, vous pouvez créer une liste de choix `yes_no` et l'appliquer à toutes vos questions Oui/Non. Cela permet de créer des formulaires de manière plus efficace et cohérente.

### Traduire les listes de choix

XLSForm simplifie la traduction des listes de choix. Vous pouvez ajouter plusieurs libellés pour différentes langues, chaque traduction étant dans une colonne **`label`** distincte. Les noms de choix sous-jacents restent les mêmes, ce qui garantit que le jeu de données exporté est cohérent d'une traduction à l'autre et facilite l'analyse.

<p class="note">
Pour en savoir plus sur l'ajout de traductions dans XLSForm, consultez <a href="language_xls.html">Ajouter des traductions dans XLSForm</a>.
</p>

### Fichiers médias comme choix

En plus du texte, les choix dans XLSForm peuvent également être des **fichiers médias**, tels que des images, de l'audio ou de la vidéo. Cela améliore l'expérience d'enquête en fournissant des indices visuels ou auditifs aux répondant(e)s.

<p class="note">
Pour en savoir plus sur l'utilisation de fichiers médias comme choix, consultez <a href="media.html">Ajouter des médias à un XLSForm</a>.
</p>

### Filtrer les listes de choix

XLSForm vous permet de filtrer les listes de choix en fonction des réponses aux questions précédentes. Cette fonctionnalité, connue sous le nom de **filtres de choix**, peut être utilisée de diverses manières. Par exemple, elle peut être utilisée pour les **questions de sélection en cascade**, où la liste de choix d'une question enfant (par exemple, les villes) est filtrée en fonction de la réponse à une question parent (par exemple, le pays). Elle peut également être utilisée pour filtrer une question à choix multiples afin d'afficher uniquement les options sélectionnées dans une question précédente.

<p class="note">
Pour en savoir plus sur le filtrage des listes de choix dans XLSForm, consultez <a href="choice_filters_xls.html">Ajouter des filtres de choix dans XLSForm</a>.
</p>

### Dupliquer les noms de choix

Au sein d'une liste de choix donnée, **les noms de choix doivent être uniques**. Cependant, le même nom de choix peut être réutilisé dans différentes listes. Par exemple, une liste de choix `yes_no` et une liste de choix `yes_no_maybe` peuvent toutes deux inclure les noms de choix `yes` et `no`.

Par défaut, le déploiement d'un formulaire avec des noms de choix répétés dans la même liste entraînera une erreur. Cependant, lors de l'utilisation de filtres de choix, vous pouvez avoir besoin d'autoriser les noms de choix en double au sein d'une liste. Pour activer cette option, activez le paramètre `allow_choice_duplicates` dans votre feuille `settings`.

<p class="note">
Pour plus d'informations, consultez <a href="form_settings_xls.html">Paramètres de formulaire dans XLSForm</a>.
</p>

### Gérer les longues listes de choix

Pour les très grandes listes de choix, contenant des centaines ou des milliers d'options, il est recommandé d'utiliser les types de questions `select_one_from_file` ou `select_multiple_from_file`, qui relient une question d'enquête à un **fichier externe** contenant la liste de choix. Cette approche est plus efficace que la saisie manuelle des choix dans l'XLSForm, permet d'éviter les temps de chargement lents et les XLSForms volumineux, et simplifie la gestion ou la modification d'ensembles d'options étendus.

<p class="note">
Pour en savoir plus sur les listes de choix externes dans XLSForm, consultez <a href="select_from_file_xls.html">Sélectionner des options à partir d'un fichier externe</a>.
</p>