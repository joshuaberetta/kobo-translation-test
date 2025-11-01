# Solución de problemas de formularios web de Enketo

[Los formularios web de Enketo](enketo.md) funcionan en todos los dispositivos ya que se abren en navegadores web normales y permiten la recolección de datos en línea o sin conexión. En general, recomendamos encarecidamente la última versión de todos los [navegadores modernos](https://enke.to/modern-browsers). También puedes visitar las [Preguntas frecuentes de Enketo](https://enketo.org/faq/#browsers) para obtener más información sobre _qué navegadores son compatibles y recomendados_ por Enketo.

## Problemas conocidos con formularios sin conexión en iOS

Los dispositivos iOS (que se ejecutan en iPhones y iPads) tienen varias limitaciones conocidas con el uso de formularios habilitados sin conexión debido a la plataforma del sistema operativo de Apple. Nos esforzamos por tener la última versión de iOS totalmente compatible.

-   La recolección de datos sin conexión funciona en cualquier navegador moderno. En iOS solo recomendamos Chrome o Safari.
-   La versión 9.x muestra "NotFoundError: DOM IDBDatabase Exception 8". Solución: Cierra todas las pestañas de Enketo en tu navegador y luego vuelve a abrir el formulario. El error debería desaparecer para siempre.
-   La versión 9.3.1 muestra "Attempted to assign to readonly property" al cargar el formulario sin conexión
-   La versión 8.x muestra "undefined is not an object (evaluating 'c.resources')". Solución: Actualiza a la última versión de iOS

Si no se requiere la recolección de datos sin conexión y estás viendo un error en iOS, considera usar la _versión solo en línea_ en lugar de la URL sin conexión.

## Pérdida de datos

Al recolectar datos a través de Enketo, los/as usuarios/as nunca deben borrar la caché del navegador (ya sea manualmente o usando alguna aplicación). Borrar la caché de tu navegador (durante la recolección de datos) eliminará toda la información almacenada en el navegador y, por lo tanto, tu información no llegará a tu servidor de KoboToolbox. Esta pérdida de datos es irreversible. Por lo tanto, recomendamos encarecidamente a los/as usuarios/as borrar la caché del navegador si y solo si has enviado exitosamente todos tus datos a tu servidor de KoboToolbox.