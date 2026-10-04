# Cómo actualizar el firmware de las balanzas BeeApiary

Antes de actualizar, seleccione el firmware que coincida con la generación del dispositivo y el idioma de interfaz requerido.

## Seleccione la generación del firmware

| Dispositivo | Fuente de actualización | Estado de desarrollo |
|---|---|---|
| Fabricado antes de agosto de 2026. | [Hive_Controller](https://github.com/Ivan-Bdgilko/Hive_Controller) | Ya no se admite el desarrollo de funciones para la versión anterior. |
| Fabricado después de agosto de 2026. | [Hive_Controller_Ble](https://github.com/Ivan-Bdgilko/Hive_Controller_Ble) | La nueva versión continúa recibiendo actualizaciones y nuevas funcionalidades. |

!!! danger "Migrar un dispositivo antiguo a la nueva versión"
    Cualquier dispositivo fabricado previamente se puede migrar a la nueva versión de software, pero esto requiere una actualización de fábrica. Actualmente no existe un parche simple para una migración de autoservicio, por lo que el procedimiento estándar en esta página no migra un dispositivo entre generaciones.

## Seleccione el idioma del firmware

Ambas generaciones proporcionan compilaciones multilingües. El sufijo en el nombre de la versión identifica el idioma:

| sufijo | Idioma |
|---|---|
| `-de` | alemán |
| `-en` | ingles |
| `-es` | español |
| `-fr` | francés |
| `-pl` | polaco |
| `-uk` | Ucraniano |

Seleccione el idioma descargando y flasheando el archivo correspondiente. Las compilaciones de idiomas están disponibles públicamente en los repositorios enumerados anteriormente y se pueden agregar más idiomas más adelante si es necesario.

## Actualiza el dispositivo usando microSD

1. Espere hasta que el dispositivo entre en modo de suspensión y luego retire la tarjeta microSD.
2. Crea el `/fm` directorio en la raíz de la tarjeta si aún no existe.
3. Coloque el `Apiary.bin` actualizar archivo en `/fm`.
4. Vuelva a insertar la tarjeta microSD en el dispositivo.
5. [Activar o reiniciar el dispositivo](../device/installation.md#activation-reset) con la llave magnética.
6. Espere un mensaje SMS normal que contenga mediciones; la actualización suele tardar hasta dos minutos.
7. En la parte inferior de la página de inicio de la interfaz web, verifique la versión del firmware, el sufijo de idioma, la fecha y hora de compilación y el número de dispositivo único.

![Versión de firmware, sufijo de idioma, tiempo de compilación e identificación única en la interfaz web del dispositivo](../../assets/common/guides/update-device/device-version-build-time-and-id.png){ .doc-screenshot }

La cadena de versión completa incluye el sufijo de localización, por ejemplo `-uk`. Compárelo con la versión de actualización correspondiente en el repositorio para la generación de su dispositivo. La misma página también muestra la fecha y hora de compilación y el identificador único del dispositivo.

!!! warning "Verifique el archivo antes de actualizar"
    Asegúrate `Apiary.bin` está diseñado para la generación de su dispositivo y el idioma requerido. Los métodos de actualización del servicio a través de FTP o un servidor están fuera del alcance de este procedimiento.
