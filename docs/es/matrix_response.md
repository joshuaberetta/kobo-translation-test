# Tipo de respuesta de matriz de preguntas

El tipo de respuesta de matriz de preguntas permite a los/as usuarios/as crear un grupo de preguntas que se muestran en formato de matriz, donde cada celda dentro de la matriz representa una pregunta separada. Para usar este tipo de respuesta, define el número de filas y columnas que deseas en tu conjunto de matriz y asigna a cada fila y columna una etiqueta o nombre. Cada columna puede ser un tipo de pregunta diferente. En la captura de pantalla anterior, las primeras dos columnas son preguntas de seleccionar una, y la tercera columna es una pregunta de número.

![image](/images/matrix_response/matrix_example.png)

<p class="note">Este tipo de respuesta <strong>solo funciona cuando se usa Enketo</strong>, utilizando el <strong>diseño de tema de cuadrícula</strong>. Los formularios están configurados en diseño de página única de forma predeterminada; para cambiarlo, encuentra el botón "diseño" en la barra de herramientas del editor de formularios de KoboToolbox (Formbuilder), selecciona "tema de cuadrícula", guarda este cambio y vuelve a desplegar tu formulario para que estos cambios entren en vigor.</p>

<p class='note'>Enketo admite solo hasta <code>10</code> columnas en versiones anteriores a <code>2.8.0</code>, hasta <code>13</code> incluyendo y después de <code>2.8.0</code>.</p>

## Crear una matriz de preguntas en el editor de formularios

1. Ve a tu editor de formularios y haz click en "Agregar pregunta"
2. Selecciona 'Matriz de preguntas'

    ![image](/images/matrix_response/question_matrix.png)

3. Haz click en el ícono de engranaje en cada columna para establecer el tipo de pregunta.

    ![image](/images/matrix_response/question_type.png)

4. Selecciona el tipo de pregunta

5. Agrega la etiqueta de columna y la etiqueta de respuesta

    ![image](/images/matrix_response/label_response.png)

6. Selecciona el ícono de engranaje dentro de 'Fila' para definir la etiqueta de fila

    ![image](/images/matrix_response/row.png)

## Crear una matriz de preguntas en XLSForm

Alternativamente, también puedes crear una matriz de preguntas en un XLSForm siguiendo las instrucciones descritas en las imágenes a continuación:

**hoja survey**

| type             | name | label                                      | required | `kobo--matrix_list` |
| :--------------- | :--- | :----------------------------------------- | :------- | :----------------   |
| begin_kobomatrix | M1   | Artículos                                  |          | assets              |
| select_one yn    | Q1   | P1. ¿Qué artículos tienes en casa?         | TRUE     |                     |
| integer          | Q2   | P2. Número de artículos                    | TRUE     |                     |
| end_kobomatrix   |      |                                            |          |                     |
| survey |

**hoja choices**

| list_name | name | label      |
| :-------- | :--- | :--------- |
| assets    | car  | Auto       |
| assets    | bike | Bicicleta  |
| assets    | tv   | Televisión |
| yn        | yes  | Sí         |
| yn        | no   | No         |
| choices |

**hoja settings**

| style                        |
| :--------------------------- |
| theme-grid no-text-transform |
| settings |

<p class="note">Este método usa <code>begin_kobomatrix</code>,
<code>end_kobomatrix</code> y <code>kobo--matrix_list</code>.</p>

Siguiendo los pasos anteriores, deberías ver la matriz de preguntas que se muestra en la captura de pantalla a continuación (solo en [Enketo](data_through_webforms.md)):

![image](/images/matrix_response/preview.png)

También es posible incluir condiciones `relevant` y `constraint` dentro de la matriz de la siguiente manera:

**hoja survey**

| type             | name | label                                      | required | `kobo--matrix_list` | relevant      | constraint |
| :--------------- | :--- | :----------------------------------------- | :------- | :----------------   | :------------ | :--------- |
| begin_kobomatrix | M1   | Artículos                                  |          | assets              |               |            |
| select_one yn    | Q1   | P1. ¿Qué artículos tienes en casa?         | TRUE     |                     |               |            |
| integer          | Q2   | P2. Número de artículos                    | TRUE     |                     | ${Q1} = 'yes' | . > 2      |
| end_kobomatrix   |      |                                            |          |                     |               |            |
| survey |