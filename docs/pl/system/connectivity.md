---
title: "Monitoring pasieki przez GSM, Wi-Fi i Bluetooth"
description: "Porównaj GSM, bezpośrednie Wi-Fi, sieć pasieczną i Bluetooth do odbierania pomiarów BeeApiary: wymagania dotyczące połączenia i dostępna historia."
---

# Monitoring pasieki przez GSM, Wi-Fi i Bluetooth { #_1 }

Do monitorowania pasieki wykorzystuje się dane z BeeApiary Waga ula może połączyć się z aplikacją na cztery sposoby: poprzez GSM/SMS, bezpośrednie połączenie Wi-Fi, pasieczną sieć Wi-Fi lub Bluetooth. Wybór pomiędzy monitorowaniem lokalnym a zdalnym zależy od lokalizacji telefonu i dostępnego połączenia w pobliżu wagi.

| Kanał | Lokalizacja telefonu | Wymagania | Jak dane docierają do aplikacji |
|---|---|---|---|
| [GSM i SMS-y](gsm-and-sms.md) | Wszędzie z zasięgiem komórkowym | Karta SIM w urządzeniu z podstawowym planem SMS; uprawnienie aplikacji do SMS | Aplikacja automatycznie przetwarza skompresowane SMS-y; Internet mobilny nie jest potrzebny. [Skonfiguruj GSM](../guides/configure-gsm.md) |
| [Bezpośrednie połączenie z punktem dostępowym urządzenia](local-wifi.md#direct-access-point) | W pobliżu urządzenia | Aktywuj urządzenie kluczem magnetycznym i połącz się z `apiary_net` w dostępnym przedziale czasu, zwykle około jednej minuty; karta SIM i Internet nie są potrzebne | Aplikacja odnajduje urządzenie, prosi o pozwolenie na pobranie archiwum i po potwierdzeniu importuje dane. [Pobierz archiwum](../guides/download-archive.md) |
| [Trasowanie poprzez pasieczną sieć Wi-Fi](local-wifi.md#apiary-wifi-routing) | Wszędzie tam, gdzie jest dostęp do Internetu | W pobliżu urządzenia musi być dostępna skonfigurowana sieć Wi-Fi z dostępem do Internetu | Dane są automatycznie kierowane do aplikacji; nie jest wymagana osobna karta SIM dla każdego urządzenia. [Skonfiguruj Wi-Fi](../guides/configure-wifi-sync.md) |
| [Bluetooth](bluetooth.md) | W pobliżu, w zasięgu Bluetooth | **BLE info**, skanowanie BLE i działanie aplikacji w tle są włączone; czas jest zsynchronizowany; nie jest wymagana karta SIM ani Internet | Aplikacja automatycznie synchronizuje aktualne dane i może przywrócić dostępną historię. [Skonfiguruj Bluetooth](../guides/configure-bluetooth-sync.md) |

## GSM i SMS-y

Zwykłe SMS-y można czytać bez aplikacji; aplikacja zapisuje wiadomości skompresowane jako pomiary. [Formaty SMS](gsm-and-sms.md).

## Bezpośrednie połączenie z urządzeniem

Połączony telefon otrzymuje archiwum dopiero po potwierdzeniu. [Połącz z punktem dostępowym](../guides/configure-local-wifi.md).

## Trasowanie przez pasieczną sieć Wi-Fi

Przed konfiguracją aplikacja musi co najmniej raz otrzymać dane przez SMS lub bezpośrednie pobranie archiwum. Usługa nie jest trwałym magazynem: kopie pozostają na wadze i telefonie. Może działać niestabilnie lub stać się płatna; sprawdź [zgodność i warunki](../guides/configure-wifi-sync.md).

## Bluetooth

Po włączeniu pobierania historii luki mogą zostać uzupełnione przy kolejnym połączeniu. [Zasada działania i zgodność](bluetooth.md).

## Działanie bez połączenia

Tymczasowa lub całkowita utrata dowolnego kanału komunikacyjnego nie wstrzymuje pomiarów: urządzenie kontynuuje ich zapis na karcie microSD. Po przywróceniu połączenia aplikacja może odzyskać utracone dane, ale dostępna głębokość historii zależy od wybranego kanału.

| Kanał | Historia dostępna po przywróceniu połączenia | Uwaga |
|---|---|---|
| GSM i SMS-y | 2 do 12 godzin | Zależy od skonfigurowanego harmonogramu transmisji SMS |
| Bezpośrednie połączenie z punktem dostępowym urządzenia | Do 1 roku | Dane można pobrać, jeśli w lokalnym archiwum znajdują się odpowiednie rekordy |
| Bluetooth | 1 dzień do 1 tygodnia | Zależy od ustawień pobierania historii i dostępnych rekordów |
| Trasowanie poprzez pasieczną sieć Wi-Fi | Historia jest niedostępna | Przekaźnik online przesyła aktualne dane, ale nie przechowuje ich na serwerze |

Limity te dotyczą jedynie ilości utraconych danych, które można odtworzyć za pomocą określonego kanału. Lokalny [archiwum microSD](data-storage.md) nie posiada rocznego limitu przechowywania: jego głębokość ograniczona jest jedynie pojemnością karty, która wystarcza na cały przewidywany okres użytkowania urządzenia. W razie potrzeby dane można także odczytać bezpośrednio z karty microSD.
