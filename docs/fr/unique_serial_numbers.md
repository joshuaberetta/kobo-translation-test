# Créer des numéros de série uniques

Il peut arriver que vous souhaitiez générer un numéro de série unique pour chaque formulaire d'un projet. Cet article présente différentes solutions pour créer des numéros de série uniques à l'aide du type de question `calculate`.

## Approche 1 : Créer des numéros de série uniques séquentiels basés sur la date et l'heure

Cette méthode fonctionne mieux avec les [formulaires web Enketo](data_through_webforms.md). Elle utilise une fonction de calcul pour créer un numéro de série unique basé sur la date et l'heure à la première milliseconde près. Bien que cette méthode ne réponde pas nécessairement à tous vos besoins, elle devrait vous donner une illustration de la flexibilité des fonctions de calcul.

Créez une <a class="reference" href="calculate_questions.html">question de type <code>calculate</code></a> dans l'interface de création de formulaires ou dans un **XLSForm** et utilisez la formule ci-dessous.

```
concat(substr(today(), 0, 4), substr(today(), 5, 7), substr(today(), 8, 10), substr(now(), 11, 13), substr(now(), 14, 16), substr(now(), 17, 19))
```

<p class="note">
  La même formule peut fonctionner comme une question de type <code>integer</code> lorsque vous travaillez dans un <strong>XLSForm</strong>.
</p>

![Calculate example](/images/unique_serial_numbers/calculate_example.png)

Dans l'exemple, lorsque vous prévisualisez le formulaire déployé dans **Enketo**, vous devriez pouvoir voir le numéro de série dans la question de type note comme indiqué dans l'image ci-dessous :

![Preview form](/images/unique_serial_numbers/preview_form.png)

## Approche 2 : Créer des numéros de série uniques à partir de variables sélectionnées

Cet exemple montre comment créer des numéros de série uniques à partir de variables existantes déjà définies dans votre formulaire en utilisant l'expression [`concat()`](https://docs.getodk.org/form-operators-functions/#concat) dans une question de type `calculate`. L'exemple est présenté sous forme d'**XLSForm**, mais peut tout aussi facilement être réalisé dans l'interface de création de formulaires.

**onglet survey**

| type      | name    | label                                           | calculation                                                           |
| :-------- | :------ | :---------------------------------------------- | :-------------------------------------------------------------------- |
| text      | Q1      | Nom de la région                                |                                                                       |
| text      | Q2      | Nom du district                                 |                                                                       |
| text      | Q3      | Nom du groupement                               |                                                                       |
| text      | Q4      | Nom du village                                  |                                                                       |
| text      | Q5      | Numéro de série du ménage                       |                                                                       |
| calculate | Q1_C    |                                                 | substr(${Q1}, 0, 3)                                                   |
| calculate | Q2_C    |                                                 | substr(${Q2}, 0, 3)                                                   |
| calculate | Q3_C    |                                                 | substr(${Q3}, 0, 3)                                                   |
| calculate | Q4_C    |                                                 | substr(${Q4}, 0, 3)                                                   |
| calculate | ID      |                                                 | concat(${Q1_C}, '-', ${Q2_C}, '-', ${Q3_C}, '-', ${Q4_C}, '-', ${Q5}) |
| note      | note_id | Votre identifiant unique pour ce formulaire est : ${ID} |                                                                       |

Lorsque vous prévisualisez l'exemple dans les formulaires web **Enketo**, le numéro de série sera présenté dans la question de type note comme indiqué dans l'image ci-dessous :

![Preview unique id](/images/unique_serial_numbers/preview_uniqueid.png)