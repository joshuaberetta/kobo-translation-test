# Conversión de datos a SPSS y/o Stata

<p class="note">
  Este artículo te ayuda a convertir tus datos a <strong>SPSS</strong> y
  <strong>Stata</strong>. Ten en cuenta que necesitas
  <strong>IBM SPSS</strong> o <strong>Stata</strong>, que son aplicaciones de terceros.
</p>

Dado que **KoboToolbox** no exporta datos directamente en formato **SPSS** o **Stata**,
este artículo será una guía para realizar la conversión.

## Conversión a SPSS

1. Descarga tus datos como XLS usando las instrucciones proporcionadas en
   [este artículo de ayuda](export_download.md) o como se ilustra en la imagen
   a continuación.

    ![Exportar XLS](/images/converting_to_spss_and_stata/export_xls.gif)

2. Descarga las **Etiquetas SPSS** desde la misma ventana **DATOS** como se muestra en la imagen
   a continuación. Este proceso generará una carpeta comprimida que contiene la
   sintaxis de **SPSS**.

    ![Exportar Etiquetas SPSS](/images/converting_to_spss_and_stata/export_spss_labels.gif)

3. Ahora necesitarás **IBM SPSS** para importar los datos en XLS usando el siguiente
   método que es compatible con todas las versiones de **SPSS**.

    - Dentro de **SPSS**, haz click en **Archivo -> Abrir -> Datos** (como se muestra a continuación).
    - Una vez que hagas click en la pestaña **Datos**, aparecerá un cuadro de datos.
      En el cuadro de tipo de **Archivos**, selecciona **Excel**.
    - Navega a la carpeta que contiene tu archivo de **Excel**, y encuentra el
      archivo de **Excel** que contiene los datos que descargaste.
    - Abre el archivo, y obtendrás el cuadro de diálogo **Leer archivo de Excel**.

    ![Importar a SPSS](/images/converting_to_spss_and_stata/import_into_spss.gif)

4. Ahora abre la sintaxis que descargaste en el _Paso 2_ y ejecuta la sintaxis.

    ![Ejecutar Sintaxis](/images/converting_to_spss_and_stata/run_syntax.jpg)

Ahora estás listo/a para manipular tus datos en **SPSS**.

## Conversión del archivo SPSS a un archivo STATA

Desafortunadamente no tenemos una opción para descargar directamente un archivo **SPSS DO**.
Necesitas seguir el proceso anterior y luego guardar los datos finales como datos
**Stata** `.dta`.

Asegúrate de elegir guardar todas las opciones que necesitas al guardar.

![datos dta](/images/converting_to_spss_and_stata/dta_data.jpg)