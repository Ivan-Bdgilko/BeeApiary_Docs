# Configuration du système

!!! danger "Attention : l'appareil est déjà entièrement configuré"
    Nouveau BeeApiary Les balances pour ruches sont fournies configurées et calibrées. Le numéro d'utilisateur est déjà enregistré dans les paramètres de la balance, vous n'avez donc pas besoin de les reconfigurer.

    N'apportez pas de modifications vous-même. Habituellement, il vous suffit de suivre les quatre premières étapes ci-dessous pour que tout fonctionne.

    Ne retirez pas la batterie, ne tarez pas, ne calibrez pas la balance et ne modifiez aucun réglage sans avoir d'abord lu les instructions pertinentes jusqu'à la fin. Il est fortement déconseillé de le faire lors de la configuration initiale.

!!! warning "Avant d'installer la carte SIM"
    Utilisez uniquement une micro-SIM et désactivez sa protection PIN au préalable.

1. Ouvrez le couvercle de l'unité de collecte de données.

    ![Cellule de collecte de données ouvertes](../../assets/common/device/installation/open-data-collection-unit.png){ .doc-photo }

2. Insérez la micro-SIM dans l'emplacement approprié.

    Position correcte de la carte :

    ![Micro-SIM correctement insérée](../../assets/common/device/installation/micro-sim-insertion-orientation.jpeg){ .doc-photo }

    Insérez la carte SIM et appuyez doucement jusqu'à ce qu'elle soit presque entièrement enfoncée dans l'emplacement et que vous entendiez un léger clic confirmant son verrouillage :

    ![micro-SIM verrouillée dans l'emplacement](../../assets/common/device/installation/micro-sim-locked-in-slot.jpeg){ .doc-photo }

3. [Activer ou redémarrer l'appareil](../device/installation.md#activation-reset): maintenez brièvement la clé magnétique contre la marque au dos de l'unité principale.

    ![BeeApiary clé magnétique](../../assets/common/device/installation/magnetic-key.png){ .doc-photo }

    ![Cible à clé magnétique de marque](../../assets/common/device/installation/magnetic-key-target.png){ .doc-photo }

4. Attendez environ une minute et confirmez que le premier SMS arrive au numéro d'utilisateur préconfiguré.

Terminé. Félicitations : l'appareil collecte des données, les envoie via GSM et conserve une archive locale.

## Application — si nécessaire

Le BeeApiary l'application n'est pas nécessaire pour recevoir des messages SMS ordinaires. Installez-le si vous souhaitez recevoir automatiquement les données de l'appareil, afficher les mesures et utiliser d'autres fonctionnalités de l'application.

1. [Installez le BeeApiary application](app-only.md) et assurez-vous de lui accorder l'autorisation de traiter les messages SMS.
2. Dans l'application, sélectionnez **Ajouter un appareil**.
3. Saisissez le numéro de la micro-SIM installée dans le BeeApiary balances pour ruches.

!!! note
    Saisissez le numéro de la carte SIM installée dans l'appareil, et non le numéro de téléphone de l'utilisateur.

Si le premier SMS n’arrive pas, ne modifiez pas les paramètres au hasard. Voir [Aucun SMS reçu](../troubleshooting/no-sms.md). Changez le numéro d'utilisateur via [Paramètres GSM](../guides/configure-gsm.md) seulement lorsque cela est nécessaire.

[Vidéo : installer la carte SIM](https://www.youtube.com/shorts/GF2KLso4DMo)

En savoir plus : [GSM et SMS](../system/gsm-and-sms.md) et [Flux de données](../system/data-flow.md).
