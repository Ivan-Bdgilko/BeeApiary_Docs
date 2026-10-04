# `mset.xml`: Paramètres de l'appareil

La configuration principale est stockée dans `/setting/mset.xml` sur la carte microSD et dispose d'un `<settings>` élément racine.

!!! warning "Le fichier actuel n'est pas une liste de valeurs d'usine"
    Les valeurs dans le XML d'un appareil particulier peuvent avoir été modifiées par l'utilisateur, l'interface Web ou automatiquement. Par exemple, `sefe_start_interval="60000"` et `alarm_sms_sec_interval="10"` ne sont pas des valeurs initiales : une nouvelle configuration utilise `120000` millisecondes et `180` s respectivement.

Voir aussi le [règles d'édition sécurisées](service-reference.md). Ne change pas `SERVICE` paramètres sans sauvegarde et compréhension de leur effet sur l’appareil.

## `net_settings`

Cette section stocke les paramètres du point d'accès de l'appareil, de la connexion à un réseau Wi-Fi externe, de la transmission de données et du FTP. Un `SSID`/`PASSWORD` ou `SSID_STA`/`PASSWORD_STA` La paire est appliquée uniquement lorsque les deux valeurs sont présentes et non vides.

| Champ | Fonction | Caractère obligatoire | Valeurs autorisées / limites | Valeur initiale | Si non défini | Niveau |
|---|---|---|---|---|---|---|
| `SSID` | Nom du point d'accès local de l'appareil | Conditionnellement requis avec `PASSWORD` | Chaîne ; jusqu’à 32 caractères | `apiary_net` | La nouvelle paire de points d'accès n'est pas appliquée | `USER` |
| `PASSWORD` | Mot de passe du point d'accès local | Conditionnellement requis avec `SSID` | Chaîne ; jusqu’à 32 caractères | `apiary_wifi` | La nouvelle paire de points d'accès n'est pas appliquée | `USER` |
| `SSID_STA` | SSID du réseau Wi-Fi externe | Facultatif | Chaîne non vide ; longueur maximale non définie | `-` | Les nouveaux paramètres STA ne sont pas appliqués | `ADVANCED` |
| `PASSWORD_STA` | Mot de passe pour le réseau Wi-Fi externe | Conditionnellement requis avec `SSID_STA` | Chaîne ; longueur maximale non définie | `-` | Les nouveaux paramètres STA ne sont pas appliqués | `ADVANCED` |
| `STA_KEY` | Clé d'authentification utilisée lors de la transmission | Facultatif | Chaîne ; le format dépend de la méthode d’authentification | `-` | Le paramètre Wi-Fi n'est pas modifié | `SERVICE` |
| `UPLOAD_URL` | Adresse du récepteur de données Wi-Fi | Facultatif | URL ; la longueur maximale n'est pas spécifiée | Dépend de la configuration de l'appareil | Définir sur un seul espace ; la transmission n'est effectivement pas configurée | `SERVICE` |
| `wifi_sync` | Permet la synchronisation via un réseau Wi-Fi externe | Facultatif | `true`, `false` | `false` | `false` | `ADVANCED` |
| `FTP_USER` | Nom d'utilisateur pour le FTP local | En option dans le cadre d'une paire | Chaîne ; jusqu’à 32 caractères | Dépend de la configuration de l'appareil | Si l'un des champs FTP est manquant, les paramètres FTP initiaux sont utilisés | `ADVANCED` |
| `FTP_PASSWORD` | Mot de passe pour le FTP local | En option dans le cadre d'une paire | Chaîne ; jusqu’à 32 caractères | Dépend de la configuration de l'appareil | Si l'un des champs FTP est manquant, les paramètres FTP initiaux sont utilisés | `ADVANCED` |

!!! note "Le `-` valeur"
    Pour `SSID_STA`, `PASSWORD_STA`, et `STA_KEY`, le trait d'union est une valeur initiale littérale. Il est traité comme une chaîne non vide. Ne l'utilisez donc pas comme une indication fiable qu'un paramètre n'est « pas configuré ».

Changer le mot de passe initial `apiary_wifi` après le premier contrôle de l'appareil.

## `apairy_set`

Le nom de la section contient une erreur historique et doit rester `apairy_set`. Cette section est nécessaire pour créer la liste des ruches.

| Champ | Fonction | Caractère obligatoire | Valeurs autorisées / limites | Valeur initiale | Si non défini | Niveau |
|---|---|---|---|---|---|---|
| `hive_count` | Nombre de fichiers de configuration de ruche | Champ facultatif dans une section obligatoire | Entier ; `1` ou plus est recommandé ; les limites ne sont pas vérifiées automatiquement | `1` | `1` | `ADVANCED` |
| `hive1`…`hiveN` | Noms de base des fichiers de ruche sans `.xml` | Obligatoire pour chaque numéro jusqu'à `hive_count` | Chaîne ; jusqu’à 8 caractères ASCII recommandés pour la compatibilité | `hive1` | Erreur de lecture d'attribut ; la ruche correspondante n'est pas créée | `SERVICE` |

Le chemin a la forme `/setting/<значення>.xml`. Le nom utilise un tampon interne de 24 octets, n'utilisez donc pas de noms longs ni de séparateurs de chemin.

## `GSM`

Cette section décrit deux destinataires. Si la section est absente, la structure GSM est effacée. La section elle-même doit donc être considérée comme obligatoire même en cas de fonctionnement sans carte SIM.

| Champ | Fonction | Caractère obligatoire | Valeurs autorisées / limites | Valeur initiale | Si non défini | Niveau |
|---|---|---|---|---|---|---|
| `sms_format1` | Format SMS pour `number1` | Facultatif | `1` - texte; `2` — format d'application compact | `2` | `2` | `USER` |
| `sms_format2` | Format SMS pour `number2` | Facultatif | `1` - texte; `2` — format d'application compact | `2` | `2` | `USER` |
| `number1` | Numéro du destinataire principal | Facultatif | Format international ; tampon interne de 15 octets | Chaîne vide | Aucun destinataire n'est configuré au premier chargement | `USER` |
| `number2` | Numéro de destinataire supplémentaire | Facultatif | Format international ; tampon interne de 15 octets | Chaîne vide | Aucun destinataire n'est configuré au premier chargement | `USER` |
| `sms_wait_to_send_sec` | Temps d'attente avant d'envoyer un SMS sur un réseau faible | Facultatif | Nombre entier de secondes ; pas de limites fixes | `50` s | `50` s | `ADVANCED` |
| `alarm_call_wait_sec` | Intervalle entre les tentatives répétées d'appel d'alarme | Facultatif | Nombre entier de secondes ; pas de limites fixes | `80` s | `80` s | `ADVANCED` |

Spécifiez un numéro vide comme `number1=""` ou `number2=""`. N'incluez pas de vrais numéros de téléphone dans les exemples publiés.

## `NTP`

Cette section appartient à la même structure interne que le GSM. Si `NTP` est totalement absent, les paramètres GSM qui viennent d'être lus sont également réinitialisés. La section doit donc rester présente même lorsque la synchronisation est désactivée.

| Champ | Fonction | Caractère obligatoire | Valeurs autorisées / limites | Valeur initiale | Si non défini | Niveau |
|---|---|---|---|---|---|---|
| `synchronize` | Synchronisation automatique de l'heure via un mécanisme réseau disponible | Champ facultatif dans une section obligatoire | `true`, `false` | `false` | `false` | `USER` |
| `time_zone` | Décalage de fuseau horaire spécifié en heures entières dans le XML | Facultatif | Entier ; `-11` à `12` est recommandé ; les limites ne sont pas vérifiées automatiquement | `2` | `3` | `ADVANCED` |
| `ntp1` | Serveur de temps principal | Facultatif | Nom d'hôte ; tampon interne jusqu'à 30 octets | `0.europe.pool.ntp.org` | Vide au premier chargement | `ADVANCED` |
| `ntp2` | Serveur de temps secondaire | Facultatif | Nom d'hôte ; tampon interne jusqu'à 30 octets | `1.europe.pool.ntp.org` | Vide au premier chargement | `ADVANCED` |
| `ntp3` | Troisième serveur de temps | Facultatif | Nom d'hôte ; tampon interne jusqu'à 30 octets | `2.europe.pool.ntp.org` | Vide au premier chargement | `ADVANCED` |

`time_zone` a des valeurs différentes dans les deux cas : un nouveau fichier reçoit `2`, alors qu'un attribut manquant entraîne `3`. Tenez compte de cette différence avant de modifier la configuration initiale.

L'orthographe `synсhronize` contient la lettre cyrillique `с` et n'est pas reconnu. Utiliser uniquement `synchronize`.

## `options`

Les attributs individuels sont facultatifs et ont des valeurs de secours. **Ne supprimez pas la section entière :** s'il est absent, les paramètres de la section sont effacés au lieu de recevoir les valeurs initiales indiquées ci-dessous.

| Champ | Fonction | Caractère obligatoire | Valeurs autorisées / limites | Valeur initiale | Si non défini | Niveau |
|---|---|---|---|---|---|---|
| `meteo` | Indique la présence d'un capteur de pression et d'humidité | Facultatif | `true`, `false` | `false` | `false` | `SERVICE` |
| `pir_sensor` | Indique la présence d'un capteur de mouvement PIR | Facultatif | `true`, `false` | `false` | `false` | `SERVICE` |
| `temperature_twist` | Échange les valeurs logiques T1 et T2 | Facultatif | `true`, `false` | `false` | `false` | `ADVANCED` |
| `oled` | Indique la présence d'un écran OLED | Facultatif | `true`, `false` | `false` | `false` | `SERVICE` |
| `oled_invert` | Inverse l'image OLED | Facultatif | `true`, `false` | `false` | `false` | `SERVICE` |
| `sefe_start_interval` | Durée de la fenêtre active après le démarrage | Facultatif | Millisecondes ; les limites ne sont pas vérifiées automatiquement | `120000` millisecondes | `120000` millisecondes | `SERVICE` |
| `alarm_sms_sec_interval` | Intervalle minimum entre les messages SMS d'alarme | Facultatif | Nombre entier non signé de secondes | `180` s | `180` s | `ADVANCED` |
| `alarm_by_changes_count` | Nombre de changements d'état PIR requis pour confirmer une alarme | Facultatif | Entier non signé ; la valeur pratique dépend de l'emplacement | `3` | `3` | `ADVANCED` |
| `alarm_by_long_state` | Durée d'un état PIR actif requis pour une alarme | Facultatif | Nombre entier non signé de secondes | `10` s | `10` s | `ADVANCED` |
| `time_ms_compensate` | Compensation de fréquence d'horloge quotidienne | Facultatif | Nombre de millisecondes signé sur 32 bits | `0` millisecondes | `0` millisecondes | `SERVICE` |
| `sync_time_sec` | Horodatage du service pour la synchronisation manuelle | Facultatif | Nombre de secondes signé sur 64 bits | `0` | `0` | `SERVICE` |

`sefe_start_interval` est le nom historique exact du champ. Sa valeur initiale est `120000` millisecondes ; la portée n'est pas vérifiée automatiquement, il est donc dangereux de la réduire arbitrairement.

Les indicateurs matériels modifiés via l'interface Web sont immédiatement enregistrés, mais la configuration de fonctionnement les applique après la nouvelle lecture des paramètres.

## `BLE`

La section entière est facultative pour des raisons de compatibilité avec les fichiers plus anciens. S'il est absent, BLE est désactivé et les valeurs actuelles et les intervalles standard sont utilisés.

| Champ | Fonction | Caractère obligatoire | Valeurs autorisées / limites | Valeur initiale | Si non défini | Niveau |
|---|---|---|---|---|---|---|
| `ble_enable` | Active BLE | Facultatif | `true`, `false` | `false` | `false`; une valeur invalide désactive également BLE | `USER` |
| `static_values` | Sélectionne les valeurs statiques au lieu des valeurs actuelles | Facultatif | `true`, `false` | `false` | `false` | `SERVICE` |
| `update_time_sec` | Intervalle de mise à jour des données BLE | Facultatif | `3`–`60` s ; les valeurs inférieures sont normalisées à `3`, des valeurs plus élevées à `60` | `30` s | `30` s | `ADVANCED` |
| `advertising_time_sec` | Durée de la publicité BLE | Facultatif | `0` ou `10`–`60` s ; valeurs de `1` à `9` sont normalisés à `0`, valeurs ci-dessus `60` à `60` | `20` s | `20` s | `ADVANCED` |

Pour `static_values`, seule la sélection de valeurs statiques au lieu de valeurs actuelles est décrite ; aucun autre effet du paramètre n'est défini.

## Exemple minimal { #minimal-example }

Cet exemple laisse STA, FTP et BLE à leurs valeurs initiales. Un vide mais présent `<options />` La section active la valeur de repli de chaque attribut au lieu d'effacer toute la structure.

```xml
<settings>
  <net_settings SSID="apiary_net" PASSWORD="apiary_wifi" />
  <apairy_set hive_count="1" hive1="hive1" />
  <GSM sms_format1="2" sms_format2="2"
       number1="" number2=""
       sms_wait_to_send_sec="50" alarm_call_wait_sec="80" />
  <NTP synchronize="false" time_zone="2"
       ntp1="0.europe.pool.ntp.org"
       ntp2="1.europe.pool.ntp.org"
       ntp3="2.europe.pool.ntp.org" />
  <options />
</settings>
```

## Exemple complet de désinfection { #full-example }

Les valeurs `SITE_WIFI`, `WIFI_PASSWORD`, `DEVICE_KEY`, `FTP_USER`, `FTP_PASSWORD`et l'URL sont des espaces réservés et non des données provenant d'un appareil d'exploitation.

```xml
<settings>
  <net_settings SSID="apiary_net" PASSWORD="apiary_wifi"
                SSID_STA="SITE_WIFI" PASSWORD_STA="WIFI_PASSWORD"
                STA_KEY="DEVICE_KEY"
                UPLOAD_URL="https://example.invalid/beeapiary"
                wifi_sync="false"
                FTP_USER="FTP_USER" FTP_PASSWORD="FTP_PASSWORD" />
  <apairy_set hive_count="1" hive1="hive1" />
  <GSM sms_format1="2" sms_format2="2"
       number1="+380XXXXXXXXX" number2=""
       sms_wait_to_send_sec="50" alarm_call_wait_sec="80" />
  <NTP synchronize="false" time_zone="2"
       ntp1="0.europe.pool.ntp.org"
       ntp2="1.europe.pool.ntp.org"
       ntp3="2.europe.pool.ntp.org" />
  <options meteo="false" pir_sensor="false"
           temperature_twist="false" oled="false" oled_invert="false"
           sefe_start_interval="120000"
           alarm_sms_sec_interval="180"
           alarm_by_changes_count="3" alarm_by_long_state="10"
           time_ms_compensate="0" sync_time_sec="0" />
  <BLE ble_enable="false" static_values="false"
       update_time_sec="30" advertising_time_sec="20" />
</settings>
```
