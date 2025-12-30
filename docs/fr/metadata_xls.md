# Métadonnées de formulaire dans XLSForm

Les questions de métadonnées collectent automatiquement des informations sur le processus de collecte de données, telles que la date, l'heure et l'appareil utilisé, sans nécessiter de saisie de la part du répondant.

Les questions de métadonnées ne sont pas visibles pour les répondants. Les informations collectées en arrière-plan peuvent être utilisées pour l'audit, pour garantir l'intégrité des données et pour soutenir l'analyse des données.

<p class="note">
<strong>Remarque :</strong> Cet article se concentre sur l'ajout de questions de métadonnées dans <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">XLSForm</a>. Pour en savoir plus sur l'ajout de questions de métadonnées dans l'interface de création de formulaires KoboToolbox (KoboToolbox Formbuilder), consultez <a href="https://support.kobotoolbox.org/form_meta.html">Paramètres de formulaire et métadonnées</a>.
</p>

## Ajouter des questions de métadonnées dans XLSForm

Les questions de métadonnées sont ajoutées à XLSForm de la même manière que tout autre type de question :

1. Saisissez le **type** de question de métadonnées dans une nouvelle ligne, en utilisant le nom exact indiqué [dans le tableau ci-dessous](https://support.kobotoolbox.org/metadata_xls.html#available-metadata-questions-in-xlsform).
2. Incluez un **nom** de question.
3. Les **libellés** de question ne sont pas requis, car ils ne sont pas affichés dans le formulaire.

**Feuille survey**

| type | name       | label        |
|:-----|:-----------|:-------------|
| start | start_time |              |
| end   | end_time   |              |

## Questions de métadonnées disponibles dans XLSForm

Les questions de métadonnées disponibles dans XLSForm incluent :

| Type       | Description |
|:--------------------|:-------------|
| `start` | Enregistre l'heure et la date exactes du début d'une soumission. |
| `end` | Enregistre la date et l'heure de finalisation d'une soumission. |
| `today` | Enregistre la date de la soumission. |
| `deviceid` | Enregistre l'identification unique de l'appareil ou du navigateur utilisé pour collecter les données. Le <code>deviceid</code> est généré automatiquement et ne peut pas être modifié par les utilisatrices et utilisateurs.<br><br>**Remarque :** Dans KoboCollect, le <code>deviceid</code> est mis à jour chaque fois que l'application est réinstallée sur un appareil. Dans Enketo, le <code>deviceid</code> est réinitialisé chaque fois qu'une nouvelle fenêtre de navigateur est utilisée. |
| `username` | Dans KoboCollect, enregistre le nom d'utilisateur enregistré dans les <a href="https://support.kobotoolbox.org/kobocollect_settings.html#user-and-device-identity-settings">paramètres de l'application KoboCollect</a>. Si aucun nom d'utilisateur n'est défini, il enregistre celui utilisé pour se connecter au serveur.<br>Dans Enketo, enregistre le nom d'utilisateur du compte uniquement si <a href="https://support.kobotoolbox.org/project_sharing_settings.html#allowing-submissions-without-authentication">l'authentification est requise</a>.<br><br>**Remarque :** Étant donné que le champ `username` peut être modifié dans KoboCollect, il peut ne pas correspondre au compte utilisé pour s'authentifier au serveur. Pour voir quel compte a soumis les données, consultez le champ `_submitted_by` généré automatiquement.|
| `phonenumber` | Enregistre le numéro de téléphone stocké dans les <a href="https://support.kobotoolbox.org/kobocollect_settings.html#user-and-device-identity-settings">paramètres de l'application KoboCollect</a>. Cette question de métadonnées n'est pas prise en charge dans Enketo. |
| `email` | Enregistre l'adresse e-mail des <a href="https://support.kobotoolbox.org/kobocollect_settings.html#user-and-device-identity-settings">paramètres de l'application KoboCollect</a>. Cette question de métadonnées n'est pas prise en charge dans Enketo. |
| `start-geopoint` | Capture les coordonnées GPS lorsque le formulaire est ouvert pour la première fois. Peut être utilisé pour préchauffer le GPS de l'appareil afin que les questions GPS ultérieures puissent atteindre des lectures précises plus rapidement. |
| `background-geopoint` | Capture les coordonnées GPS lorsqu'une question spécifique reçoit une réponse. La question doit être spécifiée dans la colonne <code>trigger</code> de la question <code>background-geopoint</code>. |
| `background-audio` | Enregistre l'audio en arrière-plan pendant qu'un formulaire est ouvert. Pour en savoir plus sur cette fonctionnalité, consultez <a href="https://support.kobotoolbox.org/recording-interviews.html">Enregistrement d'entretiens avec enregistrement audio en arrière-plan</a>. | 
| `audit` | Capture un journal détaillé du processus d'entretien, y compris l'heure de début, l'heure de fin, l'emplacement et les actions de l'utilisateur pendant l'ensemble du processus de collecte de données. Cette question de métadonnées n'est pas prise en charge dans Enketo.<br><br>Pour en savoir plus sur l'utilisation de la question audit pour les journaux d'audit et la configuration des paramètres, consultez <a href="https://docs.getodk.org/form-audit-log/">Journal d'audit de formulaire (ODK)</a>. |

## Configurer les métadonnées dans KoboCollect

L'adresse e-mail, le numéro de téléphone et le nom d'utilisateur par défaut peuvent être [configurés](https://support.kobotoolbox.org/kobocollect_settings.html#user-and-device-identity-settings) et modifiés dans l'application KoboCollect :
1. Ouvrez l'application KoboCollect.
2. Appuyez sur l'**icône Projet** dans le coin supérieur droit de votre écran.
3. Appuyez sur **Paramètres**.
4. Faites défiler jusqu'à **Identité de l'utilisateur et de l'appareil**, puis **Métadonnées de formulaire**.
5. Saisissez le nom d'utilisateur, le numéro de téléphone et/ou l'adresse e-mail. Vous pouvez également consulter l'ID d'appareil actuel.