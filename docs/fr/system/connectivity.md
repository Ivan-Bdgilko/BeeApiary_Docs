---
title: "Suivi du rucher par GSM, Wi-Fi et Bluetooth"
description: "Comparez le GSM, le Wi-Fi direct, le réseau rucher et le Bluetooth pour recevoir des mesures en BeeApiary: conditions de connexion et historique disponible."
---

# Suivi du rucher par GSM, Wi-Fi et Bluetooth { #_1 }

Pour le suivi des ruchers, les données du BeeApiary Les balances pour ruches peuvent accéder à l'application de quatre manières : via GSM/SMS, une connexion Wi-Fi directe, le réseau Wi-Fi du rucher ou Bluetooth. Le choix entre la surveillance locale et à distance dépend de l’emplacement du téléphone et de la connexion disponible à proximité de la balance.

| Chaîne | Localisation du téléphone | Exigences | Comment les données parviennent à l'application |
|---|---|---|---|
| [GSM et SMS](gsm-and-sms.md) | Partout avec une couverture mobile | Une carte SIM dans l'appareil avec un forfait SMS de base | L'application traite automatiquement les messages SMS. l'Internet mobile n'est pas requis |
| [Connexion directe au point d'accès de l'appareil](local-wifi.md#direct-access-point) | À proximité de l'appareil | Activez l'appareil avec la clé magnétique et connectez-vous à `apiary_net` dans l'intervalle disponible, généralement environ une minute | L'application trouve l'appareil, demande l'autorisation de récupérer l'archive et importe les données après confirmation |
| [Routage via le réseau Wi-Fi du rucher](local-wifi.md#apiary-wifi-routing) | Partout avec accès à Internet | Un réseau Wi-Fi configuré avec accès Internet doit être disponible à proximité de l'appareil | Les données sont automatiquement acheminées vers l'application ; une carte SIM distincte pour chaque appareil n'est pas nécessaire |
| [Bluetooth](bluetooth.md) | À proximité, à portée Bluetooth | **BLE info**, l'analyse BLE et le fonctionnement en arrière-plan de l'application sont activés ; l'heure est synchronisée ; aucune carte SIM ni Internet n'est requis | L'application synchronise automatiquement les données actuelles et peut restaurer l'historique disponible |

## GSM et SMS

L'appareil envoie des messages SMS réguliers ou compacts sans Internet mobile. L'application reconnaît les messages compacts et ajoute automatiquement les mesures au stockage local du téléphone.

## Connexion directe à l'appareil

Après activation avec la clé magnétique, l'appareil crée temporairement le `apiary_net` point d'accès. Un téléphone qui y est connecté n'a pas besoin de carte SIM ni d'accès Internet. L'application trouve automatiquement l'appareil mais télécharge l'archive uniquement après que l'utilisateur a confirmé la demande.

Pour la procédure détaillée, voir [Téléchargez les archives](../guides/download-archive.md).

## Routage via le réseau Wi-Fi Apiary

L'appareil peut utiliser un réseau Wi-Fi existant avec accès Internet au rucher. Le propriétaire reçoit des données à distance dans l'application sans carte SIM distincte pour chaque appareil.

Avant la configuration initiale, l'application doit avoir reçu des données de l'appareil au moins une fois par SMS ou par téléchargement direct d'archives. L'enregistrement est effectué sur un téléphone avec accès à Internet, et les paramètres Wi-Fi et cloud préparés sont ensuite transférés à l'appareil via son `apiary_net` point d'accès.

Le relais en ligne ne stocke pas de données. Les copies permanentes restent dans le BeeApiary la mémoire des balances pour ruches et sur le téléphone de l'utilisateur.

Pour la procédure détaillée, voir [Configurer la synchronisation via le réseau Wi-Fi Apiary](../guides/configure-wifi-sync.md).

## Bluetooth

Lorsque le téléphone est à portée Bluetooth, l'application synchronise automatiquement les données disponibles. Cela ne nécessite pas de carte SIM, d'Internet mobile ou d'activation du `apiary_net` point d'accès. Lorsque la récupération de l'historique est activée, les lacunes temporaires peuvent être comblées lors de la prochaine connexion réussie.

Pour une explication, voir [Synchronisation des données Bluetooth](bluetooth.md). Pour la procédure pratique, voir [Configurer la synchronisation Bluetooth](../guides/configure-bluetooth-sync.md).

## Fonctionnement sans connexion

Une perte temporaire ou totale d'un canal de communication n'arrête pas les mesures : l'appareil continue de les enregistrer sur microSD. Une fois la connexion rétablie, l'application peut récupérer les données manquées, mais la profondeur de l'historique disponible dépend du canal sélectionné.

| Chaîne | Historique disponible après restauration de la connexion | Remarque |
|---|---|---|
| GSM et SMS | 2 à 12 heures | Dépend du calendrier de transmission SMS configuré |
| Connexion directe au point d'accès de l'appareil | Jusqu'à 1 an | Les données peuvent être téléchargées si les enregistrements correspondants sont présents dans les archives locales |
| Bluetooth | 1 jour à 1 semaine | Dépend du paramètre de récupération de l'historique et des enregistrements disponibles |
| Routage via le réseau Wi-Fi du rucher | L'historique n'est pas disponible | Le relais en ligne transfère les données actuelles mais ne les stocke pas sur le serveur |

Ces limites s'appliquent uniquement à la quantité de données manquées pouvant être restaurées via un canal particulier. Le local [archives microSD](data-storage.md) n'a pas de limite de stockage d'un an : sa profondeur n'est limitée que par la capacité de la carte, qui est suffisante pour toute la durée de vie prévue de l'appareil. Si nécessaire, les données peuvent également être lues directement depuis la carte microSD.
