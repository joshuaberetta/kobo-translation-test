# Tipo de pregunta de metadatos de registro de auditoría

El registro de auditoría puede ser una herramienta útil para monitorear el comportamiento de los/as encuestadores/as y descubrir qué preguntas están tomando más tiempo en responder, comprender mejor cómo los/as encuestadores/as están navegando un formulario determinado y ver qué encuestadores/as generalmente están tomando períodos de tiempo más largos para enviar respuestas.

<p class="note">Esta funcionalidad requiere analizar manualmente archivos CSV.</p>

La pregunta de metadatos de registro de auditoría es un tipo de pregunta que solo es compatible al usar la [aplicación de Android de KoboCollect](kobocollect_on_android_latest.md).

Para agregar un tipo de pregunta de metadatos `audit` a un formulario y visualizar los datos finalizados, sigue los pasos a continuación:

1. En un archivo XLSForm, agrega `audit` de la misma manera que agregarías cualquier otra pregunta de metadatos. Luego carga el archivo del formulario a tu proyecto y despliega el formulario.

**Hoja survey**

| type  | name  | label                      |
| :---- | :---- | :------------------------- |
| start | start |                            |
| end   | end   |                            |
| audit | audit |                            |
| text  | Q1    | Q1. ¿Cuál es tu nombre?    |
| survey |

2. Recolecta datos usando la [aplicación de Android de KoboCollect](kobocollect_on_android_latest.md) y envía los formularios finalizados de vuelta al servidor. KoboCollect guarda los registros de auditoría para cada envío en un archivo CSV que se guardan y cargan al servidor de la misma manera que lo haría una foto adjunta.

3. Después de que los datos hayan sido enviados, abre tu proyecto en el navegador y ve a **DATOS**, luego **Descargas**. Selecciona **Archivos multimedia adjuntos (ZIP)** como el tipo de exportación y luego click en **Nuevo exportable**. Una vez que la descarga esté lista, click en el archivo para descargarlo a tu computadora.

![image](/images/audit_logging/zip_export.png)

4. Una vez que el archivo ZIP haya sido extraído y abierto, click en el archivo etiquetado 'audit.csv' para visualizar los registros de auditoría. Es importante tener en cuenta que el CSV usa el tiempo [Unix Epoch](https://www.unixtimestamp.com/index.php), por lo que los registros se graban en milisegundos.

5. Debido a que las marcas de tiempo se guardan para cada envío individual, probablemente necesitarás copiar los valores en una nueva hoja de cálculo para hacer un análisis más detallado de todos los envíos (por ejemplo, por encuestador/a o por pregunta). La recopilación de muchos archivos CSV diferentes se puede hacer mediante [muchas herramientas gratuitas o escribiendo un script](https://www.google.com/search?q=merge+many+CSV). Para leer información más detallada sobre la estructura de registros y tipos de eventos, visita la excelente documentación de ODK sobre [Registro del comportamiento de encuestadores/as](https://docs.getodk.org/form-audit-log/#).

Siéntete libre de publicar en nuestro [Foro de la comunidad](https://community.kobotoolbox.org/) para compartir tu enfoque o script favorito para usar esta funcionalidad para que otras personas puedan aprender de tu ejemplo.