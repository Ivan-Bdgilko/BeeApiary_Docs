# Warum BeeApiary so funktioniert

## Von den BeeApiary-Entwicklern

BeeApiary wurde als eigenständiges Werkzeug entwickelt, bei dem die Daten und wesentlichen Entscheidungen unter der Kontrolle des Imkers bleiben. Diese Seite erläutert einige konstruktive und softwarebezogene Entscheidungen, die nicht sofort offensichtlich sind.

## Warum sind die Abdeckungen transparent?

Durch die transparente Abdeckung kannst du erkennen, wann das Gerät arbeitet und ob Kondenswasser, Insekten oder Schmutz in das Gehäuse gelangt sind. Dies erleichtert die Kontrolle, ohne das Gehäuse unnötig zu öffnen.

Das Projekt ist offen für Hinweise und Vorschläge: Die Konstruktion verbirgt den Zustand der wichtigsten Komponenten nicht vor dem Besitzer.

## Warum gibt es keinen verpflichtenden Serverspeicher?

Der grundlegende Betrieb der Bienenstockwaage und der App ist nicht von einem dauerhaften BeeApiary-Speicher auf einem externen Server abhängig. Messwerte werden auf der [microSD-Karte des Geräts](../system/data-storage.md) und lokal auf dem Telefon des Benutzers gespeichert. Das System erfordert keine zentrale Speicherung des Standorts oder Aktivitätsverlaufs des Besitzers.

Für die [Synchronisierung über das WLAN-Netzwerk am Bienenstand](../system/local-wifi.md#apiary-wifi-routing) kann ein optionaler Vermittlungsdienst verwendet werden. Er überträgt Daten an die App, ist jedoch kein dauerhafter Speicher und wird für die anderen Kommunikationskanäle nicht benötigt.

## Warum verwendet GSM SMS?

Im Feld oder bei einer Wanderung des Bienenstands ist SMS häufig auch dort verfügbar, wo der mobile Internetzugang unzuverlässig ist. Ein günstiger SMS-Tarif genügt, und die App empfängt die Daten ohne separates Serverabonnement.

Mit dem passenden Nachrichtenformat können zwei SMS pro Tag die Ergebnisse aller stündlichen Messungen eines ganzen Tages übertragen. Die App arbeitet direkt auf dem Telefon des Besitzers und kann in einer typischen Konfiguration bis zu fünf Geräte verwalten; bei Bedarf lässt sich diese Anzahl erhöhen.

Weitere Informationen: [GSM und SMS](../system/gsm-and-sms.md).

## Warum wird jede Stunde gemessen?

Ein stündlicher Verlauf hilft dabei, den morgendlichen Ausflug und die abendliche Rückkehr der Bienen, Gewichtsänderungen während des Trocknens von Nektar und tägliche Temperaturschwankungen zu erkennen. Diese Daten bilden eine Grundlage für die weitere Analyse der Volksstärke, der Futtervorräte und anderer Vorgänge im Bienenstock.

## Warum werden SMS nicht jede Stunde gesendet?

Eine häufige Übertragung verbessert die Messungen selbst nicht, verbraucht jedoch Akkuladung und Kommunikationsguthaben. Mehrere Nachrichten pro Tag übertragen die gesammelten stündlichen Daten wesentlich sparsamer.

Eine praktische Schätzung bei zwei SMS pro Tag liegt bei mindestens 160 Betriebstagen mit einer Akkuladung. Dies ist ein Richtwert und keine Garantie: Die Laufzeit hängt vom Akku, von der Gerätekonfiguration, der Temperatur, der GSM-Abdeckung und den aktivierten Übertragungskanälen ab.

Wenn ein Alarmsensor installiert ist, kann ein Notfallereignis oder ein Versuch, den Bienenstock zu bewegen, unabhängig vom regulären Zeitplan einen Anruf und eine SMS auslösen.

## Warum sollte der Akku nicht entfernt werden?

Das Gerät verfügt über drei Schutzstufen für den Akku und wechselt bei niedrigem Ladezustand automatisch in einen tiefen Energiesparmodus. Für die Lagerung muss der Akku nicht entfernt werden; eine falsche Polung beim erneuten Einsetzen kann die Elektronik dauerhaft beschädigen.

Ausnahmen und Regeln für die Winterlagerung findest du auf den Seiten [Stromversorgung und Laden](power.md) und [Nutzung und Lagerung im Winter](winter-use-and-storage.md).

## Warum werden Firmware-Updates nicht automatisch installiert?

Der Besitzer entscheidet selbst, wann das Gerät aktualisiert wird und ob die Funktionen einer neuen Version benötigt werden. Ein kontrolliertes Update verringert das Risiko unerwarteter Verhaltensänderungen eines autonomen Systems.

Die Bienenstockwaage kann ohne Telefon als eigenständige Waage und Wetterdatenlogger arbeiten. Die Android-App erweitert die Anzeige-, Imkereitagebuch- und Synchronisierungsfunktionen, ist für die Messungen jedoch nicht erforderlich. Anleitung: [Gerät aktualisieren](../guides/update-device.md).

## Wie lange werden Messungen gespeichert?

Das Archiv auf der microSD-Karte ist nicht auf ein Jahr begrenzt. Die Speicherdauer hängt von der Kapazität und dem Zustand der Karte ab; bei einem üblichen Messdatenumfang reicht sie für die voraussichtliche Nutzungsdauer des Geräts aus.

## Zwei SMS-Typen und ein frei einstellbarer Zeitplan. Warum?

Zu der Frage, wann, wie und wo mit den Messungen begonnen werden soll, gibt es viele Überlegungen; um dem Rechnung zu tragen, können SMS-Format und Sendezeit nach Wunsch des Benutzers frei eingestellt werden. Es gibt jedoch bestimmte Empfehlungen zur Anzahl der Nachrichten pro Tag, um Energie zu sparen.
