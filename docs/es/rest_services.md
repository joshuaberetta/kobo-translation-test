# Servicios REST

**Cómo vincular tus datos a otros servidores o servicios usando Servicios REST**

KoboToolbox tiene una serie de funcionalidades avanzadas integradas basadas en nuestras bibliotecas de código abierto, que incluyen complementos útiles para casos de uso avanzados.

Puedes vincular tus datos recolectados con KoboToolbox a otros servidores o servicios que poseas a través de Servicios REST. Los Servicios REST admiten formatos JSON o XML, y autenticación básica. Además, es posible enviar solo un subconjunto de campos.

En caso de fallo, la tarea en segundo plano reintentará 3 veces enviar los datos (primera vez después de 60 segundos, segunda vez después de 600 segundos, y tercera vez después de 6,000 segundos). Se pueden habilitar notificaciones por correo electrónico para recibir un informe de fallos.

Ten en cuenta que tus datos se envían al servidor externo solo al momento de la creación. No se envía nada cuando los datos son editados.

Aquí hay algunos videos tutoriales para usar Servicios REST:

1. Creación

    [![Creación](/images/rest_services/thumbnail_1.jpg)](https://fast.wistia.net/embed/iframe/6i2hw2gcr1 "Creación")

2. Subconjunto de campos (Los campos se agregan presionando "Enter" o "Tab")

    [![Subconjunto de campos](/images/rest_services/thumbnail_2.jpg)](https://fast.wistia.net/embed/iframe/u6su0atm2w "Subconjunto de campos")

3. Fallo/Reintento

    [![Fallo / Reintento](/images/rest_services/thumbnail_3.jpg)](https://fast.wistia.net/embed/iframe/7my5eab5lm "Fallo / Reintento")

4. Envoltura personalizada (Solo disponible con formato JSON)

    [![Envoltura personalizada](/images/rest_services/thumbnail_4.jpg)](https://fast.wistia.net/embed/iframe/pd0czyksbx "Envoltura personalizada")