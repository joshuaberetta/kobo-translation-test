# Tipos de preguntas de fecha y hora

Existen 3 tipos diferentes de preguntas de fecha y hora en KoboToolbox: "Fecha",
"Hora" y "Fecha y hora".

El tipo de pregunta "Fecha" sirve para capturar valores de fecha, por ejemplo al
preguntar por la fecha de nacimiento, etc. Tanto en KoboCollect como en los
formularios web de Enketo, se mostrará un selector de fecha estilo calendario
para seleccionar la fecha.

El tipo de pregunta "Hora" sirve para capturar valores de hora, por ejemplo en
una pregunta como "¿A qué hora sales al trabajo?" Tanto en KoboCollect como en
Enketo, se muestra un selector de hora donde el/la usuario/a puede seleccionar
su respuesta.

El tercer tipo "Fecha y hora" sirve para capturar respuestas de fecha y hora en
una sola pregunta.

## Cómo configurar los tipos de preguntas de Fecha y Hora

### Configuración en el editor de formularios de KoboToolbox (Formbuilder)

Añadir preguntas de "Fecha", "Hora" y "Fecha y hora" es sencillo:

- En el editor de formularios de KoboToolbox (Formbuilder), click en el botón
  <i class="k-icon k-icon-plus"></i> para añadir una nueva pregunta
- Escribe el texto de la pregunta, por ejemplo "¿Cuál es tu fecha de
  nacimiento?", luego click en **AÑADIR PREGUNTA** o presiona ENTER en tu
  teclado
- Elige el tipo de pregunta

![Añadir las preguntas](images/date_time/adding.gif)

### Configuración en XLSForm

Para añadir preguntas de "Fecha", "Hora" y "Fecha y hora" en el XLSForm, usa
los tipos de pregunta `date`, `time` y `datetime` como se muestra en el ejemplo
a continuación:

En XLSForm, puedes configurar lo siguiente:

| type     | name      | label                                                    |
| :------- | :-------- | :------------------------------------------------------- |
| date     | dob       | ¿En qué fecha naciste?                                   |
| time     | time      | ¿A qué hora sales al trabajo?                            |
| datetime | date_time | ¿En qué fecha y hora comenzó la capacitación?            |
| survey   |

## Aspecto de los tipos de preguntas de fecha y hora en formularios web y KoboCollect

### Aspecto predeterminado

![Aspectos predeterminados](images/date_time/default_appearances.png)

### Aspectos avanzados

Al añadir el tipo de pregunta "Fecha" en el editor de formularios, puedes elegir
entre varias opciones de visualización (en la configuración de la pregunta). Los
aspectos cambian la forma en que se muestra la pregunta en los formularios web y
en KoboCollect.

Para el tipo de pregunta "Fecha", puedes controlar cómo se muestra el calendario
gregoriano predeterminado eligiendo entre las opciones "month-year", "year" y
"no-calendar". Además de estas opciones, también puedes cambiar el estilo del
calendario a calendarios no gregorianos compatibles.

![Añadir aspectos avanzados](images/date_time/advanced_appearance.png)

Para añadir valores de aspecto que no están listados en el menú desplegable del
editor de formularios, elige "other" y escribe el valor del aspecto en el campo
de texto que aparece.

![Aspectos avanzados](images/date_time/advanced_appearances.png)

_\* Estas opciones deben ingresarse manualmente en el editor de formularios
después de seleccionar "other"._

### Añadir aspectos personalizados para preguntas de fecha en XLSForm

Puedes especificar aspectos avanzados en XLSForm a través de la columna
appearance (aspecto) de la siguiente manera:

#### Aspectos del selector de fecha

| type   | name             | label                                                      | appearance  |
| :----- | :--------------- | :--------------------------------------------------------- | :---------- |
| date   | rains_start      | ¿Cuándo comenzaron las lluvias de siembra?                 | month-year  |
| date   | year_migrate     | ¿En qué año migraste?                                      | year        |
| date   | no-calendar_date | Selector de fecha sin calendario                           | no-calendar |
| survey |

### Calendarios no gregorianos compatibles

| type   | name                | label                                       | appearance     |
| :----- | :------------------ | :------------------------------------------ | :------------- |
| date   | coptic_date         | Selector de fecha con calendario copto      | coptic         |
| date   | ethiopian_date      | Selector de fecha con calendario etíope     | ethiopian      |
| date   | islamic_date        | Selector de fecha con calendario islámico   | islamic        |
| date   | bikhram_sambat_date | Selector de fecha con calendario Bikram Sambat | bikhram_sambat |
| date   | myanmar_date        | Selector de fecha con calendario birmano    | myanmar        |
| date   | persian_date        | Selector de fecha con calendario persa      | persian        |
| survey |

## Usar preguntas de fecha y hora en lógica personalizada

Al definir lógica de omisión personalizada (relevant), criterios de validación
(constraint) y criterios de respuesta obligatoria (required) usando código
XLSForm, los valores de fecha deben incluirse
[usando la función `date()`](https://docs.getodk.org/form-operators-functions/#date),
y en el formato `"YYYY-MM-DD"`. Por ejemplo, si estás creando criterios de
validación en una pregunta de fecha para que todas las respuestas de la encuesta
sean anteriores a la fecha "10 de abril de 2022", tu lógica de validación será
`. < date('2022-04-11')`.

Para usar preguntas de "Hora" en la lógica de XLSForm, siempre es buena idea
convertir los valores de hora sin procesar en un número que represente la hora
como una fracción de un día, llamado hora decimal. Puedes hacer esto usando
[la función `decimal-time()`](https://docs.getodk.org/form-operators-functions/#decimal-time).
Luego, puedes comparar este valor con otro valor de hora decimal. Por ejemplo,
si deseas limitar la hora ingresada en una pregunta a solo después de las 12 del
mediodía, puedes definir la siguiente lógica de validación personalizada
`decimal-time(.)>=0.5`.

Aprende más sobre temas relacionados:

- [Lógica de omisión](skip_logic.md)
- [Criterios de validación](validation_criteria.md)
- [Funciones de fecha y hora](https://docs.getodk.org/form-operators-functions/#date-and-time)
  (documentación de ODK)

<p class="note">
  Puedes descargar el ejemplo de XLSForm
  <a
    download
    class="reference"
    href="./_static/files/date_time/date_time.xlsx"
    >aquí <i class="k-icon k-icon-file-xls"></i></a
  >.
</p>