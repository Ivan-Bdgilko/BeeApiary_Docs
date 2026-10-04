# Cómo configurar nuevas balanzas BeeApiary

1. Cargue el dispositivo a través de USB Type-C.

    !!! note "Elegir cargador y cable"
        El dispositivo no admite carga rápida, incluida la entrega de energía USB (PD). Utilice una fuente de alimentación estándar con un puerto USB tipo A y un cable USB tipo A-USB tipo C. No se recomienda un cable USB Type-C-USB Type-C para cargar.

2. Instale el dispositivo y los sensores según las [pautas de colocación](../device/placement.md).
3. Inserte una micro-SIM con la protección PIN desactivada.

    Utilice el formato micro-SIM:

    ![Comparación de formatos de tarjetas SIM](../../assets/en/quick-start/gsm/micro-sim-format-comparison.png){ .doc-photo }

    Tarjeta correctamente instalada:

    ![Micro-SIM correctamente instalada](../../assets/common/device/installation/micro-sim-insertion-orientation.jpeg){ .doc-photo }

    Inserta la tarjeta SIM y presiónala suavemente casi por completo en la ranura hasta que escuches un suave clic que confirme que está bloqueada en su lugar:

    ![micro-SIM bloqueada en la ranura](../../assets/common/device/installation/micro-sim-locked-in-slot.jpeg){ .doc-photo }

4. Active o reinicie el dispositivo: mantenga brevemente la llave magnética contra la marca en la parte posterior de la unidad principal.

    ![BeeApiary llave magnética](../../assets/common/device/installation/magnetic-key.png){ .doc-photo }

    ![Objetivo de llave magnética con marca](../../assets/common/device/installation/magnetic-key-target.png){ .doc-photo }

    Para obtener más información, consulte [Activación y reinicio](../device/installation.md#activation-reset).

5. Conéctate a `apiary_net` y abierto `http://192.168.4.1`.
6. Ingrese el número de teléfono del propietario en formato internacional.
7. Desconectarse de `apiary_net` y verifique el primer mensaje SMS.

Resultado: el dispositivo recopila mediciones, las envía al propietario y almacena un archivo.
