---
title: "Bienenstockwaage mit WLAN — direkte und Netzwerkverbindung"
description: "BeeApiary-Bienenstockwaage über WLAN verbinden: direkter Zugangspunkt für das Telefon und entfernte Übertragung über das Netzwerk am Bienenstand."
---

# Bienenstockwaage mit WLAN — direkte und Netzwerkverbindung { #wlan-verbindung-des-gerats }

Die BeeApiary-Bienenstockwaage mit WLAN unterstützt zwei Wege zum Datenempfang: die direkte Verbindung des Telefons mit dem Zugangspunkt des Geräts (AP) und die Übertragung über das WLAN-Netzwerk am Bienenstand (STA). Die erste Methode funktioniert in der Nähe der Waage; die zweite ermöglicht den Datenzugriff aus der Ferne, wenn Internetzugang verfügbar ist.

## Direkte Verbindung zum Gerät { #direct-access-point }

Nach der Aktivierung mit dem Magnetschlüssel erstellt das Gerät vorübergehend einen lokalen Zugangspunkt. Er ist gewöhnlich etwa eine Minute lang verfügbar; dieses Zeitfenster kann jedoch in den Einstellungen geändert werden.

Standardeinstellungen:

```text
SSID: apiary_net
Passwort: apiary_wifi
Weboberfläche: http://192.168.4.1
```

Über die lokale Verbindung kannst du:

- der App erlauben, das Messwertarchiv abzurufen;
- die Weboberfläche öffnen;
- die Telefonnummer des Besitzers und den Zeitplan konfigurieren;
- Ladezustand und Firmware-Version anzeigen;
- per FTP auf Dateien der microSD-Karte zugreifen.

Nachdem das Telefon mit `apiary_net` verbunden ist, findet die App das Gerät und zeigt die Abfrage **„Gerät in der Nähe. Archiv abrufen?“** an. Die Daten werden erst nach Bestätigung durch den Benutzer heruntergeladen.

!!! warning "Passwort ändern"
    Das Standardpasswort ist allgemein bekannt. Lege nach der ersten Prüfung ein eigenes Passwort mit höchstens 32 Zeichen fest.

Ausführliche Anleitungen:

- [Mit dem Zugangspunkt des Geräts verbinden](../guides/configure-local-wifi.md);
- [Archiv in die App herunterladen](../guides/download-archive.md);
- [zusätzliche Geräteeinstellungen anzeigen](../device/additional-settings.md).

## Weiterleitung über das WLAN-Netzwerk am Bienenstand { #apiary-wifi-routing }

Das Gerät kann sich mit einem vorhandenen WLAN-Netzwerk am Bienenstand verbinden und Daten automatisch über das Internet an die App des Besitzers senden. Das Telefon kann sich überall befinden, wo es Internetzugang hat.

Für diese Methode ist keine eigene SIM-Karte in jedem Gerät erforderlich. In der Nähe des Geräts müssen jedoch ein konfiguriertes WLAN-Netzwerk und Internetzugang verfügbar sein.

### So funktioniert die Einrichtung

Registriere ein der App bereits bekanntes Gerät; der Dienst erstellt Kennungen und Schlüssel. Übertrage anschließend die WLAN-Einstellungen vom Telefon über den Zugangspunkt `apiary_net` des Geräts.

Nach einem Neustart mit dem Magnetschlüssel oder im nächsten geplanten stündlichen Zyklus verwendet das Gerät das festgelegte Netzwerk für die automatische Übertragung. Das Telefon muss sich danach nicht mehr in der Nähe befinden.

### Voraussetzungen

- Das Gerät wurde bereits zur App hinzugefügt.
- Die App hat mindestens einmal Daten über SMS oder durch direktes Herunterladen des Archivs empfangen.
- Das Telefon hat während der Registrierung Internetzugang.
- In der Nähe des Geräts ist ein WLAN-Netzwerk mit Internetzugang verfügbar.
- Der Benutzer kennt den Namen und das Passwort dieses Netzwerks.

Der Online-Dienst ist kein dauerhafter Speicher: Die Daten bleiben auf Waage und Telefon. Der Dienst kann instabil oder kostenpflichtig werden; Gerätekompatibilität und weitere Bedingungen stehen in der Anleitung.

Das schrittweise Verfahren findest du unter [Synchronisierung über das WLAN-Netzwerk am Bienenstand einrichten](../guides/configure-wifi-sync.md).
