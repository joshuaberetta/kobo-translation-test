# Descripción general de las herramientas de recolección de datos

KoboToolbox permite la recolección de datos de múltiples maneras. Debido a que KoboToolbox está construido sobre los [estándares Xform/ODK](https://xlsform.org), nuestros formularios son compatibles con [una serie de herramientas diferentes](https://xlsform.org/en/#tools-that-support-xlsforms) que se pueden utilizar para la recolección de datos.

Para dispositivos Android, recomendamos usar la [aplicación de Android de KoboCollect](https://play.google.com/store/apps/details?id=org.koboc.collect.android&hl=en_US), que se puede descargar desde Google Play Store e instalar en cualquier teléfono o tableta Android estándar.

Para cualquier otro dispositivo (incluyendo iPhones, iPads o cualquier computadora portátil o de escritorio), recomendamos usar el formulario web [para recolectar datos](data_through_webforms.md).

## Un resumen rápido de las diferencias entre las dos opciones

| &nbsp;                                                                         | Formularios web                                    | KoboCollect                                            |
| :----------------------------------------------------------------------------- | :------------------------------------------------- | :----------------------------------------------------- |
| Dispositivos                                                                   | Cualquier dispositivo móvil o computadora          | Solo Android                                           |
| Se ejecuta en...                                                               | Navegador                                          | Aplicación nativa de Android                           |
| Configurable                                                                   | A nivel del servidor                               | En cada dispositivo                                    |
| Visualización predeterminada del formulario                                    | Todas las preguntas en la misma pantalla           | Una pregunta por pantalla                              |
| Carga de datos                                                                 | Automáticamente cuando hay conexión disponible     | A petición del usuario o inmediatamente si hay conexión disponible |
| Metapreguntas específicas del teléfono (`subscriberid`, `simserial`, `phonenumber`) | No                                          | Sí                                                     |
| Tipo de pregunta `barcode`                                                     | No (excepto entrada manual)                        | Sí                                                     |
| Diferentes estilos de formulario                                               | Sí                                                 | No                                                     |
| Encriptación                                                                   | No para almacenamiento, pero siempre durante la transferencia | Se puede habilitar en el dispositivo, siempre durante la transferencia |
| Aspecto `hide-input` para mapas para ocultar entradas GPS manuales            | Sí                                                 | No                                                     |
| Opciones avanzadas de aspecto de mapas (`streets`, `terrain`, `satellite`, `[other]`) | Sí                                          | No                                                     |
| Formato de texto en notas y etiquetas (negrita, cursiva, enlaces)             | Sí                                                 | No                                                     |
| Combinar notas consecutivas en una sola nota en la pantalla                    | Sí                                                 | No                                                     |
| Aspecto `multiline` para preguntas de tipo `text`                             | Sí                                                 | Sí                                                     |
| Aspecto `horizontal-compact` para preguntas de tipo selección                  | Sí                                                 | No                                                     |
| Aspecto de escala `likert` para preguntas de tipo selección                   | Sí                                                 | Sí                                                     |
| Aspecto `compact-2` para preguntas de tipo selección                          | No                                                 | Sí                                                     |
| Aspecto `no-calendar`                                                          | No                                                 | Sí                                                     |
| Aspectos avanzados de imagen (`annotate`, `draw`, `signature`)                | Sí                                                 | Sí                                                     |
| Comando de cálculo `repeat_count()`                                            | Establecer un número mínimo de grupos de repetición | Establecer un número exacto de grupos de repetición   |

### Recolectar datos usando KoboCollect

Después de desplegar un proyecto, puedes ir a **FORMULARIO - Recolectar datos**, y luego seleccionar la aplicación de Android.

![image](/images/data_collection_tool/KoboCollect.gif)

Para obtener detalles sobre cómo configurar KoboCollect en cualquier dispositivo Android, [lee este artículo](kobocollect_on_android_latest.md).

### Recolectar datos usando el formulario web Enketo

Para [usar el formulario web](data_through_webforms.md), después de desplegar un proyecto, puedes ir a **FORMULARIO - Recolectar datos**, hay múltiples opciones disponibles (en línea o sin conexión, envío único o múltiple). La opción predeterminada es **En línea-Sin conexión (envío múltiple)**.

![image](/images/data_collection_tool/Webform.gif)