# Gerät nach längerer Lagerung wiederherstellen

Nach längerer Lagerung kann die Batterie vollständig entladen sein und das Gerät nicht auf eine normale Stromverbindung reagieren. Liegt die Spannung der 18650-Zelle unter `3,5 V`, stelle das Gerät in der folgenden Reihenfolge wieder her.

!!! danger "Batteriepolarität"
    Suche vor dem Entfernen der Batterie die Markierungen `+` und `-` an der Zelle und am Halter. Merke dir die richtige Ausrichtung oder fotografiere sie. Eine Batterie mit vertauschter Polarität kann das Gerät dauerhaft beschädigen.

1. Entferne die Batterie aus dem Gerät.
2. Lade sie in einem separaten Ladegerät für 18650-Zellen.
3. Prüfe nach dem Laden die Batteriespannung. Setze die Batterie erst ab einer Spannung von `4,0 V` in das Gerät ein.
4. Setze die Batterie unter genauer Beachtung der markierten Polarität ein.
5. Schließe eine gewöhnliche externe Stromversorgung ohne Power-Delivery-Schnellladen (PD) an den USB-Type-C-Anschluss des Geräts an. Verwende ein Netzteil mit USB-Type-A-Anschluss und ein USB-Type-A-auf-USB-Type-C-Kabel; ein USB-Type-C-auf-USB-Type-C-Kabel wird nicht empfohlen.
6. Wenn die Batterie eingesetzt und die externe Stromversorgung angeschlossen ist, [aktiviere das Gerät mit dem Magnetschlüssel](../device/installation.md#activation-reset).
7. Synchronisiere die Uhrzeit auf eine der folgenden Arten:

    - [verbinde dich über WLAN mit dem Zugangspunkt des Geräts](../guides/configure-local-wifi.md) und öffne seine Startseite — diese Methode ist standardmäßig verfügbar;
    - [richte die Bluetooth-Synchronisierung ein](../guides/configure-bluetooth-sync.md), öffne die BeeApiary-App und lasse das Telefon in der Nähe des Geräts — diese Methode funktioniert nur, wenn die entsprechenden Einstellungen am Gerät und in der App aktiviert sind.

8. Stelle sicher, dass Datum und Uhrzeit korrekt sind und der Zeitstempel der letzten Synchronisierung aktualisiert wurde.

Nach der Wiederherstellung von Stromversorgung und Uhrzeit ist das Gerät wieder betriebsbereit.

Siehe auch [Stromversorgung und Laden](../device/power.md) und [Zeitsynchronisierung](../system/time-synchronization.md).
