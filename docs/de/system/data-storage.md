# Datenspeicherung

Das BeeApiary-Messgerät zeichnet Daten auf der microSD-Karte auf, unabhängig davon, ob GSM verfügbar ist. Für jedes Jahr wird ein Verzeichnis `YEARxx` angelegt. Für die Monate werden CSV-Dateien mit Datum, Uhrzeit und verfügbaren Messwerten erstellt.

Die CSV-Datei kann Folgendes enthalten:

- `Date`, `Time`;
- `Weight[Kg]`;
- `T1 [°C]`, `T2 [°C]` und zusätzliche Temperaturen;
- Batterieladung;
- Druck und Luftfeuchtigkeit;
- GSM RSSI;
- Service-Metadaten der Firmware.

Die enthaltenen Spalten hängen von der Gerätekonfiguration und der Firmware-Version ab. Messwerte benötigen ungefähr 2 MB pro Jahr, Serviceprotokolle etwa 40–50 MB pro Jahr.

Zum Abrufen der Daten siehe [Archiv herunterladen](../guides/download-archive.md).
