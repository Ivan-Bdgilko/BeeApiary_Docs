# Energía y carga

El dispositivo funciona desde una o dos celdas 18650 y se carga a través de USB Type-C. La fuente de energía puede ser un cargador, un banco de energía o un panel solar opcional.

!!! note "Elegir cargador y cable"
    El dispositivo no admite carga rápida, incluida la entrega de energía USB (PD). Utilice una fuente de alimentación estándar con un puerto USB tipo A y un cable USB tipo A-USB tipo C. No se recomienda un cable USB Type-C-USB Type-C para cargar.

![Puerto de alimentación USB tipo C abierto](../../assets/common/device/power/open-usb-type-c-port.jpeg){ .doc-photo }

Cierre la cubierta protectora del puerto después de cargar:

![Cubierta protectora cerrada sobre el puerto de alimentación.](../../assets/common/device/power/closed-usb-type-c-cover.jpeg){ .doc-photo }

- el indicador azul permanece encendido cuando la batería está completamente cargada y la alimentación externa todavía está conectada;
- el nivel de carga se muestra en los mensajes SMS y en la configuración general de la interfaz web;

  ![Carga de batería en la interfaz web.](../../assets/en/device/power/battery-charge-status.png){ .doc-screenshot }

- por debajo del 20%, el dispositivo entra en modo de ahorro de energía, detiene las mediciones periódicas y los mensajes SMS y comprueba periódicamente el nivel de carga;
- después de una descarga crítica, la batería se desconecta automáticamente y [sincronización de tiempo](../system/time-synchronization.md) puede ser necesario después de la carga.

!!! warning "Después de un almacenamiento prolongado"
    Si el voltaje de la batería está por debajo `3,5 В`, no intentes restaurar el dispositivo usando solo su puerto USB. Sigue el [procedimiento de recuperación después de un almacenamiento prolongado](../troubleshooting/recovery-after-storage.md).

!!! danger
    No utilice el dispositivo sin una celda 18650 instalada. Observe estrictamente la polaridad al reemplazarlo: una polaridad incorrecta dañará el dispositivo.
