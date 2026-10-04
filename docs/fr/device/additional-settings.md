# Paramètres supplémentaires de l'appareil

Le **Paramètres supplémentaires** la page appartient à l'interface web du BeeApiary balances pour ruches. Il précise quel matériel supplémentaire est installé et contrôle les différents canaux de transmission de données.

## Comment l'ouvrir

1. [Connectez-vous au point d'accès de l'appareil](../guides/configure-local-wifi.md).
2. Ouvert `http://192.168.4.1`.
3. Sur la page d'accueil, sélectionnez **Paramètres supplémentaires**.
4. Lisez l'avertissement de l'interface Web. Procédez uniquement pour vérifier ou modifier délibérément les paramètres.

!!! warning "Ne modifiez pas les paramètres au hasard"
    Une valeur incorrecte peut perturber le fonctionnement de l'appareil. Activez les indicateurs matériels uniquement lorsque le matériel correspondant est physiquement installé. Ne modifiez pas les paramètres ou les clés réseau inutilement.

![Paramètres supplémentaires dans l'interface Web du BeeApiary balances pour ruches](../../assets/uk/device/additional-settings/device-additional-settings.jpg){ .doc-screenshot }

Les valeurs de réseau dans la capture d'écran ne sont que des exemples. Ils seront différents sur votre appareil.

## Commutateurs

| Article | Fonction | Remarques |
|---|---|---|
| **BLE info** | Permet la synchronisation des données locales via Bluetooth. | Après l'avoir activé, configurez [Synchronisation Bluetooth dans l'application](../guides/configure-bluetooth-sync.md). |
| **GSM** | Permet le module GSM et la transmission de données par SMS. | Désactivez-le si la communication GSM n'est pas utilisée, par exemple pendant l'hivernage sans transmission de données. |
| **Synchronisation Wi-Fi** | Permet la transmission automatique de données via un réseau Wi-Fi externe. | Généralement activé automatiquement lorsque l'application transfère les paramètres Wi-Fi et cloud préparés vers l'appareil. Ne l'activez pas manuellement sans les champs réseau corrects. |
| **Écran** | Indique à l'appareil qu'un écran OLED est physiquement installé et permet son fonctionnement. | Activer uniquement si un écran est installé. |
| **Inversé** | Fait pivoter l’image de l’écran OLED de 180°. | Uniquement pertinent lorsque **Écran** est activé. |
| **Météo** | Active le capteur météo installé pour la pression, l'humidité et la température supplémentaire. | Activer uniquement si le capteur est installé. |
| **Échanger T1/T2** | Échange les valeurs transmises des principaux thermomètres T1 et T2. | Utile si les capteurs internes et externes ont été physiquement échangés. Laissez les noms et paramètres des chaînes dans l’application inchangés. |
| **Capteur PIR** | Permet l'entrée d'alarme pour PIR ou un autre capteur de réveil du système compatible. | Activer uniquement si un capteur est connecté. |

## Champs de réseau

| Champ | Fonction | Remarques |
|---|---|---|
| **Réseau Wi-Fi** | Nom du réseau Wi-Fi externe auquel l'appareil se connectera. | Doit correspondre exactement au SSID du réseau disponible à proximité de l'appareil. |
| **Mot de passe Wi-Fi** | Mot de passe du réseau Wi-Fi externe. | L'interface Web masque la valeur. |
| **Clé STA** | Clé de transmission de service obtenue lors de l'inscription via l'application. | Ne modifiez pas manuellement. |

Il est plus sûr de définir les paramètres Wi-Fi via [paramètres de synchronisation dans l'application](../guides/configure-wifi-sync.md). L'application crée les données requises et les transfère à l'appareil lors d'une connexion directe à `apiary_net`.
