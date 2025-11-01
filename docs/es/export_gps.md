# Mapeo, Compartir y Exportar Datos GPS

Tu proyecto puede incluir una o más preguntas GPS en su formulario. KoboToolbox
incluirá los datos GPS (latitud, longitud, altitud, precisión) en el
conjunto de datos que se puede descargar como XLS o CSV. También es posible ver
las coordenadas GPS en un mapa en línea y descargar los puntos como un archivo KML para
usar en otras aplicaciones.

## Visualizar tus puntos GPS

![image](/images/export_gps/view_gps.jpg)

Ambas opciones siguientes solo aparecen si tu formulario tiene preguntas GPS y
tiene envíos con coordenadas GPS.

**Opción 1 - Ver puntos GPS en línea.**

Click en el botón **Ver en el mapa**, que te lleva a la vista de mapa en línea. Esta
visualización también permite ver los envíos basados en ciertas respuestas de preguntas. Cuando visualizas tus datos en un mapa, también puedes desagregar por
respuestas de preguntas, como mostrar encuestados/as masculinos y femeninos, u otros
tipos de respuestas donde una simple distribución geográfica podría ser interesante.
Una lista completa de las funcionalidades actuales del mapa se encuentra a continuación:

1. Ajustes: Carga superposiciones de datos y elige esquemas de color de marcadores.
2. Alternar capas: Alterna entre múltiples opciones de fondo de mapa.
3. Alternar pantalla completa
4. Mostrar datos como puntos (predeterminado)
5. Mostrar datos como mapa de calor

**Opción 2 - Descargar puntos GPS como KML.**

Click en el botón **Descargar Puntos GPS**. Esto iniciará un nuevo proceso de exportación
con los datos más recientes. Las exportaciones anteriores se listarán por su fecha de creación, permitiéndote ver instantáneas de coordenadas GPS en varios puntos en el
tiempo. Los archivos KML se pueden importar en una variedad de software, incluyendo Google
Earth, Google Maps, o software GIS profesional, como ArcMap.

![image](/images/export_gps/kml_exports.jpg)

Nota: En caso de que tu formulario use más de una pregunta GPS, solo la primera se
usará en el mapa.

**Opción 3 - Exportar datos como CSV y cargar a software GIS.**

Como alternativa a exportar tus datos GPS como un archivo KML, es posible y
fácil exportar y cargar tus datos como un archivo CSV (que incluirá todos
los atributos) directamente en software GIS como un shapefile. Para una guía paso a paso,
consulta este [artículo de ayuda](upload_to_gis.md).

## Cómo compartir datos del mapa

Puedes compartir un mapa con otras personas yendo a los Ajustes de tu Proyecto y habilitando
Compartir Datos. Esto significa que cualquier persona puede ver tus datos - es decir, en formato de mapa, tabla, o
descarga de archivo. No podrán editar nada, lo cual requeriría
dar permisos de Puede Editar a un/a usuario/a en particular. Después de esto puedes enviar la
URL del mapa (ver arriba).