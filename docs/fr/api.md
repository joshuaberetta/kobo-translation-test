# Introduction à l'API

Une **interface de programmation d'application (API)** permet à deux composants logiciels de communiquer en utilisant un ensemble de définitions et de protocoles. Avec une API, un script ou une application peut fonctionner avec KoboToolbox sans utiliser l'interface web. Par exemple, vous pouvez générer automatiquement des exports de données qui se connectent à des sources externes telles que des tableaux de bord ou des dossiers de sauvegarde.

Avec l'**API** KoboToolbox, vous pouvez :

- **Télécharger des données** automatiquement en JSON, CSV ou XLSX.
- **Générer des exports à la demande** pour des tableaux de bord, des sauvegardes ou des analyses.
- **Soumettre ou modifier des soumissions** à partir d'autres outils de collecte de données.
- **Créer ou déployer des projets** et cloner des projets existants par code.
- **Gérer les utilisateur(rice)s**, les autorisations et l'activité des projets à grande échelle.

L'utilisation de l'API KoboToolbox vous permet d'automatiser les tâches routinières, de maintenir les tableaux de bord à jour et d'intégrer KoboToolbox à d'autres systèmes, tout en réduisant les étapes manuelles et les erreurs. Cet article fournit une introduction à l'API KoboToolbox et couvre les étapes suivantes :

- Récupération de votre **URL de serveur**
- Récupération de votre **clé API**
- Récupération de l'UID de l'actif du projet
- Exportation de vos données à l'aide de l'API
- Documentation avancée de l'API

## Récupération de votre URL de serveur

L'**URL de serveur** est l'adresse web de base de votre serveur KoboToolbox. Elle est placée au début de chaque requête API.

Pour la plupart des utilisateur(rice)s, l'URL de serveur est [kf.kobotoolbox.org](https://kf.kobotoolbox.org/) (si vous utilisez le serveur mondial) ou [eu.kobotoolbox.org](https://eu.kobotoolbox.org/) (si vous utilisez le serveur de l'Union européenne).

![Récupérer l'URL du serveur](images/api/server_URL.png)

## Récupération de votre clé API

Votre **clé API** est un jeton personnel qui agit comme un mot de passe, permettant à un logiciel d'accéder à votre compte via l'API. Elle peut être requise lorsqu'un script, un tableau de bord ou une application externe nécessite une authentification pour récupérer ou envoyer des données de projet via l'API.

Il existe différentes façons d'obtenir votre **clé API**.

**Méthode 1 :**

1. Cliquez sur l'icône de votre profil dans le coin supérieur droit.
2. Sélectionnez **PARAMÈTRES DU COMPTE**.
3. Accédez à l'onglet **Sécurité**.
4. Votre clé API est masquée par défaut. Cliquez sur **Afficher** pour la visualiser.

**Méthode 2 :**

Dans votre navigateur web, accédez à `https://[url-serveur]/token/?format=json`. Assurez-vous de remplacer `[url-serveur]` par votre URL de serveur.

**Méthode 3 :**

Dans le terminal, utilisez la commande curl suivante :

`curl -u nom_utilisateur:mot_de_passe "https://[url-serveur]/token/?format=json"`

Assurez-vous de remplacer `[url-serveur]` par votre URL de serveur.

## Récupération de l'UID de l'actif de votre projet

L'**UID de l'actif du projet** est un code unique qui identifie un projet KoboToolbox spécifique et doit être inclus dans les appels API pour cibler ce projet.

Vous pouvez trouver l'**UID de l'actif du projet** dans l'URL de la page de résumé de votre projet. Il s'agit de la chaîne de lettres et de chiffres qui apparaît après « forms/ » dans l'URL, comme suit : `https://[url-serveur]/#/forms/[UID de l'actif du projet]/summary`.

![Récupération de l'UID de l'actif du projet](images/api/project_UID.png)

## Exportation de vos données à l'aide de l'API

Il existe deux approches principales pour connecter vos données à l'aide de l'API avec KoboToolbox :

- **Exports synchronisés :** Renvoie un fichier CSV ou XLSX prêt à l'emploi, basé sur des paramètres d'exportation prédéfinis, que les applications externes (par exemple, Power BI ou Excel) peuvent charger directement.
- **Point de terminaison JSON :** Envoie chaque soumission sous forme de fichier JSON brut. C'est la meilleure option pour les pipelines basés sur du code, et non pour une utilisation directe dans des outils de feuilles de calcul ou de tableaux de bord.

Chaque approche nécessite de connaître l'URL du serveur et l'UID de l'actif du projet pour créer une URL d'exportation personnalisée. Selon l'application, votre clé API peut être nécessaire pour l'authentification.

<p class="note">
    Pour plus d'informations sur les exports synchronisés, consultez <a href="https://support.kobotoolbox.org/synchronous_exports.html">Utiliser l'API pour les exports synchronisées</a>. 
<br><br>
Pour en savoir plus sur la connexion de vos données à Power BI pour créer des tableaux de bord personnalisés, consultez <a href="https://support.kobotoolbox.org/pulling_data_into_powerbi.html">Connexion de KoboToolbox à Power BI</a>. 
<br><br>
Pour en savoir plus sur la connexion de vos données à Microsoft Excel, consultez <a href="https://support.kobotoolbox.org/pulling_data_into_excelquery.html">Connexion de KoboToolbox à Microsoft Excel</a>.
</p>

## Documentation avancée

La documentation de l'API à l'adresse `https://[url-serveur]/api/v2/docs/` fournit une interface interactive pour les points de terminaison de l'API. Elle remplace les informations précédemment présentées dans chaque point de terminaison.

| **Serveur KoboToolbox**    | **Documentation de l'API**                     |
| :----------------- | :--------------------------------------------- |
| Le serveur KoboToolbox mondial               | [https://kf.kobotoolbox.org/api/v2/docs/](https://kf.kobotoolbox.org/api/v2/docs/)  |
| Le serveur KoboToolbox Union européenne       | [https://eu.kobotoolbox.org/api/v2/docs/](https://eu.kobotoolbox.org/api/v2/docs/)  |

Ces pages de documentation avancée répertorient tous les points de terminaison, affichent les paramètres de requête autorisés, incluent une barre de recherche, affichent des exemples de réponses, montrent des exemples de réponses d'erreur et permettent de tester directement les requêtes dans votre navigateur. Utilisez cette documentation pour vérifier l'authentification, découvrir les fonctions et copier les URL exactes dans des scripts personnalisés.

Vous pouvez également télécharger le schéma de documentation de l'API au format YAML à l'adresse `https://[url-serveur]/api/v2/schema/` ou au format JSON à l'adresse `https://[url-serveur]/api/v2/schema/?format=json`.

<p class="note">
    <strong>Note :</strong> Les points de terminaison V1 sont désormais obsolètes et leur déclassement est prévu pour janvier 2026, au profit de l'API KPI v2, plus robuste et entièrement prise en charge. Pour plus d'informations sur la migration vers KPI v2, consultez <a href="https://support.kobotoolbox.org/migrating_api.html">Migration de l'API v1 vers l'API v2</a>.
</p>

Pour plus d'exemples d'utilisation de l'API, consultez ce [post du Forum communautaire](https://community.kobotoolbox.org/t/kobo-api-examples-using-new-kpi-endpoints/2742).