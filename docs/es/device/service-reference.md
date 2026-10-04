# Documentación de servicio

Esta sección es un archivo de configuración técnica para el BeeApiary balanzas de colmena. Está destinado a técnicos de servicio y usuarios experimentados que necesitan restaurar o inspeccionar archivos XML manualmente.

Los valores iniciales de algunos parámetros de hardware y red dependen de la configuración del dispositivo en particular.

!!! danger "Edición manual"
    Los pines de hardware, los valores de calibración o los intervalos de servicio incorrectos pueden interrumpir las mediciones o el funcionamiento del dispositivo. Utilice la interfaz web para cambios habituales. Cree siempre una copia de seguridad del `/setting` directorio antes de editar archivos manualmente.

## Procedimiento seguro

1. Espere hasta que el dispositivo entre en modo de suspensión. El dispositivo no tiene un botón de encendido estándar: durante el funcionamiento, está activo o en hibernación.
2. Retire la tarjeta microSD y guarde una copia completa del `/setting` directorio.
3. Edite el XML en un editor de texto sin cambiar los nombres de secciones o atributos.
4. Asegúrese de que el XML tenga uno `<settings>` elemento raíz y que todas las comillas y etiquetas de cierre estén presentes.
5. Vuelva a insertar la tarjeta microSD mientras el dispositivo está inactivo. La configuración actualizada se aplica la próxima vez que la configuración se cargue normalmente; Algunos cambios realizados a través de la interfaz web también entran en vigor solo después de reiniciar.
6. Consultar medidas, comunicación y registro de servicios. Mantenga la copia de seguridad hasta que se complete la verificación.

Al guardar, el dispositivo puede normalizar el archivo: agregar secciones o atributos faltantes, sustituir valores alternativos y reescribir el orden de los elementos.

## Archivos

- [`/setting/mset.xml`](settings-reference.md) — red, GSM, hora, opciones de hardware, alarmas generales y BLE.
- [`/setting/<hive>.xml`](hive-settings-reference.md) — sensores para una colmena en particular, peso, horario, frecuencia de verificación y alarmas de umbral.
- [Restaurando la configuración](recovery.md) — reemplazo seguro de microSD, restauración desde una copia de seguridad y verificación XML.

El nombre del archivo de la colmena está especificado por el `hive1`, `hive2`y atributos posteriores sin extensión. el `.xml` La extensión se agrega automáticamente.

## Niveles de acceso

| Etiqueta | Significado |
|---|---|
| `USER` | El valor se puede cambiar a través de la interfaz estándar. |
| `ADVANCED` | Se requiere una comprensión de su efecto sobre la comunicación o la lógica operativa. |
| `SERVICE` | Los cambios manuales pueden hacer que el dispositivo no funcione o distorsionar los datos. |

En las mesas, `—` significa que los límites no se aplican al campo. **Valor inicial** es el valor en una configuración recién creada, no en el XML de un dispositivo en particular. **Si no se especifica** describe el valor utilizado cuando el atributo está ausente, que puede diferir del valor inicial.

## Nombres históricos

Los identificadores XML exactos no se corrigen incluso cuando contienen errores: `apairy_set`, `sefe_start_interval`, `normal_pecision`, y `calibrate_pecision` debe permanecer exactamente como está escrito. la ortografía `synсhronize` con la letra cirílica `с` es incorrecto; usar `synchronize`.
