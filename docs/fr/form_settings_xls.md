# Paramètres de formulaire dans XLSForm

XLSForm vous permet de configurer les paramètres de vos formulaires en utilisant la feuille de calcul `settings`. Par exemple, vous pouvez spécifier un titre de formulaire, définir une langue par défaut ou suivre les numéros de version.

Cet article explique comment ajouter et utiliser les paramètres de formulaire disponibles dans XLSForm.

<p class="note">
<strong>Remarque :</strong> Cet article se concentre sur les paramètres de formulaire dans <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">XLSForm</a>. Pour en savoir plus sur la configuration des paramètres de formulaire dans l'interface de création de formulaires KoboToolbox (KoboToolbox Formbuilder), consultez <a href="https://support.kobotoolbox.org/form_meta.html">Paramètres de formulaire et métadonnées</a>.
</p>

## Ajouter des paramètres de formulaire dans XLSForm

Pour ajouter des paramètres de formulaire dans XLSForm :
1. Ajoutez une feuille de calcul `settings` à votre XLSForm.
2. Créez une nouvelle colonne pour chaque paramètre, en utilisant le nom de colonne exact indiqué [dans le tableau ci-dessous](https://support.kobotoolbox.org/form_settings_xls.html#available-form-settings-in-xlsform).
3. Sous chaque paramètre, spécifiez la valeur pertinente (voir l'exemple ci-dessous).

**Feuille de calcul settings**

| form_title            | version | default_language | style |
|:----------------------|:--------|:----------------|:------|
| Paramètres de formulaire dans XLSForm | v3     | Français (fr)    | pages |
| settings | 

## Paramètres de formulaire disponibles dans XLSForm

Les paramètres de formulaire disponibles dans XLSForm incluent :

| Paramètre de formulaire               | Description |
|:----------------------------|:------------|
| <code>form_title</code>     | Spécifie le titre du formulaire qui est affiché aux utilisatrices et utilisateurs. Cela peut également être défini et géré dans KoboToolbox lorsque le formulaire est importé. |
| <code>version</code>        | Inclut une chaîne de caractères qui représente la version actuelle du XLSForm (par exemple, v1 ou AAAAMMJJ). Utile pour suivre les versions de formulaire lors de la collaboration. |
| <code>instance_name</code>  | Spécifie un nom unique pour chaque soumission de formulaire en utilisant les champs remplis par l'utilisatrice ou l'utilisateur pendant l'enquête. Apparaît dans le tableau de données pour chaque soumission. Peut être utilisé pour créer des identifiants personnalisés de participant(e)s ou de soumissions.<br><br>Par exemple, <code>concat(${lname}, '-', ${fname}, '-', today())</code> renvoie <code>nomdefamille-prenom-date</code>. |
| <code>default_language</code> | Définit la langue par défaut dans les <a href="https://support.kobotoolbox.org/language_xls.html">formulaires traduits</a>. Le format <strong>langue (code)</strong> est utilisé, tel que défini sur le <a href="https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry">site web du registre de langues IANA</a>. |
| <code>style</code>          | Spécifie un <a href="https://support.kobotoolbox.org/form_style_xls.html">thème alternatif pour les formulaires web Enketo</a>. |
| <code>allow_choice_duplicates</code> | Permet à un XLSForm de réutiliser des noms d'options dupliqués <strong>au sein</strong> d'une liste de choix (par exemple, lors de l'utilisation de filtres de choix où les noms de choix sont dupliqués). |
| <code>public_key</code>     | Spécifie la clé publique pour les <a href="https://support.kobotoolbox.org/encrypting_forms.html?highlight=encryption">formulaires avec chiffrement activé</a>. |