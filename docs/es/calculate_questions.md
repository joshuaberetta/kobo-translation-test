# Tipo de pregunta Cálculo

Algunos formularios avanzados pueden requerir que se realice un cálculo interno como parte del formulario (en lugar de hacerlo después durante el análisis). Esto se puede hacer agregando un Cálculo y escribiendo la expresión matemática en el campo de etiqueta de la pregunta.

![image](/images/calculate_questions/calculation.gif)

Una expresión matemática podría ser tan simple como `5 + 1`, pero lo más probable es que incluya una referencia a otra pregunta.

Para hacer referencia a otras preguntas en tu pregunta de cálculo, es necesario asignar nombres fijos a otras preguntas a través de la configuración de la pregunta, como `niñas` o `ingresos`. Al hacer referencia a esas preguntas, siempre debes usar el nombre único de la pregunta (no la etiqueta) - `${niñas}` o `${ingresos}`

Por ejemplo, si quieres convertir la respuesta a una pregunta sobre los ingresos de alguien a otra moneda (como de francos ruandeses a dólares estadounidenses), debes escribir `${ingresos} div 688`.

También puedes usar la respuesta a esta pregunta de Cálculo para otros propósitos, como construir tu lógica de omisión (por ejemplo, hacer una pregunta de seguimiento solo por encima de cierto umbral de ingresos) o mostrándola dentro de una Nota ([ver aquí](responses_inside_question.md) para obtener ayuda sobre cómo mostrar la respuesta a una pregunta en la etiqueta de otra pregunta).

## Lista de funciones disponibles

Hay muchas opciones diferentes disponibles, como la función round() (por ejemplo, `round(${int_1} div ${int_2}, 1`) redondeará el resultado de una división a un solo decimal). Para obtener una lista de algunas de las muchas expresiones matemáticas que se pueden usar en este campo, consulta las [especificaciones de XForm sobre funciones de cálculo](https://docs.getodk.org/form-operators-functions/) para conocer los antecedentes técnicos de todas las funciones disponibles en KoboToolbox y XLSForms. Para el uso avanzado de cálculos en KoboToolbox, consulta [este artículo](advanced_calculate.md).

## Lista de operadores matemáticos disponibles

| Operador               | Descripción                         |
| :--------------------- | :---------------------------------- |
| `+`                    | Suma                                |
| `-`                    | Resta                               |
| `*`                    | Multiplicación                      |
| `div`                  | División                            |
| `=`                    | Igual                               |
| `!=`                   | No igual                            |
| `<`                    | Menor que                           |
| `<=`                   | Menor o igual que                   |
| `>`                    | Mayor que                           |
| `>=`                   | Mayor o igual que                   |
| `or`                   | O                                   |
| `and`                  | Y                                   |
| `mod`                  | Módulo (residuo de la división)     |
| `pow([base], [power])` | Potencia / exponente                |