# Tipo de pregunta de cálculo avanzado

Algunos formularios avanzados pueden requerir que se realice un cálculo interno como parte del formulario (en lugar de hacerlo después durante el análisis). Esto se puede hacer agregando un **Cálculo** y escribiendo la expresión matemática en el campo de etiqueta de la pregunta.

Este artículo proporciona instrucciones paso a paso sobre cómo agregar cálculos mientras usas el editor de formularios o descargándolo y agregándolo directamente al XLSForm.

Para ver una lista completa y detallada de todas las funciones, visita la excelente [documentación de funciones XPath de ODK](https://getodk.github.io/xforms-spec).

## Enfoques para agregar preguntas de cálculo:

### Usar el editor de formularios

Paso 1: Agrega una pregunta de cálculo

![image](/images/advanced_calculate/calculate_question.jpg)

Paso 2: Escribe tu fórmula de cálculo donde normalmente escribirías tu pregunta.

![image](/images/advanced_calculate/formulas.jpg)

Nota:

* Tu pregunta de cálculo no se mostrará al realizar la entrada/recolección de datos, ya sea en KoboCollect o Enketo. Sin embargo, se mostrará al ver los datos en la vista de tabla o en la versión descargada.
* Debes seguir reglas similares a las de los XLSForms (consulta nuestra sección de reglas a continuación).

### Usar XLSForms

Recomendamos este enfoque cuando trabajas con funciones de cálculo más avanzadas.

Los XLSForms permiten el uso de la función de cálculo en diferentes tipos de preguntas.

* Puedes imitar el enfoque utilizado en el editor de formularios donde la pregunta no se mostrará en la recolección de datos simplemente definiendo el tipo de pregunta como 'calculate' y luego escribiendo tu cálculo dentro de la columna calculate.
* Puedes usar 'calculate' para diferentes tipos de preguntas, y en este caso la pregunta se mostrará durante la recolección de datos. Puedes elegir hacer que esa pregunta sea de solo lectura para que nadie pueda cambiar la entrada. Los tipos de preguntas que hemos probado con este enfoque incluyen:

    a. integer (solo aceptará funciones de cálculo numéricas)  
    b. text (solo aceptará funciones de cálculo de cadenas)  
    c. note (solo aceptará referencias a preguntas y no funciones de cálculo)  
    d. date (solo aceptará funciones de cálculo de fecha)  
    e. time (solo aceptará funciones de cálculo de hora)
    
    ![image](/images/advanced_calculate/xls.png)

## Reglas al trabajar con preguntas de cálculo:

### Estas reglas se aplican tanto al editor de formularios como al XLSForm

1. No puedes usar cálculos numéricos y de cadenas dentro de la misma pregunta
2. Tus cálculos numéricos seguirán la regla BODMAS al aplicar cálculos, es decir, el orden de ejecución de los cálculos será Paréntesis, Divisiones, Multiplicaciones, Sumas y luego Restas (Recuerda siempre esto al ordenar una pregunta)
3. Las preguntas de cálculo que hacen referencia a otras preguntas no deben colocarse en el mismo grupo que las preguntas de referencia, ya que el cálculo no aparecerá a menos que te muevas del grupo
4. Al hacer referencia a una pregunta en un cálculo, debes indicarla como `${Pregunta}` donde pregunta es el nombre de la pregunta
5. Puedes "forzar" que un cálculo se evalúe configurando 'required' como TRUE

### Lista de funciones de cálculo probadas

_(No dudes en recomendar otras adicionales y las actualizaremos)_

![image](/images/advanced_calculate/list.png)

### Trabajar con el comando IF en cálculos

![image](/images/advanced_calculate/if_command.png)

### Soluciones alternativas para cálculos

_Recomendado para usuarios/as avanzados/as_

#### Solución alternativa 1: Crear preguntas ficticias para el cálculo de la puntuación final en una serie de preguntas

Digamos que tienes una pregunta como `P1 ¿Tienes una pregunta?` Respuestas `Sí=1 No=2 No sé=999`

En este caso, es posible que desees crear una P1 ficticia justo después de P1 para tener en cuenta las diferencias en la codificación y definir el equivalente matemático. Entonces crearás una pregunta de cálculo P1f (_nota: esta es mi propia convención de nomenclatura, f significa ficticia) y definirás el valor predeterminado como 0 pero escribirás la fórmula como **If (${P1}=1,1,0)**

Observa que en mi formulario de prueba logré crear la situación y los datos aparecen como codificados para P1 y como calculados para el significado matemático para P1f. Este debería ser el significado que pretende tu puntuación. _Puedes hacer esto para cálculos como riqueza donde Sí y No podrían significar un valor diferente en diferentes países._

Una vez que hagas esto para todas tus preguntas, puedes agregar una pregunta de cálculo que sume todas las ficticias como:

`${P1f}+${P2f}+ etc`