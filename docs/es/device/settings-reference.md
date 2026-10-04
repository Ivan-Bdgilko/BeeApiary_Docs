# `mset.xml`: Configuración del dispositivo

La configuración principal se almacena en `/setting/mset.xml` en la tarjeta microSD y tiene una `<settings>` elemento raíz.

!!! warning "El archivo actual no es una lista de valores de fábrica."
    Los valores en el XML de un dispositivo en particular pueden haber sido cambiados por el usuario, la interfaz web o automáticamente. Por ejemplo, `sefe_start_interval="60000"` y `alarm_sms_sec_interval="10"` no son valores iniciales: una nueva configuración utiliza `120000` milisegundos y `180` respectivamente.

Ver también el [reglas de edición segura](service-reference.md). no cambiar `SERVICE` parámetros sin una copia de seguridad y una comprensión de su efecto en el dispositivo.

## `net_settings`

Esta sección almacena parámetros para el punto de acceso del dispositivo, conexión a una red Wi-Fi externa, transmisión de datos y FTP. un `SSID`/`PASSWORD` o `SSID_STA`/`PASSWORD_STA` El par se aplica solo cuando ambos valores están presentes y no están vacíos.

| Campo | Función | Obligatoriedad | Valores permitidos / límites | Valor inicial | Si no se especifica | Nivel |
|---|---|---|---|---|---|---|
| `SSID` | Nombre del punto de acceso local del dispositivo | Requerido condicionalmente con `PASSWORD` | Cadena; hasta 32 caracteres | `apiary_net` | El nuevo par de puntos de acceso no se aplica | `USER` |
| `PASSWORD` | Contraseña para el punto de acceso local | Requerido condicionalmente con `SSID` | Cadena; hasta 32 caracteres | `apiary_wifi` | El nuevo par de puntos de acceso no se aplica | `USER` |
| `SSID_STA` | SSID de la red Wi-Fi externa | Opcional | Cadena no vacía; no se especifica una longitud máxima | `-` | Los nuevos parámetros de STA no se aplican | `ADVANCED` |
| `PASSWORD_STA` | Contraseña de la red Wi-Fi externa | Requerido condicionalmente con `SSID_STA` | Cadena; no se especifica una longitud máxima | `-` | Los nuevos parámetros de STA no se aplican | `ADVANCED` |
| `STA_KEY` | Clave de autenticación utilizada durante la transmisión | Opcional | Cadena; el formato depende del método de autenticación | `-` | El parámetro Wi-Fi no se cambia. | `SERVICE` |
| `UPLOAD_URL` | Dirección del receptor de datos Wi-Fi | Opcional | URL; La longitud máxima no está especificada. | Depende de la configuración del dispositivo | Establecer en un solo espacio; la transmisión no está efectivamente configurada | `SERVICE` |
| `wifi_sync` | Permite la sincronización a través de una red Wi-Fi externa | Opcional | `true`, `false` | `false` | `false` | `ADVANCED` |
| `FTP_USER` | Nombre de usuario para FTP local | Opcional como parte de un par. | Cadena; hasta 32 caracteres | Depende de la configuración del dispositivo | Si falta alguno de los campos FTP, se utilizan las configuraciones iniciales de FTP. | `ADVANCED` |
| `FTP_PASSWORD` | Contraseña para FTP local | Opcional como parte de un par. | Cadena; hasta 32 caracteres | Depende de la configuración del dispositivo | Si falta alguno de los campos FTP, se utilizan las configuraciones iniciales de FTP. | `ADVANCED` |

!!! note "El `-` valor"
    Para `SSID_STA`, `PASSWORD_STA`, y `STA_KEY`, el guión es un valor inicial literal. Se procesa como una cadena no vacía, por lo que no la utilice como una indicación confiable de que una configuración "no está configurada".

Cambiar la contraseña inicial `apiary_wifi` después de la primera comprobación del dispositivo.

## `apairy_set`

El nombre de la sección contiene un error histórico y debe permanecer `apairy_set`. Esta sección es necesaria para crear la lista de colmenas.

| Campo | Función | Obligatoriedad | Valores permitidos / límites | Valor inicial | Si no se especifica | Nivel |
|---|---|---|---|---|---|---|
| `hive_count` | Número de archivos de configuración de colmena | Campo opcional en una sección obligatoria | Entero; `1` o más se recomienda; los límites no se verifican automáticamente | `1` | `1` | `ADVANCED` |
| `hive1`…`hiveN` | Nombres base de archivos de colmena sin `.xml` | Requerido para cada número hasta `hive_count` | Cadena; se recomiendan hasta 8 caracteres ASCII por compatibilidad | `hive1` | Error de lectura de atributo; no se crea la colmena correspondiente | `SERVICE` |

El camino tiene la forma. `/setting/<значення>.xml`. El nombre utiliza un búfer interno de 24 bytes, por lo que no utilice nombres largos ni separadores de ruta.

## `GSM`

Esta sección describe dos destinatarios. Si la sección está ausente, se borra la estructura GSM. Por lo tanto, la sección en sí debe considerarse necesaria incluso cuando se utiliza sin tarjeta SIM.

| Campo | Función | Obligatoriedad | Valores permitidos / límites | Valor inicial | Si no se especifica | Nivel |
|---|---|---|---|---|---|---|
| `sms_format1` | formato SMS para `number1` | Opcional | `1` - texto; `2` — formato de aplicación compacto | `2` | `2` | `USER` |
| `sms_format2` | formato SMS para `number2` | Opcional | `1` - texto; `2` — formato de aplicación compacto | `2` | `2` | `USER` |
| `number1` | Número de destinatario principal | Opcional | Formato internacional; buffer interno de 15 bytes | cadena vacía | No se configura ningún destinatario en la primera carga | `USER` |
| `number2` | Número de destinatario adicional | Opcional | Formato internacional; buffer interno de 15 bytes | cadena vacía | No se configura ningún destinatario en la primera carga | `USER` |
| `sms_wait_to_send_sec` | Es hora de esperar antes de enviar un SMS en una red débil | Opcional | Número entero de segundos; sin límites fijos | `50` s | `50` s | `ADVANCED` |
| `alarm_call_wait_sec` | Intervalo entre intentos repetidos de llamada de alarma | Opcional | Número entero de segundos; sin límites fijos | `80` s | `80` s | `ADVANCED` |

Especifique un número vacío como `number1=""` o `number2=""`. No incluya números de teléfono reales en los ejemplos publicados.

## `NTP`

Esta sección pertenece a la misma estructura interna que GSM. si `NTP` está completamente ausente, los parámetros GSM recién leídos también se restablecen. Por lo tanto, la sección debe permanecer presente incluso cuando la sincronización esté desactivada.

| Campo | Función | Obligatoriedad | Valores permitidos / límites | Valor inicial | Si no se especifica | Nivel |
|---|---|---|---|---|---|---|
| `synchronize` | Sincronización horaria automática a través de un mecanismo de red disponible | Campo opcional en una sección obligatoria | `true`, `false` | `false` | `false` | `USER` |
| `time_zone` | Desplazamiento de zona horaria especificado en horas enteras en el XML | Opcional | Entero; `-11` a `12` se recomienda; los límites no se verifican automáticamente | `2` | `3` | `ADVANCED` |
| `ntp1` | Servidor de hora principal | Opcional | Nombre de host; buffer interno hasta 30 bytes | `0.europe.pool.ntp.org` | Vacío en la primera carga | `ADVANCED` |
| `ntp2` | Servidor de hora secundario | Opcional | Nombre de host; buffer interno hasta 30 bytes | `1.europe.pool.ntp.org` | Vacío en la primera carga | `ADVANCED` |
| `ntp3` | Servidor por tercera vez | Opcional | Nombre de host; buffer interno hasta 30 bytes | `2.europe.pool.ntp.org` | Vacío en la primera carga | `ADVANCED` |

`time_zone` tiene valores diferentes en los dos casos: un nuevo archivo recibe `2`, mientras que un atributo faltante da como resultado `3`. Tenga en cuenta esta diferencia antes de cambiar la configuración inicial.

la ortografía `synсhronize` contiene la letra cirílica `с` y no es reconocido. Usar solo `synchronize`.

## `options`

Los atributos individuales son opcionales y tienen valores alternativos. **No elimines toda la sección:** si está ausente, los parámetros de la sección se borran en lugar de recibir los valores iniciales que se muestran a continuación.

| Campo | Función | Obligatoriedad | Valores permitidos / límites | Valor inicial | Si no se especifica | Nivel |
|---|---|---|---|---|---|---|
| `meteo` | Indica la presencia de un sensor de presión y humedad. | Opcional | `true`, `false` | `false` | `false` | `SERVICE` |
| `pir_sensor` | Indica la presencia de un sensor de movimiento PIR | Opcional | `true`, `false` | `false` | `false` | `SERVICE` |
| `temperature_twist` | Intercambia los valores lógicos T1 y T2. | Opcional | `true`, `false` | `false` | `false` | `ADVANCED` |
| `oled` | Indica la presencia de una pantalla OLED | Opcional | `true`, `false` | `false` | `false` | `SERVICE` |
| `oled_invert` | Invierte la imagen OLED | Opcional | `true`, `false` | `false` | `false` | `SERVICE` |
| `sefe_start_interval` | Duración de la ventana activa después del inicio | Opcional | Milisegundos; los límites no se verifican automáticamente | `120000` milisegundos | `120000` milisegundos | `SERVICE` |
| `alarm_sms_sec_interval` | Intervalo mínimo entre mensajes SMS de alarma | Opcional | Número entero sin signo de segundos | `180` s | `180` s | `ADVANCED` |
| `alarm_by_changes_count` | Número de cambios de estado de PIR necesarios para confirmar una alarma | Opcional | Entero sin signo; El valor práctico depende de la ubicación. | `3` | `3` | `ADVANCED` |
| `alarm_by_long_state` | Duración de un estado PIR activo requerido para una alarma | Opcional | Número entero sin signo de segundos | `10` s | `10` s | `ADVANCED` |
| `time_ms_compensate` | Compensación diaria de la velocidad del reloj | Opcional | Número de milisegundos de 32 bits firmados | `0` milisegundos | `0` milisegundos | `SERVICE` |
| `sync_time_sec` | Marca de tiempo del servicio para sincronización manual | Opcional | Número de segundos firmado de 64 bits | `0` | `0` | `SERVICE` |

`sefe_start_interval` es el nombre histórico exacto del campo. Su valor inicial es `120000` milisegundos; el rango no se verifica automáticamente, por lo que reducirlo arbitrariamente es peligroso.

Los indicadores de hardware modificados a través de la interfaz web se guardan inmediatamente, pero la configuración operativa los aplica después de leer la configuración nuevamente.

## `BLE`

Toda la sección es opcional por compatibilidad con archivos más antiguos. Si está ausente, BLE se desactiva y se utilizan los valores actuales y los intervalos estándar.

| Campo | Función | Obligatoriedad | Valores permitidos / límites | Valor inicial | Si no se especifica | Nivel |
|---|---|---|---|---|---|---|
| `ble_enable` | Habilita BLE | Opcional | `true`, `false` | `false` | `false`; un valor no válido también desactiva BLE | `USER` |
| `static_values` | Selecciona valores estáticos en lugar de valores actuales | Opcional | `true`, `false` | `false` | `false` | `SERVICE` |
| `update_time_sec` | Intervalo de actualización de datos BLE | Opcional | `3`–`60` s; los valores más bajos se normalizan a `3`, valores más altos para `60` | `30` s | `30` s | `ADVANCED` |
| `advertising_time_sec` | Duración de la publicidad BLE | Opcional | `0` o `10`–`60` s; valores de `1` a `9` están normalizados a `0`, valores superiores `60` a `60` | `20` s | `20` s | `ADVANCED` |

Para `static_values`, sólo se describe la selección de valores estáticos en lugar de valores actuales; no se define ningún otro efecto del parámetro.

## Ejemplo mínimo { #minimal-example }

Este ejemplo deja STA, FTP y BLE en sus valores iniciales. Un vacío pero presente `<options />` La sección activa el valor de reserva de cada atributo en lugar de borrar toda la estructura.

```xml
<settings>
  <net_settings SSID="apiary_net" PASSWORD="apiary_wifi" />
  <apairy_set hive_count="1" hive1="hive1" />
  <GSM sms_format1="2" sms_format2="2"
       number1="" number2=""
       sms_wait_to_send_sec="50" alarm_call_wait_sec="80" />
  <NTP synchronize="false" time_zone="2"
       ntp1="0.europe.pool.ntp.org"
       ntp2="1.europe.pool.ntp.org"
       ntp3="2.europe.pool.ntp.org" />
  <options />
</settings>
```

## Ejemplo completo de desinfección { #full-example }

los valores `SITE_WIFI`, `WIFI_PASSWORD`, `DEVICE_KEY`, `FTP_USER`, `FTP_PASSWORD`y la URL son marcadores de posición, no datos de un dispositivo operativo.

```xml
<settings>
  <net_settings SSID="apiary_net" PASSWORD="apiary_wifi"
                SSID_STA="SITE_WIFI" PASSWORD_STA="WIFI_PASSWORD"
                STA_KEY="DEVICE_KEY"
                UPLOAD_URL="https://example.invalid/beeapiary"
                wifi_sync="false"
                FTP_USER="FTP_USER" FTP_PASSWORD="FTP_PASSWORD" />
  <apairy_set hive_count="1" hive1="hive1" />
  <GSM sms_format1="2" sms_format2="2"
       number1="+380XXXXXXXXX" number2=""
       sms_wait_to_send_sec="50" alarm_call_wait_sec="80" />
  <NTP synchronize="false" time_zone="2"
       ntp1="0.europe.pool.ntp.org"
       ntp2="1.europe.pool.ntp.org"
       ntp3="2.europe.pool.ntp.org" />
  <options meteo="false" pir_sensor="false"
           temperature_twist="false" oled="false" oled_invert="false"
           sefe_start_interval="120000"
           alarm_sms_sec_interval="180"
           alarm_by_changes_count="3" alarm_by_long_state="10"
           time_ms_compensate="0" sync_time_sec="0" />
  <BLE ble_enable="false" static_values="false"
       update_time_sec="30" advertising_time_sec="20" />
</settings>
```
