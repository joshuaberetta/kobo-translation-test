# Recolección de ubicaciones GPS

Las coordenadas de ubicación se pueden recolectar fácilmente en todos los formularios con los tipos de respuesta 'GPS'.

## Creación de los diferentes tipos de preguntas GPS

Para recolectar coordenadas GPS durante el proceso de recolección de datos, simplemente añade una pregunta GPS a tu formulario. Hay tres tipos de preguntas GPS: **Punto**, **Línea** y **Área**

-   Cuando usas el **editor de formularios de KoboToolbox (Formbuilder)**, estos tipos de pregunta se pueden encontrar al hacer click en el botón de añadir pregunta, como se ilustra a continuación.

![image](/images/collect_gps/formbuilder.jpg)

-   Cuando usas el diseño **XLSForm**, tienes que definir los tipos de pregunta como se muestra a continuación para obtener la pregunta que deseas.

**hoja survey**

| type     | name  | label                              | hint                                                                                                      |
| :------- | :---- | :--------------------------------- | :-------------------------------------------------------------------------------------------------------- |
| geopoint | point | Registra tu ubicación actual       | Esta pregunta recolecta una única coordenada GPS que denota un solo punto                                 |
| geotrace | line  | Registra una línea                 | Esta pregunta recolecta dos coordenadas para formar una línea                                             |
| geoshape | area  | Registra un área                   | Esta pregunta recolecta coordenadas GPS que marcan un bucle/área cerrada en cualquier forma               |
| survey |

## Recolección de datos usando las preguntas GPS

Durante la entrada de datos, el/la encuestador/a verá diferentes opciones para recolectar las coordenadas, que dependen del tipo de dispositivo de recolección de datos y del enfoque.

## Recolección de datos usando formularios web Enketo

El formulario tendrá varias opciones de recolección, incluyendo

**1. Recolección manual:** Simplemente toca cualquier punto(s) en el mapa para recolectar las coordenadas de ubicación o puedes escribir las coordenadas de latitud y longitud si se conocen.

![image](/images/collect_gps/point_manual.png)

**2. Pegar puntos KML:** Pega las coordenadas KML en el cuadro de texto que aparece.

![image](/images/collect_gps/kml.png)

**3. Detectar ubicación actual:** Simplemente haz click en el botón que se muestra a continuación para recolectar las coordenadas GPS actuales de la ubicación del dispositivo.

![image](/images/collect_gps/current_location.jpg)

## Recolección de datos usando KoboCollect

El/la entrevistador/a verá varias opciones dependiendo del tipo de pregunta GPS

**1. Coordenada de punto GPS único**

-   El/la encuestador/a verá esta pantalla en la que puede tocar Iniciar Geopunto.

![image](/images/collect_gps/geopoint.jpg)

-   Si el/la encuestador/a toca Iniciar Geopunto, verá la ubicación cargándose y la precisión alcanzada. Si la pregunta no se había configurado para seleccionar un nivel de precisión específico, esperará a que el/la encuestador/a guarde el Geopunto como se ilustra a continuación.

![image](/images/collect_gps/autopoint.jpg)

**2. Línea GPS**

-   Los/as encuestadores/as verán la siguiente opción para la pregunta de línea.

![image](/images/collect_gps/line.jpg)

-   Si tocan el botón Iniciar GeoLínea, verán una opción para recolectar el trazado manual o automáticamente como se muestra a continuación.

![image](/images/collect_gps/trace_mode.jpg)

-   Si los/as encuestadores/as seleccionan el modo manual para recolectar datos, podrán seleccionar los puntos manualmente presionando los puntos en el mapa. El/la encuestador/a tendrá que seleccionar al menos dos coordenadas para hacer un trazado de línea.

-   Si los/as encuestadores/as seleccionan el modo automático, verán una opción de cuánto tiempo debe esperar el sistema antes de recolectar diferentes puntos, como se muestra en la figura a continuación.

![image](/images/collect_gps/automodes.jpg)

**3. Área GPS**

El área GPS te permite recolectar manualmente el área GPS basándose en el modo manual presionando el mapa para seleccionar los puntos que crean el polígono; los/as encuestadores/as necesitarían recolectar al menos tres puntos para crear un polígono.

## Precisión de las coordenadas GPS recolectadas

La precisión del GPS recolectado depende de varios factores.

**Ausencia de sensor GPS o GPS desactivado**

Al recolectar coordenadas GPS y el dispositivo no tiene un sensor GPS o el GPS está desactivado, una ubicación puede determinarse usando otros medios, que pueden no ser tan precisos. Los servicios de ubicación son controlados por el dispositivo, y no todos los dispositivos están equipados con un sensor GPS. El GPS también puede estar apagado, o el dispositivo puede estar configurado para usar WiFi y redes celulares para establecer una ubicación en lugar de usar sistemas de navegación por satélite.

**El tiempo que tarda un dispositivo en determinar sus coordenadas GPS varía mucho y puede depender de:**

-   La calidad del sensor GPS
-   La última vez que el dispositivo determinó su ubicación GPS
-   Cobertura de nubes
-   Edificios u otras estructuras que obstruyen la vista del cielo

**Para obtener una señal GPS debes estar al aire libre con buena visibilidad del cielo. Para obtener una señal GPS fuerte:**

-   Mantente lo más lejos posible de edificios, árboles u otras estructuras
-   Asegúrate de que tu cuerpo no esté obstruyendo la vista del cielo
-   Obtén una ubicación GPS inicial al comienzo del día antes de comenzar a recolectar puntos en el campo
-   Activa A-GPS (asistido por red de datos) en tu dispositivo

<p class="note">GPS en este contexto no se refiere exclusivamente al <a class="reference" href="https://en.wikipedia.org/wiki/Global_Positioning_System">Sistema de Posicionamiento Global</a> sino también a otros sistemas de navegación por satélite utilizados por dispositivos móviles, como <a class="reference" href="https://en.wikipedia.org/wiki/GLONASS">GLONASS</a>.</p>

## Solución de problemas

Si no puedes obtener una ubicación GPS con el tipo de respuesta GPS, verifica estas opciones:

-   Configuración de ubicación en tu dispositivo para asegurarte de que el GPS esté activado
-   Instala una aplicación gratuita que use GPS para ver si puedes obtener una ubicación GPS de esa manera (por ejemplo,
    [GPS Status para Android](https://play.google.com/store/apps/details?id=com.eclipsim.gpsstatus2)
    o
    [GPS Status para iPhones](https://apps.apple.com/ca/app/gps-status/id378085995)
-   Revisa la configuración de tu teléfono/manual del fabricante para ver si el dispositivo tiene GPS disponible
-   Si tus puntos GPS recolectados están apuntando a la ubicación incorrecta, es posible que tu dispositivo esté configurado para recolectar su ubicación desde una torre de red que se compró de segunda mano y no se ha restablecido correctamente con la nueva ubicación codificada. Puedes evitar este problema desactivando la ubicación de red como una opción dentro de la configuración del sistema Android, forzando a Collect a esperar la ubicación GPS real.