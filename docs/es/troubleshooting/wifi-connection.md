# No se puede conectar a Wi-Fi

!!! warning "Wi-Fi del dispositivo: solo 2,4 GHz"
    El punto de acceso `apiary_net` de las básculas solo funciona en 2,4 GHz. El teléfono, la tableta o el portátil debe admitir conexiones Wi-Fi en esta banda. Seleccione el SSID de una red de 2,4 GHz; no se admiten redes exclusivas de 5 GHz.

1. [Activar o reiniciar el BeeApiary balanzas de colmena](../guides/set-up-device.md#activation-reset): mantenga brevemente la llave magnética contra la marca en la parte posterior de la unidad principal.
2. Busque la red durante el primer minuto después del reinicio.
3. Verifique el SSID; el valor predeterminado es `apiary_net`.
4. Verifique la contraseña; el valor predeterminado es `apiary_wifi` a menos que haya sido cambiado.
5. Después de conectar, abra manualmente `http://192.168.4.1`.
6. Si la página no se abre, desactive los datos móviles o el cambio automático a una conexión a Internet para esta sesión local y vuelva a intentarlo.

Si ha transcurrido un minuto, vuelva a mantener brevemente la llave contra la marca. Para más detalles, consulte [Wifi local](../system/local-wifi.md).
