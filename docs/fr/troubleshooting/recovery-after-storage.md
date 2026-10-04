# Récupérer l'appareil après un stockage à long terme

Après un stockage à long terme, la batterie peut être complètement déchargée et l'appareil peut ne pas répondre à une connexion électrique normale. Si la tension de la cellule 18650 est inférieure `3,5 В`, récupérez l'appareil dans l'ordre suivant.

!!! danger "Polarité de la batterie"
    Avant de retirer la batterie, localisez le `+` et `-` marquages sur la cellule et le support. Rappelez-vous ou photographiez la bonne orientation. L'installation de la batterie avec une polarité inversée peut endommager définitivement l'appareil.

1. Retirez la batterie de l'appareil.
2. Chargez-le dans un chargeur séparé conçu pour 18650 cellules.
3. Après le chargement, vérifiez la tension de la batterie. Installez-le dans l'appareil uniquement lorsque la tension est `4,0 В` ou supérieur.
4. Installez la batterie en respectant soigneusement la polarité indiquée.
5. Connectez une source d'alimentation externe standard au port USB Type-C de l'appareil sans charge rapide Power Delivery (PD). Utilisez un chargeur avec un port USB Type-A et un câble USB Type-A vers USB Type-C ; un câble USB Type-C vers USB Type-C n’est pas recommandé.
6. Avec la batterie installée et l'alimentation externe connectée, [activer l'appareil avec la clé magnétique](../device/installation.md#activation-reset).
7. Synchronisez l'heure de l'une des manières suivantes :

    - [se connecter au point d'accès de l'appareil via Wi-Fi](../guides/configure-local-wifi.md) et ouvrez sa page d'accueil — cette méthode est disponible par défaut ;
    - [configurer la synchronisation Bluetooth](../guides/configure-bluetooth-sync.md), ouvrez le BeeApiary et laissez le téléphone à proximité de l'appareil. Cette méthode ne fonctionne que lorsque les paramètres correspondants sont activés à la fois sur l'appareil et dans l'application.

8. Assurez-vous que la date et l'heure sont correctes et que l'horodatage de la dernière synchronisation a été mis à jour.

L'appareil est prêt à fonctionner normalement une fois l'alimentation et l'heure rétablies.

Voir aussi [Alimentation et chargement](../device/power.md) et [Synchronisation du temps](../system/time-synchronization.md).
