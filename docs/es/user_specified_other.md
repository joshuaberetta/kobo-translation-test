# Respuestas "Otro" especificadas por el/la usuario/a para preguntas de opción múltiple

Crear respuestas "Otro" especificadas por el/la usuario/a para preguntas de opción múltiple en un solo paso es una funcionalidad que actualmente está en la hoja de ruta de desarrollo de KoboToolbox. Mientras tanto, aquí te explicamos cómo crearlas manualmente en tu formulario usando lógica de omisión.

1. Añade la pregunta deseada a tu formulario como una pregunta de opción múltiple ordinaria. Puede ser del tipo "Seleccionar una" (como se muestra aquí) o "Seleccionar varias".

    ![image](/images/user_specified_other/type.png)

2. Añade una pregunta de seguimiento del tipo "Texto" en la cual el/la encuestado/a pueda especificar manualmente su respuesta cuando sea necesario.

    ![image](/images/user_specified_other/text.png)

    NOTA: Si estás usando la aplicación KoboCollect para la recolección de datos, es importante no mostrar la segunda pregunta de texto en un grupo en la misma pantalla, ya que de lo contrario no sería visible. Esto se debe a que KoboCollect solo muestra preguntas en la misma pantalla que son relevantes en el momento en que la pantalla se muestra por primera vez. Solo asegúrate de colocarla fuera del grupo cuando elijas mostrar múltiples preguntas en la misma pantalla. (Cuando se usan formularios web de Enketo esto no es un problema, ya que muestra dinámicamente las preguntas una vez que se vuelven relevantes.)

3. Añade una [lógica de omisión](skip_logic.md) a la pregunta de seguimiento anterior para que solo se muestre cuando sea necesario.

    ![image](/images/user_specified_other/skip_logic.png)

4. Por último, previsualiza tu formulario para asegurarte de que se comporta como se espera.

    ![image](/images/user_specified_other/preview.png)