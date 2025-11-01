# Incluir P-Codes en los datos de salida

Si utilizas listas en cascada, por favor [sigue las instrucciones](cascading_select.md)
para selecciones en cascada.

Normalmente, solo el "Name" (nombre) y NO el "Label" (etiqueta) aparecerá en tu archivo Excel
exportado, lo que significa que solo el P-code O el nombre de la ubicación aparecerá.

Para obtener **tanto el P-code como el nombre** como parte de tus datos exportados, haz lo
siguiente:

1. En todas las columnas "Name" (nombre) de tu formulario exportado, usa el P-code de la ubicación
2. En todas las columnas "Label" (etiqueta) de tu formulario exportado, usa el nombre de la ubicación
3. Para cada nivel administrativo que uses, añade una pregunta con tipo "calculate" (cálculo), usando la
   sintaxis:

`if(string-length(${name_of_pcode_column}) != 0,jr:choice-name(${name_of_pcode_column},'${name_of_pcode_column}'),'(unspecified name_of_pcode_column)')`

<p class="note">Esta fórmula extraerá el "Label" (etiqueta) (es decir, el nombre de la ubicación) de la entrada, y obtendrás en tus resultados exportados tanto el nombre como el p-code.</p>

## Ejemplo con 3 niveles administrativos, usando listas en cascada

**hoja survey**

| type              | name         | label   | choice_filter                                    | calculation                                                                                                               |
| :---------------- | :----------- | :------ | :----------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------ |
| select_one admin1 | pcode_admin1 | Admin 1 |                                                  |                                                                                                                           |
| select_one admin2 | pcode_admin2 | Admin 2 | state=${pcode_admin1}                            |                                                                                                                           |
| select_one admin3 | pcode_admin3 | Admin 3 | state=${pcode_admin1} and county=${pcode_admin2} |                                                                                                                           |
| calculate         | name_admin1  |         |                                                  | if(string-length(${pcode_admin1}) != 0, jr:choice-name(${pcode_admin1}, '${pcode_admin1}'), '(unspecified pcode_admin1)') |
| calculate         | name_admin2  |         |                                                  | if(string-length(${pcode_admin2}) != 0, jr:choice-name(${pcode_admin2}, '${pcode_admin2}'), '(unspecified pcode_admin2)') |
| calculate         | name_admin3  |         |                                                  | if(string-length(${pcode_admin3}) != 0, jr:choice-name(${pcode_admin3}, '${pcode_admin3}'), '(unspecified pcode_admin3)') |
| survey |

**hoja choices**

| list_name | name | label       | state | county |
| :-------- | :--- | :---------- | :---- | :----- |
| admin1    | 11   | Texas       |       |        |
| admin1    | 12   | Washington  |       |        |
| admin2    | 13   | King        | 11    |        |
| admin2    | 14   | Pierce      | 11    |        |
| admin2    | 15   | Puyallup    | 12    |        |
| admin2    | 16   | Cameron     | 12    |        |
| admin3    | 17   | Dumont      | 11    | 13     |
| admin3    | 18   | Finney      | 11    | 13     |
| admin3    | 19   | Brownsville | 11    | 14     |
| admin3    | 20   | Harlingen   | 11    | 14     |
| admin3    | 21   | Seattle     | 12    | 15     |
| admin3    | 22   | Redmond     | 12    | 15     |
| admin3    | 23   | Tacoma      | 12    | 16     |
| admin3    | 24   | King        | 12    | 16     |
| choices |