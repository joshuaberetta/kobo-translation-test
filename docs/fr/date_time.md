# Questions de type date et heure dans KoboToolbox

Il existe 3 types de questions de date et d'heure dans KoboToolbox : « Date », « Heure » et « Date et heure ».

La question de type « Date » permet de recueillir des valeurs de date, par exemple pour demander une date de naissance, etc. Dans KoboCollect et dans les formulaires web Enketo, un sélecteur de date de style calendrier s'affiche pour sélectionner la date.

La question de type « Heure » permet de recueillir des valeurs d'heure, par exemple pour une question comme « À quelle heure partez-vous au travail ? ». Dans KoboCollect et Enketo, un sélecteur d'heure s'affiche où l'utilisateur(rice) peut sélectionner sa réponse.

Le troisième type « Date et heure » permet de recueillir à la fois la date et l'heure dans une seule question.

## Comment configurer les questions de type Date et Heure

### Configuration dans l'interface de création de formulaires

L'ajout de questions « Date », « Heure » et « Date et heure » est simple :

- Dans l'interface de création de formulaires, cliquez sur le bouton <i class="k-icon k-icon-plus"></i> pour ajouter une nouvelle question
- Saisissez le texte de la question, par exemple « Quelle est votre date de naissance ? », puis cliquez sur **AJOUTER UNE QUESTION** ou appuyez sur ENTRÉE sur votre clavier
- Choisissez le type de question

![Ajout des questions](images/date_time/adding.gif)

### Configuration dans XLSForm

Pour ajouter des questions « Date », « Heure » et « Date et heure » dans XLSForm, utilisez les types de questions `date`, `time` et `datetime` comme indiqué dans l'exemple ci-dessous :

Dans XLSForm, vous pouvez configurer ce qui suit :

| type     | name      | label                                                   |
| :------- | :-------- | :------------------------------------------------------ |
| date     | dob       | À quelle date êtes-vous né(e) ?                         |
| time     | time      | À quelle heure partez-vous au travail ?                 |
| datetime | date_time | À quelle date et heure la formation a-t-elle commencé ? |
| survey   |

## Apparence des questions de type date et heure dans les formulaires web et KoboCollect

### Apparence par défaut

![Apparences par défaut](images/date_time/default_appearances.png)

### Apparences avancées

Lors de l'ajout d'une question de type « Date » dans l'interface de création de formulaires, vous pouvez choisir parmi plusieurs options d'affichage (sous les paramètres de la question). Les apparences modifient la façon dont la question s'affiche dans les formulaires web et dans KoboCollect.

Pour la question de type « Date », vous pouvez contrôler l'affichage du calendrier grégorien par défaut en choisissant entre les options « month-year » (mois année), « year » (année) et « no-calendar » (sans calendrier). En plus de ces options, vous pouvez également modifier le style de calendrier pour utiliser des calendriers non grégoriens pris en charge.

![Ajout d'apparences avancées](images/date_time/advanced_appearance.png)

Pour ajouter des valeurs d'apparence qui ne figurent pas dans la liste déroulante de l'interface de création de formulaires, choisissez « other » (autre) et saisissez la valeur d'apparence dans le champ de texte qui apparaît.

![Apparences avancées](images/date_time/advanced_appearances.png)

_\* Ces options doivent être saisies manuellement dans l'interface de création de formulaires après avoir sélectionné « other »._

### Ajout d'apparences personnalisées pour les questions de date dans XLSForm

Vous pouvez spécifier des apparences avancées dans XLSForm via la colonne `appearance` comme suit :

#### Apparences du sélecteur de date

| type   | name             | label                                                | appearance  |
| :----- | :--------------- | :--------------------------------------------------- | :---------- |
| date   | rains_start      | Quand les pluies de plantation ont-elles commencé ?  | month-year  |
| date   | year_migrate     | En quelle année avez-vous migré ?                    | year        |
| date   | no-calendar_date | Sélecteur de date sans calendrier                    | no-calendar |
| survey |

### Calendriers non grégoriens pris en charge

| type   | name                | label                                      | appearance     |
| :----- | :------------------ | :----------------------------------------- | :------------- |
| date   | coptic_date         | Sélecteur de date avec calendrier copte    | coptic         |
| date   | ethiopian_date      | Sélecteur de date avec calendrier éthiopien| ethiopian      |
| date   | islamic_date        | Sélecteur de date avec calendrier islamique| islamic        |
| date   | bikhram_sambat_date | Sélecteur de date avec calendrier Bikram Sambat | bikhram_sambat |
| date   | myanmar_date        | Sélecteur de date avec calendrier birman   | myanmar        |
| date   | persian_date        | Sélecteur de date avec calendrier persan   | persian        |
| survey |

## Utilisation des questions de date et d'heure dans la logique personnalisée

Lors de la définition d'une logique de saut personnalisée (`relevant`), de critères de validation (`constraint`) et de critères de réponse obligatoire (`required`) à l'aide du code XLSForm, les valeurs de date doivent être incluses [en utilisant la fonction `date()`](https://docs.getodk.org/form-operators-functions/#date), et au format `"AAAA-MM-JJ"`. Par exemple, si vous créez des critères de validation sur une question de date afin que toutes les réponses à l'enquête soient antérieures à la date « 10 avril 2022 », votre logique de validation sera `. < date('2022-04-11')`.

Pour utiliser des questions « Heure » dans la logique XLSForm, il est toujours recommandé de convertir les valeurs d'heure brutes en un nombre représentant l'heure sous forme de fraction d'une journée, appelé heure décimale. Vous pouvez le faire en utilisant [la fonction `decimal-time()`](https://docs.getodk.org/form-operators-functions/#decimal-time). Ensuite, vous pouvez comparer cette valeur avec une autre valeur d'heure décimale. Par exemple, si vous souhaitez limiter l'heure saisie dans une question à uniquement après 12h00, vous pouvez définir la logique de validation personnalisée suivante `decimal-time(.)>=0.5`.

Pour en savoir plus sur les sujets connexes :

- [Logique de saut](skip_logic.md)
- [Critères de validation](validation_criteria.md)
- [Fonctions de date et d'heure](https://docs.getodk.org/form-operators-functions/#date-and-time) (documentation ODK)

<p class="note">
  Vous pouvez télécharger l'exemple XLSForm
  <a
    download
    class="reference"
    href="./_static/files/date_time/date_time.xlsx"
    >ici <i class="k-icon k-icon-file-xls"></i></a
  >.
</p>