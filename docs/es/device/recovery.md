# Restaurando la configuración

Esta página explica cómo reemplazar la tarjeta microSD de forma segura, restaurar la configuración desde una copia de seguridad y verificar los archivos XML después de iniciar el dispositivo.

!!! danger "No retires la tarjeta microSD mientras el dispositivo esté activo"
    El dispositivo no tiene un botón de encendido estándar. Antes de retirar o instalar la tarjeta microSD, espere hasta que el dispositivo entre en modo de suspensión. Primero, guarde una copia completa del `/setting` directorio.

## Normalización automática

- el archivo principal se encuentra en `/setting/mset.xml`;
- si falta el archivo principal, el dispositivo puede crear una configuración inicial;
- un archivo de colmena faltante o incompleto se puede guardar nuevamente utilizando valores alternativos del estado actual;
- un desaparecido `hive`, `thermometer`, o `schedule` sección, así como una existente incompleta `scales` sección, desencadena la normalización del archivo colmena;
- un completamente desaparecido `scales` sección no es un error: las balanzas simplemente no se crean;
- errores estructurales en el elemento XML raíz, el `apairy_set` sección, o la `hiveN` El atributo puede impedir que se lea la configuración.

Creando una inicial `mset.xml` no significa que cada parámetro tendrá un valor universal. `UPLOAD_URL`, las credenciales FTP, los pines HX711 y algunos otros campos dependen de la configuración del dispositivo o de la configuración individual.

!!! warning "Se requiere una copia de seguridad"
    No confíe en la recuperación automática como única copia de seguridad. Antes de reemplazar la tarjeta microSD, guarde toda la `/setting` directorio si la tarjeta aún se puede leer.

## Reemplazo de la tarjeta microSD de forma segura

1. Espere a que el dispositivo entre en modo de suspensión.
2. Retire la tarjeta microSD y, si es legible, copie todo su contenido.
3. Prepare la tarjeta microSD de acuerdo con los requisitos de la versión de hardware específica del dispositivo.
4. Restaurar el `/setting` directorio a partir de una copia de seguridad verificada.
5. Si no existe una copia de seguridad, no utilice los valores de calibración de la báscula de otro dispositivo. Primero restaurar un mínimo [`mset.xml`](settings-reference.md#minimal-example), luego cree el archivo colmena sin un `scales` sección o realice el procedimiento de calibración estándar.
6. Instale la tarjeta microSD mientras el dispositivo está inactivo y espere el siguiente ciclo de funcionamiento.
7. Consulta la hora, red, números GSM, sensores disponibles, horario y peso.
8. Compare los archivos XML normalizados con la copia de seguridad: es posible que el dispositivo haya agregado campos con valores alternativos o secciones reescritas.

## Si la configuración no se puede leer

1. Comprueba que el archivo tiene uno. `<settings>` elemento raíz.
2. Comprueba los nombres exactos `apairy_set`, `synchronize`, `sefe_start_interval`, y `pecision` en los tres campos de filtro.
3. Asegúrate `hive_count` tiene coincidencia `hive1`…`hiveN` atributos.
4. Asegúrese de que todos los referenciados `/setting/<hive>.xml` el archivo existe.
5. No intente solucionar el problema copiando `scales` desde otro dispositivo. Retire temporalmente la sección de báscula y verifique el resto de la configuración.
6. Guarde los archivos XML problemáticos y los registros de servicio para realizar diagnósticos.

Para obtener una descripción completa de los campos, consulte la [`mset.xml`](settings-reference.md) y [`HIVE*.XML`](hive-settings-reference.md) referencias.
