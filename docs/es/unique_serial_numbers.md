# Crear seriales únicos

Hay ocasiones en las que puedes querer generar un serial único para cada uno de los formularios en un proyecto. Este artículo discute varias alternativas sobre cómo crear seriales únicos usando el tipo de pregunta `calculate` (cálculo).

## Enfoque 1: Crear seriales únicos secuenciales basados en fecha y hora

Este método funciona mejor con [formularios web de Enketo](data_through_webforms.md). Utiliza una función de cálculo para crear un serial único basado en la fecha y hora hasta el primer milisegundo. Aunque este método puede no satisfacer todas tus necesidades, debería darte una ilustración de cuánto puedes extender las funciones de cálculo.

Crea un
<a class="reference" href="calculate_questions.html">tipo de pregunta <code>calculate</code> (cálculo)</a> ya sea en el Formbuilder o en **XLSForm** y utiliza la fórmula a continuación.

```
concat(substr(today(), 0, 4), substr(today(), 5, 7), substr(today(), 8, 10), substr(now(), 11, 13), substr(now(), 14, 16), substr(now(), 17, 19))
```

<p class="note">
  La misma fórmula puede funcionar como una pregunta <code>integer</code> (número entero) cuando trabajas en un <strong>XLSForm</strong>.
</p>

![Calculate example](/images/unique_serial_numbers/calculate_example.png)

En el ejemplo, cuando previsualizas el formulario implementado en **Enketo**, deberías poder ver el serial dentro de la pregunta de tipo nota como se muestra en la imagen a continuación:

![Preview form](/images/unique_serial_numbers/preview_form.png)

## Enfoque 2: Crear seriales únicos a partir de variables seleccionadas

Este ejemplo muestra cómo crear seriales únicos a partir de variables existentes, ya definidas en tu formulario, utilizando la expresión
[`concat()`](https://docs.getodk.org/form-operators-functions/#concat)
en un tipo de pregunta `calculate` (cálculo). El ejemplo se muestra como un **XLSForm**, pero puede hacerse igual de fácilmente dentro del Formbuilder.

**hoja survey**

| type      | name    | label                                         | calculation                                                           |
| :-------- | :------ | :-------------------------------------------- | :-------------------------------------------------------------------- |
| text      | Q1      | Nombre de la región                           |                                                                       |
| text      | Q2      | Nombre del distrito                           |                                                                       |
| text      | Q3      | Nombre del grupo                              |                                                                       |
| text      | Q4      | Nombre de la aldea                            |                                                                       |
| text      | Q5      | Serial del hogar                              |                                                                       |
| calculate | Q1_C    |                                               | substr(${Q1}, 0, 3)                                                   |
| calculate | Q2_C    |                                               | substr(${Q2}, 0, 3)                                                   |
| calculate | Q3_C    |                                               | substr(${Q3}, 0, 3)                                                   |
| calculate | Q4_C    |                                               | substr(${Q4}, 0, 3)                                                   |
| calculate | ID      |                                               | concat(${Q1_C}, '-', ${Q2_C}, '-', ${Q3_C}, '-', ${Q4_C}, '-', ${Q5}) |
| note      | note_id | Tu identificación única para este formulario es: ${ID} |                                                                       |
| survey |

Cuando previsualizas el ejemplo en formularios web de **Enketo**, el serial se presentará dentro de la pregunta de tipo nota como se muestra en la imagen a continuación:

![Preview unique id](/images/unique_serial_numbers/preview_uniqueid.png)