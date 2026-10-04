# `HIVE*.XML`: Paramètres de la ruche

La configuration de la ruche est stockée dans `/setting/<hive>.xml`. Le `<hive>` le nom de base est spécifié par le `hive1`, `hive2`, et les attributs suivants dans [`mset.xml`](settings-reference.md); le `.xml` L’extension est ajoutée automatiquement.

!!! danger "Valeurs dépendantes du matériel"
    Ne copiez pas le `scales` section à partir d’un autre appareil. Les broches de la carte et les valeurs d'étalonnage dépendent de la version du matériel et de l'ensemble particulier de capteurs de poids. Des valeurs incorrectes peuvent fausser les mesures ou les rendre indisponibles.

Voir le [règles d'édition sécurisées](service-reference.md).

## Réécriture automatique

Après avoir lu le fichier, l'appareil peut le sauvegarder à nouveau :

- un fichier manquant ou endommagé est créé à partir de l'état actuel disponible ;
- manquant `hive`, `thermometer`, ou `schedule` les sections permettent la normalisation ;
- un attribut manquant dans un objet existant `scales` ou `thermometer` la section est remplacée par une valeur de repli et permet la normalisation ;
- complet `scales`, `booster`, et `range_alarmer` les sections sont facultatives ;
- la normalisation écrit également le `booster`, `range_alarmer`, `thermometer`, et `schedule` sections même si certaines d’entre elles étaient absentes du fichier source.

## `hive`

| Champ | Fonction | Caractère obligatoire | Valeurs autorisées / limites | Valeur initiale | Si non défini | Niveau |
|---|---|---|---|---|---|---|
| `hive_name` | Nom interne de la ruche | Facultatif | Chaîne ; jusqu’à 8 caractères ASCII recommandés pour la compatibilité | Nom de `mset.xml`, par exemple `hive1` | `hive_<індекс>`; le fichier est marqué pour réécriture | `ADVANCED` |
| `bus_number` | Numéro de la ruche sur le bus interne | Facultatif | Nombre entier ; les limites ne sont pas vérifiées | Indice d'instance, `0` pour le premier | Indice d'instance ; le fichier est marqué pour réécriture | `SERVICE` |
| `main_device` | Indique l'appareil principal avec des capteurs matériels locaux | Facultatif | `true`, `false` | `true` dans un fichier nouvellement créé | L'instance ne devient pas le périphérique principal ; l'omission à elle seule ne permet pas la réécriture | `SERVICE` |

La prise en charge des appareils subordonnés est obsolète. La valeur `main_device="false"` est accepté lors du chargement, mais après sauvegarde, l'attribut devient `main_device="true"`. Ne pas utiliser `false` comme une configuration stable.

## `scales`

Si la section est entièrement absente, l’objet représentant la balance n’est pas créé et la mesure du poids est désactivée. Si la section existe, chaque champ absent ou incorrect est remplacé par une valeur de secours, puis le fichier entier peut être réécrit.

| Champ | Fonction | Caractère obligatoire | Valeurs autorisées / limites | Valeur initiale | Si non défini | Niveau |
|---|---|---|---|---|---|---|
| `pin_hc711_data` | GPIO de données du HX711 | Obligatoire si la section existe | GPIO pour la carte particulière | La section n'est pas créée automatiquement ; dépendant du matériel | Épingle pour le tableau en question ; le fichier est réécrit | `SERVICE` |
| `pin_hc711_clk` | GPIO d’horloge du HX711 | Obligatoire si la section existe | GPIO pour la carte particulière | La section n'est pas créée automatiquement ; dépendant du matériel | Épingle pour le tableau en question ; le fichier est réécrit | `SERVICE` |
| `gain` | Mode gain HX711 | Obligatoire si la section existe | Valeur du mode gain HX711 | Canal A, gain 128 | Canal A, gain 128 ; le fichier est réécrit | `SERVICE` |
| `zero_calibrate_measurement` | Valeur ADC brute pour une charge nulle | Obligatoire si la section existe | Entier signé sur 32 bits | Dépend du matériel | Valeur de repli `-486050`; le fichier est réécrit | `SERVICE` |
| `weight_calibrate_measurement` | Valeur ADC brute avec le poids de référence | Obligatoire si la section existe | Entier signé sur 32 bits | Dépend du matériel | Valeur de repli `-498030`; le fichier est réécrit | `SERVICE` |
| `calibrate_weight` | Masse de référence d'étalonnage | Obligatoire si la section existe | Grammes ; entier positif ; les limites ne sont pas vérifiées automatiquement | Dépend du matériel | `500` g; le fichier est réécrit | `USER` |
| `start_weight` | Tare soustraite du résultat | Obligatoire si la section existe | Grammes ; `-100000` à `100000` est recommandé ; les limites ne sont pas vérifiées automatiquement | Dépend du matériel | `0` g; le fichier est réécrit | `USER` |
| `source_weight` | Filtre dont le résultat est utilisé comme poids principal | Obligatoire si la section existe | `1` — `immediate`; `2` — `stable`; `3` — `calibration` | La section n'est pas créée automatiquement | `1`; le fichier est réécrit. Les autres valeurs sont traitées comme `1` pendant le fonctionnement | `SERVICE` |
| `normal_pecision` | Paramètre de précision du filtre rapide | Obligatoire si la section existe | Nombre à virgule flottante ; les limites ne sont pas vérifiées | La section n'est pas créée automatiquement | `0.5`; le fichier est réécrit | `SERVICE` |
| `normal_desired_deviation` | Déviation souhaitée du filtre rapide | Obligatoire si la section existe | Nombre à virgule flottante ; les limites ne sont pas vérifiées | La section n'est pas créée automatiquement | `10`; le fichier est réécrit | `SERVICE` |
| `stable_pecision` | Paramètre de précision du filtre stable | Obligatoire si la section existe | Nombre à virgule flottante ; les limites ne sont pas vérifiées | La section n'est pas créée automatiquement | `0.35`; le fichier est réécrit | `SERVICE` |
| `stable_desired_deviation` | Déviation souhaitée du filtre stable | Obligatoire si la section existe | Nombre à virgule flottante ; les limites ne sont pas vérifiées | La section n'est pas créée automatiquement | `5`; le fichier est réécrit | `SERVICE` |
| `calibrate_pecision` | Paramètre de précision du filtre d'étalonnage | Obligatoire si la section existe | Nombre à virgule flottante ; les limites ne sont pas vérifiées | La section n'est pas créée automatiquement | `0.25`; le fichier est réécrit | `SERVICE` |
| `calibrate_desired_deviation` | Déviation souhaitée du filtre d'étalonnage | Obligatoire si la section existe | Nombre à virgule flottante ; les limites ne sont pas vérifiées | La section n'est pas créée automatiquement | `3`; le fichier est réécrit | `SERVICE` |
| `median_window` | Taille de la fenêtre du filtre médian | Obligatoire si la section existe | `3`–`100`; les valeurs hors limites sont remplacées | La section n'est pas créée automatiquement | `100`; le fichier est réécrit | `SERVICE` |

Les identifiants `normal_pecision`, `stable_pecision`, et `calibrate_pecision` contenir l'erreur historique `pecision`, qui ne doit pas être corrigé dans le XML.

`gain` est chargé à partir du fichier, mais la sauvegarde définit toujours le canal A avec un gain de 128. Ne le modifiez pas manuellement sans les données de votre appareil particulier.

## `thermometer`

Une section manquante permet la normalisation des fichiers. La valeur `sensors_count="0"` désactive l'interrogation des capteurs DS18B20.

| Champ | Fonction | Caractère obligatoire | Valeurs autorisées / limites | Valeur initiale | Si non défini | Niveau |
|---|---|---|---|---|---|---|
| `pin_onewire` | GPIO de bus à 1 fil | Facultatif | GPIO pour la carte particulière | `4` | `4`; le fichier est réécrit | `SERVICE` |
| `sensors_count` | Nombre de capteurs DS18B20 | Facultatif | `0` désactive les capteurs ; entier positif ; la limite supérieure n'est pas vérifiée | `2` | `2`; le fichier est réécrit | `ADVANCED` |

## `schedule`

Le `TimeSlot0`–`TimeSlot23` les attributs définissent l'action pour l'heure correspondante. Après la minute 30, l'action pour l'heure suivante est sélectionnée ; après l'heure 23, `TimeSlot0` est sélectionné.

| Champ | Fonction | Caractère obligatoire | Valeurs autorisées / limites | Valeur initiale | Si non défini | Niveau |
|---|---|---|---|---|---|---|
| `TimeSlot0`…`TimeSlot23` | Type d'action planifiée pour l'heure `0`–`23` | Tous les attributs sont facultatifs, mais au moins un emplacement avec `2` est requis | Entier de `0` à `5`; voir ci-dessous | `5` pendant des heures `0`–`20`; `1` pour `21` et `22`; `2` pour `23` | Un emplacement manquant devient `0`. Si non `2` reste après la lecture, l'ensemble du planning est réinitialisé au planning initial | `ADVANCED` |

| Valeur | Action | Recommandation |
|---:|---|---|
| `0` | Aucune action programmée | Peut être utilisé pour un emplacement vide |
| `1` | Mesure | Pris en charge |
| `2` | Transmission via le canal principal | Obligatoire dans au moins un emplacement |
| `3` | Réservé à la transmission via Wi-Fi | Ne pas utiliser |
| `4` | Réservé à la transmission via BLE | Ne pas utiliser |
| `5` | Réveil horaire pour la synchronisation | Utilisé par le planning initial |

Les autres entiers ne sont pas rejetés mais n'ont pas de comportement défini. Utilisez uniquement les valeurs du tableau.

### Calendrier initial

```xml
<schedule
  TimeSlot0="5" TimeSlot1="5" TimeSlot2="5" TimeSlot3="5"
  TimeSlot4="5" TimeSlot5="5" TimeSlot6="5" TimeSlot7="5"
  TimeSlot8="5" TimeSlot9="5" TimeSlot10="5" TimeSlot11="5"
  TimeSlot12="5" TimeSlot13="5" TimeSlot14="5" TimeSlot15="5"
  TimeSlot16="5" TimeSlot17="5" TimeSlot18="5" TimeSlot19="5"
  TimeSlot20="5" TimeSlot21="1" TimeSlot22="1" TimeSlot23="2" />
```

## `booster`

Cette section définit l'intervalle des réveils supplémentaires pour vérifier les paramètres critiques. Si la section est absente, un intervalle horaire est utilisé pendant le fonctionnement ; l'absence elle-même ne déclenche pas de réécriture.

| Champ | Fonction | Caractère obligatoire | Valeurs autorisées / limites | Valeur initiale | Si non défini | Niveau |
|---|---|---|---|---|---|---|
| `booster_time_sec` | Intervalle de contrôle supplémentaire | Facultatif | `180`, `240`, `300`, `360`, `600`, `720`, `900`, `1200`, `1800`, ou `3600` s | `3600` s | `3600` s | `ADVANCED` |

Une valeur en dessous `180` s devient `180`; une valeur ci-dessus `3600` s devient `3600`. Les autres valeurs comprises dans la plage sont arrondies à l'intervalle pris en charge le plus proche dans le tableau.

## `range_alarmer`

Cette rubrique est facultative. S'il est absent, l'alarme de seuil n'est pas initialisée. Si `alarm="false"` ou le `alarm` l'attribut est absent, les limites ne sont pas lues et la tâche d'alarme en arrière-plan n'est pas démarrée.

| Champ | Fonction | Caractère obligatoire | Valeurs autorisées / limites | Valeur initiale | Si non défini | Niveau |
|---|---|---|---|---|---|---|
| `alarm` | Active les alarmes de seuil | Facultatif | `true`, `false` | `false` | `false` | `USER` |
| `T1_min` | Limite inférieure T1 | Facultatif | Nombre à virgule flottante, °C ; les limites physiques et l'ordre min/max ne sont pas vérifiés automatiquement | `-500` °C dans un fichier nouvellement créé | Avec `alarm="true"`, il n'y a pas de limite inférieure | `ADVANCED` |
| `T1_max` | Limite supérieure T1 | Facultatif | Nombre à virgule flottante, °C ; les limites physiques et l'ordre min/max ne sont pas vérifiés automatiquement | `500` °C dans un fichier nouvellement créé | Avec `alarm="true"`, il n'y a pas de limite supérieure | `ADVANCED` |
| `T2_min` | Limite inférieure T2 | Facultatif | Nombre à virgule flottante, °C ; les limites physiques et l'ordre min/max ne sont pas vérifiés automatiquement | `-500` °C dans un fichier nouvellement créé | Avec `alarm="true"`, il n'y a pas de limite inférieure | `ADVANCED` |
| `T2_max` | Limite supérieure T2 | Facultatif | Nombre à virgule flottante, °C ; les limites physiques et l'ordre min/max ne sont pas vérifiés automatiquement | `500` °C dans un fichier nouvellement créé | Avec `alarm="true"`, il n'y a pas de limite supérieure | `ADVANCED` |
| `Humidity_min` | Limite inférieure d'humidité | Facultatif | Nombre à virgule flottante, % ; les limites physiques et l'ordre min/max ne sont pas vérifiés automatiquement | `-20` % dans un fichier nouvellement créé | Avec `alarm="true"`, il n'y a pas de limite inférieure | `ADVANCED` |
| `Humidity_max` | Limite supérieure d'humidité | Facultatif | Nombre à virgule flottante, % ; les limites physiques et l'ordre min/max ne sont pas vérifiés automatiquement | `200` % dans un fichier nouvellement créé | Avec `alarm="true"`, il n'y a pas de limite supérieure | `ADVANCED` |

Pour chaque source – T1, T2 ou humidité – une limite suffit. Si aucune limite n'est spécifiée pour une source particulière, elle n'est pas ajoutée au contrôle. L'ordre de `_min` et `_max` n’est pas vérifié automatiquement.

### Exemple d'alarme unilatérale

Dans cet exemple, T1 est surveillé uniquement par le haut, T2 uniquement par le bas et l'humidité n'est pas surveillée :

```xml
<range_alarmer alarm="true" T1_max="45.0" T2_min="-10.0" />
```

La fréquence générale des SMS et la confirmation de l'alarme PIR sont configurées par `alarm_sms_sec_interval`, `alarm_by_changes_count`, et `alarm_by_long_state` dans [`mset.xml`](settings-reference.md#options).

## Exemple structurel sans balance

Ce fichier utilise le planning initial, deux capteurs de température et des alarmes de seuil désactivées. Le `scales` La section est absente, donc aucun objet balance n'est créé.

```xml
<settings>
  <hive hive_name="hive1" bus_number="0" main_device="true" />
  <booster booster_time_sec="3600" />
  <range_alarmer alarm="false"
                 T1_max="500" T1_min="-500"
                 T2_max="500" T2_min="-500"
                 Humidity_max="200" Humidity_min="-20" />
  <thermometer pin_onewire="4" sensors_count="2" />
  <schedule
    TimeSlot0="5" TimeSlot1="5" TimeSlot2="5" TimeSlot3="5"
    TimeSlot4="5" TimeSlot5="5" TimeSlot6="5" TimeSlot7="5"
    TimeSlot8="5" TimeSlot9="5" TimeSlot10="5" TimeSlot11="5"
    TimeSlot12="5" TimeSlot13="5" TimeSlot14="5" TimeSlot15="5"
    TimeSlot16="5" TimeSlot17="5" TimeSlot18="5" TimeSlot19="5"
    TimeSlot20="5" TimeSlot21="1" TimeSlot22="1" TimeSlot23="2" />
</settings>
```

## Section Balances complètes

L'exemple structurel suivant utilise des valeurs de secours et est fourni uniquement à titre de référence d'archivage. **Ne l'installez pas sur un appareil :** les valeurs d'étalonnage et les broches doivent provenir d'une sauvegarde de cet appareil particulier ou être créées par la procédure d'étalonnage standard.

```xml
<scales pin_hc711_data="27" pin_hc711_clk="26" gain="0"
        zero_calibrate_measurement="-486050"
        weight_calibrate_measurement="-498030"
        calibrate_weight="500" start_weight="0" source_weight="1"
        normal_pecision="0.5" normal_desired_deviation="10"
        stable_pecision="0.35" stable_desired_deviation="5"
        calibrate_pecision="0.25" calibrate_desired_deviation="3"
        median_window="100" />
```

GPIO `27` et `26` ne sont qu'un exemple pour un appareil et ne sont pas universels. Utilisez les valeurs de la sauvegarde de votre appareil particulier.
