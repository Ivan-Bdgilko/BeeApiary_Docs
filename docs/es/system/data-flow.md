---
title: "Cómo llegan los datos de la colmena al teléfono"
description: "como BeeApiary mide, almacena y transfiere datos de la colmena a su teléfono para ver lecturas actuales, historial y gráficos."
---

# Cómo llegan los datos de la colmena al teléfono { #_1 }

BeeApiary El monitoreo de colmenas cubre la medición, el almacenamiento local y la transmisión de datos a la aplicación. Los pasos a continuación muestran la ruta desde una medición en el dispositivo hasta las lecturas, el historial y los gráficos actuales en su teléfono.

1. Al comienzo de cada hora, el BeeApiary Las básculas para colmenas toman las medidas configuradas.
2. El resultado se guarda en el archivo microSD local cuando la tarjeta está disponible.
3. El dispositivo proporciona los datos a través del canal configurado:

    - envía un mensaje SMS regular o compacto según el horario;
    - enruta datos a través de la red Wi-Fi del apiario;
    - [transmite los datos disponibles por Bluetooth](bluetooth.md) cuando el teléfono está cerca;
    - proporciona el archivo a la aplicación a través de su propio punto de acceso después de la confirmación del usuario.

4. La aplicación reconoce los valores recibidos y los añade al almacenamiento local del teléfono.
5. El usuario ve los valores actuales, el historial y los gráficos.

La ausencia de GSM, Wi-Fi, Bluetooth o un teléfono cercano no detiene el proceso de medición central. Los datos se pueden transferir a la aplicación cuando haya una conexión disponible.

Cuando los datos se enrutan de forma remota a través de Wi-Fi, el relé en línea no los almacena. Las copias permanentes permanecen en el BeeApiary memoria de la báscula para colmenas y en el teléfono del usuario.

Para una comparación de canales, consulte [Recibir datos en la aplicación](connectivity.md).

Para configurar el canal remoto, consulte [Sincronización a través de la red Wi-Fi del Apiary](../guides/configure-wifi-sync.md).

Para configurar el canal automático local, consulte [Sincronización Bluetooth](../guides/configure-bluetooth-sync.md).
