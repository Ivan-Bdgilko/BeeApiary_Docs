# Impossible de se connecter au Wi-Fi

!!! warning "Wi-Fi de l’appareil : 2,4 GHz uniquement"
    Le point d’accès `apiary_net` des balances fonctionne uniquement à 2,4 GHz. Le téléphone, la tablette ou l’ordinateur portable doit prendre en charge les connexions Wi-Fi dans cette bande. Sélectionnez le SSID d’un réseau de 2,4 GHz ; les réseaux fonctionnant uniquement à 5 GHz ne sont pas pris en charge.

1. [Activez ou redémarrez le BeeApiary balances pour ruches](../guides/set-up-device.md#activation-reset): maintenez brièvement la clé magnétique contre la marque au dos de l'unité principale.
2. Recherchez le réseau pendant la première minute après le redémarrage.
3. Vérifiez le SSID ; la valeur par défaut est `apiary_net`.
4. Vérifiez le mot de passe ; la valeur par défaut est `apiary_wifi` à moins qu'il ait été modifié.
5. Après la connexion, ouvrez manuellement `http://192.168.4.1`.
6. Si la page ne s'ouvre pas, désactivez les données mobiles ou le passage automatique à une connexion Internet pour cette session locale, puis réessayez.

Après une minute, maintenez à nouveau brièvement la clé contre le repère. Pour plus de détails, voir [Wi-Fi local](../system/local-wifi.md).
