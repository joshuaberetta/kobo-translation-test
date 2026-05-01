# Collecte de données avec KoboCollect

<iframe src="https://www.youtube.com/embed/IEm61fpLoz4?si=TdlWhcVt0OxETlxl&cc_lang_pref=fr&hl=fr" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

KoboCollect est une application KoboToolbox gratuite et open source conçue pour la collecte de données sur les appareils mobiles Android. Avant de commencer, [installez et configurez](../fr/kobocollect_on_android_latest.md) l'application KoboCollect.

Une fois configurée, KoboCollect vous permet de remplir et d'envoyer des formulaires depuis votre appareil mobile, même hors ligne. Cet article explique comment utiliser l'application pour collecter des données, notamment comment accéder aux formulaires, enregistrer et modifier les réponses, et envoyer les soumissions finalisées.

## Télécharger des formulaires

Pour commencer la collecte de données avec KoboCollect, vous devrez télécharger le(s) formulaire(s) KoboToolbox sur votre appareil. Avant de télécharger, assurez-vous d'avoir :

- Au moins un [formulaire déployé](../fr/deploy_form_new_project.md) dans votre compte KoboToolbox (dont vous êtes propriétaire ou qui a été partagé avec vous).
- Un projet (compte) [configuré sur KoboCollect](../fr/kobocollect_on_android_latest.md).
- Une connexion Internet sur votre appareil.
  
Pour télécharger des formulaires sur votre appareil :
- Depuis le menu principal, appuyez sur **Télécharger formulaire**.
- Sélectionnez le(s) formulaire(s) que vous souhaitez télécharger individuellement en appuyant sur la case à cocher à côté de chaque formulaire, ou appuyez sur **Tout sélectionner** pour télécharger tous les formulaires déployés.
- Appuyez sur **Télécharger la sélection**.

Les formulaires téléchargés apparaîtront lorsque vous appuyez sur **Remplir un formulaire** depuis le menu principal de l'application.

<p class="note">
  <strong>Note :</strong> Vous devrez répéter ce processus chaque fois qu'une mise à jour est apportée au formulaire ou aux médias au sein du formulaire. Si vous prévoyez des mises à jour fréquentes du formulaire ou si vous utilisez la <a href="../fr/dynamic_data_attachment.md">liaison dynamique de projets</a>, nous vous recommandons d'activer le <a href="../fr/kobocollect_settings.md#form-management-settings">téléchargement automatique des formulaires</a>.
</p>

## Collecter des données

Une fois les formulaires téléchargés, vous pouvez commencer la collecte de données. Notez qu'une fois que vous avez téléchargé le(s) formulaire(s) dans l'application, vous n'avez pas besoin d'une connexion Internet pour collecter des données.

1. Depuis le menu principal, appuyez sur **Remplir un formulaire**.
2. Sélectionnez le formulaire avec lequel vous souhaitez collecter des données.
3. Pour changer la langue du formulaire, appuyez sur l'**icône à trois points** <i class="k-icon-more"></i> dans le coin supérieur droit de l'écran et appuyez sur **Changer la langue**.
4. Naviguez entre les questions en balayant vers la gauche ou en appuyant sur **SUIVANT** après avoir répondu.
5. À la fin de l'enquête, vous pouvez choisir d'**Enregistrer comme brouillon**, de **Finaliser** ou d'**Envoyer** le formulaire (selon vos [paramètres du projet](../fr/kobocollect_settings.md#form-management-settings)).

| **Option** | **Description**                                |
| :----------------- | :--------------------------------------------- |
| Enregistrer comme brouillon  &emsp;&emsp;&emsp;        | Le formulaire sera enregistré dans **Brouillons** et pourra toujours être modifié avant d'être finalisé. |
| Finaliser      | Le formulaire sera enregistré dans **Prêt à envoyer** et ne pourra plus être modifié. Cette option n'apparaît que si le paramètre **Envoi automatique** est défini sur **Désactivé**.                                  |
| Envoyer           | Le formulaire sera envoyé directement au serveur ou mis en file d'attente jusqu'à ce qu'une connexion Internet soit disponible. Il ne pourra plus être modifié. Cette option n'apparaît que si le paramètre **Envoi automatique** est activé.            |

Par défaut, les formulaires et les données restent sur l'appareil jusqu'à ce qu'ils soient supprimés manuellement. Si vous activez **Supprimer après envoi** dans les [paramètres du projet](../fr/kobocollect_settings.md#form-management-settings), les formulaires seront automatiquement supprimés une fois qu'ils auront été soumis au serveur.

## Modifier les brouillons

Si vous avez enregistré une enquête comme brouillon, vous pouvez la modifier avant de l'envoyer au serveur :

1. Depuis le menu principal, sélectionnez **Brouillons**.
2. Une liste des formulaires brouillons enregistrés apparaîtra. Sélectionnez celui que vous souhaitez modifier.
3. Apportez les modifications nécessaires, puis appuyez sur **Finaliser** ou **Envoyer**, selon votre flux de travail.

<p class="note">
  <strong>Note :</strong> Vous n'avez pas besoin d'une connexion Internet pour modifier un formulaire enregistré dans KoboCollect.
</p>

## Envoyer les formulaires finalisés au serveur

Après avoir finalisé vos formulaires, vous devez les importer sur le serveur KoboToolbox. Les formulaires sont souvent remplis et finalisés hors ligne, puis importés en masse une fois qu'une connexion Internet est disponible. Pour envoyer vos formulaires au serveur KoboToolbox :

1. Assurez-vous que l'appareil dispose d'une connexion Internet sécurisée.
2. Depuis le menu principal, appuyez sur **Prêt à envoyer**. Une liste de formulaires finalisés apparaîtra.
3. Appuyez sur **Tout sélectionner**, ou sélectionnez manuellement les formulaires que vous souhaitez importer en cochant la case.
4. Appuyez sur **Envoyer éléments sélectionnés** pour soumettre les formulaires au serveur.

Pour vérifier que l'importation a réussi, allez dans le menu principal et sélectionnez **Envoyés**. Vous verrez tous les formulaires envoyés au serveur, ainsi que leur date de synchronisation.

<p class="note">
  <strong>Note :</strong> Si votre projet est <strong>configuré pour envoyer automatiquement les formulaires finalisés</strong>, la page <strong>Prêt à envoyer</strong> n'apparaîtra pas dans le menu principal, et vous pouvez ignorer ces étapes. Pour plus d'informations sur les paramètres du projet dans KoboCollect, consultez l'article <a href="../fr/kobocollect_settings.md">Personnaliser les paramètres KoboCollect</a>.
</p>

## Supprimer les formulaires enregistrés et les formulaires vierges

Après avoir finalisé la collecte de données et importé tous les formulaires remplis sur le serveur, vous voudrez peut-être supprimer les données de formulaire restantes de l'application KoboCollect, à moins que la suppression automatique ne soit [déjà activée](../fr/kobocollect_settings.md#form-management-settings) pour votre appareil. Cela permet de protéger la confidentialité des données et d'éviter toute confusion lors de la collecte de données pour un nouveau projet.

Il existe deux types de formulaires qui peuvent être supprimés :

- **Formulaires enregistrés** : Il s'agit de formulaires pour lesquels des données ont été remplies, y compris les brouillons, les formulaires finalisés et les formulaires qui ont été envoyés au serveur.
- **Formulaires vierges** : Il s'agit de formulaires de collecte de données vides qui ont été téléchargés sur l'appareil depuis la page **Télécharger formulaire**. Ne supprimez ces formulaires qu'une fois la collecte de données terminée pour ceux-ci.
  
Pour supprimer des formulaires :
1. Depuis le menu principal, appuyez sur **Supprimer formulaire**. Vous verrez deux onglets.
2. Sous **Formulaires enregistrés** :
    - Appuyez sur **Tout sélectionner** pour supprimer tous les formulaires enregistrés, ou sélectionnez des formulaires individuels.
    - Appuyez sur **Supprimer la sélection**.
3. Sous **Formulaires vierges** :
    - Appuyez sur **Tout sélectionner** pour supprimer tous les formulaires vierges, ou sélectionnez des formulaires individuels.
    - Appuyez sur **Supprimer la sélection**.

<p class="note">
  <strong>Note :</strong> Vous n'avez pas besoin d'une connexion Internet pour supprimer les formulaires enregistrés dans KoboCollect. Cependant, si des formulaires vierges sont accidentellement supprimés hors ligne, une connexion Internet est nécessaire pour les récupérer afin de poursuivre la collecte de données. Pour éviter toute suppression accidentelle, vous pouvez définir des contrôles d'accès dans les <a href="../fr/kobocollect_settings.md#access-control">paramètres du projet</a>.
</p>