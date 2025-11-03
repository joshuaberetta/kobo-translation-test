# Tipo de pregunta Código de barras/Código QR

El tipo de pregunta "Código de barras/Código QR" se utiliza para escanear, decodificar y capturar códigos de barras y códigos QR usando la cámara del dispositivo. Cuando se escanea un código con la cámara, se captura el valor (ya sean números o texto) almacenado en el código.

<p class="note">
  El escaneo de códigos de barras/códigos QR solo funciona cuando <a href="https://support.kobotoolbox.org/kobocollect_on_android_latest.html">usas KoboCollect</a> en dispositivos móviles.
</p>

Se admite una amplia gama de formatos de códigos de barras y códigos QR, incluidos los siguientes:

- UPC-A
- UPC-E
- EAN-8
- EAN-13
- Code 39
- Code 93
- Code 128
- Codabar
- ITF
- RSS-14
- RSS-Expanded
- QR Code
- Data Matrix
- Aztec
- PDF 417
- MaxiCode

Las preguntas de "Código de barras/Código QR" se pueden usar en diferentes escenarios, incluida la gestión de activos o la distribución de artículos. Por ejemplo, puedes escanear un código QR en una tarjeta de identidad de beneficiario/a para capturar su número de identificación. Luego puedes usar la función `pulldata()` para completar automáticamente campos desde un CSV adjunto a tu proyecto o desde un [proyecto vinculado](dynamic_data_attachment.md) con información sobre el/la beneficiario/a. Puedes obtener más información sobre la función `pulldata()` [aquí](https://xlsform.org/en/#how-to-pull-data-from-csv).

## Cómo configurar el tipo de pregunta "Código de barras/Código QR"

### Configuración en el editor de formularios de KoboToolbox (Formbuilder)

Para añadir una pregunta de "Código de barras/Código QR":

- Haz click en el botón <i class="k-icon k-icon-plus"></i> para añadir una nueva pregunta
- Escribe el texto de la pregunta, por ejemplo "Recolectar el código de identificación del/de la beneficiario/a", luego haz click en **AÑADIR PREGUNTA** o presiona ENTER en tu teclado
- Elige el tipo de pregunta

![Añadir preguntas de Código de barras/Código QR](images/barcode_qrcode_questions/adding_barcode_qrcode_questions.gif)

### Configuración en XLSForm

Para añadir una pregunta de "Código de barras/Código QR" en XLSForm, añade una pregunta con el tipo `barcode` de la siguiente manera:

| type    | name           | label                                         |
| :------ | :------------- | :-------------------------------------------- |
| barcode | beneficiary_id | Capturar el código de identificación del/de la beneficiario/a |
| survey  |

## Cómo se muestran las preguntas de "Código de barras/Código QR" en formularios web y KoboCollect

### Aspecto predeterminado

![Aspecto predeterminado de las preguntas de Código de barras/Código QR](images/barcode_qrcode_questions/barcode_qrcode_default.png)

### Aspecto avanzado

Al añadir el tipo de pregunta "Código de barras/Código QR", puedes cambiar la configuración de aspecto para cambiar del uso de la cámara predeterminada (trasera) del dispositivo al uso de la cámara frontal.

### Cambiar el aspecto avanzado en el editor de formularios de KoboToolbox (Formbuilder)

Ve a la configuración de la pregunta "Código de barras/Código QR" y escribe "front" en el cuadro "Aspecto (Avanzado)"

![Cambiar el aspecto de las preguntas de Código de barras/Código QR](images/barcode_qrcode_questions/change_appearance_barcode_qrcode_questions.png)

### Cambiar el aspecto avanzado en XLSForm

En XLSForm, puedes configurar la cámara predeterminada para capturar el "Código de barras/Código QR" como la cámara frontal escribiendo 'front' en la columna `appearance` de la siguiente manera:

| type    | name             | label                                         | appearance |
| :------ | :--------------- | :-------------------------------------------- | :--------- |
| barcode | beneficiary_id_2 | Capturar el código de identificación del/de la beneficiario/a | front      |
| survey  |

<p class="note">
  Puedes descargar un XLSForm con ejemplos de este artículo
  <a
    download
    class="reference"
    href="./_static/files/barcode_qrcode_questions/barcode_qrcode_questions.xlsx"
    >aquí</a
  >.
</p>