# Cómo configurar la sincronización Bluetooth

!!! danger "Compatibilidad del dispositivo"
    Esta función solo es compatible con dispositivos fabricados después de agosto de 2026. Los dispositivos fabricados antes también pueden obtener esta funcionalidad, pero deben actualizarse en fábrica. Actualmente no existe ningún parche sencillo que pueda instalar usted mismo.

Este procedimiento configura la recuperación automática de datos desde BeeApiary báscula de colmena mientras el teléfono está cerca. La sincronización no requiere una tarjeta SIM ni acceso a Internet.

## Antes de comenzar

1. Asegúrese de que las básculas cumplan con los requisitos de compatibilidad anteriores.
2. [Sincronizar el reloj de la báscula](../system/time-synchronization.md) con el teléfono. La diferencia no debe exceder los dos minutos.
3. Active Bluetooth en el teléfono.
4. Otorgue a la aplicación todos los permisos solicitados, incluidos los permisos de Bluetooth.
5. Permita que la aplicación se ejecute en segundo plano y se active a la hora requerida. Revisar el actual [recomendaciones de instalación de aplicaciones](../app/installation.md).

!!! warning "Verifique el tiempo antes de la configuración"
    Si la diferencia supera los dos minutos, la báscula puede volverse disponible antes o después de que el teléfono comience a escuchar, impidiendo la sincronización automática.

## Habilite la información BLE en las básculas

1. [Conéctese al punto de acceso de la báscula](configure-local-wifi.md).
2. Abierto `http://192.168.4.1` y seleccione **Configuraciones adicionales**.
3. Seleccionar **BLE info** y guarda los cambios.

Esta opción y los otros interruptores se explican en [Configuraciones adicionales del dispositivo](../device/additional-settings.md).

## Habilitar la sincronización en la aplicación.

4. Abra el menú principal de la aplicación, vaya a **Configuración**y abre **Configuraciones adicionales**.
5. Habilitar **Buscar dispositivos BLE** para que la aplicación pueda encontrar básculas cercanas y recibir mediciones.
6. Habilitar **Historia BLE** para que la aplicación también recupere el historial almacenado, incluidos los datos del día anterior.

    ![Opciones de Bluetooth en la configuración adicional del BeeApiary aplicación de Android](../../assets/en/app/additional-settings/app-additional-settings.jpg){ .doc-screenshot }

    !!! warning "Habilite las opciones requeridas"
        La captura de pantalla es un ejemplo general, por lo que ambos interruptores de Bluetooth se muestran como deshabilitados. **Buscar dispositivos BLE** debe estar habilitado para la sincronización. Habilitando **Historia BLE** También se recomienda para que la aplicación pueda recuperar el historial disponible y restaurar las mediciones perdidas.

    Para obtener una descripción completa de esta pantalla, consulte [Configuraciones de aplicaciones adicionales](../app/additional-settings.md).

7. Regrese a la pantalla de inicio de la aplicación. Mantenga Bluetooth habilitado y el teléfono dentro del alcance confiable de Bluetooth durante el siguiente ciclo horario.

## Comprueba el resultado

La sincronización ocurre sólo cuando **BLE info** está habilitado en la báscula y Bluetooth y las opciones de la aplicación correspondiente están habilitadas en el teléfono. Las básculas quedan disponibles para la comunicación durante un despertar programado o después [activación con la llave magnética](../device/installation.md#activation-reset).

La aplicación puede intercambiar datos mientras está abierta o en segundo plano si Android permite que se ejecute y se active en el momento requerido.

8. Espere un mensaje que confirme que se han recibido los datos.

    ![Resultado de la recepción de medidas vía Bluetooth en el BeeApiary aplicación](../../assets/en/system/bluetooth/bluetooth-sync-result.jpg){ .doc-screenshot }

    Esta ventana muestra:

    - el nombre de la colmena y el número de la balanza;
    - el último conjunto de medidas disponible para la configuración de la báscula;
    - la fecha y hora de la medición recibida;
    - la hora y el resultado de la sincronización del reloj.

    Cuando se conecta a básculas que aún no han sido registradas, aparece un **Agregar dispositivo** También puede aparecer el botón . Úselo para completar el estándar. [procedimiento para agregar BeeApiary balanzas de colmena](../app/add-device.md) una vez. Entonces la aplicación los reconocerá automáticamente.

9. Toque **bien**. Si es necesario, abra el último mensaje nuevamente a través de **BLE Info** en el menú principal.
10. Asegúrese de que los nuevos valores aparezcan en la pantalla de inicio y en los gráficos de la aplicación.

Listo: mientras el teléfono esté cerca, la aplicación recuperará automáticamente los datos disponibles. Si la conexión no estuvo disponible durante varias horas, habilitado **Historia BLE** puede restaurar las mediciones perdidas durante la siguiente sincronización exitosa, dentro de la profundidad del historial disponible de un día a una semana.

Para obtener más información sobre cómo funciona, consulte [Sincronización de datos por Bluetooth](../system/bluetooth.md).
