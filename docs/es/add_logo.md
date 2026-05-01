# Añadir un logotipo personalizado

Añadir un logotipo personalizado en la parte superior de tu formulario es un proceso simple y principalmente
sigue los mismos pasos que [añadir contenido multimedia a tus formularios](media.md).

Para comenzar:

1. Comienza creando tu archivo de imagen del logotipo y guárdalo con un nombre de archivo corto.

2. En tu XLSForm, haz que la primera pregunta sea un tipo de pregunta Nota, deja la
   etiqueta en blanco y añade una columna titulada `media::image` con el nombre de tu archivo de logotipo
   en la celda. Como se muestra a continuación:

**hoja de trabajo survey**

| type | name | label | media::image |
| :--- | :--- | :---- | :----------- |
| note | logo |       | logo.jpg     |
| survey|

3. Cuando termines de editar el formulario, carga el XLSForm en un proyecto nuevo o
   existente.

4. Implementa o vuelve a implementar tu formulario, dependiendo de si es un proyecto nuevo o está
   reemplazando un formulario existente.

5. En la página de tu proyecto ve a **CONFIGURACIONES>MULTIMEDIA** y [carga](media.md) tu
   archivo `logo.jpg`.

## Consejos:

-   Mantén tu imagen pequeña.
-   Tu imagen de logotipo no aparecerá en la vista previa del formulario, solo cuando el formulario esté
    abierto.
-   Omitir el paso final significará que tu formulario se mostrará sin
    los archivos multimedia. Asegúrate de que los archivos multimedia estén cargados antes de descargar
    el formulario a tus dispositivos cuando uses la aplicación Android.

<p class="note">Si abres el editor de formularios de KoboToolbox **(Formbuilder)** después de implementar tu XLSForm con el archivo de imagen del logotipo, automáticamente le dará a la pregunta una etiqueta de texto y necesitarás eliminarla para que el texto automatizado no aparezca junto a tu logotipo en tu formulario.</p>