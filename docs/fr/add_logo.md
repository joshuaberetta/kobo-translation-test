# Ajouter un logo personnalisé

Ajouter un logo personnalisé en haut de votre formulaire est un processus simple qui suit principalement les mêmes étapes que l'[ajout de contenu multimédia à vos formulaires](media.md).

Pour commencer :

1. Commencez par créer votre fichier image de logo et enregistrez-le avec un nom de fichier court.

2. Dans votre XLSForm, définissez la première question comme une question de type note, laissez le libellé vide et ajoutez une colonne intitulée `media::image` avec le nom de votre fichier de logo dans la cellule. Comme indiqué ci-dessous :

**onglet survey**

| type | name | label | media::image |
| :--- | :--- | :---- | :----------- |
| note | logo |       | logo.jpg     |
| survey|

3. Lorsque vous avez terminé de modifier le formulaire, importez l'XLSForm dans un projet nouveau ou existant.

4. Déployez ou redéployez votre formulaire, selon qu'il s'agit d'un nouveau projet ou qu'il remplace un formulaire existant.

5. Dans la page de votre projet, accédez à **PARAMÈTRES>MÉDIAS** et [importez](media.md) votre fichier `logo.jpg`.

## Conseils :

-   Gardez votre image petite.
-   Votre image de logo n'apparaîtra pas dans l'aperçu du formulaire, seulement lorsque le formulaire sera ouvert.
-   Sauter la dernière étape signifie que votre formulaire sera affiché sans les fichiers multimédias. Assurez-vous que les fichiers multimédias sont importés avant de télécharger le formulaire sur vos appareils lors de l'utilisation de l'application Android.

<p class="note">Si vous ouvrez l'interface de création de formulaires KoboToolbox (KoboToolbox Formbuilder) après avoir déployé votre XLSForm avec le fichier image du logo, elle attribuera automatiquement un libellé de texte à la question et vous devrez le supprimer pour que le texte automatisé n'apparaisse pas à côté de votre logo dans votre formulaire.</p>