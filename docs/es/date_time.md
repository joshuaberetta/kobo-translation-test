# Tipos de preguntas de fecha y hora

Hay 3 tipos diferentes de preguntas de fecha y hora en KoboToolbox: "Fecha",
"Hora" y "Fecha y hora".

El tipo de pregunta "Fecha" es para capturar valores de fecha, por ejemplo al
preguntar por la fecha de nacimiento, etc. Tanto en KoboCollect como en los
formularios web de Enketo, se mostrará un selector de fechas estilo calendario
para seleccionar la fecha.

El tipo de pregunta "Hora" es para capturar valores de hora, por ejemplo en una
pregunta como "¿A qué hora sales al trabajo?" Tanto en KoboCollect como en
Enketo, se muestra un selector de hora donde el/la usuario/a puede seleccionar
su respuesta.

El tercer tipo "Fecha y hora" es para capturar respuestas de fecha y hora en
una sola pregunta.

## Cómo configurar los tipos de preguntas de Fecha y Hora

### Configuración en el editor de formularios de KoboToolbox (Formbuilder)

Añadir preguntas de "Fecha", "Hora" y "Fecha y hora" es sencillo:

- En el editor de formularios de KoboToolbox (Formbuilder), click en el botón <i class="k-icon k-icon-plus"></i> para añadir
  una nueva pregunta
- Escribe el texto de la pregunta, por ejemplo "¿Cuál es tu fecha de nacimiento?", luego click en
  **AÑADIR PREGUNTA** o presiona ENTER en tu teclado
- Elige el tipo de pregunta

![Añadiendo las preguntas](images/date_time/adding.gif)

### Configuración en XLSForm

Para añadir preguntas de "Fecha", "Hora" y "Fecha y hora" en el Formato estándar XLSForm, usa los
tipos de pregunta `date`, `time` y `datetime` como se muestra en el ejemplo a continuación:

En XLSForm, puedes configurar lo siguiente:

| type     | name      | label                                                  |
| :------- | :-------- | :----------------------------------------------------- |
| date     | dob       | ¿En qué fecha naciste?                                 |
| time     | time      | ¿A qué hora sales al trabajo?                          |
| datetime | date_time | ¿En qué fecha y hora comenzó la capacitación?          |
| survey   |

## Aspecto de los tipos de preguntas de fecha y hora en formularios web y KoboCollect

### Aspecto predeterminado

![Aspectos predeterminados](images/date_time/default_appearances.png)

### Aspectos avanzados

Al añadir el tipo de pregunta "Fecha" en el editor de formularios, puedes elegir entre varias
opciones de visualización (en la configuración de la pregunta). Los aspectos de las preguntas cambian la
forma en que se muestra la pregunta en los formularios web y en KoboCollect.

Para el tipo de pregunta "Fecha", puedes controlar cómo se muestra el calendario gregoriano predeterminado
eligiendo entre las opciones "month-year (mes-año)", "year (año)" y "no-calendar (sin calendario)".
Además de estas opciones, también puedes cambiar el estilo del calendario a calendarios
no gregorianos compatibles.

![Añadiendo aspectos avanzados](images/date_time/advanced_appearance.png)

Para añadir valores de aspecto que no están listados en la lista desplegable del
editor de formularios, elige "other (otro)", y escribe el valor del aspecto en el campo de texto
que aparece.

![Aspectos avanzados](images/date_time/advanced_appearances.png)

_\* Estas opciones deben ingresarse manualmente en el editor de formularios después de seleccionar "other (otro)"._

### Añadiendo aspectos personalizados para preguntas de fecha en XLSForm

Puedes especificar aspectos avanzados en XLSForm a través de la columna appearance (aspecto) de la
siguiente manera:

#### Aspectos del selector de fechas

| type   | name             | label                                                | appearance  |
| :----- | :--------------- | :--------------------------------------------------- | :---------- |
| date   | rains_start      | ¿Cuándo comenzaron las lluvias de siembra?           | month-year  |
| date   | year_migrate     | ¿En qué año migraste?                                | year        |
| date   | no-calendar_date | Selector de fechas sin calendario                    | no-calendar |
| survey |

### Calendarios no gregorianos compatibles

| type   | name                | label                                       | appearance     |
| :----- | :------------------ | :------------------------------------------ | :------------- |
| date   | coptic_date         | Selector de fechas con calendario copto     | coptic         |
| date   | ethiopian_date      | Selector de fechas con calendario etíope    | ethiopian      |
| date   | islamic_date        | Selector de fechas con calendario islámico  | islamic        |
| date   | bikhram_sambat_date | Selector de fechas con calendario Bikram Sambat | bikhram_sambat |
| date   | myanmar_date        | Selector de fechas con calendario birmano   | myanmar        |
| date   | persian_date        | Selector de fechas con calendario persa     | persian        |
| survey |

## Uso de preguntas de fecha y hora en lógica personalizada

Al definir lógica de omisión personalizada (relevant), criterio simple de validación (constraint),
y criterio de respuesta obligatoria (required) usando código XLSForm, los valores de fecha
deben incluirse
[usando la función `date()`](https://docs.getodk.org/form-operators-functions/#date),
y en el formato `"YYYY-MM-DD"`. Por ejemplo, si estás creando un criterio simple de validación
en una pregunta de fecha para que todas las respuestas de la encuesta sean antes de la fecha
"10 de abril de 2022", tu lógica de validación será `. < date('2022-04-11')`.

Para usar preguntas de "Hora" en lógica XLSForm, siempre es una buena idea convertir
los valores de hora sin procesar en un número que representa el tiempo como una fracción de un día,
llamado tiempo decimal. Puedes hacer esto usando
[la función `decimal-time()`](https://docs.getodk.org/form-operators-functions/#decimal-time).
Luego, puedes comparar este valor con otro valor de tiempo decimal. Por ejemplo,
si deseas limitar la hora ingresada en una pregunta a solo después de las 12 del mediodía,
puedes definir la siguiente lógica de validación personalizada `decimal-time(.)>=0.5`.

Aprende más sobre temas relacionados:

- [Lógica de omisión](skip_logic.md)
- [Criterio simple de validación](validation_criteria.md)
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