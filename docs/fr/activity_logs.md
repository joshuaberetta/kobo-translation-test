# Journaux d'activité

Les journaux d'activité sont des enregistrements numériques qui capturent les actions et événements importants dans votre compte KoboToolbox. Les journaux d'activité vous donnent un historique détaillé de l'accès au compte et de l'activité du projet.
Ces journaux peuvent être utiles pour :

-   Surveillance de la sécurité : Voir qui a accédé à votre compte et d'où
-   Suivi des modifications : Savoir quand les éléments du projet ont été modifiés
-   Responsabilité : Identifier quels membres de l'équipe ont effectué des modifications spécifiques
-   Résolution de problèmes : Comprendre quand et comment des problèmes ont pu survenir

KoboToolbox fournit deux types de journaux d'activité pour vous aider à surveiller différents aspects de votre travail :

-   **Journaux d'accès :** Soutiennent la sécurité du compte en affichant toutes les connexions.
-   **Journaux d'historique de projet :** Suivent toutes les actions et modifications effectuées par n'importe quel utilisateur(rice) dans un projet spécifique et ses données.


<p class="note">
  <b>Note :</b> Les journaux d'activité sont un ajout relativement récent à KoboToolbox. Nous travaillons activement à l'expansion de ces fonctionnalités dans les mois à venir et à fournir un compte encore plus détaillé des actions dans vos comptes et projets.
</p>

## Journaux d'accès

Les journaux d'accès enregistrent tous les événements d'authentification (connexions) pour votre compte KoboToolbox. Ils vous aident à surveiller la sécurité du compte en vous montrant quand et où votre compte a été accédé.

Ils se trouvent sous le titre « Activité récente du compte », que vous pouvez atteindre facilement en ouvrant vos Paramètres du compte sous la section Sécurité.

Les journaux d'accès affichent :

-   Date et heure de chaque connexion
-   Adresse IP (informations de localisation)
-   Source (informations sur l'appareil et le navigateur)

![image](/images/activity_logs/Logs-image01.jpg)

Notez que les événements similaires (authentifications) se produisant dans les 60 minutes les uns des autres seront regroupés.

### Exporter les journaux d'accès

![image](images/activity_logs/Logs-image02.jpg)

Cette section vous permet également d'exporter tous vos enregistrements d'accès en cliquant sur le bouton « Exporter les données du journal » dans le coin supérieur droit du tableau. Cliquer sur ce bouton déclenchera le processus d'exportation des données :
1. Le traitement des enregistrements dans un fichier d'exportation .csv commencera
2. Une fenêtre modale s'affichera vous informant que le processus a commencé et quelles sont les prochaines étapes.
3. Vous recevrez un email avec un lien pour télécharger le fichier une fois qu'il sera prêt. La quantité de données incluses dans vos journaux déterminera le temps nécessaire pour recevoir l'email.
4. Cliquer sur l'URL dans l'email devrait immédiatement démarrer le téléchargement du fichier .csv, selon les paramètres de votre navigateur.

Le fichier d'exportation inclura des informations plus détaillées de tous les événements d'authentification, y compris le type d'authentification et le timing exact.

### Se déconnecter de tous les appareils

Vous pouvez forcer tous les appareils actuellement connectés à votre compte à se déconnecter immédiatement en cliquant sur le lien « Se déconnecter de tous les appareils » à gauche du bouton d'exportation des données.

Cette action vous déconnectera également de votre session actuelle.

## Journaux d'historique de projet

Les journaux d'historique de projet fournissent un enregistrement détaillé de toutes les activités au sein d'un projet spécifique. Ils montrent chaque action effectuée, que ce soit par les utilisateur(rice)s ou par des processus automatisés, vous donnant une visibilité complète sur l'historique de votre projet.

Pour voir les journaux d'un projet spécifique, allez dans l'onglet PARAMÈTRES de votre projet et allez dans la section Activité.

![image](/images/activity_logs/Logs-image3.jpg)

Dans cette page, vous trouverez une vue en tableau avec toute l'activité du projet, triée par date. Chaque action unique est listée avec l'utilisateur(rice) qui l'a effectuée et l'horodatage associé à cette activité.

Les journaux d'historique de projet capturent presque toutes les actions possibles qui peuvent être effectuées dans un projet.

| Catégorie                         | Actions incluses                                                                                                                                    |
| :---------------------------------| :---------------------------------------------------------------------------------------------------------------------------------------------------|
| Modifications du projet           | Mises à jour du nom du projet, Déploiements et redéploiements, Archivage et désarchivage, Connexions de projets                                    |
| Modifications du formulaire       | Importations XLSForm, Modifications du formulaire, Création de questions d'analyse qualitative                                                      |
| Modifications de gestion de données | Exportations de données, Modifications des pièces jointes multimédias, Modifications des paramètres de partage de données, Modifications des services REST |
| Autorisations                     | Mises à jour de l'accès utilisateur(rice), Paramètres d'accès public, Transferts de propriété                                                      |
| Soumissions                       | L'utilisateur(rice) modifie ou supprime des soumissions. L'ajout de soumissions est affiché dans l'exportation des journaux, mais pas dans l'interface KoboToolbox |

### Trouver et enquêter sur des activités spécifiques

Vous pouvez filtrer le journal d'historique par type d'activité (par exemple, déploiements, modifications de formulaire, modifications d'autorisations, etc.) en utilisant la fonctionnalité de basculement dans le coin supérieur droit. Cela permettra également aux propriétaires et gestionnaires de projet de suivre rapidement les changements/mises à jour sur des aspects spécifiques du projet.

![image](/images/activity_logs/Logs-GIF01.gif)

Vous pouvez également exporter toutes vos données d'historique de projet en utilisant le bouton d'exportation dans le coin supérieur droit de votre tableau.
Si vous avez besoin de plus d'informations sur une activité spécifique, cliquez simplement sur « Voir les détails » pour une vue étendue de cette entrée. Cela affichera toutes les informations sur cet événement, révélant ce qui s'est produit dans le backend et toutes les métadonnées associées.

## Problèmes courants avec les journaux d'activité

**« Je ne vois pas les activités récentes »**
-   Vérifiez que vous regardez le bon projet
-   Assurez-vous d'avoir les bonnes autorisations pour voir les journaux. Seuls les propriétaires de projet et les utilisateur(rice)s avec des autorisations de « gestion de projet » peuvent voir les journaux.
-   Notez que les journaux ne sont disponibles que pour une période de 60 jours. Les journaux plus anciens sont supprimés et ne sont pas récupérables. Cette période peut être configurée au niveau administrateur pour les organisations avec un serveur privé.

**« J'ai besoin de données de journal plus anciennes »**
-   Les données au-delà de la période de rétention sont automatiquement supprimées et ne sont pas récupérables. Si vous avez besoin d'avoir accès à des données de journal de plus de 60 jours et que vous utilisez un serveur privé, vous pouvez contacter votre administrateur pour augmenter la période de rétention.

**« Je ne peux pas télécharger le fichier d'exportation des données du journal »**
-   Lorsque vous cliquez sur le lien que vous avez reçu par email pour télécharger le fichier d'exportation des données du journal, il peut ouvrir une page web avec du texte au lieu de télécharger le fichier csv.
-   Pour télécharger le fichier .csv depuis la page web, faites un clic droit sur la page et sélectionnez Enregistrer la page sous…. Conservez le format comme « Source de la page »
-   Si vous cliquez sur le lien et obtenez un message d'erreur, tel que 403 Interdit, essayez d'ouvrir le lien avec un autre navigateur (par exemple, Safari).

![image](/images/getting_started_organization_feature/organizations_project_views.gif)