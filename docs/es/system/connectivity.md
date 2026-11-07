---
title: "Monitorización del apiario por GSM, Wi-Fi y Bluetooth"
description: "Compare GSM, Wi-Fi directo, la red del apiario y Bluetooth para recibir mediciones en BeeApiary: requisitos de conexión e historial disponible."
---

# Monitorización del apiario por GSM, Wi-Fi y Bluetooth { #_1 }

Para el monitoreo de apiarios, los datos del BeeApiary Las básculas para colmenas pueden acceder a la aplicación de cuatro maneras: a través de GSM/SMS, una conexión Wi-Fi directa, la red Wi-Fi del apiario o Bluetooth. La elección entre monitoreo local y remoto depende de la ubicación del teléfono y de la conexión disponible cerca de la báscula.

| canal | Ubicación del teléfono | Requisitos | Cómo llegan los datos a la aplicación |
|---|---|---|---|
| [GSM y SMS](gsm-and-sms.md) | En cualquier lugar con cobertura móvil | Una tarjeta SIM en el dispositivo con un plan de SMS básico; permiso SMS para la aplicación | La aplicación procesa automáticamente SMS compactos; no necesita Internet móvil. [Configurar GSM](../guides/configure-gsm.md) |
| [Conexión directa al punto de acceso del dispositivo](local-wifi.md#direct-access-point) | Cerca del dispositivo | Active el dispositivo con la llave magnética y conéctese a `apiary_net` dentro del intervalo disponible, generalmente alrededor de un minuto; no se necesita SIM ni Internet | La aplicación encuentra el dispositivo, solicita permiso para recuperar el archivo e importa los datos después de la confirmación. [Descargar archivo](../guides/download-archive.md) |
| [Enrutamiento a través de la red wifi del apiario](local-wifi.md#apiary-wifi-routing) | Cualquier lugar con acceso a Internet | Debe haber una red Wi-Fi configurada con acceso a Internet disponible cerca del dispositivo | Los datos se enrutan a la aplicación automáticamente; no se requiere una tarjeta SIM separada para cada dispositivo. [Configurar Wi-Fi](../guides/configure-wifi-sync.md) |
| [bluetooth](bluetooth.md) | Cerca, dentro del alcance de Bluetooth | **BLE info**, el escaneo BLE y la operación en segundo plano de la aplicación están habilitados; la hora está sincronizada; no se requiere tarjeta SIM ni Internet | La aplicación sincroniza automáticamente los datos actuales y puede restaurar el historial disponible. [Configurar Bluetooth](../guides/configure-bluetooth-sync.md) |

## GSM y SMS

Los SMS normales se leen sin aplicación; la aplicación guarda los mensajes compactos como mediciones. [Formatos SMS](gsm-and-sms.md).

## Conexión directa al dispositivo

El teléfono conectado recibe el archivo solo tras la confirmación. [Conectar al punto de acceso](../guides/configure-local-wifi.md).

## Enrutamiento a través de la red Wi-Fi del Apiary

Antes de configurar, la aplicación debe haber recibido datos de la báscula al menos una vez por SMS o descarga directa. El servicio no almacena copias permanentes: permanecen en la báscula y el teléfono. Puede ser inestable o de pago; consulta la [compatibilidad y condiciones](../guides/configure-wifi-sync.md).

## bluetooth

Si está activada la recuperación del historial, los intervalos faltantes pueden completarse en la próxima conexión. [Funcionamiento y compatibilidad](bluetooth.md).

## Operación sin conexión

Una pérdida temporal o total de cualquier canal de comunicación no detiene las mediciones: el dispositivo continúa grabándolas en microSD. Una vez que se restablece la conexión, la aplicación puede recuperar los datos perdidos, pero la profundidad del historial disponible depende del canal seleccionado.

| canal | Historial disponible después de restaurar la conexión | Nota |
|---|---|---|
| GSM y SMS | 2 a 12 horas | Depende del horario de transmisión de SMS configurado |
| Conexión directa al punto de acceso del dispositivo | Hasta 1 año | Los datos se pueden descargar si los registros correspondientes están presentes en el archivo local. |
| bluetooth | 1 día a 1 semana | Depende de la configuración de recuperación del historial y de los registros disponibles |
| Enrutamiento a través de la red wifi del apiario | El historial no está disponible | El repetidor en línea transfiere los datos actuales pero no los almacena en el servidor. |

Estos límites se aplican únicamente a la cantidad de datos perdidos que se pueden restaurar a través de un canal en particular. el local [archivo microSD](data-storage.md) no tiene límite de almacenamiento de un año: su profundidad está limitada únicamente por la capacidad de la tarjeta, que es suficiente para toda la vida útil esperada del dispositivo. Si es necesario, los datos también se pueden leer directamente desde la tarjeta microSD.
