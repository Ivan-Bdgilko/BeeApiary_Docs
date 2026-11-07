# Kalibrierung und Tarierung

!!! danger "Ein neues Gerät muss nicht kalibriert werden"
    Eine Kalibrierung ist hauptsächlich nach einer Reparatur oder dem Verlust der werkseitigen Kalibrierungsdaten erforderlich. Verwende sie nicht als allgemeines Verfahren zur Behebung eines falschen Gewichtswerts.

<span id="calibration"></span>
## Kalibrierung

1. Trenne die externe Stromversorgung.
2. Stelle alle Wägesensoren auf eine feste, ebene Fläche und lasse die Plattform leer.
3. Verbinde dich mit dem Zugangspunkt des Geräts und öffne in seiner Weboberfläche **Allgemeine Einstellungen → Waageneinstellungen**.

    ![Schaltfläche zum Öffnen der Waageneinstellungen](../../assets/de/device/calibration-and-tare/open-scale-settings.png){ .doc-screenshot }

4. Starte die **Nullpunktkalibrierung** und warte, bis sie abgeschlossen ist, ohne die Plattform zu berühren.

    Der Bildschirm zeigt zwei Kalibrierungsschritte:

    ![Schritte der Waagenkalibrierung](../../assets/de/device/calibration-and-tare/calibration-steps.png){ .doc-screenshot }

    ![Laufende Nullpunktkalibrierung](../../assets/de/device/calibration-and-tare/zero-calibration-progress.png){ .doc-screenshot }

5. Wähle ein verfügbares Referenzgewicht von 500, 1000 oder 5000 g und lege es auf die Plattform.

    ![Referenzgewicht auswählen](../../assets/de/device/calibration-and-tare/reference-weight-selection.png){ .doc-screenshot }

6. Starte die **Referenzkalibrierung** und warte auf das Ergebnis.

    ![Laufende Referenzkalibrierung](../../assets/de/device/calibration-and-tare/reference-weight-calibration-progress.png){ .doc-screenshot }

    ![Ergebnis der Waagenkalibrierung](../../assets/de/device/calibration-and-tare/calibration-result.png){ .doc-screenshot }

Ergebnis: Das Gerät hat die neuen Kalibrierwerte gespeichert. Prüfe, ob das Referenzgewicht angezeigt wird.

<span id="tare"></span>
## Tarierung

Beim Tarieren wird das Gewicht der Plattform oder einer anderen dauerhaften Konstruktion ausgeschlossen.

1. [Verbinde dich mit der Weboberfläche der Waage](../guides/configure-local-wifi.md).
2. Öffne **Allgemeine Einstellungen → Waageneinstellungen**.
3. Wähle eine Methode:

    - Ist das Taragewicht bekannt, gib es in Gramm ein und wähle **Taragewicht festlegen**.

        ![Bekanntes Taragewicht eingeben](../../assets/de/device/calibration-and-tare/known-tare-weight-form.png){ .doc-screenshot }

    - Oder lasse die Konstruktion auf den Sensoren und übernimm den aktuellen Wert als null.

        ![Aktuelles Gewicht als null übernehmen](../../assets/de/device/calibration-and-tare/use-current-weight-as-zero.png){ .doc-screenshot }

4. Prüfe anschließend den angezeigten Wert.

Ergebnis: Das Gerät zieht die Tara von den folgenden Messungen ab. Die Tarierung ändert den werkseitigen Kalibrierfaktor nicht.
