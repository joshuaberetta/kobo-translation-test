# Styliser vos formulaires avec XLSForm

Avec KoboToolbox, vous pouvez personnaliser l'apparence de vos formulaires et questions pour mettre en évidence les informations clés et adapter la mise en page à vos besoins de collecte de données. Cela inclut l'application de thèmes aux formulaires web Enketo, l'ajout d'en-têtes et de listes dans les questions de type note, et l'utilisation de couleurs ou de mise en gras pour l'emphase.

Cet article couvre les thèmes pour les formulaires web Enketo ainsi que les options de stylisation pour les notes et questions au sein d'un formulaire.

<p class="note">
<strong>Note :</strong> Cet article se concentre sur la stylisation des formulaires en <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">XLSForm</a>. Pour en savoir plus sur la définition des thèmes Enketo dans l'interface de création de formulaires KoboToolbox (KoboToolbox Formbuilder), consultez <a href="https://support.kobotoolbox.org/alternative_enketo.html">Utiliser des styles alternatifs pour les formulaires web Enketo</a>.
</p>

## Thèmes pour les formulaires web Enketo

Les thèmes Enketo vous permettent de personnaliser l'apparence et la mise en page des [formulaires web Enketo](https://support.kobotoolbox.org/enketo.html). Les thèmes s'appliquent uniquement aux formulaires web Enketo et ne sont pas visibles dans KoboCollect.

### Ajouter des thèmes dans XLSForm

Pour ajouter un thème dans XLSForm :
1. Ajoutez une colonne **style** dans votre feuille `settings`.
2. Spécifiez le thème que vous souhaitez utiliser, en utilisant le nom exact indiqué dans le tableau ci-dessous.

**Feuille settings**

| style       |
|:------------|
| theme-grid  |

<p class="note">
<strong>Note :</strong> Les thèmes peuvent être combinés en saisissant les deux thèmes dans la même cellule de la colonne <code>style</code>, séparés par un espace (par exemple, <code>theme-grid pages</code>).
</p>

### Thèmes disponibles pour les formulaires web Enketo

Les thèmes suivants sont disponibles pour personnaliser vos formulaires :

| Thème XLSForm                | Description                                                                 | Aperçu |
|:-----------------------------|:----------------------------------------------------------------------------|:--------|
| Thème par défaut             | Affiche les questions les unes après les autres, sur une seule page.       | ![Style par défaut](images/form_style_xls/theme_default.png) |
| <code>pages</code>           | Affiche une question par écran ou un <a href="https://support.kobotoolbox.org/grouping_questions_xls.html">groupe de questions</a> ensemble sur le même écran, similaire à la mise en page de KoboCollect. | ![Style pages](images/form_style_xls/theme_pages.png) |
| <code>theme-grid</code>      | Un affichage alternatif plus compact, similaire aux formulaires papier, qui utilise l'espace efficacement en organisant plusieurs questions par ligne. Les questions sont en majuscules par défaut. Nécessite de <a href="https://support.kobotoolbox.org/form_style_xls.html#setting-up-an-xlsform-for-theme-grid">configurer votre XLSForm</a>. | ![Theme-grid](images/form_style_xls/theme_grid.png) |
| <code>theme-grid no-text-transform</code> | Identique à theme-grid, mais sans mise en majuscules automatique des questions. | ![Theme-grid no-text-transform](images/form_style_xls/theme_grid_no_text_transform.png) |

### Configurer un XLSForm pour theme_grid

Dans les formulaires web Enketo, la mise en page `theme_grid` vous permet d'afficher les questions en plusieurs colonnes, rendant votre formulaire plus compact et visuellement organisé. La configuration de ces colonnes, y compris leur nombre et leur largeur, est contrôlée en attribuant des `valeurs w` à chaque question dans la colonne **appearance** de votre XLSForm.

<p class="note">
  Pour un aperçu complet de l'utilisation de <code>theme_grid</code> dans XLSForm, consultez ce <a href="https://ee.kobotoolbox.org/n41GqUkf">tutoriel sur le thème Grid</a> et cet <a href="https://docs.google.com/spreadsheets/d/1qKmxPTA4B0vihU6GsKgi1CJE2Db2FfE7KZpOig4nTEI/edit?gid=0#gid=0">exemple de XLSForm</a>.
</p>

Avant d'attribuer des `valeurs w` à chaque question, commencez par placer toutes les questions dans des [groupes de questions](https://support.kobotoolbox.org/grouping_questions_xls.html). La largeur par défaut pour un groupe ou une répétition est de quatre colonnes (`w4`), donc un groupe avec `w4` peut contenir un maximum de quatre questions `w1` sur une seule ligne. La `valeur w` d'une question est relative à la `valeur w` de son groupe.

Pour spécifier la largeur relative de chaque question au sein d'une ligne :
1. Ajoutez une colonne **appearance** dans votre feuille `survey`.
2. Pour chaque question, attribuez des valeurs d'apparence (par exemple, `w1`, `w2`, `w3`) pour spécifier sa largeur relative au sein d'une ligne.
3. Modifiez la largeur du groupe si nécessaire en utilisant la même approche.

Les lignes s'étendront toujours automatiquement sur toute la largeur de la page. Par exemple, une ligne contenant une question avec une valeur d'apparence de `w2` et une autre avec `w1` divisera la ligne en deux tiers et un tiers, respectivement.

<p class="note">
<strong>Note :</strong> Appliquez les <code>valeurs w</code> uniquement aux groupes ou répétitions de premier niveau. Bien que leur application aux groupes ou répétitions imbriqués soit prise en charge, l'affichage peut ne pas être optimal.
</p>

## Styliser le texte

Vous pouvez utiliser Markdown et HTML dans XLSForm pour **styliser le texte**, **ajouter de l'emphase** avec du gras ou de l'italique, **créer des en-têtes** de différentes tailles, **modifier les polices et les couleurs**, et **ajouter des liens web cliquables**. La stylisation du texte peut être appliquée aux questions, notes et libellés de choix.

<p class="note">
<strong>Note :</strong> Certaines fonctionnalités de stylisation peuvent ne pas être prises en charge dans KoboCollect ou Enketo. Il est recommandé de prévisualiser vos formulaires dans votre méthode de collecte de données choisie pour confirmer que toutes les fonctionnalités de stylisation sont entièrement prises en charge.
</p>

Les fonctionnalités de stylisation de texte dans XLSForm incluent :
| Fonctionnalité | Formatage |
|:---------------|:-----------|
| Italique       | `*italique*` ou `_italique_` |
| Gras           | `**gras**` ou `__gras__` |
| Hyperlien      | `[nom du lien](url)` |
| En-têtes       | `# En-tête 1` (le plus grand) à `###### En-tête 6` (le plus petit) |
| Listes à puces | - Ceci est une liste non ordonnée<br>- en markdown |
| Listes numérotées | 1. Ceci est une liste numérotée<br>2. en markdown |
| Emojis         | Par exemple, 🙂 😐 🙁 😦 😧 😩 😱 |
| Exposant       | `100 m<sup>2</sup>` devient 100 m² |
| Indice         | `H<sub>2</sub>O` devient H₂O |
| Texte coloré   | `<span style="color:#f58a1f">orange</span>` devient <span style="color:#f58a1f">orange</span> <br>`<span style="color:red">rouge</span>` devient <span style="color:red">rouge</span> |
| Police         | `<span style="font-family:cursive">cursive</span>` devient <span style="font-family:cursive">cursive</span> <br>`<span style="color:red; font-family:cursive">rouge et cursive</span>` devient <span style="color:red; font-family:cursive">rouge et cursive</span>|
| Centrer        | `<p style="text-align:center">Libellé centré</p>` centre le texte à l'écran |

<p class="note">
<strong>Note :</strong> Utilisez le caractère <code>\</code> avant <code>#</code>, <code>*</code>, <code>_</code> et <code>\</code> pour empêcher que les effets de stylisation spéciaux ne soient déclenchés par ces caractères.
</p>