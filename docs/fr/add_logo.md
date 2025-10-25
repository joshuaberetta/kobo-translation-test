# Ajouter un logo personnalisé
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/47cbc8887d6df73ef3bf760d5a3962b77ab26ed8/source/add_logo.md" class="reference">29 Jul 2025</a>

Ajouter un logo personnalisé en haut de votre formulaire est un processus simple qui suit principalement les mêmes étapes que [l'ajout de contenu média à vos formulaires](media.md).

Pour commencer :

1. Commencez par créer votre fichier image de logo et enregistrez-le avec un nom de fichier court.

2. Dans votre XLSForm, faites de la première question un type de question Note, laissez l'étiquette vide et ajoutez une colonne intitulée `media::image` avec le nom de votre fichier de logo dans la cellule. Comme indiqué ci-dessous :

**feuille survey**

| type | name | label | media::image |
| :--- | :--- | :---- | :----------- |
| note | logo |       | logo.jpg     |
| survey|

3. Lorsque vous avez terminé de modifier le formulaire, importez l'XLSForm vers un nouveau projet ou un projet existant.

4. Déployez ou redéployez votre formulaire, selon qu'il s'agit d'un nouveau projet ou qu'il remplace un formulaire existant dans votre compte.

5. Dans la page de votre projet, allez dans **PARAMÈTRES>MÉDIAS** et [importez](media.md) votre fichier `logo.jpg`.

## Conseils :

-   Gardez votre image aussi petite que possible pour améliorer les temps de chargement.
-   Votre image de logo n'apparaîtra pas dans l'aperçu du formulaire, seulement lorsque le formulaire est ouvert.
-   Sauter la dernière étape signifiera que votre formulaire sera affiché sans les fichiers médias. Assurez-vous que les fichiers médias sont importés avant de télécharger le formulaire sur vos appareils lors de l'utilisation de l'application Android.

<p class="note">Si vous ouvrez l'interface de création de formulaires après avoir déployé votre XLSForm avec le fichier image du logo, elle donnera automatiquement à la question une étiquette de texte et vous devrez la supprimer pour que le texte automatisé n'apparaisse pas à côté de votre logo dans votre formulaire.</p>