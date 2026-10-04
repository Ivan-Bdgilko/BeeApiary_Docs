---
title: "Monitorización del apiario por GSM, Wi-Fi y Bluetooth"
description: "Compare GSM, Wi-Fi directo, la red del apiario y Bluetooth para recibir mediciones en BeeApiary: requisitos de conexión e historial disponible."
---

# Monitorización del apiario por GSM, Wi-Fi y Bluetooth { #_1 }

Para el monitoreo de apiarios, los datos del BeeApiary Las básculas para colmenas pueden acceder a la aplicación de cuatro maneras: a través de GSM/SMS, una conexión Wi-Fi directa, la red Wi-Fi del apiario o Bluetooth. La elección entre monitoreo local y remoto depende de la ubicación del teléfono y de la conexión disponible cerca de la báscula.

| canal | Ubicación del teléfono | Requisitos | Cómo llegan los datos a la aplicación |
|---|---|---|---|
| [GSM y SMS](gsm-and-sms.md) | En cualquier lugar con cobertura móvil | Una tarjeta SIM en el dispositivo con un plan de SMS básico | La aplicación procesa mensajes SMS automáticamente; No se requiere Internet móvil |
| [Conexión directa al punto de acceso del dispositivo](local-wifi.md#direct-access-point) | Cerca del dispositivo | Active el dispositivo con la llave magnética y conéctese a `apiary_net` dentro del intervalo disponible, generalmente alrededor de un minuto | La aplicación encuentra el dispositivo, solicita permiso para recuperar el archivo e importa los datos después de la confirmación. |
| [Enrutamiento a través de la red wifi del apiario](local-wifi.md#apiary-wifi-routing) | Cualquier lugar con acceso a Internet | Debe haber una red Wi-Fi configurada con acceso a Internet disponible cerca del dispositivo | Los datos se enrutan a la aplicación automáticamente; no se requiere una tarjeta SIM separada para cada dispositivo |
| [bluetooth](bluetooth.md) | Cerca, dentro del alcance de Bluetooth | **BLE info**, el escaneo BLE y la operación en segundo plano de la aplicación están habilitados; la hora está sincronizada; no se requiere tarjeta SIM ni Internet | La aplicación sincroniza automáticamente los datos actuales y puede restaurar el historial disponible. |

## GSM y SMS

El dispositivo envía mensajes SMS regulares o compactos sin Internet móvil. La aplicación reconoce mensajes compactos y agrega automáticamente las medidas al almacenamiento local del teléfono.

## Conexión directa al dispositivo

Después de la activación con la llave magnética, el dispositivo crea temporalmente la `apiary_net` punto de acceso. Un teléfono conectado no necesita una tarjeta SIM ni acceso a Internet. La aplicación encuentra el dispositivo automáticamente pero descarga el archivo solo después de que el usuario confirma la solicitud.

Para conocer el procedimiento detallado, consulte [Descargar el archivo](../guides/download-archive.md).

## Enrutamiento a través de la red Wi-Fi del Apiary

El dispositivo puede utilizar una red Wi-Fi existente con acceso a Internet en el colmenar. El propietario recibe datos de forma remota en la aplicación sin una tarjeta SIM separada para cada dispositivo.

Antes de la configuración inicial, la aplicación debe haber recibido datos del dispositivo al menos una vez a través de SMS o una descarga directa de un archivo. El registro se completa en un teléfono con acceso a Internet y la configuración de Wi-Fi y de nube preparada se transfiere al dispositivo a través de su `apiary_net` punto de acceso.

El relé en línea no almacena datos. Las copias permanentes permanecen en el BeeApiary memoria de la báscula para colmenas y en el teléfono del usuario.

Para conocer el procedimiento detallado, consulte [Configurar la sincronización a través de la red Wi-Fi de Apiary](../guides/configure-wifi-sync.md).

## bluetooth

Cuando el teléfono está dentro del alcance de Bluetooth, la aplicación sincroniza automáticamente los datos disponibles. Esto no requiere una tarjeta SIM, Internet móvil o activación del `apiary_net` punto de acceso. Cuando la recuperación del historial está habilitada, los espacios temporales se pueden llenar durante la próxima conexión exitosa.

Para una explicación, ver [Sincronización de datos por Bluetooth](bluetooth.md). Para el procedimiento práctico, consulte [Configurar la sincronización Bluetooth](../guides/configure-bluetooth-sync.md).

## Operación sin conexión

Una pérdida temporal o total de cualquier canal de comunicación no detiene las mediciones: el dispositivo continúa grabándolas en microSD. Una vez que se restablece la conexión, la aplicación puede recuperar los datos perdidos, pero la profundidad del historial disponible depende del canal seleccionado.

| canal | Historial disponible después de restaurar la conexión | Nota |
|---|---|---|
| GSM y SMS | 2 a 12 horas | Depende del horario de transmisión de SMS configurado |
| Conexión directa al punto de acceso del dispositivo | Hasta 1 año | Los datos se pueden descargar si los registros correspondientes están presentes en el archivo local. |
| bluetooth | 1 día a 1 semana | Depende de la configuración de recuperación del historial y de los registros disponibles |
| Enrutamiento a través de la red wifi del apiario | El historial no está disponible | El repetidor en línea transfiere los datos actuales pero no los almacena en el servidor. |

Estos límites se aplican únicamente a la cantidad de datos perdidos que se pueden restaurar a través de un canal en particular. el local [archivo microSD](data-storage.md) no tiene límite de almacenamiento de un año: su profundidad está limitada únicamente por la capacidad de la tarjeta, que es suficiente para toda la vida útil esperada del dispositivo. Si es necesario, los datos también se pueden leer directamente desde la tarjeta microSD.
