# WLAN-Verbindung des Geräts

Das BeeApiary-Messgerät unterstützt sowohl die direkte Verbindung eines Telefons mit seinem eigenen Zugangspunkt als auch die entfernte Übertragung über ein vorhandenes WLAN-Netzwerk am Bienenstand.

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
- [zusätzliche Geräteeinstellungen anzeigen](additional-settings.md).

## Weiterleitung über das WLAN-Netzwerk am Bienenstand { #apiary-wifi-routing }

Das Gerät kann sich mit einem vorhandenen WLAN-Netzwerk am Bienenstand verbinden und Daten automatisch über das Internet an die App des Besitzers senden. Das Telefon kann sich überall befinden, wo es Internetzugang hat.

Für diese Methode ist keine eigene SIM-Karte in jedem Gerät erforderlich. In der Nähe des Geräts müssen jedoch ein konfiguriertes WLAN-Netzwerk und Internetzugang verfügbar sein.

### So funktioniert die Einrichtung

Zuerst registriert der Benutzer in der App ein Gerät, das der App bereits bekannt ist. Während der Registrierung muss das Telefon Internetzugang haben, muss aber noch nicht mit dem Gerät selbst verbunden sein. Der Dienst erstellt Kennungen und Schlüssel für die Kommunikation zwischen App und Gerät.

Anschließend gibt der Benutzer in der App den Namen und das Passwort des WLAN-Netzwerks am Bienenstand ein. Die App speichert diese Einstellungen auf dem Telefon, das Gerät besitzt sie aber noch nicht. Um sie zu übertragen, verbinde das Telefon vorübergehend mit dem Zugangspunkt `apiary_net`, kehre zur App zurück und bestätige, dass die vorbereiteten Einstellungen auf das Gerät geschrieben werden sollen.

Nach einem Neustart mit dem Magnetschlüssel oder im nächsten geplanten stündlichen Zyklus verwendet das Gerät das festgelegte Netzwerk für die automatische Übertragung. Das Telefon muss sich danach nicht mehr in der Nähe befinden.

### Voraussetzungen

- Das Gerät wurde bereits zur App hinzugefügt.
- Die App hat mindestens einmal Daten über SMS oder durch direktes Herunterladen des Archivs empfangen.
- Das Telefon hat während der Registrierung Internetzugang.
- In der Nähe des Geräts ist ein WLAN-Netzwerk mit Internetzugang verfügbar.
- Der Benutzer kennt den Namen und das Passwort dieses Netzwerks.

Der Online-Übertragungsdienst speichert keine Daten. Die dauerhafte Speicherung erfolgt lokal auf dem Messgerät und auf dem Telefon des Benutzers.

Das schrittweise Verfahren findest du unter [Synchronisierung über das WLAN-Netzwerk am Bienenstand einrichten](../guides/configure-wifi-sync.md).
