# Agregar lógica de omisión a una matriz de preguntas

En la mayoría de las situaciones, puedes agregar lógica de omisión a cualquier tipo de pregunta como se describe en el artículo de ayuda **[Añadir lógica de salto al Formbuilder](skip_logic.md)**. Sin embargo, al trabajar dentro del editor de formularios, agregar lógica de omisión a una pregunta de tipo `matrix` aún no es posible. En su lugar, se puede usar un XLSForm para implementar lógica de omisión para este tipo de pregunta. Este artículo de ayuda ilustra cómo puedes agregar lógica de omisión a una pregunta de tipo `matrix` usando XLSForm.

Si has leído el artículo de ayuda **[Agregar una matriz de preguntas usando el Formbuilder](matrix_response.md)**, ya sabrás que hay 2 enfoques para crear una pregunta de tipo `matrix` en KoboToolbox: el _enfoque del editor de formularios_ y el _enfoque `kobo--matrix_list`_. Este artículo de ayuda proporciona una descripción general de los pasos necesarios para agregar lógica de omisión a una pregunta de tipo `matrix` al usar cualquiera de estos enfoques.

## El enfoque del editor de formularios:

Este enfoque funciona con **Enketo**, también conocido como **formularios web**, utilizando el **diseño de tema de cuadrícula**. Puede no funcionar como se espera si ignoras la configuración del **diseño de tema de cuadrícula** como se describe en el artículo de ayuda **[Diseñar formularios web usando el Formbuilder](alternative_enketo.md)**.

Sigue los pasos que se describen a continuación para agregar lógica de omisión a una pregunta de tipo `matrix` usando el enfoque del editor de formularios.

**Paso 1:** Crear una pregunta de tipo `matrix` en el editor de formularios:

El primer paso es crear una pregunta de tipo `matrix` en el editor de formularios como se describe en el artículo de ayuda **[Agregar una matriz de preguntas usando el Formbuilder](matrix_response.md)**. Simplemente agrega filas y columnas con las variables para las que deseas recolectar datos.

**Paso 2:** Descargar el formulario como XLSForm:

Una vez que la pregunta de tipo `matrix` esté lista, **GUARDA** el formulario y luego [descárgalo como un XLSForm](getting_started_xlsform.md#downloading-an-xlsform-from-kobotoolbox).

**Paso 3:** Agregar el encabezado de columna relevant y lógica de omisión a tu XLSForm:

Ahora abre el XLSForm y luego agrega el encabezado de columna `relevant` al XLSForm. Una vez que tengas el encabezado de columna `relevant`, podrás agregar lógica de omisión a todas las preguntas según sea necesario.

Para mejorar la forma en que se muestran las preguntas de tipo `matrix` al responder, se recomienda agregar un tipo de pregunta `note` (resaltado en amarillo en la imagen a continuación) y luego incluir lógica de omisión según corresponda. Esto es completamente opcional ya que simplemente afectará el formato de la pregunta de tipo `matrix`. La diferencia entre _usar_ y _no usar_ el tipo de pregunta `note` se ilustra a continuación en el **Paso 6: Recolectar datos**.

![XLSForm enfoque del editor de formularios](images/adding_skip_to_matrix/formbuilder_xlsform.png)

**Paso 4:** Reemplazar el XLSForm:

Carga y reemplaza tu XLSForm en el proyecto existente, o crea un nuevo proyecto (si es necesario).

**Paso 5:** Implementar el formulario:

Una vez que hayas reemplazado el XLSForm (o cargado el XLSForm como un nuevo proyecto), deberás implementar tu formulario.

**Paso 6:** Recolectar datos:

Después de implementar el formulario, puedes ir a **FORMULARIO>Recolectar datos>ABRIR** para comenzar a recolectar datos con el formulario web.

**Pantalla de entrada de datos como se ve en Enketo (formulario web): _cuando no se ingresa nada_.**

![Formulario Enketo vacío enfoque del editor de formularios](images/adding_skip_to_matrix/formbuilder_enketo_form_empty.png)

**Pantalla de entrada de datos como se ve en Enketo (formulario web) con el tipo de pregunta `note` agregado: _cuando la pregunta de tipo `matrix` está completada_.**

![Formulario Enketo completado enfoque del editor de formularios](images/adding_skip_to_matrix/formbuilder_enketo_form_filled_no_issue.png)

Como puedes ver en la imagen anterior, el formato de la pregunta de tipo `matrix` no se ha distorsionado. Así es como se mostrará la tabla `matrix` cuando uses el tipo de pregunta `note` que se resaltó en la imagen compartida anteriormente.

**Pantalla de entrada de datos como se ve en Enketo (formulario web) con el tipo de pregunta `note` no agregado: _cuando la pregunta de tipo `matrix` está completada_.**

![Formulario Enketo completado enfoque del editor de formularios](images/adding_skip_to_matrix/formbuilder_enketo_form_filled_with_issue.png)

En este caso, el formato de la pregunta de tipo `matrix` se ha distorsionado. Esta es la tabla `matrix` que se mostrará cuando no se use el tipo de pregunta `note`.

<p class="note">
  Puedes acceder al XLSForm
  <a
    download
    class="reference"
    href="./_static/files/adding_skip_to_matrix/adding_skip_to_a_matrix_question.xls"
    >aquí</a
  >
  que se usó para este enfoque
  <em
    >(agregar lógica de omisión a una pregunta de tipo <code>matrix</code> usando el
    enfoque del editor de formularios)</em
  >.
</p>

## Enfoque `kobo--matrix_list`:

Al igual que con el enfoque del editor de formularios, este método de agregar lógica de omisión con un XLSForm funciona con **Enketo** usando el **diseño de tema de cuadrícula**.

Sigue los pasos a continuación para agregar lógica de omisión a una pregunta de tipo `matrix` con un XLSForm usando el enfoque `kobo--matrix_list`.

**Paso 1:** Crear una pregunta de tipo `matrix` en el XLSForm:

Crea una pregunta de tipo `matrix` en el XLSForm, como se describe en el artículo de ayuda **[Agregar una matriz de preguntas usando el Formbuilder](matrix_response.md)**.

**Paso 2:** Agregar el encabezado de columna `relevant` y lógica de omisión a tu XLSForm:

Una vez que la pregunta de tipo `matrix` esté lista, debes agregar el encabezado de columna `relevant`. Ahora puedes agregar lógica de omisión a todas las preguntas bajo el encabezado de columna `relevant`.

![XLSForm enfoque kobo_matrix](images/adding_skip_to_matrix/kobo_matrix_xlsform.png)

**Paso 3:** Cargar el XLSForm:

Si tu XLSForm está listo, cárgalo como un nuevo proyecto.

**Paso 4:** Implementar el formulario:

Una vez que hayas cargado el XLSForm, deberás implementar tu formulario.

**Paso 5:** Recolectar datos:

Ahora puedes ir a **FORMULARIO>Recolectar datos>ABRIR** para comenzar a recolectar datos.

**Pantalla de entrada de datos como se ve en Enketo (formulario web): _cuando no se ingresa nada_.**

![Formulario Enketo vacío enfoque kobo_matrix](images/adding_skip_to_matrix/kobo_matrix_enketo_form_empty.png)

**Pantalla de entrada de datos como se ve en Enketo (formulario web): _cuando la pregunta de tipo `matrix` está completada_.**

![Formulario Enketo completado enfoque kobo_matrix](images/adding_skip_to_matrix/kobo_matrix_enketo_form_filled.png)

Como puedes ver en la segunda imagen, el formato de la pregunta de tipo `matrix` se ha distorsionado. En el enfoque `kobo--matrix_list` no tienes el espacio para corregir la tabla `matrix` como lo tenías con el enfoque del editor de formularios.

<p class="note">
  Puedes acceder al XLSForm
  <a
    download
    class="reference"
    href="./_static/files/adding_skip_to_matrix/adding_skip_to_a_matrix_question_kobo_matrix.xls"
    >aquí</a
  >
  que se usó para este enfoque
  <em
    >(agregar lógica de omisión a una pregunta de tipo <code>matrix</code> usando el
    enfoque <code>kobo--matrix_list</code>)</em
  >.
</p>