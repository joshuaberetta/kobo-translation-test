# Options avancées pour l'export des données

Les options avancées offrent un meilleur contrôle et une plus grande flexibilité lors du téléchargement et de l'export de vos données. Cet article vous guidera dans la personnalisation de vos exports de données, de la sélection des champs de données et de la gestion de différents types de questions à la définition de paramètres pour différents besoins analytiques.

<p class="note">
    Pour en savoir plus sur le téléchargement de données, y compris un aperçu des types d'export et des formats disponibles, consultez l'article <a href="https://support.kobotoolbox.org/fr/export_download.html?highlight=export">Exporter et télécharger vos données.</a>
</p>

## Options d'export pour les questions à choix multiples

L'option **{{ui:Exporta ##SELECT_MANY## preguntas como…}}** vous permet de choisir comment exporter les données des questions **{{ui:Choix multiple}}** (également appelées `select_multiple`). Vous pouvez choisir de les exporter comme :

| **Option d'export**    | **Description**                                |
| :----------------- | :------------------------------------ |
| Colonnes uniques et distinctes &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;              | Ce paramètre par défaut exporte une colonne avec toutes les options sélectionnées des questions <strong>{{ui:Choix multiple}}</strong>, plus des colonnes individuelles pour chaque réponse, comme indiqué ci-dessous.<br> ![How to select many columns](images/advanced_export/select_many_columns.png) |
| Colonnes distinctes  | Chaque réponse aux questions <strong>{{ui:Choix multiple}}</strong> sera exportée dans des colonnes distinctes.|
| Colonne unique   | Les réponses aux questions <strong>{{ui:Choix multiple}}</strong> seront exportées dans une seule colonne.            |


<p class="note">
  <strong>Note :</strong> Dans les colonnes distinctes, une valeur de « 1 » indique que l'option a été sélectionnée, tandis que « 0 » signifie que le/la répondant(e) n'a pas choisi cette option.
</p>

## Sélectionner les champs de données à exporter

Les options d'export avancées vous permettent d'affiner votre téléchargement de données en incluant les données de toutes les versions du formulaire ou en sélectionnant des questions spécifiques à exporter.

| **Paramètre d'{{ui:Exporter}}**    | **Description**                                |
| :----------------- | :------------------------------------ |
| Inclure les champs des […] versions &emsp;&emsp;&emsp;&emsp;&emsp;&emsp; | Par défaut, cette option est cochée. Cela vous permet de télécharger les données de toutes les versions du formulaire, y compris les questions ou choix supprimés. Si elle n'est pas cochée, seules les données de la dernière version déployée du formulaire seront téléchargées. |
| Sélectionner les questions à exporter | Pour exporter les données de questions spécifiques, activez cette option et sélectionnez les questions à inclure. |
| Plage de données | Pour exporter les données soumises dans une plage de dates spécifique, activez cette option et sélectionnez les dates de début et/ou de fin. Les filtres de date sont basés sur l'heure de soumission et utilisent le fuseau horaire UTC. Les données soumises aux dates de <strong>début</strong> et de <strong>fin</strong> sont incluses dans les exports. |

![How to select data fields](images/advanced_export/select_data_fields.png)

## Options supplémentaires de format de données

KoboToolbox offre des options supplémentaires de format de données pour personnaliser davantage vos exports, telles que l'inclusion des noms de groupes dans les en-têtes, le stockage des réponses de date et de nombre sous forme de texte, ou l'inclusion des URL des médias.

| **Paramètre d'{{ui:Exporter}}**    | **Description**                                |
| :----------------- | :------------------------------------ |
| Inclure les groupes dans les en-têtes | Choisissez cette option pour ajouter les noms de groupes à chaque en-tête de question, comme indiqué dans l'exemple ci-dessous. ![Include groups in headers](images/advanced_export/group_headers2.png) | 
| Enregistrer les réponses date et nombre sous forme de texte &emsp;&emsp;&emsp;&emsp;&emsp;&emsp; | Par défaut, les questions <strong>{{ui:Date}}, {{ui:Date et heure}}, {{ui:Chiffre}},</strong> et <strong>{{ui:Décimale}}</strong> sont enregistrées avec leurs types de données correspondants lors de l'export vers XLS. Cochez cette option si vous préférez les exporter sous forme de texte.<br><br><strong>Note :</strong> Les formats de temps Excel ne prennent pas en charge les données de fuseau horaire ; par conséquent, toutes les données de fuseau horaire dans la valeur de réponse seront supprimées lors de l'export. Pour conserver ces informations, cochez l'option pour exporter les dates sous forme de valeurs textuelles. |
| Inclure les URL des médias | Si votre formulaire a collecté des médias (photos, audio, vidéos ou fichiers), cochez cette option pour vous assurer que votre fichier exporté inclut des liens vers ces fichiers multimédias. |

## Enregistrer les paramètres d'export

Vous pouvez enregistrer vos paramètres d'export définis pour une utilisation future ou pour générer un lien d'[export synchronisé](https://support.kobotoolbox.org/fr/synchronous_exports.html) pour des logiciels comme PowerBI ou Excel.

| **Paramètre d'{{ui:Exporter}}** | **Description**                                |
| :-------------------- | :------------------------------------ |
| Enregistrer la sélection sous… &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;| Cochez cette option et saisissez un nom pour vos paramètres d'export. Lorsque vous cliquez sur <strong>{{ui:Exporter|upper}}</strong>, ces paramètres seront enregistrés et le nom apparaîtra dans la zone <strong>{{ui:Appliquer les paramètres d'exportation enregistrés}}</strong>. | 

Pour utiliser les paramètres d'export enregistrés, cliquez sur le menu déroulant sous **{{ui:Appliquer les paramètres d'exportation enregistrés}}** et sélectionnez les paramètres d'export nommés de votre choix.