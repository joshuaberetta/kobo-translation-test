# Usar estilos alternativos de formularios web de Enketo

Los formularios web de Enketo se pueden personalizar en la forma en que se presentan las preguntas.
Hay dos estilos alternativos que se pueden seleccionar e incluso combinar:
**Múltiples páginas** y **Tema de cuadrícula**.

El modo **Múltiples páginas** muestra una pregunta a la vez por pantalla, o un [grupo
de preguntas](group_repeat.md) configurado para mostrarse en la misma pantalla. Esta es la misma forma en que
funciona KoboCollect.

**Tema de cuadrícula** es una visualización alternativa de preguntas diseñada para ser más compacta
y más parecida a los formularios en papel donde el espacio suele ser una preocupación importante. theme-grid
permite mostrar múltiples preguntas por fila y se adapta de manera flexible en caso de lógica de omisión
haciendo que una nueva pregunta aparezca o desaparezca. Para mostrar múltiples preguntas
en una fila, deben ser parte de un grupo, que por defecto muestra hasta cuatro
preguntas una al lado de la otra. Este tema se puede personalizar definiendo el
número de preguntas que se incluirán en cada fila a través del campo de aspecto de
la configuración de cada pregunta. Para más detalles
[consulta esta publicación](https://blog.enketo.org/gorgeous-grid).

También es posible usar tanto **Múltiples páginas** como **Tema de cuadrícula** juntos.
Puedes configurar estos estilos a través de la interfaz de usuario del editor de formularios de KoboToolbox:

![image](/images/alternative_enketo/multiple_grid.gif)

Si estás creando tu proyecto de encuesta a través de XLSForm, podrías hacer lo mismo
definiendo el tema en la columna `style` en la hoja `settings`:

**hoja settings**

| form_title        | style |
| :---------------- | :---- |
| Formulario temático | pages |
| settings |

## Estilos disponibles en XLSForm:

| Tema XLSForm                         | Descripción                                                |
| :----------------------------------- | :--------------------------------------------------------- |
| (dejar en blanco)                    | Predeterminado: una sola página                            |
| `theme-grid no-text-transform`       | Tema de cuadrícula                                         |
| `theme-grid`                         | Tema de cuadrícula con encabezados en MAYÚSCULAS          |
| `pages`                              | Múltiples páginas                                          |
| `theme-grid pages no-text-transform` | Tema de cuadrícula + múltiples páginas                     |
| `theme-grid pages`                   | Tema de cuadrícula + múltiples páginas + encabezados en MAYÚSCULAS |