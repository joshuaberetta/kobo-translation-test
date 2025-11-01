# Tipo de pregunta Seleccionar una o varias de un archivo externo

En algunos casos, puede ser conveniente alojar una lista de opciones de respuesta en un archivo externo, en lugar de directamente en el XLSForm del proyecto. Por ejemplo, una lista larga de opciones (por ejemplo, cientos o miles) podría ralentizar la carga y navegación del formulario, o agregar nuevas opciones de respuesta después de que la recolección de datos haya comenzado podría ser problemático en ocasiones.

<p class="note"> <b>Nota:</b> Este artículo cubre los pasos para configurar preguntas de Seleccionar una o varias de un archivo externo en XLSForm. Para configurar estas preguntas en el editor de formularios de KoboToolbox (Formbuilder), primero debes cargar el archivo de opciones externo a KoboToolbox, en la pestaña <b>Datos multimedia</b> de la página <b>AJUSTES</b>. Una vez que el archivo haya sido cargado, los tipos de pregunta Seleccionar una o varias de un archivo externo aparecerán en el editor de formularios. </p>

![image](/images/external_file/select_from_file.png)

Este artículo proporciona un ejemplo detallado y un método para crear un tipo de pregunta `select_one` o `select_many` con la lista de opciones en un archivo externo separado. Consulta la [documentación de XLSForm](https://xlsform.org/en/#multiple-choice-from-file) para obtener más información.

**1.** En el XLSForm, el tipo debe ser `select_one_from_file [nombre del archivo]` o `select_multiple_from_file [nombre del archivo]`:

<p class="note">El tipo de archivo puede ser <code>CSV</code> o <code>XML</code></p>

**Hoja survey**

| type                            | name   | label                          |
| :------------------------------ | :----- | :----------------------------- |
| text                            | name   | ¿Cuál es tu nombre?            |
| select_one sex                  | sex    | ¿Cuál es tu sexo?              |
| select_one_from_file fruits.csv | fruits | ¿Cuál es tu fruta favorita?    |
| survey |

**Hoja choices**

| list_name | name | label    |
| :-------- | :--- | :------- |
| sex       | 1    | Hombre   |
| sex       | 2    | Mujer    |
| choices |

<p class="note">El archivo <code>fruits.csv</code> es el nombre del archivo que contiene las opciones para la pregunta "¿Cuál es tu fruta favorita?".</p>

**2.** Crea un nuevo archivo `CSV` y estructúralo de la misma manera que la hoja `choices` en el XLSForm:

**fruits.csv**

| list_name | name | label       |
| :-------- | :--- | :---------- |
| fruits    | 1    | Manzana     |
| fruits    | 2    | Sandía      |
| fruits    | 3    | Naranja     |
| fruits    | 4    | Pera        |
| fruits    | 5    | Cereza      |
| fruits    | 6    | Fresa       |
| fruits    | 7    | Nectarina   |
| fruits    | 8    | Uva         |
| fruits    | 9    | Mango       |
| fruits    | 10   | Arándano    |
| fruits    | 11   | Granada     |

**3.** Carga y despliega el XLSForm en KoboToolbox.

**4.** Carga el archivo `CSV` de la misma manera que [agregarías un archivo multimedia al formulario](media.md)