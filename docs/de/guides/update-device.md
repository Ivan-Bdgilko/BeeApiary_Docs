# Firmware des BeeApiary-Messgeräts aktualisieren

Wähle vor der Aktualisierung eine Firmware aus, die zur Gerätegeneration und zur gewünschten Sprache der Benutzeroberfläche passt.

## Firmwaregeneration auswählen

| Gerät | Quelle der Aktualisierungen | Entwicklungsstatus |
|---|---|---|
| Vor August 2026 hergestellt | [Hive_Controller](https://github.com/Ivan-Bdgilko/Hive_Controller) | Der Funktionsausbau der vorherigen Version wird nicht mehr unterstützt |
| Nach August 2026 hergestellt | [Hive_Controller_Ble](https://github.com/Ivan-Bdgilko/Hive_Controller_Ble) | Die neue Version erhält weiterhin Aktualisierungen und neue Funktionen |

!!! danger "Ein älteres Gerät auf die neue Version umstellen"
    Jedes früher hergestellte Gerät kann auf die neue Softwareversion umgestellt werden. Dafür ist jedoch eine Aktualisierung beim Hersteller erforderlich. Derzeit gibt es keinen einfachen Patch für eine selbstständige Umstellung; die Standardanleitung auf dieser Seite wechselt daher nicht zwischen den Gerätegenerationen.

## Sprache der Firmware auswählen

Für beide Generationen stehen mehrsprachige Builds zur Verfügung. Das Suffix im Versionsnamen kennzeichnet die Sprache:

| Suffix | Sprache |
|---|---|
| `-de` | Deutsch |
| `-en` | Englisch |
| `-es` | Spanisch |
| `-fr` | Französisch |
| `-pl` | Polnisch |
| `-uk` | Ukrainisch |

Wähle die Sprache aus, indem du die entsprechende Datei herunterlädst und installierst. Die Sprach-Builds sind in den oben genannten Repositorys frei verfügbar. Bei Bedarf können später weitere Sprachen hinzukommen.

## Gerät über microSD aktualisieren

1. Warte, bis das Gerät in den Ruhezustand wechselt, und entferne dann die microSD-Karte.
2. Erstelle im Stammverzeichnis der Karte den Ordner `/fm`, falls er noch nicht vorhanden ist.
3. Lege die Aktualisierungsdatei `Apiary.bin` in `/fm` ab.
4. Setze die microSD-Karte wieder in das Gerät ein.
5. [Aktiviere das Gerät oder starte es neu](../device/installation.md#activation-reset), indem du den Magnetschlüssel verwendest.
6. Warte auf eine normale SMS mit Messwerten; die Aktualisierung dauert gewöhnlich bis zu zwei Minuten.
7. Prüfe unten auf der Startseite der Weboberfläche die Firmwareversion, das Sprachsuffix, Datum und Uhrzeit des Builds sowie die eindeutige Gerätenummer.

![Firmwareversion, Sprachsuffix, Build-Zeit und eindeutige ID in der Weboberfläche des Geräts](../../assets/common/guides/update-device/device-version-build-time-and-id.png){ .doc-screenshot }

Die vollständige Versionszeichenfolge enthält das Lokalisierungssuffix, zum Beispiel `-uk`. Vergleiche sie mit der entsprechenden Aktualisierungsversion im Repository deiner Gerätegeneration. Auf derselben Seite werden außerdem Datum und Uhrzeit des Builds sowie die eindeutige Geräte-ID angezeigt.

!!! warning "Datei vor der Aktualisierung prüfen"
    Stelle sicher, dass `Apiary.bin` für deine Gerätegeneration und die gewünschte Sprache vorgesehen ist. Serviceverfahren zur Aktualisierung über FTP oder einen Server gehören nicht zu dieser Anleitung.
