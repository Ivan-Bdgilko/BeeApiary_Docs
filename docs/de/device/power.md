# Stromversorgung und Laden

Das Gerät wird mit einer oder zwei 18650-Zellen betrieben und über USB Type-C geladen. Als Stromquelle können ein Ladegerät, eine Powerbank oder ein optionales Solarmodul dienen.

!!! note "Ladegerät und Kabel auswählen"
    Das Gerät unterstützt kein Schnellladen, einschließlich USB Power Delivery (PD). Verwende eine normale Stromquelle mit einem USB-Type-A-Anschluss und ein USB-Type-A–USB-Type-C-Kabel. Ein USB-Type-C–USB-Type-C-Kabel wird zum Laden nicht empfohlen.

![Geöffneter USB-Type-C-Stromanschluss](../../assets/common/device/power/open-usb-type-c-port.jpeg){ .doc-photo }

Schließe nach dem Laden die Schutzabdeckung des Anschlusses:

![Geschlossene Schutzabdeckung des Stromanschlusses](../../assets/common/device/power/closed-usb-type-c-cover.jpeg){ .doc-photo }

- Die blaue Anzeige leuchtet, wenn die Batterie vollständig geladen und die externe Stromversorgung noch angeschlossen ist.
- Der Ladezustand wird in SMS-Nachrichten und in den allgemeinen Einstellungen der Weboberfläche angezeigt.

  ![Batterieladung in der Weboberfläche](../../assets/de/device/power/battery-charge-status.png){ .doc-screenshot }

- Unter 20 % wechselt das Gerät in den Energiesparmodus, beendet normale Messungen und SMS-Nachrichten und prüft regelmäßig den Ladezustand.
- Nach einer kritischen Entladung wird die Batterie automatisch getrennt; nach dem Laden kann eine [Zeitsynchronisierung](../system/time-synchronization.md) erforderlich sein.

!!! warning "Nach längerer Lagerung"
    Wenn die Batteriespannung unter `3,5 V` liegt, versuche nicht, das Gerät nur über seinen USB-Anschluss wiederherzustellen. Führe das [Wiederherstellungsverfahren nach längerer Lagerung](../troubleshooting/recovery-after-storage.md) durch.

!!! danger
    Verwende das Gerät nicht ohne eingesetzte 18650-Zelle. Beachte beim Austausch unbedingt die Polarität: Eine falsche Polarität beschädigt das Gerät.
