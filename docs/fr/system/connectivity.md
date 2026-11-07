---
title: "Suivi du rucher par GSM, Wi-Fi et Bluetooth"
description: "Comparez le GSM, le Wi-Fi direct, le réseau rucher et le Bluetooth pour recevoir des mesures en BeeApiary: conditions de connexion et historique disponible."
---

# Suivi du rucher par GSM, Wi-Fi et Bluetooth { #_1 }

Pour le suivi des ruchers, les données du BeeApiary Les balances pour ruches peuvent accéder à l'application de quatre manières : via GSM/SMS, une connexion Wi-Fi directe, le réseau Wi-Fi du rucher ou Bluetooth. Le choix entre la surveillance locale et à distance dépend de l’emplacement du téléphone et de la connexion disponible à proximité de la balance.

| Chaîne | Localisation du téléphone | Exigences | Comment les données parviennent à l'application |
|---|---|---|---|
| [GSM et SMS](gsm-and-sms.md) | Partout avec une couverture mobile | Une carte SIM dans l'appareil avec un forfait SMS de base ; autorisation SMS pour l’application | L’application traite automatiquement les SMS compacts ; Internet mobile n’est pas nécessaire. [Configurer le GSM](../guides/configure-gsm.md) |
| [Connexion directe au point d'accès de l'appareil](local-wifi.md#direct-access-point) | À proximité de l'appareil | Activez l'appareil avec la clé magnétique et connectez-vous à `apiary_net` dans l'intervalle disponible, généralement environ une minute ; aucune SIM ni connexion Internet nécessaire | L'application trouve l'appareil, demande l'autorisation de récupérer l'archive et importe les données après confirmation. [Télécharger l’archive](../guides/download-archive.md) |
| [Routage via le réseau Wi-Fi du rucher](local-wifi.md#apiary-wifi-routing) | Partout avec accès à Internet | Un réseau Wi-Fi configuré avec accès Internet doit être disponible à proximité de l'appareil | Les données sont automatiquement acheminées vers l'application ; une carte SIM distincte pour chaque appareil n'est pas nécessaire. [Configurer le Wi-Fi](../guides/configure-wifi-sync.md) |
| [Bluetooth](bluetooth.md) | À proximité, à portée Bluetooth | **BLE info**, l'analyse BLE et le fonctionnement en arrière-plan de l'application sont activés ; l'heure est synchronisée ; aucune carte SIM ni Internet n'est requis | L'application synchronise automatiquement les données actuelles et peut restaurer l'historique disponible. [Configurer Bluetooth](../guides/configure-bluetooth-sync.md) |

## GSM et SMS

Les SMS ordinaires se lisent sans application ; les messages compacts sont enregistrés comme mesures par l’application. [Formats SMS](gsm-and-sms.md).

## Connexion directe à l'appareil

Le téléphone connecté ne reçoit l’archive qu’après confirmation. [Se connecter au point d’accès](../guides/configure-local-wifi.md).

## Routage via le réseau Wi-Fi Apiary

Avant la configuration, l’application doit avoir reçu des données au moins une fois par SMS ou téléchargement direct. Le relais n’est pas un stockage permanent : les copies restent sur la balance et le téléphone. Il peut devenir instable ou payant ; vérifie la [compatibilité et les conditions](../guides/configure-wifi-sync.md).

## Bluetooth

Si la récupération de l’historique est activée, les lacunes peuvent être comblées lors de la prochaine connexion réussie. [Fonctionnement et compatibilité](bluetooth.md).

## Fonctionnement sans connexion

Une perte temporaire ou totale d'un canal de communication n'arrête pas les mesures : l'appareil continue de les enregistrer sur microSD. Une fois la connexion rétablie, l'application peut récupérer les données manquées, mais la profondeur de l'historique disponible dépend du canal sélectionné.

| Chaîne | Historique disponible après restauration de la connexion | Remarque |
|---|---|---|
| GSM et SMS | 2 à 12 heures | Dépend du calendrier de transmission SMS configuré |
| Connexion directe au point d'accès de l'appareil | Jusqu'à 1 an | Les données peuvent être téléchargées si les enregistrements correspondants sont présents dans les archives locales |
| Bluetooth | 1 jour à 1 semaine | Dépend du paramètre de récupération de l'historique et des enregistrements disponibles |
| Routage via le réseau Wi-Fi du rucher | L'historique n'est pas disponible | Le relais en ligne transfère les données actuelles mais ne les stocke pas sur le serveur |

Ces limites s'appliquent uniquement à la quantité de données manquées pouvant être restaurées via un canal particulier. Le local [archives microSD](data-storage.md) n'a pas de limite de stockage d'un an : sa profondeur n'est limitée que par la capacité de la carte, qui est suffisante pour toute la durée de vie prévue de l'appareil. Si nécessaire, les données peuvent également être lues directement depuis la carte microSD.
