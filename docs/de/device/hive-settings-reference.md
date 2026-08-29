# `HIVE*.XML`: Bienenstockeinstellungen

Die Bienenstockkonfiguration wird unter `/setting/<hive>.xml` gespeichert. Der Basisname `<hive>` wird durch die Attribute `hive1`, `hive2` usw. in [`mset.xml`](settings-reference.md) festgelegt; die Erweiterung `.xml` wird automatisch angefügt.

!!! danger "Hardwareabhängige Werte"
    Kopiere den Abschnitt `scales` nicht von einem anderen Gerät. Platinenanschlüsse und Kalibrierungswerte hängen von der Hardwareversion und dem jeweiligen Satz von Wägesensoren ab. Falsche Werte können Messungen verfälschen oder verhindern.

Beachte die [Regeln zur sicheren Bearbeitung](service-reference.md).

## Automatisches Neuschreiben

Nach dem Lesen kann das Gerät die Datei erneut speichern:

- Eine fehlende oder beschädigte Datei wird aus dem verfügbaren aktuellen Zustand erstellt.
- Fehlende Abschnitte `hive`, `thermometer` oder `schedule` aktivieren die Normalisierung.
- Ein fehlendes Attribut in einem vorhandenen Abschnitt `scales` oder `thermometer` wird durch einen Ersatzwert ersetzt und aktiviert die Normalisierung.
- Die vollständigen Abschnitte `scales`, `booster` und `range_alarmer` sind optional.
- Bei der Normalisierung werden auch die Abschnitte `booster`, `range_alarmer`, `thermometer` und `schedule` geschrieben, selbst wenn einige davon in der Ausgangsdatei fehlten.

## `hive`

| Feld | Zweck | Erforderlichkeit | Zulässige Werte / Bereich | Anfangswert | Wenn nicht angegeben | Ebene |
|---|---|---|---|---|---|---|
| `hive_name` | Interner Name des Bienenstocks | Optional | Zeichenfolge; für Kompatibilität werden bis zu 8 ASCII-Zeichen empfohlen | Name aus `mset.xml`, beispielsweise `hive1` | `hive_<Index>`; die Datei wird zum Neuschreiben markiert | `ADVANCED` |
| `bus_number` | Nummer des Bienenstocks auf dem internen Bus | Optional | Ganzzahl; Grenzen werden nicht geprüft | Instanzindex, bei der ersten Instanz `0` | Instanzindex; die Datei wird zum Neuschreiben markiert | `SERVICE` |
| `main_device` | Kennzeichnet das Hauptgerät mit lokalen Hardwaresensoren | Optional | `true`, `false` | `true` in einer neu erstellten Datei | Die Instanz wird nicht zum Hauptgerät; das Fehlen allein aktiviert kein Neuschreiben | `SERVICE` |

Die Unterstützung untergeordneter Geräte ist veraltet. Der Wert `main_device="false"` wird beim Laden akzeptiert, nach dem Speichern lautet das Attribut jedoch `main_device="true"`. Verwende `false` nicht als dauerhafte Konfiguration.

## `scales`

Wenn der gesamte Abschnitt fehlt, wird kein Waagenobjekt erstellt und die Gewichtsmessung ist deaktiviert. Ist der Abschnitt vorhanden, wird jedes fehlende oder ungültige Feld durch einen Ersatzwert ersetzt; anschließend kann die gesamte Datei neu geschrieben werden.

| Feld | Zweck | Erforderlichkeit | Zulässige Werte / Bereich | Anfangswert | Wenn nicht angegeben | Ebene |
|---|---|---|---|---|---|---|
| `pin_hc711_data` | Daten-GPIO des HX711 | In einem vorhandenen Abschnitt erforderlich | GPIO der jeweiligen Platine | Der Abschnitt wird nicht automatisch erstellt; hardwareabhängig | Anschluss der jeweiligen Platine; die Datei wird neu geschrieben | `SERVICE` |
| `pin_hc711_clk` | Takt-GPIO des HX711 | In einem vorhandenen Abschnitt erforderlich | GPIO der jeweiligen Platine | Der Abschnitt wird nicht automatisch erstellt; hardwareabhängig | Anschluss der jeweiligen Platine; die Datei wird neu geschrieben | `SERVICE` |
| `gain` | Verstärkungsmodus des HX711 | In einem vorhandenen Abschnitt erforderlich | Wert des HX711-Verstärkungsmodus | Kanal A, Verstärkung 128 | Kanal A, Verstärkung 128; die Datei wird neu geschrieben | `SERVICE` |
| `zero_calibrate_measurement` | ADC-Rohwert bei Nulllast | In einem vorhandenen Abschnitt erforderlich | Vorzeichenbehaftete 32-Bit-Ganzzahl | Hardwareabhängig | Ersatzwert `-486050`; die Datei wird neu geschrieben | `SERVICE` |
| `weight_calibrate_measurement` | ADC-Rohwert mit Referenzgewicht | In einem vorhandenen Abschnitt erforderlich | Vorzeichenbehaftete 32-Bit-Ganzzahl | Hardwareabhängig | Ersatzwert `-498030`; die Datei wird neu geschrieben | `SERVICE` |
| `calibrate_weight` | Masse des Kalibrierungsreferenzgewichts | In einem vorhandenen Abschnitt erforderlich | Gramm; positive Ganzzahl; Grenzen werden nicht automatisch geprüft | Hardwareabhängig | `500` g; die Datei wird neu geschrieben | `USER` |
| `start_weight` | Tara, die vom Ergebnis abgezogen wird | In einem vorhandenen Abschnitt erforderlich | Gramm; `-100000` bis `100000` wird empfohlen; Grenzen werden nicht automatisch geprüft | Hardwareabhängig | `0` g; die Datei wird neu geschrieben | `USER` |
| `source_weight` | Filter, dessen Ergebnis als Hauptgewicht verwendet wird | In einem vorhandenen Abschnitt erforderlich | `1` — `immediate`; `2` — `stable`; `3` — `calibration` | Der Abschnitt wird nicht automatisch erstellt | `1`; die Datei wird neu geschrieben. Andere Werte werden während des Betriebs als `1` behandelt | `SERVICE` |
| `normal_pecision` | Genauigkeitsparameter des schnellen Filters | In einem vorhandenen Abschnitt erforderlich | Gleitkommazahl; Grenzen werden nicht geprüft | Der Abschnitt wird nicht automatisch erstellt | `0.5`; die Datei wird neu geschrieben | `SERVICE` |
| `normal_desired_deviation` | Gewünschte Abweichung des schnellen Filters | In einem vorhandenen Abschnitt erforderlich | Gleitkommazahl; Grenzen werden nicht geprüft | Der Abschnitt wird nicht automatisch erstellt | `10`; die Datei wird neu geschrieben | `SERVICE` |
| `stable_pecision` | Genauigkeitsparameter des stabilen Filters | In einem vorhandenen Abschnitt erforderlich | Gleitkommazahl; Grenzen werden nicht geprüft | Der Abschnitt wird nicht automatisch erstellt | `0.35`; die Datei wird neu geschrieben | `SERVICE` |
| `stable_desired_deviation` | Gewünschte Abweichung des stabilen Filters | In einem vorhandenen Abschnitt erforderlich | Gleitkommazahl; Grenzen werden nicht geprüft | Der Abschnitt wird nicht automatisch erstellt | `5`; die Datei wird neu geschrieben | `SERVICE` |
| `calibrate_pecision` | Genauigkeitsparameter des Kalibrierungsfilters | In einem vorhandenen Abschnitt erforderlich | Gleitkommazahl; Grenzen werden nicht geprüft | Der Abschnitt wird nicht automatisch erstellt | `0.25`; die Datei wird neu geschrieben | `SERVICE` |
| `calibrate_desired_deviation` | Gewünschte Abweichung des Kalibrierungsfilters | In einem vorhandenen Abschnitt erforderlich | Gleitkommazahl; Grenzen werden nicht geprüft | Der Abschnitt wird nicht automatisch erstellt | `3`; die Datei wird neu geschrieben | `SERVICE` |
| `median_window` | Fenstergröße des Medianfilters | In einem vorhandenen Abschnitt erforderlich | `3`–`100`; Werte außerhalb des Bereichs werden ersetzt | Der Abschnitt wird nicht automatisch erstellt | `100`; die Datei wird neu geschrieben | `SERVICE` |

Die Kennungen `normal_pecision`, `stable_pecision` und `calibrate_pecision` enthalten den historischen Fehler `pecision`, der in der XML-Datei nicht korrigiert werden darf.

`gain` wird aus der Datei geladen, beim Speichern jedoch immer auf Kanal A mit Verstärkung 128 gesetzt. Ändere den Wert nicht manuell ohne die Daten deines konkreten Geräts.

## `thermometer`

Ein fehlender Abschnitt aktiviert die Normalisierung der Datei. Der Wert `sensors_count="0"` deaktiviert die Abfrage der DS18B20-Sensoren.

| Feld | Zweck | Erforderlichkeit | Zulässige Werte / Bereich | Anfangswert | Wenn nicht angegeben | Ebene |
|---|---|---|---|---|---|---|
| `pin_onewire` | GPIO des 1-Wire-Busses | Optional | GPIO der jeweiligen Platine | `4` | `4`; die Datei wird neu geschrieben | `SERVICE` |
| `sensors_count` | Anzahl der DS18B20-Sensoren | Optional | `0` deaktiviert die Sensoren; positive Ganzzahl; Obergrenze wird nicht geprüft | `2` | `2`; die Datei wird neu geschrieben | `ADVANCED` |

## `schedule`

Die Attribute `TimeSlot0`–`TimeSlot23` bestimmen die Aktion für die jeweilige Stunde. Nach Minute 30 wird die Aktion der nächsten Stunde ausgewählt; nach Stunde 23 wird `TimeSlot0` verwendet.

| Feld | Zweck | Erforderlichkeit | Zulässige Werte / Bereich | Anfangswert | Wenn nicht angegeben | Ebene |
|---|---|---|---|---|---|---|
| `TimeSlot0`…`TimeSlot23` | Art der geplanten Aktion für die Stunde `0`–`23` | Alle Attribute sind optional, mindestens ein Slot mit `2` ist jedoch erforderlich | Ganzzahl von `0` bis `5`; siehe unten | `5` für die Stunden `0`–`20`; `1` für `21` und `22`; `2` für `23` | Ein fehlender Slot wird zu `0`. Wenn nach dem Lesen keine `2` vorhanden ist, wird der gesamte Zeitplan auf den Anfangszeitplan zurückgesetzt | `ADVANCED` |

| Wert | Aktion | Empfehlung |
|---:|---|---|
| `0` | Keine geplante Aktion | Kann für einen leeren Slot verwendet werden |
| `1` | Messung | Unterstützt |
| `2` | Übertragung über den Hauptkanal | In mindestens einem Slot erforderlich |
| `3` | Für die Übertragung über WLAN reserviert | Nicht verwenden |
| `4` | Für die Übertragung über BLE reserviert | Nicht verwenden |
| `5` | Stündliches Aufwachen zur Synchronisierung | Wird vom Anfangszeitplan verwendet |

Andere Ganzzahlen werden nicht abgelehnt, besitzen aber kein definiertes Verhalten. Verwende nur Werte aus der Tabelle.

### Anfangszeitplan

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

Dieser Abschnitt legt das Intervall für zusätzliche Aufwachvorgänge zur Prüfung kritischer Parameter fest. Wenn der Abschnitt fehlt, wird während des Betriebs ein stündliches Intervall verwendet; das Fehlen selbst löst kein Neuschreiben aus.

| Feld | Zweck | Erforderlichkeit | Zulässige Werte / Bereich | Anfangswert | Wenn nicht angegeben | Ebene |
|---|---|---|---|---|---|---|
| `booster_time_sec` | Intervall der zusätzlichen Prüfung | Optional | `180`, `240`, `300`, `360`, `600`, `720`, `900`, `1200`, `1800` oder `3600` s | `3600` s | `3600` s | `ADVANCED` |

Ein Wert unter `180` s wird zu `180`, ein Wert über `3600` s zu `3600`. Andere Werte innerhalb des Bereichs werden auf das nächstgelegene unterstützte Intervall aus der Tabelle gerundet.

## `range_alarmer`

Dieser Abschnitt ist optional. Wenn er fehlt, wird der Schwellenwertalarm nicht initialisiert. Wenn `alarm="false"` gesetzt ist oder das Attribut `alarm` fehlt, werden die Grenzen nicht gelesen und die Hintergrundaufgabe für Alarme wird nicht gestartet.

| Feld | Zweck | Erforderlichkeit | Zulässige Werte / Bereich | Anfangswert | Wenn nicht angegeben | Ebene |
|---|---|---|---|---|---|---|
| `alarm` | Aktiviert Schwellenwertalarme | Optional | `true`, `false` | `false` | `false` | `USER` |
| `T1_min` | Untere Grenze für T1 | Optional | Gleitkommazahl, °C; physikalische Grenzen und Reihenfolge von min/max werden nicht automatisch geprüft | `-500` °C in einer neu erstellten Datei | Bei `alarm="true"` gibt es keine untere Grenze | `ADVANCED` |
| `T1_max` | Obere Grenze für T1 | Optional | Gleitkommazahl, °C; physikalische Grenzen und Reihenfolge von min/max werden nicht automatisch geprüft | `500` °C in einer neu erstellten Datei | Bei `alarm="true"` gibt es keine obere Grenze | `ADVANCED` |
| `T2_min` | Untere Grenze für T2 | Optional | Gleitkommazahl, °C; physikalische Grenzen und Reihenfolge von min/max werden nicht automatisch geprüft | `-500` °C in einer neu erstellten Datei | Bei `alarm="true"` gibt es keine untere Grenze | `ADVANCED` |
| `T2_max` | Obere Grenze für T2 | Optional | Gleitkommazahl, °C; physikalische Grenzen und Reihenfolge von min/max werden nicht automatisch geprüft | `500` °C in einer neu erstellten Datei | Bei `alarm="true"` gibt es keine obere Grenze | `ADVANCED` |
| `Humidity_min` | Untere Luftfeuchtigkeitsgrenze | Optional | Gleitkommazahl, %; physikalische Grenzen und Reihenfolge von min/max werden nicht automatisch geprüft | `-20` % in einer neu erstellten Datei | Bei `alarm="true"` gibt es keine untere Grenze | `ADVANCED` |
| `Humidity_max` | Obere Luftfeuchtigkeitsgrenze | Optional | Gleitkommazahl, %; physikalische Grenzen und Reihenfolge von min/max werden nicht automatisch geprüft | `200` % in einer neu erstellten Datei | Bei `alarm="true"` gibt es keine obere Grenze | `ADVANCED` |

Für jede Quelle T1, T2 oder Luftfeuchtigkeit genügt eine Grenze. Wenn für eine bestimmte Quelle keine Grenze angegeben ist, wird sie nicht in die Prüfung aufgenommen. Die Reihenfolge von `_min` und `_max` wird nicht automatisch geprüft.

### Beispiel für einseitige Alarme

In diesem Beispiel wird T1 nur nach oben und T2 nur nach unten überwacht; die Luftfeuchtigkeit wird nicht überwacht:

```xml
<range_alarmer alarm="true" T1_max="45.0" T2_min="-10.0" />
```

Die allgemeine SMS-Häufigkeit und die Bestätigung von PIR-Alarmen werden durch `alarm_sms_sec_interval`, `alarm_by_changes_count` und `alarm_by_long_state` in [`mset.xml`](settings-reference.md#options) festgelegt.

## Strukturbeispiel ohne Waage

Diese Datei verwendet den Anfangszeitplan, zwei Temperatursensoren und deaktivierte Schwellenwertalarme. Der Abschnitt `scales` fehlt, daher wird kein Waagenobjekt erstellt.

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

## Vollständiger Waagenabschnitt

Das folgende Strukturbeispiel enthält Ersatzwerte und dient ausschließlich als Archivreferenz. **Installiere es nicht auf einem Gerät:** Kalibrierungswerte und Anschlüsse müssen aus einer Sicherung genau dieses Geräts stammen oder durch die reguläre Kalibrierung erzeugt werden.

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

GPIO `27` und `26` sind nur ein Beispiel für ein einzelnes Gerät und nicht universell. Verwende die Werte aus der Sicherung deines konkreten Geräts.
