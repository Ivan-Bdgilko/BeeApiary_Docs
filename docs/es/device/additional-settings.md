# Configuraciones adicionales del dispositivo

El **Configuraciones adicionales** La página pertenece a la interfaz web del BeeApiary balanzas de colmena. Especifica qué hardware adicional está instalado y controla los canales de transmisión de datos individuales.

## Cómo abrirlo

1. [Conéctese al punto de acceso del dispositivo](../guides/configure-local-wifi.md).
2. Abierto `http://192.168.4.1`.
3. En la página de inicio, seleccione **Configuraciones adicionales**.
4. Lea la advertencia de la interfaz web. Proceda únicamente a comprobar o cambiar deliberadamente la configuración.

!!! warning "No cambie la configuración al azar"
    Un valor incorrecto puede interrumpir el funcionamiento del dispositivo. Habilite los indicadores de hardware solo cuando el hardware correspondiente esté instalado físicamente. No cambie la configuración o las claves de la red innecesariamente.

![Configuraciones adicionales en la interfaz web del BeeApiary balanzas de colmena](../../assets/uk/device/additional-settings/device-additional-settings.jpg){ .doc-screenshot }

Los valores de red en la captura de pantalla son solo ejemplos. Serán diferentes en su dispositivo.

## interruptores

| Artículo | Función | Notas |
|---|---|---|
| **BLE info** | Permite la sincronización de datos locales a través de Bluetooth. | Después de habilitarlo, configure [Sincronización Bluetooth en la aplicación](../guides/configure-bluetooth-sync.md). |
| **GSM** | Habilita el módulo GSM y la transmisión de datos vía SMS. | Desactívelo si no se utiliza la comunicación GSM, por ejemplo durante el almacenamiento invernal sin transmisión de datos. |
| **Sincronización WiFi** | Permite la transmisión automática de datos a través de una red Wi-Fi externa. | Por lo general, se habilita automáticamente cuando la aplicación transfiere la configuración de nube y Wi-Fi preparada al dispositivo. No lo habilites manualmente sin los campos de red correctos. |
| **Pantalla** | Le indica al dispositivo que hay una pantalla OLED instalada físicamente y habilita su funcionamiento. | Habilítelo solo si hay una pantalla instalada. |
| **invertido** | Gira la imagen de la pantalla OLED 180°. | Sólo es relevante cuando **Pantalla** está habilitado. |
| **El tiempo** | Habilita el sensor meteorológico instalado para presión, humedad y temperatura adicional. | Habilítelo solo si el sensor está instalado. |
| **Intercambiar T1/T2** | Intercambia los valores transmitidos de los termómetros principales T1 y T2. | Útil si los sensores internos y externos se han intercambiado físicamente. Deje los nombres de los canales y la configuración en la aplicación sin cambios. |
| **Sensor PIR** | Habilita la entrada de alarma para PIR u otro sensor de despertador del sistema compatible. | Habilítelo solo si hay un sensor conectado. |

## Campos de red

| Campo | Función | Notas |
|---|---|---|
| **Red Wi-Fi** | Nombre de la red Wi-Fi externa a la que se conectará el dispositivo. | Debe coincidir exactamente con el SSID de la red disponible cerca del dispositivo. |
| **contraseña wifi** | Contraseña de la red Wi-Fi externa. | La interfaz web enmascara el valor. |
| **clave STA** | Clave de transmisión del servicio obtenida durante el registro a través de la aplicación. | No editar manualmente. |

Es más seguro configurar los parámetros de Wi-Fi a través de [configuración de sincronización en la aplicación](../guides/configure-wifi-sync.md). La aplicación crea los datos necesarios y los transfiere al dispositivo durante una conexión directa a `apiary_net`.
