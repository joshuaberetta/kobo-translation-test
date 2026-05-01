# Comenzar con la API

Una **interfaz de programación de aplicaciones (API)** permite que dos componentes de software se comuniquen utilizando un conjunto de definiciones y protocolos. Con una API, un script o aplicación puede trabajar con KoboToolbox sin usar la interfaz web. Por ejemplo, puedes generar automáticamente exportaciones de datos que se vinculen a fuentes externas como tableros de control o carpetas de respaldo.

Con la **API** de KoboToolbox, puedes:

- **Descargar datos** automáticamente en JSON, CSV o XLSX.
- **Generar exportaciones bajo demanda** para tableros de control, respaldos o análisis.
- **Enviar o editar envíos** desde otras herramientas de recolección de datos.
- **Crear o implementar proyectos** y clonar los existentes a través de código.
- **Gestionar usuarios/as**, permisos y actividad del proyecto a escala.

Usar la API de KoboToolbox te permite automatizar tareas rutinarias, mantener actualizados los tableros de control e integrar KoboToolbox con otros sistemas, al tiempo que reduces los pasos manuales y los errores. Este artículo proporciona una introducción a la API de KoboToolbox y cubre los siguientes pasos:

- Recuperar tu **URL del servidor**
- Recuperar tu **Clave de la API**
- Recuperar el UID del recurso del proyecto
- Exportar tus datos usando la API
- Documentación avanzada de la API

## Recuperar tu URL del servidor
La **URL del servidor** es la dirección web base de tu servidor de KoboToolbox. Se coloca al inicio de cada solicitud de API.

Para la mayoría de los/as usuarios/as, la URL del servidor es [kf.kobotoolbox.org](https://kf.kobotoolbox.org/) (si estás usando el Servidor Global) o [eu.kobotoolbox.org](https://eu.kobotoolbox.org/) (si estás usando el Servidor con sede en la Unión Europea).

![Recuperar URL del servidor](images/api/server_URL.png)

## Recuperar tu Clave de la API
Tu **Clave de la API** es un token personal que actúa como una contraseña, permitiendo que el software acceda a tu cuenta a través de la API. Puede ser requerida cuando un script, tablero de control o aplicación externa necesita autenticación para recuperar o enviar datos del proyecto a través de la API.

Hay diferentes formas de obtener tu **Clave de la API**.

**Método 1:**

1. Haz clic en el ícono de tu perfil en la esquina superior derecha.
2. Selecciona **CUENTA**.
3. Ve a la ventana **Seguridad**.
4. Tu Clave de la API está oculta de forma predeterminada. Haz clic en **Mostrar** para verla.

**Método 2:**

En tu navegador web, navega a `https://[url-del-servidor]/token/?format=json`. Asegúrate de reemplazar `[url-del-servidor]` con tu URL del servidor.

**Método 3:**

En la terminal, usa el siguiente comando curl:

`curl -u nombre_de_usuario:contraseña "https://[url-del-servidor]/token/?format=json"`

Asegúrate de reemplazar `[url-del-servidor]` con tu URL del servidor.

## Recuperar el UID del recurso de tu proyecto

El **UID del recurso del proyecto** es un código único que identifica un proyecto específico de KoboToolbox y debe incluirse en las llamadas de API para dirigirse a ese proyecto.

Puedes encontrar el **UID del recurso del proyecto** en la URL de la página de resumen de tu proyecto. Es la cadena de letras y números que aparece después de "forms/" en la URL, de la siguiente manera: `https://[url-del-servidor]/#/forms/[UID del recurso del proyecto]/summary`.

![Recuperar UID del recurso del proyecto](images/api/project_UID.png)

## Exportar tus datos usando la API

Hay dos enfoques principales para conectar tus datos usando la API con KoboToolbox:

- **Exportaciones sincrónicas:** Devuelve un archivo CSV o XLSX listo para usar, basado en configuraciones de exportación predefinidas, que las aplicaciones externas (por ejemplo, Power BI o Excel) pueden cargar directamente.
- **Endpoint JSON:** Envía cada envío como un archivo JSON sin procesar. Esto es mejor para flujos de trabajo basados en código, no para uso directo en herramientas de hojas de cálculo o tableros de control.

Cada enfoque requiere conocer la URL del servidor y el UID del recurso del proyecto para construir una URL de exportación personalizada. Dependiendo de la aplicación, tu Clave de la API puede ser necesaria para la autenticación.

<p class="note">
    Para obtener más información sobre exportaciones sincrónicas, consulta <a href="https://support.kobotoolbox.org/synchronous_exports.html">Usar la API para exportaciones sincrónicas</a>.
<br><br>
Para obtener más información sobre cómo conectar tus datos a Power BI para crear tableros de control personalizados, consulta <a href="https://support.kobotoolbox.org/pulling_data_into_powerbi.html">Conectar KoboToolbox con Power BI</a>.
<br><br>
Para obtener más información sobre cómo conectar tus datos a Microsoft Excel, consulta <a href="https://support.kobotoolbox.org/pulling_data_into_excelquery.html">Conectar KoboToolbox con Microsoft Excel</a>.
</p>

## Documentación avanzada

La documentación de la API en `https://[url-del-servidor]/api/v2/docs/` proporciona una interfaz interactiva para los endpoints de la API. Reemplaza la información presentada anteriormente en cada endpoint.

| **Servidor de KoboToolbox**    | **Documentación de la API**                     |
| :----------------- | :--------------------------------------------- |
| Servidor Global               | [https://kf.kobotoolbox.org/api/v2/docs/](https://kf.kobotoolbox.org/api/v2/docs/)  |
| Servidor con sede en la Unión Europea       | [https://eu.kobotoolbox.org/api/v2/docs/](https://eu.kobotoolbox.org/api/v2/docs/)  |

Estas páginas de documentación avanzada enumeran todos los endpoints, muestran los parámetros de consulta permitidos, incluyen una barra de búsqueda, muestran respuestas de ejemplo, muestran respuestas de error de ejemplo y permiten pruebas directas de solicitudes en tu navegador. Usa esta documentación para verificar la autenticación, descubrir funciones y copiar URLs exactas en scripts personalizados.

También puedes descargar el esquema de documentación de la API en formato YAML en `https://[url-del-servidor]/api/v2/schema/` o en formato JSON en `https://[url-del-servidor]/api/v2/schema/?format=json`.

<p class="note">
    <strong>Nota:</strong> Los endpoints V1 ahora están obsoletos y programados para ser descontinuados en enero de 2026, en favor de la API KPI v2, más robusta y totalmente compatible. Para obtener más información sobre la migración a KPI v2, consulta <a href="https://support.kobotoolbox.org/migrating_api.html">Migración de API v1 a API v2</a>.
</p>

Para más ejemplos de uso de la API, consulta esta [publicación del Foro de la comunidad](https://community.kobotoolbox.org/t/kobo-api-examples-using-new-kpi-endpoints/2742).