# Konfiguration wiederherstellen

Diese Seite beschreibt den sicheren Austausch der microSD-Karte, die Wiederherstellung der Konfiguration aus einer Sicherung und die Prüfung der XML-Dateien nach dem Start des Geräts.

!!! danger "microSD-Karte nicht während des aktiven Betriebs entfernen"
    Das Gerät besitzt keinen normalen Ein-/Ausschalter. Warte vor dem Entfernen oder Einsetzen der microSD-Karte, bis das Gerät in den Ruhezustand wechselt. Speichere zuerst eine vollständige Kopie des Verzeichnisses `/setting`.

## Automatische Normalisierung

- Die Hauptdatei befindet sich unter `/setting/mset.xml`.
- Wenn die Hauptdatei fehlt, kann das Gerät eine Ausgangskonfiguration erstellen.
- Eine fehlende oder unvollständige Bienenstockdatei kann mit Ersatzwerten des aktuellen Zustands neu gespeichert werden.
- Ein fehlender Abschnitt `hive`, `thermometer` oder `schedule` sowie ein unvollständiger vorhandener Abschnitt `scales` lösen die Normalisierung der Bienenstockdatei aus.
- Ein vollständig fehlender Abschnitt `scales` ist kein Fehler: Die Waage wird dann einfach nicht angelegt.
- Strukturfehler im XML-Wurzelelement, im Abschnitt `apairy_set` oder im Attribut `hiveN` können das Lesen der Konfiguration verhindern.

Das Erstellen einer anfänglichen `mset.xml` bedeutet nicht, dass alle Parameter universelle Werte erhalten. `UPLOAD_URL`, FTP-Zugangsdaten, HX711-Anschlüsse und einige andere Felder hängen von der Gerätekonfiguration oder der individuellen Einrichtung ab.

!!! warning "Eine Sicherung ist erforderlich"
    Verlasse dich nicht allein auf die automatische Wiederherstellung. Speichere vor dem Austausch der microSD-Karte das gesamte Verzeichnis `/setting`, sofern die Karte noch gelesen werden kann.

## microSD-Karte sicher austauschen

1. Warte, bis das Gerät in den Ruhezustand wechselt.
2. Entferne die microSD-Karte und kopiere ihren gesamten Inhalt, sofern sie lesbar ist.
3. Bereite die microSD-Karte gemäß den Anforderungen der jeweiligen Hardwareversion des Geräts vor.
4. Stelle das Verzeichnis `/setting` aus einer geprüften Sicherung wieder her.
5. Wenn keine Sicherung vorhanden ist, verwende keine Kalibrierungswerte der Waage von einem anderen Gerät. Stelle zuerst eine minimale [`mset.xml`](settings-reference.md#minimal-example) wieder her und erstelle die Bienenstockdatei anschließend ohne Abschnitt `scales`, oder führe die reguläre Kalibrierung durch.
6. Setze die microSD-Karte ein, während das Gerät schläft, und warte auf den nächsten Betriebszyklus.
7. Prüfe Uhrzeit, Netzwerk, GSM-Nummern, vorhandene Sensoren, Zeitplan und Gewicht.
8. Vergleiche die normalisierten XML-Dateien mit der Sicherung: Das Gerät kann Felder mit Ersatzwerten ergänzt oder Abschnitte neu geschrieben haben.

## Wenn die Konfiguration nicht gelesen werden kann

1. Prüfe, ob die Datei genau ein Wurzelelement `<settings>` besitzt.
2. Prüfe die exakten Namen `apairy_set`, `synchronize`, `sefe_start_interval` und `pecision` in den drei Filterfeldern.
3. Stelle sicher, dass `hive_count` die entsprechenden Attribute `hive1`…`hiveN` enthält.
4. Stelle sicher, dass jede angegebene Datei `/setting/<hive>.xml` vorhanden ist.
5. Versuche das Problem nicht zu beheben, indem du `scales` von einem anderen Gerät kopierst. Entferne vorübergehend den Waagenabschnitt und prüfe den Rest der Konfiguration.
6. Speichere die problematischen XML-Dateien und Serviceprotokolle für die Diagnose.

Eine vollständige Beschreibung der Felder findest du in den Referenzen zu [`mset.xml`](settings-reference.md) und [`HIVE*.XML`](hive-settings-reference.md).
