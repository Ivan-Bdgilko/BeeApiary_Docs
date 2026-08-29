# `mset.xml`: Geräteeinstellungen

Die Hauptkonfiguration befindet sich unter `/setting/mset.xml` auf der microSD-Karte und besitzt das Wurzelelement `<settings>`.

!!! warning "Die aktuelle Datei ist keine Liste der Werkseinstellungen"
    Werte in der XML-Datei eines bestimmten Geräts können durch den Benutzer, die Weboberfläche oder automatisch geändert worden sein. Beispielsweise sind `sefe_start_interval="60000"` und `alarm_sms_sec_interval="10"` keine Anfangswerte: Für eine neue Konfiguration werden `120000` ms beziehungsweise `180` s verwendet.

Beachte außerdem die [Regeln zur sicheren Bearbeitung](service-reference.md). Ändere `SERVICE`-Parameter nicht ohne Sicherung und ohne ihre Auswirkungen auf das Gerät zu verstehen.

## `net_settings`

Dieser Abschnitt speichert die Parameter des Gerätezugangspunkts, der Verbindung zu einem externen WLAN-Netzwerk, der Datenübertragung und des FTP-Zugriffs. Ein Paar `SSID`/`PASSWORD` oder `SSID_STA`/`PASSWORD_STA` wird nur angewendet, wenn beide Werte vorhanden und nicht leer sind.

| Feld | Zweck | Erforderlichkeit | Zulässige Werte / Bereich | Anfangswert | Wenn nicht angegeben | Ebene |
|---|---|---|---|---|---|---|
| `SSID` | Name des lokalen Gerätezugangspunkts | Zusammen mit `PASSWORD` bedingt erforderlich | Zeichenfolge; bis zu 32 Zeichen | `apiary_net` | Das neue Zugangspunktpaar wird nicht angewendet | `USER` |
| `PASSWORD` | Passwort des lokalen Zugangspunkts | Zusammen mit `SSID` bedingt erforderlich | Zeichenfolge; bis zu 32 Zeichen | `apiary_wifi` | Das neue Zugangspunktpaar wird nicht angewendet | `USER` |
| `SSID_STA` | SSID des externen WLAN-Netzwerks | Optional | Nicht leere Zeichenfolge; maximale Länge nicht festgelegt | `-` | Neue STA-Parameter werden nicht angewendet | `ADVANCED` |
| `PASSWORD_STA` | Passwort des externen WLAN-Netzwerks | Zusammen mit `SSID_STA` bedingt erforderlich | Zeichenfolge; maximale Länge nicht festgelegt | `-` | Neue STA-Parameter werden nicht angewendet | `ADVANCED` |
| `STA_KEY` | Authentifizierungsschlüssel während der Übertragung | Optional | Zeichenfolge; Format hängt von der Authentifizierungsmethode ab | `-` | Der WLAN-Parameter wird nicht geändert | `SERVICE` |
| `UPLOAD_URL` | Adresse des Datenempfängers über WLAN | Optional | URL; maximale Länge nicht festgelegt | Abhängig von der Gerätekonfiguration | Wird auf ein Leerzeichen gesetzt; die Übertragung ist praktisch nicht konfiguriert | `SERVICE` |
| `wifi_sync` | Erlaubt die Synchronisierung über ein externes WLAN-Netzwerk | Optional | `true`, `false` | `false` | `false` | `ADVANCED` |
| `FTP_USER` | Benutzername für lokales FTP | Als Teil eines Paars optional | Zeichenfolge; bis zu 32 Zeichen | Abhängig von der Gerätekonfiguration | Wenn eines der FTP-Felder fehlt, werden die anfänglichen FTP-Einstellungen verwendet | `ADVANCED` |
| `FTP_PASSWORD` | Passwort für lokales FTP | Als Teil eines Paars optional | Zeichenfolge; bis zu 32 Zeichen | Abhängig von der Gerätekonfiguration | Wenn eines der FTP-Felder fehlt, werden die anfänglichen FTP-Einstellungen verwendet | `ADVANCED` |

!!! note "Der Wert `-`"
    Bei `SSID_STA`, `PASSWORD_STA` und `STA_KEY` ist der Bindestrich ein wörtlicher Anfangswert. Er wird als nicht leere Zeichenfolge verarbeitet; verwende ihn daher nicht als zuverlässiges Kennzeichen für „nicht konfiguriert“.

Ändere das anfängliche Passwort `apiary_wifi` nach der ersten Prüfung des Geräts.

## `apairy_set`

Der Abschnittsname enthält einen historischen Fehler und muss `apairy_set` bleiben. Dieser Abschnitt ist zum Erstellen der Bienenstockliste erforderlich.

| Feld | Zweck | Erforderlichkeit | Zulässige Werte / Bereich | Anfangswert | Wenn nicht angegeben | Ebene |
|---|---|---|---|---|---|---|
| `hive_count` | Anzahl der Konfigurationsdateien für Bienenstöcke | Optionales Feld in einem erforderlichen Abschnitt | Ganzzahl; `1` oder mehr wird empfohlen, Grenzen werden nicht automatisch geprüft | `1` | `1` | `ADVANCED` |
| `hive1`…`hiveN` | Basisnamen der Bienenstockdateien ohne `.xml` | Für jede Nummer bis `hive_count` erforderlich | Zeichenfolge; für Kompatibilität werden bis zu 8 ASCII-Zeichen empfohlen | `hive1` | Fehler beim Lesen des Attributs; der entsprechende Bienenstock wird nicht erstellt | `SERVICE` |

Der Pfad hat das Format `/setting/<Wert>.xml`. Für den Namen wird ein interner Puffer von 24 Byte verwendet. Verwende daher keine langen Namen oder Pfadtrennzeichen.

## `GSM`

Dieser Abschnitt beschreibt zwei Empfänger. Wenn der Abschnitt fehlt, wird die GSM-Struktur gelöscht. Der Abschnitt selbst sollte deshalb auch beim Betrieb ohne SIM-Karte als erforderlich gelten.

| Feld | Zweck | Erforderlichkeit | Zulässige Werte / Bereich | Anfangswert | Wenn nicht angegeben | Ebene |
|---|---|---|---|---|---|---|
| `sms_format1` | SMS-Format für `number1` | Optional | `1` — Text; `2` — kompaktes App-Format | `2` | `2` | `USER` |
| `sms_format2` | SMS-Format für `number2` | Optional | `1` — Text; `2` — kompaktes App-Format | `2` | `2` | `USER` |
| `number1` | Telefonnummer des Hauptempfängers | Optional | Internationales Format; interner Puffer von 15 Byte | Leere Zeichenfolge | Beim ersten Laden ist kein Empfänger konfiguriert | `USER` |
| `number2` | Telefonnummer des zusätzlichen Empfängers | Optional | Internationales Format; interner Puffer von 15 Byte | Leere Zeichenfolge | Beim ersten Laden ist kein Empfänger konfiguriert | `USER` |
| `sms_wait_to_send_sec` | Wartezeit vor dem SMS-Versand bei schwachem Netz | Optional | Ganzzahlige Sekunden; keine festen Grenzen | `50` s | `50` s | `ADVANCED` |
| `alarm_call_wait_sec` | Intervall zwischen wiederholten Alarmanrufen | Optional | Ganzzahlige Sekunden; keine festen Grenzen | `80` s | `80` s | `ADVANCED` |

Gib eine leere Nummer als `number1=""` oder `number2=""` an. Verwende in veröffentlichten Beispielen keine echten Telefonnummern.

## `NTP`

Dieser Abschnitt gehört zur gleichen internen Struktur wie GSM. Wenn `NTP` vollständig fehlt, werden auch die gerade gelesenen GSM-Parameter zurückgesetzt. Der Abschnitt muss deshalb auch bei deaktivierter Synchronisierung vorhanden bleiben.

| Feld | Zweck | Erforderlichkeit | Zulässige Werte / Bereich | Anfangswert | Wenn nicht angegeben | Ebene |
|---|---|---|---|---|---|---|
| `synchronize` | Automatische Zeitsynchronisierung über einen verfügbaren Netzwerkmechanismus | Optionales Feld in einem erforderlichen Abschnitt | `true`, `false` | `false` | `false` | `USER` |
| `time_zone` | Zeitzonenverschiebung, die in der XML-Datei in vollen Stunden angegeben wird | Optional | Ganzzahl; `-11` bis `12` wird empfohlen, Grenzen werden nicht automatisch geprüft | `2` | `3` | `ADVANCED` |
| `ntp1` | Primärer Zeitserver | Optional | Hostname; interner Puffer bis 30 Byte | `0.europe.pool.ntp.org` | Beim ersten Laden leer | `ADVANCED` |
| `ntp2` | Sekundärer Zeitserver | Optional | Hostname; interner Puffer bis 30 Byte | `1.europe.pool.ntp.org` | Beim ersten Laden leer | `ADVANCED` |
| `ntp3` | Dritter Zeitserver | Optional | Hostname; interner Puffer bis 30 Byte | `2.europe.pool.ntp.org` | Beim ersten Laden leer | `ADVANCED` |

`time_zone` besitzt in beiden Fällen unterschiedliche Werte: Eine neue Datei erhält `2`, bei fehlendem Attribut wird dagegen `3` verwendet. Berücksichtige diesen Unterschied, bevor du die Ausgangskonfiguration änderst.

Die Schreibweise `synсhronize` enthält den kyrillischen Buchstaben `с` und wird nicht erkannt. Verwende ausschließlich `synchronize`.

## `options`

Die einzelnen Attribute sind optional und besitzen Ersatzwerte. **Entferne nicht den gesamten Abschnitt:** Fehlt er, werden die Abschnittsparameter gelöscht, anstatt die unten angegebenen Anfangswerte zu erhalten.

| Feld | Zweck | Erforderlichkeit | Zulässige Werte / Bereich | Anfangswert | Wenn nicht angegeben | Ebene |
|---|---|---|---|---|---|---|
| `meteo` | Kennzeichnet einen vorhandenen Druck- und Luftfeuchtigkeitssensor | Optional | `true`, `false` | `false` | `false` | `SERVICE` |
| `pir_sensor` | Kennzeichnet einen vorhandenen PIR-Bewegungssensor | Optional | `true`, `false` | `false` | `false` | `SERVICE` |
| `temperature_twist` | Vertauscht die logischen Werte T1 und T2 | Optional | `true`, `false` | `false` | `false` | `ADVANCED` |
| `oled` | Kennzeichnet ein vorhandenes OLED-Display | Optional | `true`, `false` | `false` | `false` | `SERVICE` |
| `oled_invert` | Kehrt das OLED-Bild um | Optional | `true`, `false` | `false` | `false` | `SERVICE` |
| `sefe_start_interval` | Dauer des aktiven Zeitfensters nach dem Start | Optional | Millisekunden; Grenzen werden nicht automatisch geprüft | `120000` ms | `120000` ms | `SERVICE` |
| `alarm_sms_sec_interval` | Mindestintervall zwischen Alarm-SMS | Optional | Vorzeichenlose ganzzahlige Sekunden | `180` s | `180` s | `ADVANCED` |
| `alarm_by_changes_count` | Anzahl der PIR-Zustandsänderungen zur Bestätigung eines Alarms | Optional | Vorzeichenlose Ganzzahl; der praktische Wert hängt von der Platzierung ab | `3` | `3` | `ADVANCED` |
| `alarm_by_long_state` | Dauer eines aktiven PIR-Zustands zur Alarmauslösung | Optional | Vorzeichenlose ganzzahlige Sekunden | `10` s | `10` s | `ADVANCED` |
| `time_ms_compensate` | Tägliche Kompensation des Uhrgangs | Optional | Vorzeichenbehaftete 32-Bit-Zahl in Millisekunden | `0` ms | `0` ms | `SERVICE` |
| `sync_time_sec` | Service-Zeitstempel für die manuelle Synchronisierung | Optional | Vorzeichenbehaftete 64-Bit-Zahl in Sekunden | `0` | `0` | `SERVICE` |

`sefe_start_interval` ist der exakte historische Feldname. Der Anfangswert beträgt `120000` ms; der Bereich wird nicht automatisch geprüft, daher ist eine beliebige Verringerung gefährlich.

Über die Weboberfläche geänderte Hardwaremerkmale werden sofort gespeichert, aber von der Betriebskonfiguration erst nach dem nächsten Einlesen der Einstellungen angewendet.

## `BLE`

Der gesamte Abschnitt ist zur Kompatibilität mit älteren Dateien optional. Fehlt er, ist BLE deaktiviert und es werden die aktuellen Werte sowie die Standardintervalle verwendet.

| Feld | Zweck | Erforderlichkeit | Zulässige Werte / Bereich | Anfangswert | Wenn nicht angegeben | Ebene |
|---|---|---|---|---|---|---|
| `ble_enable` | Aktiviert BLE | Optional | `true`, `false` | `false` | `false`; ein ungültiger Wert deaktiviert BLE ebenfalls | `USER` |
| `static_values` | Wählt statische anstelle aktueller Werte | Optional | `true`, `false` | `false` | `false` | `SERVICE` |
| `update_time_sec` | Aktualisierungsintervall der BLE-Daten | Optional | `3`–`60` s; kleinere Werte werden auf `3`, größere auf `60` normalisiert | `30` s | `30` s | `ADVANCED` |
| `advertising_time_sec` | Dauer der BLE-Werbeaussendung | Optional | `0` oder `10`–`60` s; eingegebene Werte von `1` bis `9` werden auf `0`, Werte über `60` auf `60` normalisiert | `20` s | `20` s | `ADVANCED` |

Für `static_values` ist nur die Auswahl statischer anstelle aktueller Werte beschrieben; eine andere Wirkung des Parameters ist nicht festgelegt.

## Minimales Beispiel { #minimal-example }

In diesem Beispiel bleiben STA, FTP und BLE auf ihren Anfangswerten. Ein leerer, aber vorhandener Abschnitt `<options />` aktiviert den Ersatzwert jedes Attributs, anstatt die gesamte Struktur zu löschen.

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

## Vollständiges bereinigtes Beispiel { #full-example }

Die Werte `SITE_WIFI`, `WIFI_PASSWORD`, `DEVICE_KEY`, `FTP_USER`, `FTP_PASSWORD` und die URL sind Platzhalter und keine Daten eines betriebenen Geräts.

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
