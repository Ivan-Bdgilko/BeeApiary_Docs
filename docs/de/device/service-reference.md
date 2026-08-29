# Servicedokumentation

Dieser Abschnitt ist ein technisches Konfigurationsarchiv für das BeeApiary-Messgerät. Er richtet sich an Servicetechniker und erfahrene Benutzer, die XML-Dateien manuell wiederherstellen oder prüfen müssen.

Die Anfangswerte einiger Hardware- und Netzwerkparameter hängen von der Ausstattung und Einrichtung des jeweiligen Geräts ab.

!!! danger "Manuelle Bearbeitung"
    Falsche Hardwareanschlüsse, Kalibrierungswerte oder Serviceintervalle können Messungen oder den Betrieb des Geräts beeinträchtigen. Verwende für normale Änderungen die Weboberfläche. Erstelle vor der manuellen Bearbeitung unbedingt eine Sicherung des Verzeichnisses `/setting`.

## Sicheres Vorgehen

1. Warte, bis das Gerät in den Ruhezustand wechselt. Das Gerät besitzt keinen normalen Ein-/Ausschalter: Während des Betriebs ist es entweder aktiv oder im Ruhezustand.
2. Entferne die microSD-Karte und speichere eine vollständige Kopie des Verzeichnisses `/setting`.
3. Bearbeite die XML-Dateien in einem Texteditor, ohne die Namen von Abschnitten oder Attributen zu ändern.
4. Stelle sicher, dass die XML-Datei genau ein Wurzelelement `<settings>` besitzt und alle Anführungszeichen sowie schließenden Tags vorhanden sind.
5. Setze die microSD-Karte wieder ein, während das Gerät schläft. Aktualisierte Einstellungen werden beim nächsten regulären Laden der Konfiguration angewendet; einige über die Weboberfläche vorgenommene Änderungen werden ebenfalls erst nach einem Neustart wirksam.
6. Prüfe Messungen, Kommunikation und Serviceprotokoll. Bewahre die Sicherung bis zum Abschluss der Prüfung auf.

Beim Speichern kann das Gerät die Datei normalisieren: fehlende Abschnitte oder Attribute ergänzen, Ersatzwerte einsetzen und die Reihenfolge der Elemente neu schreiben.

## Dateien

- [`/setting/mset.xml`](settings-reference.md) — Netzwerk, GSM, Uhrzeit, Hardwareoptionen, allgemeine Alarme und BLE.
- [`/setting/<hive>.xml`](hive-settings-reference.md) — Sensoren eines bestimmten Bienenstocks, Gewicht, Zeitplan, Prüfhäufigkeit und Schwellenwertalarme.
- [Konfiguration wiederherstellen](recovery.md) — sicherer Austausch der microSD-Karte, Wiederherstellung aus einer Sicherung und XML-Prüfung.

Der Name der Bienenstockdatei wird ohne Erweiterung durch die Attribute `hive1`, `hive2` usw. festgelegt. Die Erweiterung `.xml` wird automatisch angefügt.

## Zugriffsebenen

| Kennzeichnung | Bedeutung |
|---|---|
| `USER` | Der Wert kann über die normale Benutzeroberfläche geändert werden. |
| `ADVANCED` | Ein Verständnis der Auswirkungen auf Kommunikation oder Betriebslogik ist erforderlich. |
| `SERVICE` | Eine manuelle Änderung kann das Gerät funktionsunfähig machen oder Daten verfälschen. |

In den Tabellen bedeutet `—`, dass für das Feld keine Grenzen gelten. **Anfangswert** bezeichnet den Wert in einer neu erstellten Konfiguration und nicht in der XML-Datei eines bestimmten Geräts. **Wenn nicht angegeben** beschreibt den Wert, der bei fehlendem Attribut verwendet wird; er kann vom Anfangswert abweichen.

## Historische Namen

Exakte XML-Kennungen werden auch dann nicht korrigiert, wenn sie Fehler enthalten: `apairy_set`, `sefe_start_interval`, `normal_pecision` und `calibrate_pecision` müssen genau so erhalten bleiben. Die Schreibweise `synсhronize` mit dem kyrillischen Buchstaben `с` ist falsch; verwende `synchronize`.
