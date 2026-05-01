# Solución de problemas de los formularios web de Enketo

[Los formularios web de Enketo](enketo.md) funcionan en todos los dispositivos ya que se abren en navegadores web regulares y permiten la recolección de datos en línea o fuera de línea. Generalmente recomendamos enfáticamente la última versión de todos los
[navegadores modernos](https://enke.to/modern-browsers). También puedes visitar
[las Preguntas Frecuentes de Enketo](https://enketo.org/faq/#browsers) para aprender
más sobre _qué navegadores son compatibles y recomendados_ por Enketo.

## Problemas conocidos con formularios fuera de línea en iOS

Los dispositivos iOS (que funcionan en iPhones y iPads) tienen varias limitaciones conocidas al
usar formularios habilitados para trabajar fuera de línea debido a la plataforma del sistema operativo Apple. Nos
esforzamos por tener la última versión de iOS totalmente compatible.

-   La recolección de datos fuera de línea funciona en cualquier navegador moderno. En iOS solo
    recomendamos Chrome o Safari.
-   La versión 9.x muestra "NotFoundError: DOM IDBDatabase Exception 8". Solución:
    Cierra todas las pestañas de Enketo en tu navegador, luego vuelve a abrir el formulario. El error
    ahora debería desaparecer para siempre.
-   La versión 9.3.1 muestra "Attempted to assign to readonly property" al cargar
    el formulario fuera de línea
-   La versión 8.x muestra "undefined is not an object (evaluating 'c.resources')".
    Solución: Actualiza a la última versión de iOS

Si no se requiere la recolección de datos fuera de línea y estás viendo un error en iOS,
considera usar la _versión solo en línea_ en lugar de la URL fuera de línea.

## Pérdida de datos

Al recolectar datos a través de Enketo, los/as usuarios/as nunca deben borrar la
caché del navegador (ya sea manualmente o usando alguna aplicación). Borrar la caché de tu navegador (durante
la recolección de datos) eliminará toda la información almacenada en el navegador y por lo tanto
tu información no llegará a tu servidor de KoboToolbox. Esta pérdida de datos es
irreversible. Por lo tanto, recomendamos enfáticamente a los/as usuarios/as borrar la caché del navegador si y
solo si has enviado exitosamente todos tus datos a tu servidor de KoboToolbox.