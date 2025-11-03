# Tipo de pregunta Consentimiento

El tipo de pregunta "Consentimiento" muestra una única opción para seleccionar "OK" en el formulario.

Puedes usar el tipo "Consentimiento" para preguntas que requieren solo 2 estados de respuesta: respondida y no respondida, o aceptada y no aceptada. Podrías usar este tipo de pregunta con un consentimiento informado en tu formulario de encuesta, o como una forma de asegurar que el/la entrevistado/a ha leído y acepta los términos, generalmente descritos usando un [tipo de pregunta "Nota"](question_types.md).

## Cómo configurar la pregunta

1. En el editor de formularios de KoboToolbox (Formbuilder), haz click en el botón <i class="k-icon k-icon-plus"></i> para agregar una nueva pregunta.
2. Escribe el texto de la pregunta. Por ejemplo, "Si aceptas continuar con la encuesta, haz click en OK."
3. Haz click en "<i class="k-icon k-icon-plus"></i> AGREGAR PREGUNTA" (o presiona la tecla Enter en el teclado).
4. Elige el tipo de pregunta "<i class="k-icon k-icon-qt-acknowledge"></i> Consentimiento".

![Agregando la pregunta de consentimiento](images/acknowledge/acknowledge_adding.gif)

## Cómo se muestra en formularios web y KoboCollect

La pregunta "Consentimiento" muestra un único botón de opción con la etiqueta "OK" como se muestra a continuación:

![Preguntas de consentimiento en KoboCollect y Enketo](images/acknowledge/acknowledge.png)

## Uso de lógica de omisión y criterios de validación

Una pregunta "Consentimiento" tiene solo 2 estados de respuesta: uno donde la pregunta es respondida, y uno donde no lo es, es decir, el valor de respuesta es "OK" o _en blanco_.

![Preguntas de consentimiento en lógica de omisión](images/acknowledge/acknowledge_skip.gif)

En el ejemplo anterior, el grupo "Encuesta" solo se mostrará si la pregunta "Consentimiento" fue respondida (el/la usuario/a hizo click en OK).

A continuación se muestra la lógica de formulario equivalente en sintaxis XLSForm:

**hoja survey**

| type        | name    | label                                              | relevant          |
| :---------- | :------ | :------------------------------------------------- | :---------------- |
| acknowledge | consent | Si aceptas continuar con la encuesta, haz click en OK |                   |
| begin_group | survey  | Encuesta                                             | ${consent} = "OK" |
| text        | name    | ¿Cuál es tu nombre?                                 |                   |
| integer     | age     | ¿Cuántos años tienes?                                   |                   |
| end_group   |         |                                                    |                   |
| survey |

<p class="note">
  Puedes descargar el ejemplo de XLSForm
  <a
    download
    class="reference"
    href="./_static/files/acknowledge/acknowledge.xlsx"
    >aquí <i class="k-icon k-icon-file-xls"></i></a
  >.
</p>