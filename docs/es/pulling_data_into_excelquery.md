# Conectar KoboToolbox a Microsoft Excel

KoboToolbox te permite conectar tu proyecto de recolección de datos a programas externos como Microsoft Excel, Power BI o Google Sheets, lo cual es posible a través de la interfaz de programación de aplicaciones (API).

Este artículo te guía a través del proceso de conectar tu proyecto a Excel. Si deseas conectarte a Power BI, consulta el artículo [aquí](pulling_data_into_powerbi.md).

## Paso 1: Obtener la URL de exportaciones síncronas

Para traer datos a Excel, primero necesitas obtener la URL de exportaciones síncronas a través de la API de KoboToolbox. El proceso paso a paso para hacer esto se describe en el artículo [aquí](synchronous_exports.md).

## Paso 2: Agregar la fuente de datos

<p class="note">Estos pasos solo funcionan en Excel 2016 y versiones posteriores.</p>

- Abre Excel y crea un libro en blanco. También puedes trabajar dentro de un libro existente, incluso si ya tiene datos.
- Haz click en la pestaña **Datos**, elige **Obtener datos -> Desde otras fuentes -> Desde la web**.
- Pega la URL de exportaciones síncronas que copiaste y haz click en **Aceptar**.

![Obtener datos](images/pulling_data_excelquery/get_data.gif)

- Dentro del cuadro de diálogo "Acceder a contenido web", haz click en **Básico** para agregar tus detalles de autenticación.
- Ingresa tu nombre de usuario y contraseña de KoboToolbox y haz click en **CONECTAR**.

![Autenticación](images/pulling_data_excelquery/authentication.gif)

<p class="note">
  Si hiciste públicos los datos de tu proyecto, puedes conectarte sin autenticación eligiendo "Anónimo" en el cuadro de diálogo "Acceder a contenido web". Obtén más información sobre los permisos de proyectos
  <a href="managing_permissions.html" class="reference">aquí</a>.
</p>

Se mostrará una lista de los datos contenidos en tu proyecto en el Navegador.

<p class="note">
  Si tu formulario tiene grupos de repetición, cada grupo aparecerá como una hoja de cálculo separada en el Navegador. Asegúrate de usar el enlace "data_url_xlsx" ya que la exportación CSV <em>no</em> incluye grupos de repetición.
</p>

- Elige los datos que deseas importar. Para importar varias tablas a la vez, haz click en "Seleccionar varios elementos" y luego elige los elementos de la lista.
- Haz click en **Cargar** para traer los datos o haz click en **Transformar datos** para abrir el Editor de Power Query, que puedes usar para limpiar y transformar los datos antes de cargarlos.

![Elegir tablas](images/pulling_data_excelquery/navigator.gif)

<p class="note">
  Puedes conectar varios proyectos en un libro de Excel. Repite el proceso anterior para cada proyecto, usando su URL de exportación síncrona. En la mayoría de los casos donde tienes varias tablas, puede ser necesario configurar relaciones entre tablas antes de poder usar los campos para crear informes y tableros de control. Configura las relaciones yendo a
  <strong>Datos -> Herramientas de datos -> Relaciones</strong>. Obtén más información sobre cómo crear relaciones entre tablas
  <a
    href="https://support.microsoft.com/en-us/office/create-a-relationship-between-tables-in-excel-fe1b6be7-1d85-4add-a629-8a3848820be3"
    class="reference"
    >aquí</a
  >.
</p>

### Usar los datos importados

Excel te ofrece varias formas de trabajar con los datos que acabas de importar.

#### 1. Crear tablas dinámicas y gráficos dinámicos desde el modelo de datos

Una tabla dinámica es una herramienta poderosa utilizada para calcular, resumir y analizar datos, lo que te permite ver comparaciones, patrones y tendencias en los datos. Los datos resumidos en tablas dinámicas se pueden visualizar de manera simple usando gráficos dinámicos.

- Haz click en la pestaña **Insertar**, luego haz click en la flecha desplegable en Tabla dinámica
- Elige **Desde modelo de datos**
- Elige **Nueva hoja de cálculo**
- Haz click en **Aceptar**

![Crear una tabla dinámica](images/pulling_data_excelquery/pivot.gif)

Las tablas importadas se mostrarán en el panel lateral **Campos de tabla dinámica** donde puedes elegir los campos necesarios.

#### 2. Cargar datos en la hoja de cálculo

Cuando importas una sola tabla, como cuando tu proyecto no tenía grupos de repetición, los datos se cargan automáticamente como una tabla en la hoja de cálculo. Sin embargo, cuando tus datos vienen como varias tablas, las tablas se enumeran en el panel **Consultas y conexiones**.

Para cargar estos datos en tu hoja de cálculo:

- Haz click derecho en una tabla del panel **Consultas y conexiones** y elige **Cargar en**. (si no ves el panel, ve a **Datos -> Consultas y conexiones**).
- En el siguiente cuadro de diálogo, elige **Tabla** y haz click en **Aceptar**. También puedes elegir las otras opciones disponibles según tu necesidad.

![Cargar una tabla en Excel](images/pulling_data_excelquery/load_table.gif)

Puedes hacer esto para todas las tablas enumeradas en el panel **Consultas y conexiones**.

## Actualizar los datos en tus informes

Cuando los datos de tu proyecto se actualizan en el servidor de KoboToolbox, como cuando tienes nuevos envíos, cambios en los estados de validación, ediciones o eliminaciones, necesitarás sincronizarlos con tus informes. En Excel:

- Navega a la pestaña **Datos**
- En "Consultas y conexiones", haz click en **Actualizar**

## Solución de problemas

### Error al conectarse a KoboToolbox

A veces, incluso después de ingresar las credenciales correctas para conectarte a tu proyecto, puedes obtener un error. Esto puede suceder si Excel se configuró para conectarse a una cuenta antes, y ahora estás intentando conectarte usando una cuenta diferente del mismo servidor de KoboToolbox, es decir, ambas del Servidor Humanitario.

Para restablecer la configuración de autenticación:

- Ve a **Pestaña Datos -> Obtener datos -> Configuración de origen de datos**. Selecciona los permisos existentes en el cuadro de diálogo y haz click en **Borrar permisos**. Cierra e intenta agregar la nueva conexión nuevamente.

![Borrar configuración de origen de datos](images/pulling_data_excelquery/data_source_settings.gif)

### Error al actualizar datos

Si obtienes un error al actualizar datos, podría haber varias razones:

- Tus detalles de autenticación podrían haber cambiado. Necesitarás seguir las instrucciones anteriores para cambiar tu **Configuración de origen de datos**.
- Uno o más campos en tu formulario podrían haber sido eliminados o renombrados. [Necesitarás editar la consulta en Power Query](https://docs.microsoft.com/en-us/power-bi/transform-model/desktop-query-overview).
- Podría haber una discrepancia de tipo de datos, especialmente si cambiaste el tipo de datos de uno o más campos en Excel. Puedes intentar restablecer el tipo de datos antes de actualizar la conexión.