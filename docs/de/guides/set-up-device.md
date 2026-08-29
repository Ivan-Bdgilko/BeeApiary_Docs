# So richtest du ein neues BeeApiary-Messgerät ein

1. Lade das Gerät über USB Type-C.

    !!! note "Ladegerät und Kabel auswählen"
        Das Gerät unterstützt kein Schnellladen, einschließlich USB Power Delivery (PD). Verwende eine normale Stromquelle mit einem USB-Type-A-Anschluss und ein USB-Type-A–USB-Type-C-Kabel. Ein USB-Type-C–USB-Type-C-Kabel wird zum Laden nicht empfohlen.

2. Installiere das Gerät und die Sensoren gemäß den [Hinweisen zur Platzierung](../device/placement.md).
3. Setze eine micro-SIM mit deaktivierter PIN-Abfrage ein.

    Verwende das Format micro-SIM:

    ![Vergleich der SIM-Kartenformate](../../assets/de/quick-start/gsm/micro-sim-format-comparison.png){ .doc-photo }

    Richtig eingesetzte Karte:

    ![Richtig eingesetzte micro-SIM](../../assets/common/device/installation/micro-sim-insertion-orientation.jpeg){ .doc-photo }

    Setze die SIM-Karte ein und drücke sie vorsichtig fast vollständig in den Steckplatz, bis ein leises Klicken bestätigt, dass sie eingerastet ist:

    ![Im Steckplatz eingerastete micro-SIM](../../assets/common/device/installation/micro-sim-locked-in-slot.jpeg){ .doc-photo }

4. Aktiviere das Gerät oder starte es neu: Halte den Magnetschlüssel kurz an die Markenkennzeichnung auf der Rückseite der Haupteinheit.

    ![BeeApiary-Magnetschlüssel](../../assets/common/device/installation/magnetic-key.png){ .doc-photo }

    ![Markierter Bereich für den Magnetschlüssel](../../assets/common/device/installation/magnetic-key-target.png){ .doc-photo }

    Weitere Informationen findest du unter [Aktivierung und Neustart](../device/installation.md#activation-reset).

5. Verbinde dich mit `apiary_net` und öffne `http://192.168.4.1`.
6. Gib die Telefonnummer des Besitzers im internationalen Format ein.
7. Trenne die Verbindung zu `apiary_net` und prüfe die erste SMS-Nachricht.

Ergebnis: Das Gerät erfasst Messwerte, sendet sie an den Besitzer und speichert ein Archiv.
