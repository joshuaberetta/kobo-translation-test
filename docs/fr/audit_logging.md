# Type de question méta pour le suivi d'activité

Le suivi d'activité peut être un outil utile pour surveiller le comportement des enquêteur(rice)s et découvrir quelles questions prennent plus de temps à répondre, mieux comprendre comment les enquêteur(rice)s naviguent dans un certain formulaire, et voir quels enquêteur(rice)s prennent généralement plus de temps pour soumettre des réponses.

<p class="note">Cette fonctionnalité nécessite l'analyse manuelle de fichiers CSV.</p>

La question méta de suivi d'activité est un type de question qui n'est pris en charge qu'en utilisant l'[application Android Collect](kobocollect_on_android_latest.md).

Pour ajouter un type de question méta `audit` à un formulaire et visualiser les données finalisées, veuillez suivre les étapes ci-dessous :

1. Dans un fichier XLSForm, ajoutez `audit` de la même manière que vous le feriez pour toute autre question méta. Ensuite, importez le fichier de formulaire dans votre projet et déployez le formulaire.

**onglet survey**

| type  | name  | label                       |
| :---- | :---- | :-------------------------- |
| start | start |                             |
| end   | end   |                             |
| audit | audit |                             |
| text  | Q1    | Q1. Quel est votre nom ? |

2. Collectez des données en utilisant l'[application Android Collect](kobocollect_on_android_latest.md) et renvoyez les formulaires finalisés au serveur. Collect enregistre les journaux d'activité pour chaque soumission dans un fichier CSV qui sont sauvegardés et importés sur le serveur de la même manière qu'une photo jointe le serait.

3. Une fois les données soumises, ouvrez votre projet dans le navigateur et allez dans **DONNÉES**, puis **Téléchargements**. Sélectionnez **Fichier média (ZIP)** comme type d'exportation, puis cliquez sur **Nouvel export**. Une fois le téléchargement terminé, cliquez sur le fichier pour le télécharger sur votre ordinateur.

![image](/images/audit_logging/zip_export.png)

4. Une fois le fichier ZIP extrait et ouvert, cliquez sur le fichier intitulé 'audit.csv' pour visualiser les journaux d'activité. Il est important de noter que le CSV utilise le temps [Unix Epoch](https://www.unixtimestamp.com/index.php), donc les journaux sont enregistrés en millisecondes.

5. Étant donné que les horodatages sont enregistrés pour chaque soumission individuelle, vous devrez probablement copier les valeurs dans une nouvelle feuille de calcul pour effectuer une analyse plus approfondie sur toutes les soumissions (par exemple, par enquêteur(rice) ou par question). La fusion de nombreux fichiers CSV différents peut être effectuée par [de nombreux outils gratuits ou en écrivant un script](https://www.google.com/search?q=merge+many+CSV). Pour lire des informations plus détaillées concernant la structure des journaux et les types d'événements, veuillez consulter l'excellente documentation d'ODK sur [l'enregistrement du comportement des enquêteur(rice)s](https://docs.getodk.org/form-audit-log/#).

N'hésitez pas à publier sur notre [forum communautaire](https://community.kobotoolbox.org/) pour partager votre approche ou script préféré pour utiliser cette fonctionnalité afin que d'autres puissent apprendre de votre exemple.