---
title: "Balanzas para colmenas con Wi-Fi — conexión directa y por red"
description: "Conectar BeeApiary Balanzas para colmenas a través de Wi-Fi: un punto de acceso directo a tu teléfono y transmisión remota a través de la red del apiario."
---

# Balanzas para colmenas con Wi-Fi — conexión directa y por red { #wi-fi- }

BeeApiary Las básculas para colmenas con Wi-Fi admiten dos formas de recibir datos: una conexión telefónica directa al punto de acceso (AP) del dispositivo y la transmisión a través de la red Wi-Fi del apiario (STA). El primer método funciona cerca de la balanza; el segundo proporciona acceso remoto a datos cuando hay conectividad a Internet disponible.

## Conexión directa al dispositivo { #direct-access-point }

Después de la activación con la llave magnética, el dispositivo crea temporalmente un punto de acceso local. Por lo general, está disponible durante aproximadamente un minuto, pero este intervalo se puede cambiar en la configuración.

Configuración predeterminada:

```text
SSID: apiary_net
Пароль: apiary_wifi
Вебінтерфейс: http://192.168.4.1
```

A través de la conexión local, puedes:

- permitir que la aplicación recupere el archivo de mediciones;
- abra la interfaz web;
- configurar el número de teléfono del propietario y el horario;
- ver el nivel de carga y la versión del firmware;
- utilice FTP para acceder a los archivos de la tarjeta microSD.

Después de que el teléfono se conecte a `apiary_net`, la aplicación encuentra el dispositivo y muestra el mensaje **"Dispositivo cercano. ¿Recuperar archivo?"**. Los datos se descargan solo después de que el usuario confirma la solicitud.

!!! warning "cambiar la contraseña"
    La contraseña predeterminada es de conocimiento público. Después de la primera verificación, establezca su propia contraseña de hasta 32 caracteres.

Procedimientos detallados:

- [Conéctese al punto de acceso del dispositivo](../guides/configure-local-wifi.md);
- [descargar el archivo a la aplicación](../guides/download-archive.md);
- [ver configuraciones adicionales del dispositivo](../device/additional-settings.md).

## Enrutamiento a través de la red Wi-Fi del Apiary { #apiary-wifi-routing }

El dispositivo puede conectarse a una red Wi-Fi existente en el colmenar y enviar datos automáticamente a través de Internet a la aplicación del propietario. El teléfono puede estar en cualquier lugar con acceso a Internet.

Este método no requiere una tarjeta SIM separada en cada dispositivo, pero debe haber una red Wi-Fi configurada con acceso a Internet disponible cerca del dispositivo.

### Cómo funciona la configuración

Primero, el usuario registra un dispositivo que ya conoce en la aplicación. Durante el registro, el teléfono debe tener acceso a Internet, pero aún no es necesario que esté conectado al dispositivo. El servicio crea identificadores y claves para la comunicación entre la aplicación y el dispositivo.

Luego, el usuario ingresa el nombre y la contraseña de la red Wi-Fi del apiario en la aplicación. La aplicación almacena estas configuraciones en el teléfono, pero el dispositivo aún no las tiene. Para transferirlos, conecte temporalmente el teléfono al `apiary_net` punto de acceso, regrese a la aplicación y confirme que la configuración preparada debe escribirse en el dispositivo.

Después de un reinicio con la llave magnética o durante el siguiente ciclo horario programado, el dispositivo utiliza la red configurada para la transmisión automática. Ya no es necesario que el teléfono esté cerca.

### Requisitos

- el dispositivo ya se ha añadido a la aplicación;
- la aplicación ha recibido sus datos al menos una vez mediante SMS o descarga directa de un archivo;
- el teléfono tiene acceso a Internet durante el registro;
- cerca del dispositivo hay disponible una red Wi-Fi con acceso a Internet;
- el usuario conoce el nombre y la contraseña de esa red.

El relé en línea no almacena datos. El almacenamiento permanente sigue siendo local en el BeeApiary memoria de la báscula para colmenas y en el teléfono del usuario.

Para conocer el procedimiento paso a paso, consulte [Configurar la sincronización a través de la red Wi-Fi de Apiary](../guides/configure-wifi-sync.md).
