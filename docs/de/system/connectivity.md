---
title: "Bienenstandüberwachung über GSM, WLAN und Bluetooth"
description: "GSM, direktes WLAN, das Netzwerk am Bienenstand und Bluetooth für den Messwertempfang in BeeApiary vergleichen: Verbindungsvoraussetzungen und verfügbarer Verlauf."
---

# Bienenstandüberwachung über GSM, WLAN und Bluetooth { #daten-in-der-app-empfangen }

Zur Bienenstandüberwachung können Daten von der BeeApiary-Bienenstockwaage auf vier Wegen zur App gelangen: über GSM/SMS, eine direkte WLAN-Verbindung, das WLAN-Netzwerk am Bienenstand oder Bluetooth. Die Wahl zwischen lokaler Überwachung und Überwachung aus der Ferne hängt davon ab, wo sich das Telefon befindet und welche Verbindung in der Nähe der Waage verfügbar ist.

| Kanal | Standort des Telefons | Voraussetzungen | So gelangen die Daten zur App |
|---|---|---|---|
| [GSM und SMS](gsm-and-sms.md) | Überall mit Mobilfunkempfang | Eine SIM-Karte im Gerät mit einem einfachen SMS-Tarif; SMS-Berechtigung für die App | Die App verarbeitet kompakte SMS automatisch; mobiles Internet ist nicht nötig. [GSM einrichten](../guides/configure-gsm.md) |
| [Direkte Verbindung zum Zugangspunkt des Geräts](local-wifi.md#direct-access-point) | In der Nähe des Geräts | Das Gerät mit dem Magnetschlüssel aktivieren und innerhalb des verfügbaren Zeitfensters, gewöhnlich etwa einer Minute, eine Verbindung zu `apiary_net` herstellen; keine SIM oder Internetverbindung nötig | Die App findet das Gerät, fragt nach der Erlaubnis zum Abrufen des Archivs und importiert die Daten nach der Bestätigung. [Archiv herunterladen](../guides/download-archive.md) |
| [Weiterleitung über das WLAN-Netzwerk am Bienenstand](local-wifi.md#apiary-wifi-routing) | Überall mit Internetzugang | In der Nähe des Geräts muss ein konfiguriertes WLAN-Netzwerk mit Internetzugang verfügbar sein | Die Daten werden automatisch zur App weitergeleitet; eine eigene SIM-Karte für jedes Gerät ist nicht erforderlich. [WLAN einrichten](../guides/configure-wifi-sync.md) |
| [Bluetooth](bluetooth.md) | In der Nähe, innerhalb der Bluetooth-Reichweite | **BLE info**, BLE-Suche und Hintergrundbetrieb der App sind aktiviert; die Uhrzeit ist synchronisiert; SIM-Karte und Internet sind nicht erforderlich | Die App synchronisiert aktuelle Daten automatisch und kann den verfügbaren Verlauf wiederherstellen. [Bluetooth einrichten](../guides/configure-bluetooth-sync.md) |

## GSM und SMS

Gewöhnliche SMS lassen sich ohne App lesen; kompakte Nachrichten speichert die App als Messwerte. [SMS-Formate](gsm-and-sms.md).

## Direkte Verbindung zum Gerät

Das verbundene Telefon erhält das Archiv erst nach Bestätigung. [Mit dem Zugangspunkt verbinden](../guides/configure-local-wifi.md).

## Weiterleitung über das WLAN-Netzwerk am Bienenstand

Vor der Einrichtung muss die App mindestens einmal Daten per SMS oder direktem Archivdownload erhalten haben. Der Dienst ist kein dauerhafter Speicher; Kopien bleiben auf Waage und Telefon. Er kann instabil oder kostenpflichtig werden; prüfe [Kompatibilität und Bedingungen](../guides/configure-wifi-sync.md).

## Bluetooth

Bei aktiviertem Verlaufsabruf können Lücken bei der nächsten erfolgreichen Verbindung gefüllt werden. [Funktionsweise und Kompatibilität](bluetooth.md).

## Betrieb ohne Verbindung

Ein vorübergehender oder vollständiger Ausfall eines Kommunikationskanals unterbricht die Messungen nicht: Das Gerät zeichnet sie weiterhin auf der microSD-Karte auf. Sobald die Verbindung wiederhergestellt ist, kann die App verpasste Daten abrufen. Die verfügbare Verlaufstiefe hängt jedoch vom gewählten Kanal ab.

| Kanal | Verfügbarer Verlauf nach Wiederherstellung der Verbindung | Hinweis |
|---|---|---|
| GSM und SMS | 2 bis 12 Stunden | Abhängig vom konfigurierten Zeitplan für den SMS-Versand |
| Direkte Verbindung zum Zugangspunkt des Geräts | Bis zu 1 Jahr | Die Daten können heruntergeladen werden, wenn die entsprechenden Einträge im lokalen Archiv vorhanden sind |
| Bluetooth | 1 Tag bis 1 Woche | Abhängig von der Einstellung zum Abrufen des Verlaufs und den verfügbaren Einträgen |
| Weiterleitung über das WLAN-Netzwerk am Bienenstand | Verlauf nicht verfügbar | Der Online-Übertragungsdienst leitet aktuelle Daten weiter, speichert sie aber nicht auf dem Server |

Diese Grenzen gelten nur für die Menge verpasster Daten, die über einen bestimmten Kanal wiederhergestellt werden kann. Das lokale [microSD-Archiv](data-storage.md) ist nicht auf ein Jahr Speicherzeit begrenzt: Seine Tiefe wird nur durch die Kartenkapazität bestimmt, die für die gesamte erwartete Nutzungsdauer des Geräts ausreicht. Bei Bedarf können die Daten auch direkt von der microSD-Karte gelesen werden.
