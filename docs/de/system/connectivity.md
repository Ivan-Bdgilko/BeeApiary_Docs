# Daten in der App empfangen

Daten vom BeeApiary-Messgerät können auf vier Wegen zur App gelangen. Die Wahl hängt davon ab, wo sich das Telefon befindet und welche Verbindung in der Nähe des Geräts verfügbar ist.

| Kanal | Standort des Telefons | Voraussetzungen | So gelangen die Daten zur App |
|---|---|---|---|
| [GSM und SMS](gsm-and-sms.md) | Überall mit Mobilfunkempfang | Eine SIM-Karte im Gerät mit einem einfachen SMS-Tarif | Die App verarbeitet SMS-Nachrichten automatisch; mobiles Internet ist nicht erforderlich |
| [Direkte Verbindung zum Zugangspunkt des Geräts](local-wifi.md#direct-access-point) | In der Nähe des Geräts | Das Gerät mit dem Magnetschlüssel aktivieren und innerhalb des verfügbaren Zeitfensters, gewöhnlich etwa einer Minute, eine Verbindung zu `apiary_net` herstellen | Die App findet das Gerät, fragt nach der Erlaubnis zum Abrufen des Archivs und importiert die Daten nach der Bestätigung |
| [Weiterleitung über das WLAN-Netzwerk am Bienenstand](local-wifi.md#apiary-wifi-routing) | Überall mit Internetzugang | In der Nähe des Geräts muss ein konfiguriertes WLAN-Netzwerk mit Internetzugang verfügbar sein | Die Daten werden automatisch zur App weitergeleitet; eine eigene SIM-Karte für jedes Gerät ist nicht erforderlich |
| [Bluetooth](bluetooth.md) | In der Nähe, innerhalb der Bluetooth-Reichweite | **BLE info**, BLE-Suche und Hintergrundbetrieb der App sind aktiviert; die Uhrzeit ist synchronisiert; SIM-Karte und Internet sind nicht erforderlich | Die App synchronisiert aktuelle Daten automatisch und kann den verfügbaren Verlauf wiederherstellen |

## GSM und SMS

Das Gerät sendet normale oder kompakte SMS-Nachrichten ohne mobiles Internet. Die App erkennt kompakte Nachrichten und fügt die Messwerte automatisch dem lokalen Speicher des Telefons hinzu.

## Direkte Verbindung zum Gerät

Nach der Aktivierung mit dem Magnetschlüssel erstellt das Gerät vorübergehend den Zugangspunkt `apiary_net`. Ein damit verbundenes Telefon benötigt weder eine SIM-Karte noch Internetzugang. Die App findet das Gerät automatisch, lädt das Archiv aber erst nach Bestätigung durch den Benutzer herunter.

Das genaue Verfahren findest du unter [Archiv herunterladen](../guides/download-archive.md).

## Weiterleitung über das WLAN-Netzwerk am Bienenstand

Das Gerät kann ein vorhandenes WLAN-Netzwerk mit Internetzugang am Bienenstand verwenden. Der Besitzer empfängt die Daten aus der Ferne in der App, ohne dass jedes Gerät eine eigene SIM-Karte benötigt.

Vor der Ersteinrichtung muss die App mindestens einmal Daten vom Gerät über SMS oder durch direktes Herunterladen des Archivs empfangen haben. Die Registrierung erfolgt auf einem Telefon mit Internetzugang. Anschließend werden die vorbereiteten WLAN- und Cloud-Einstellungen über den Zugangspunkt `apiary_net` an das Gerät übertragen.

Der Online-Übertragungsdienst speichert keine Daten. Dauerhafte Kopien verbleiben auf dem Messgerät und auf dem Telefon des Benutzers.

Das genaue Verfahren findest du unter [Synchronisierung über das WLAN-Netzwerk am Bienenstand einrichten](../guides/configure-wifi-sync.md).

## Bluetooth

Wenn sich das Telefon innerhalb der Bluetooth-Reichweite befindet, synchronisiert die App die verfügbaren Daten automatisch. Dafür sind weder eine SIM-Karte noch mobiles Internet oder eine Aktivierung des Zugangspunkts `apiary_net` erforderlich. Wenn das Abrufen des Verlaufs aktiviert ist, können vorübergehende Lücken bei der nächsten erfolgreichen Verbindung ergänzt werden.

Eine Beschreibung findest du unter [Datensynchronisierung über Bluetooth](bluetooth.md). Das praktische Verfahren steht unter [Bluetooth-Synchronisierung einrichten](../guides/configure-bluetooth-sync.md).

## Betrieb ohne Verbindung

Ein vorübergehender oder vollständiger Ausfall eines Kommunikationskanals unterbricht die Messungen nicht: Das Gerät zeichnet sie weiterhin auf der microSD-Karte auf. Sobald die Verbindung wiederhergestellt ist, kann die App verpasste Daten abrufen. Die verfügbare Verlaufstiefe hängt jedoch vom gewählten Kanal ab.

| Kanal | Verfügbarer Verlauf nach Wiederherstellung der Verbindung | Hinweis |
|---|---|---|
| GSM und SMS | 2 bis 12 Stunden | Abhängig vom konfigurierten Zeitplan für den SMS-Versand |
| Direkte Verbindung zum Zugangspunkt des Geräts | Bis zu 1 Jahr | Die Daten können heruntergeladen werden, wenn die entsprechenden Einträge im lokalen Archiv vorhanden sind |
| Bluetooth | 1 Tag bis 1 Woche | Abhängig von der Einstellung zum Abrufen des Verlaufs und den verfügbaren Einträgen |
| Weiterleitung über das WLAN-Netzwerk am Bienenstand | Verlauf nicht verfügbar | Der Online-Übertragungsdienst leitet aktuelle Daten weiter, speichert sie aber nicht auf dem Server |

Diese Grenzen gelten nur für die Menge verpasster Daten, die über einen bestimmten Kanal wiederhergestellt werden kann. Das lokale [microSD-Archiv](data-storage.md) ist nicht auf ein Jahr Speicherzeit begrenzt: Seine Tiefe wird nur durch die Kartenkapazität bestimmt, die für die gesamte erwartete Nutzungsdauer des Geräts ausreicht. Bei Bedarf können die Daten auch direkt von der microSD-Karte gelesen werden.
