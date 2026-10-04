---
title: "Comment les données de la ruche arrivent sur le téléphone"
description: "Comment BeeApiary mesure, stocke et transfère les données de la ruche sur votre téléphone pour afficher les lectures actuelles, l'historique et les graphiques."
---

# Comment les données de la ruche arrivent sur le téléphone { #_1 }

BeeApiary La surveillance de la ruche couvre la mesure, le stockage local et la transmission des données vers l'application. Les étapes ci-dessous montrent le chemin depuis une mesure sur l'appareil jusqu'aux lectures actuelles, à l'historique et aux graphiques sur votre téléphone.

1. Au début de chaque heure, le BeeApiary les balances pour ruches prennent les mesures configurées.
2. Le résultat est enregistré dans l'archive microSD locale lorsque la carte est disponible.
3. Le dispositif rend les données disponibles par le canal configuré :

    - envoie un message SMS régulier ou compact selon le planning ;
    - achemine les données via le réseau Wi-Fi du rucher ;
    - [transmet les données disponibles par Bluetooth](bluetooth.md) lorsque le téléphone est à proximité ;
    - fournit l'archive à l'application via son propre point d'accès après confirmation de l'utilisateur.

4. L’application reconnaît les valeurs reçues et les ajoute au stockage local du téléphone.
5. L'utilisateur affiche les valeurs actuelles, l'historique et les graphiques.

L'absence de GSM, Wi-Fi, Bluetooth ou téléphone à proximité n'arrête pas le processus de mesure de base. Les données peuvent être transférées vers l'application lorsqu'une connexion devient disponible.

Lorsque les données sont acheminées à distance via Wi-Fi, le relais en ligne ne les stocke pas. Les copies permanentes restent dans le BeeApiary la mémoire des balances pour ruches et sur le téléphone de l'utilisateur.

Pour une comparaison des chaînes, voir [Réception de données dans l'application](connectivity.md).

Pour configurer le canal distant, voir [Synchronisation via le réseau Wi-Fi Apiary](../guides/configure-wifi-sync.md).

Pour configurer le canal automatique local, voir [Synchronisation Bluetooth](../guides/configure-bluetooth-sync.md).
