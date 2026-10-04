---
title: "Wagi do uli z Wi-Fi — połączenie bezpośrednie i sieciowe"
description: "Połącz BeeApiary waga do ula przez Wi-Fi: bezpośredni punkt dostępu do telefonu i zdalna transmisja przez sieć pasieczną."
---

# Wagi do uli z Wi-Fi — połączenie bezpośrednie i sieciowe { #wi-fi- }

BeeApiary wagi ula z Wi-Fi obsługują dwa sposoby odbioru danych: bezpośrednie połączenie telefoniczne z punktem dostępowym urządzenia (AP) oraz transmisję poprzez pasieczną sieć Wi-Fi (STA). Pierwsza metoda działa w pobliżu wag; drugi zapewnia zdalny dostęp do danych, gdy dostępna jest łączność z Internetem.

## Bezpośrednie połączenie z urządzeniem { #direct-access-point }

Po aktywacji kluczem magnetycznym urządzenie tymczasowo tworzy lokalny punkt dostępowy. Zwykle jest dostępny przez około jedną minutę, ale ten odstęp można zmienić w ustawieniach.

Ustawienia domyślne:

```text
SSID: apiary_net
Пароль: apiary_wifi
Вебінтерфейс: http://192.168.4.1
```

Dzięki połączeniu lokalnemu możesz:

- zezwól aplikacji na pobranie archiwum pomiarów;
- otwórz interfejs sieciowy;
- skonfiguruj numer telefonu właściciela i harmonogram;
- wyświetl poziom naładowania i wersję oprogramowania;
- użyj protokołu FTP, aby uzyskać dostęp do plików na karcie microSD.

Po podłączeniu telefonu do `apiary_net`, aplikacja znajdzie urządzenie i wyświetli monit **„Urządzenie w pobliżu. Pobrać archiwum?”**. Dane są pobierane dopiero po potwierdzeniu żądania przez użytkownika.

!!! warning "Zmień hasło"
    Domyślne hasło jest publicznie znane. Po pierwszym sprawdzeniu ustaw własne hasło o długości do 32 znaków.

Szczegółowe procedury:

- [Połącz się z punktem dostępu urządzenia](../guides/configure-local-wifi.md);
- [pobierz archiwum do aplikacji](../guides/download-archive.md);
- [przeglądaj dodatkowe ustawienia urządzenia](../device/additional-settings.md).

## Trasowanie przez pasieczną sieć Wi-Fi { #apiary-wifi-routing }

Urządzenie może połączyć się z istniejącą w pasiece siecią Wi-Fi i automatycznie przesyłać dane przez Internet do aplikacji właściciela. Telefon może znajdować się w dowolnym miejscu z dostępem do Internetu.

Ta metoda nie wymaga posiadania osobnej karty SIM w każdym urządzeniu, ale w pobliżu urządzenia musi być dostępna skonfigurowana sieć Wi-Fi z dostępem do Internetu.

### Jak działa konfiguracja

Najpierw użytkownik rejestruje w aplikacji znane mu już urządzenie. Podczas rejestracji telefon musi mieć dostęp do Internetu, ale nie musi być jeszcze podłączony do samego urządzenia. Usługa tworzy identyfikatory i klucze służące do komunikacji aplikacji z urządzeniem.

Następnie użytkownik wprowadza w aplikacji nazwę i hasło pasiecznej sieci Wi-Fi. Aplikacja przechowuje te ustawienia w telefonie, ale urządzenie jeszcze ich nie ma. Aby je przenieść, podłącz tymczasowo telefon do `apiary_net` punktu dostępowego, wróć do aplikacji i potwierdź, że przygotowane ustawienia powinny zostać zapisane na urządzeniu.

Po ponownym uruchomieniu kluczem magnetycznym lub podczas kolejnego zaplanowanego cyklu godzinowego urządzenie wykorzystuje skonfigurowaną sieć do automatycznej transmisji. Telefon nie musi już znajdować się w pobliżu.

### Wymagania

- urządzenie zostało już dodane do aplikacji;
- aplikacja przynajmniej raz otrzymała swoje dane poprzez SMS lub bezpośrednie pobranie archiwum;
- telefon ma dostęp do Internetu podczas rejestracji;
- w pobliżu urządzenia dostępna jest sieć Wi-Fi z dostępem do Internetu;
- użytkownik zna nazwę i hasło tej sieci.

Przekaźnik online nie przechowuje danych. Trwałe składowanie pozostaje lokalne w BeeApiary w pamięci wagi ula oraz w telefonie użytkownika.

Aby zapoznać się z procedurą krok po kroku, zobacz [Skonfiguruj synchronizację za pośrednictwem sieci Wi-Fi pasieki](../guides/configure-wifi-sync.md).
