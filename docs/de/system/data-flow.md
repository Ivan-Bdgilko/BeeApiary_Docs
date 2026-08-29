# Datenfluss

1. Zu Beginn jeder Stunde führt das BeeApiary-Messgerät die konfigurierten Messungen durch.
2. Das Ergebnis wird im lokalen microSD-Archiv gespeichert, sofern die Karte verfügbar ist.
3. Das Gerät stellt die Daten über den konfigurierten Kanal bereit:

    - Es sendet nach Zeitplan eine normale oder kompakte SMS-Nachricht.
    - Es leitet Daten über das WLAN-Netzwerk am Bienenstand weiter.
    - Es [überträgt verfügbare Daten über Bluetooth](bluetooth.md), wenn sich das Telefon in der Nähe befindet.
    - Es stellt der App nach Bestätigung durch den Benutzer das Archiv über den eigenen Zugangspunkt bereit.

4. Die App erkennt die empfangenen Werte und fügt sie dem lokalen Speicher des Telefons hinzu.
5. Der Benutzer sieht aktuelle Werte, den Verlauf und Diagramme.

Das Fehlen von GSM, WLAN, Bluetooth oder eines Telefons in der Nähe unterbricht die grundlegende Messwerterfassung nicht. Sobald eine Verbindung verfügbar ist, können die Daten an die App übertragen werden.

Bei der entfernten Weiterleitung über WLAN speichert der Online-Übertragungsdienst die Daten nicht. Dauerhafte Kopien verbleiben auf dem Messgerät und auf dem Telefon des Benutzers.

Einen Vergleich der Kanäle findest du unter [Daten in der App empfangen](connectivity.md).

Zur Einrichtung des entfernten Kanals siehe [Synchronisierung über das WLAN-Netzwerk am Bienenstand](../guides/configure-wifi-sync.md).

Zur Einrichtung des lokalen automatischen Kanals siehe [Synchronisierung über Bluetooth](../guides/configure-bluetooth-sync.md).
