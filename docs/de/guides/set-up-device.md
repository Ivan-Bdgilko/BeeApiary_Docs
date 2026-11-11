# So richtest du die BeeApiary-Bienenstockwaage ein

1. Lade das Gerät über USB Type-C.

    !!! note "Ladegerät und Kabel auswählen"
        Das Gerät unterstützt kein Schnellladen, einschließlich USB Power Delivery (PD). Verwende eine normale Stromquelle mit einem USB-Type-A-Anschluss und ein USB-Type-A–USB-Type-C-Kabel. Ein USB-Type-C–USB-Type-C-Kabel wird zum Laden nicht empfohlen.

2. Installiere das Gerät und die Sensoren gemäß den [Hinweisen zur Platzierung](../device/placement.md).
3. Setze eine micro-SIM mit deaktivierter PIN-Abfrage ein.

    Verwende das Format micro-SIM:

    ![Vergleich der SIM-Kartenformate](../../assets/de/quick-start/gsm/micro-sim-format-comparison.png){ .doc-photo }

    Richtig eingesetzte Karte:

    Das GSM-Modul befindet sich bei älteren Platinen vor 2026 und neueren Platinen ab 2026 an unterschiedlichen Stellen.

    **Ältere Platine (vor 2026):**

    ![Richtig eingesetzte micro-SIM](../../assets/common/device/installation/micro-sim-insertion-orientation.jpeg){ .doc-photo }

    **Neuere Platine (ab 2026):**

    ![Ausrichtung der micro-SIM auf der neueren Platine](../../assets/common/device/installation/micro-sim-new-board-orientation.png){ .doc-photo }

    Setze die SIM-Karte ein und drücke sie vorsichtig fast vollständig in den Steckplatz, bis ein leises Klicken bestätigt, dass sie eingerastet ist:

    **Ältere Platine (vor 2026):**

    ![Im Steckplatz eingerastete micro-SIM](../../assets/common/device/installation/micro-sim-locked-in-slot.jpeg){ .doc-photo }

    **Neuere Platine (ab 2026):**

    ![Eingerastete micro-SIM auf der neueren Platine](../../assets/common/device/installation/micro-sim-new-board-locked.png){ .doc-photo }

4. <span id="activation-reset"></span>Aktiviere das Gerät oder starte es neu: Halte den Magnetschlüssel kurz an die Markenkennzeichnung auf der Rückseite der Haupteinheit.

    ![BeeApiary-Magnetschlüssel](../../assets/common/device/installation/magnetic-key.png){ .doc-photo }

    ![Markierter Bereich für den Magnetschlüssel](../../assets/common/device/installation/magnetic-key-target.png){ .doc-photo }

5. Wenn du Einstellungen prüfen oder ändern möchtest, [verbinde dich mit `apiary_net`](configure-local-wifi.md) und öffne `http://192.168.4.1`. Andernfalls kannst du diesen Schritt überspringen.
6. Die Nummer des Besitzers ist normalerweise vom Hersteller eingerichtet. Nur bei Bedarf kannst du sie in den [GSM-Einstellungen prüfen, ändern oder entfernen](configure-gsm.md).
7. Falls du mit `apiary_net` verbunden warst, trenne die Verbindung. Warte auf die erste SMS: Sie kommt normalerweise vor dem Einschlafen des Geräts, etwa eine Minute nach dem Trennen oder Aktivieren.

    Nach Änderungen an der Übertragung, Kalibrierung oder anderen Einstellungen kann es nötig sein, das Einschlafen abzuwarten und das Gerät erneut mit dem Magnetschlüssel zu aktivieren, ohne dich erneut mit `apiary_net` zu verbinden.

Ergebnis: Das Gerät erfasst Messwerte, sendet sie an den Besitzer und speichert ein Archiv.
