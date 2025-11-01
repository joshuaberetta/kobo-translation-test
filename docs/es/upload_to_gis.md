# Exportar y cargar datos a software GIS

**Proceso simple paso a paso para exportar y cargar tus datos como un shapefile en
software GIS, como ArcMap.**

Existen múltiples formas de importar datos basados en ubicación recolectados a través de
KoboToolbox en software GIS. Este artículo describirá un procedimiento recomendado
para descargar datos de KoboToolbox como un archivo CSV y cargarlo en ArcMap como un
shapefile. Aunque este ejemplo usa ArcMap, el proceso es similar al de
otros softwares geoespaciales, incluyendo QGIS (gratuito).

1. En la pestaña **Descargas** de la página de tu proyecto en KoboToolbox, exporta y
   descarga tus datos como un archivo CSV.

    ![image](/images/upload_to_gis/saveas_csv.jpg)

    _Nota: Puedes editar el conjunto de datos una vez que esté en el software GIS, sin embargo
    puede ser más fácil editarlo primero en Excel, o un programa similar. En Excel, usa la
    función [Texto en columnas.](https://support.office.com/en-us/article/split-a-cell-f1804d0c-e180-4ed0-a2ae-973a0b7c6a23)
    para dividir tus datos CSV en celdas individuales._

2. Abre un proyecto nuevo o existente en ArcMap, ve a **Agregar datos**, y luego vincula
   la carpeta donde tu archivo CSV está guardado en tu computadora.

    ![image](/images/upload_to_gis/find_file.jpg)

3. Abre la ventana **Catálogo** y haz clic en **Conexiones de carpeta**. Encuentra tu
   archivo CSV, haz clic derecho en él, luego selecciona **Crear clase de entidad** > **Desde tabla XY**.

4. En la ventana modal, haz clic en el menú desplegable **Campo X** y elige tu opción
   pregunta_Longitud de GPS. Además, asegúrate de elegir tu **Sistema de coordenadas
   de coordenadas de entrada**...(WGS 1984 es una buena opción, si no estás usando una
   ya) y asegúrate de que tu **Salida** esté configurada en la carpeta apropiada, luego
   haz clic en **Aceptar**.

    ![image](/images/upload_to_gis/create_feature.jpg)

5. De vuelta en la ventana **Catálogo**, haz clic y arrastra tu nuevo shapefile hacia la
   ventana **Vista de datos** o **Tabla de contenidos**.

6. Ahora deberías ver tus puntos en la pantalla y si abres la **Tabla de atributos**, verás todos los datos asociados con cada punto. Desde este
   punto, ahora puedes visualizar y ejecutar varios análisis espaciales con tus datos.

    ![image](/images/upload_to_gis/dataview_table.jpg)