# Recuperar el dispositivo después de un almacenamiento prolongado

Después de un almacenamiento prolongado, es posible que la batería se descargue por completo y que el dispositivo no responda a una conexión de alimentación normal. Si el voltaje de la celda 18650 está por debajo `3,5 В`, recupere el dispositivo en el siguiente orden.

!!! danger "Polaridad de la batería"
    Antes de retirar la batería, ubique el `+` y `-` Marcas en la celda y el soporte. Recuerde o fotografíe la orientación correcta. Instalar la batería con la polaridad invertida puede dañar permanentemente el dispositivo.

1. Retire la batería del dispositivo.
2. Cárguelo en un cargador separado diseñado para 18650 celdas.
3. Después de cargar, verifique el voltaje de la batería. Instálelo en el dispositivo sólo cuando el voltaje sea `4,0 В` o superior.
4. Instale la batería, siguiendo cuidadosamente la polaridad marcada.
5. Conecte una fuente de alimentación externa estándar al puerto USB tipo C del dispositivo sin carga rápida Power Delivery (PD). Utilice un cargador con un puerto USB tipo A y un cable USB tipo A a USB tipo C; No se recomienda un cable USB tipo C a USB tipo C.
6. Con la batería instalada y la alimentación externa conectada, [activar el dispositivo con la llave magnética](../device/installation.md#activation-reset).
7. Sincronice la hora de una de estas maneras:

    - [conectarse al punto de acceso del dispositivo a través de Wi-Fi](../guides/configure-local-wifi.md) y abra su página de inicio; este método está disponible de forma predeterminada;
    - [configurar la sincronización Bluetooth](../guides/configure-bluetooth-sync.md), abre el BeeApiary aplicación y deje el teléfono cerca del dispositivo; este método funciona solo cuando las configuraciones correspondientes están habilitadas tanto en el dispositivo como en la aplicación.

8. Asegúrese de que la fecha y la hora sean correctas y que se haya actualizado la marca de tiempo de la última sincronización.

El dispositivo está listo para funcionar normalmente después de que se haya restablecido la energía y el tiempo.

Ver también [Energía y carga](../device/power.md) y [Sincronización horaria](../system/time-synchronization.md).
