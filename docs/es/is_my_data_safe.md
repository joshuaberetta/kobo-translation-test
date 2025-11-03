# Medidas de seguridad de datos de KoboToolbox: Manteniendo tus datos seguros

Nos tomamos muy en serio la protección de datos. La seguridad de datos significa proteger los datos de nuestros/as usuarios/as de cualquier amenaza que pueda existir. Este artículo resume algunas de nuestras medidas administrativas, físicas, organizacionales y técnicas para hacer cumplir la seguridad de datos en los servidores de KoboToolbox mantenidos por Kobo, Inc., la [organización sin fines de lucro detrás de KoboToolbox](https://www.kobotoolbox.org/about-us/).

Cumplimos completamente con el Reglamento General de Protección de Datos (GDPR) de la Unión Europea. Si te encuentras en la Unión Europea, [puedes firmar un acuerdo de procesamiento de datos (DPA) aquí](https://www.digisigner.com/online/showTemplate?linkId=495db186-9c9e-4627-99f7-a943282eeab5).

## Confidencialidad

**Control de Acceso Físico**

-   Las medidas de control de acceso físico, entre otras, son implementadas por Amazon Web Services (AWS), que se utiliza para alojar nuestros servidores de KoboToolbox. Estas medidas incluyen, por ejemplo, videovigilancia y seguridad física de las instalaciones de servidores y redes, mantenimiento de control de acceso con tarjetas de identificación, limitando el acceso solo al personal autorizado. Para una lista completa de detalles sobre las medidas técnicas y organizacionales de AWS para el control de acceso físico, [consulta este artículo](https://aws.amazon.com/compliance/data-center/controls/) sobre controles de centros de datos proporcionados por AWS.

**Control de Acceso Electrónico**

-   Todas las cuentas de KoboToolbox están protegidas con contraseña. Los/as usuarios/as reciben retroalimentación visual sobre la complejidad de su contraseña, lo que les anima a seleccionar una contraseña más fuerte cuando sea aplicable. Solo se almacenan hashes de contraseñas encriptadas en el servidor de KoboToolbox, utilizando el marco de código abierto predeterminado proporcionado por Django, que usa el algoritmo [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2) con un hash SHA256. Las contraseñas en texto plano nunca se guardan en el servidor.
-   Todo el contenido de la base de datos está encriptado en reposo (encriptación a nivel de disco).
-   Los datos enviados al servidor están encriptados en tránsito usando SHA-256 con encriptación RSA.
-   Los/as usuarios/as pueden [optar por habilitar también la encriptación de los datos de su proyecto (encriptación a nivel de datos)](encrypting_forms.md) lo que los hace inaccesibles en todas las etapas del procesamiento de datos y requiere una clave privada para desencriptarlos localmente.

**Control de Acceso Interno**

-   Solo los/as administradores/as de sistemas autorizados/as pueden acceder al Servidor de KoboToolbox. Solo pueden hacerlo con el propósito expreso de actualizar el software instalado o mantener la infraestructura del servidor.
-   Los/as administradores/as de sistemas requieren autenticación adicional, incluyendo autenticación de Clave Pública SSH, para acceder al Servidor de KoboToolbox y autenticación de dos factores para acceder a los paneles de control proporcionados por AWS.
-   AWS proporciona un registro de las acciones tomadas en la Consola de AWS. Para las conexiones SSH a las instancias individuales del Servidor de KoboToolbox, Kobo recopila "eventos de acceso al sistema" por clave SSH, que luego pueden ser emparejados con los/as usuarios/as autorizados/as.
-   SSH está además protegido contra intentos de fuerza bruta y acceso no autorizado al limitar las conexiones a nivel de firewall a solo una pequeña lista de direcciones IP explícitamente permitidas.

**Protección de Datos por Diseño y por Defecto**

-   Solo se requiere información limitada para crear una cuenta de usuario/a de KoboToolbox.
-   El personal de Kobo está obligado a cumplir con las reglas establecidas en las políticas de privacidad de Kobo.
-   Los datos procesados en nombre del/de la usuario/a no son accedidos por Kobo.
-   Los/as usuarios/as tienen la opción de aplicar encriptación avanzada. Esto asegura que los datos se encripten usando una clave pública antes de ser enviados a un Servidor de KoboToolbox, y que solo puedan ser desencriptados con una clave privada en una computadora local. KoboToolbox también ofrece la posibilidad de eliminar información en masa una vez que ha sido recolectada, facilitando la seudonimización de Datos Personales (a través de la eliminación de identificadores).
-   Consulta la subsección anterior "Control de Acceso Electrónico" para detalles sobre la retroalimentación visual sobre la complejidad de la contraseña.

## Integridad

**Control de Transferencia de Datos**

-   Todos los datos en tránsito están protegidos usando SHA-256 con encriptación RSA.

**Control de Entrada de Datos**

-   Los/as usuarios/as controlan quién tiene permiso para ingresar datos según sus permisos de KoboToolbox. Los registros de acceso HTTP almacenados en el servidor incluyen el/la usuario/a autenticado/a para la mayoría de las solicitudes.

## Disponibilidad y Resiliencia

-   Kobo realiza copias de seguridad diarias de todas las bases de datos en una ubicación remota separada. En caso de una interrupción crítica, todos los datos de los/as usuarios/as serán restaurados desde la copia de seguridad más reciente lo más rápido posible.
-   Los firewalls bloquean todas las solicitudes externas excepto las conexiones SSH desde una pequeña lista de direcciones IP explícitamente permitidas. El tráfico HTTP y HTTPS público no puede conectarse directamente al Servidor de KoboToolbox, en su lugar es atendido por el balanceador de carga de AWS, que luego lo reenvía a los servidores front-end de Kobo.
-   Los Servidores de KoboToolbox están configurados para usar múltiples instancias de servidor ejecutándose simultáneamente y están configurados para aumentar el número de tales instancias para evitar el impacto de cualquier falla localizada. En caso de cualquier otra falla que amenace la operación continua de aspectos críticos del software de KoboToolbox, los/as administradores/as de sistemas están disponibles para intervenir con poca antelación para restaurar el servicio.
-   Los procedimientos de reporte de Kobo incluyen alertas automatizadas, escalamiento de problemas reportados por usuarios/as y problemas auto-detectados por el personal.
-   Los planes de contingencia incluyen la disponibilidad de múltiples personas en múltiples ubicaciones geográficas que pueden responder a emergencias y restaurar el servicio.
-   Los Servidores de KoboToolbox tienen la capacidad demostrada de continuar operando en un estado degradado, recibiendo envíos mientras simultáneamente recuperan proyectos/envíos perdidos a través de recuperación punto en el tiempo (PITR) al minuto.
-   Los/as usuarios/as que abusen del uso de sus cuentas sobrecargando el Servidor de KoboToolbox pueden ser suspendidos/as o su cuenta puede ser restringida.