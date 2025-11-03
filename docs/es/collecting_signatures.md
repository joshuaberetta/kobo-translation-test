# Tipo de pregunta Firma

Algunos formularios pueden requerir que se incluyan firmas con ellos. Puedes usar el aspecto `signature` tanto en la aplicación de Android de Collect como en Enketo. El widget de dibujo solo está disponible cuando se usa Enketo para la recolección de datos.

## Aplicación de Android de Collect

Collect permite que se recolecte una firma digital directamente en la pantalla del teléfono/tableta.

Para agregar esto a tu formulario:

1. Abre o descarga la versión XLS de tu formulario.
2. Crea la pregunta y establece el tipo como `image`
3. Establece el aspecto como `signature`

## Enketo

Las firmas digitales también funcionan en los formularios web de Enketo, donde tienes la opción adicional de usar un widget de dibujo para recolectar firmas. En tu XLSForm simplemente agrega `signature` o `draw` bajo la columna `appearance` para una pregunta de tipo `image`.

**hoja survey**

| type  | name | label            | appearance | hint                                      |
| :---- | :--- | :--------------- | :--------- | :---------------------------------------- |
| image | draw | Widget de dibujo | draw       | Tipo imagen con aspecto draw              |
| image | sign | Widget de firma  | signature  | Tipo imagen con widget de firma signature |
| survey |

[Sigue este enlace](https://enke.to/draw) para probar la diferencia entre los widgets de dibujo y firma.

## Crear un tipo de pregunta Firma en el editor de formularios

1. Crea una nueva pregunta y selecciona Foto como el tipo de pregunta.

![image](/images/collecting_signatures/new_question.jpg)

2. En Ajustes bajo Opciones de pregunta, haz click en el menú desplegable de Aspecto y selecciona Firma.

![image](/images/collecting_signatures/signature.jpg)