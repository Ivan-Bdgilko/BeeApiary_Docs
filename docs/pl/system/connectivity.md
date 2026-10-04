---
title: "Monitoring pasieki przez GSM, Wi-Fi i Bluetooth"
description: "Porównaj GSM, bezpośrednie Wi-Fi, sieć pasieczną i Bluetooth do odbierania pomiarów BeeApiary: wymagania dotyczące połączenia i dostępna historia."
---

# Monitoring pasieki przez GSM, Wi-Fi i Bluetooth { #_1 }

Do monitorowania pasieki wykorzystuje się dane z BeeApiary Waga ula może połączyć się z aplikacją na cztery sposoby: poprzez GSM/SMS, bezpośrednie połączenie Wi-Fi, pasieczną sieć Wi-Fi lub Bluetooth. Wybór pomiędzy monitorowaniem lokalnym a zdalnym zależy od lokalizacji telefonu i dostępnego połączenia w pobliżu wagi.

| Kanał | Lokalizacja telefonu | Wymagania | Jak dane docierają do aplikacji |
|---|---|---|---|
| [GSM i SMS-y](gsm-and-sms.md) | Wszędzie z zasięgiem komórkowym | Karta SIM w urządzeniu z podstawowym planem SMS | Aplikacja automatycznie przetwarza wiadomości SMS; Internet mobilny nie jest wymagany |
| [Bezpośrednie połączenie z punktem dostępowym urządzenia](local-wifi.md#direct-access-point) | W pobliżu urządzenia | Aktywuj urządzenie kluczem magnetycznym i połącz się z `apiary_net` w dostępnym przedziale czasu, zwykle około jednej minuty | Aplikacja odnajduje urządzenie, prosi o pozwolenie na pobranie archiwum i po potwierdzeniu importuje dane |
| [Trasowanie poprzez pasieczną sieć Wi-Fi](local-wifi.md#apiary-wifi-routing) | Wszędzie tam, gdzie jest dostęp do Internetu | W pobliżu urządzenia musi być dostępna skonfigurowana sieć Wi-Fi z dostępem do Internetu | Dane są automatycznie kierowane do aplikacji; nie jest wymagana osobna karta SIM dla każdego urządzenia |
| [Bluetooth](bluetooth.md) | W pobliżu, w zasięgu Bluetooth | **BLE info**, skanowanie BLE i działanie aplikacji w tle są włączone; czas jest zsynchronizowany; nie jest wymagana karta SIM ani Internet | Aplikacja automatycznie synchronizuje aktualne dane i może przywrócić dostępną historię |

## GSM i SMS-y

Urządzenie wysyła zwykłe lub skompresowane wiadomości SMS bez mobilnego Internetu. Aplikacja rozpoznaje skompresowane wiadomości i automatycznie dodaje pomiary do lokalnej pamięci telefonu.

## Bezpośrednie połączenie z urządzeniem

Po aktywacji kluczem magnetycznym urządzenie tymczasowo tworzy `apiary_net` punkt dostępu. Podłączony do niego telefon nie potrzebuje karty SIM ani dostępu do Internetu. Aplikacja automatycznie wyszukuje urządzenie, ale pobiera archiwum dopiero po potwierdzeniu żądania przez użytkownika.

Szczegółowa procedura, patrz [Pobierz archiwum](../guides/download-archive.md).

## Trasowanie przez pasieczną sieć Wi-Fi

Urządzenie może korzystać z istniejącej sieci Wi-Fi z dostępem do Internetu na terenie pasieki. Właściciel otrzymuje dane zdalnie w aplikacji bez konieczności posiadania osobnej karty SIM dla każdego urządzenia.

Przed wstępną konfiguracją aplikacja musi co najmniej raz odebrać dane z urządzenia za pośrednictwem wiadomości SMS lub bezpośredniego pobrania archiwum. Rejestracja odbywa się na telefonie z dostępem do Internetu, a przygotowane ustawienia Wi-Fi i chmury są następnie przesyłane za jego pośrednictwem na urządzenie `apiary_net` punkt dostępu.

Przekaźnik online nie przechowuje danych. Stałe kopie pozostają w BeeApiary w pamięci wagi ula oraz w telefonie użytkownika.

Szczegółowa procedura, patrz [Skonfiguruj synchronizację za pośrednictwem sieci Wi-Fi pasieki](../guides/configure-wifi-sync.md).

## Bluetooth

Gdy telefon znajdzie się w zasięgu Bluetooth, aplikacja automatycznie synchronizuje dostępne dane. Nie wymaga to karty SIM, mobilnego Internetu ani aktywacji `apiary_net` punkt dostępu. Gdy włączone jest pobieranie historii, tymczasowe luki mogą zostać uzupełnione podczas następnego pomyślnego połączenia.

Aby uzyskać wyjaśnienie, zobacz [Synchronizacja danych Bluetooth](bluetooth.md). Aby zapoznać się z praktyczną procedurą, zob [Skonfiguruj synchronizację Bluetooth](../guides/configure-bluetooth-sync.md).

## Działanie bez połączenia

Tymczasowa lub całkowita utrata dowolnego kanału komunikacyjnego nie wstrzymuje pomiarów: urządzenie kontynuuje ich zapis na karcie microSD. Po przywróceniu połączenia aplikacja może odzyskać utracone dane, ale dostępna głębokość historii zależy od wybranego kanału.

| Kanał | Historia dostępna po przywróceniu połączenia | Uwaga |
|---|---|---|
| GSM i SMS-y | 2 do 12 godzin | Zależy od skonfigurowanego harmonogramu transmisji SMS |
| Bezpośrednie połączenie z punktem dostępowym urządzenia | Do 1 roku | Dane można pobrać, jeśli w lokalnym archiwum znajdują się odpowiednie rekordy |
| Bluetooth | 1 dzień do 1 tygodnia | Zależy od ustawień pobierania historii i dostępnych rekordów |
| Trasowanie poprzez pasieczną sieć Wi-Fi | Historia jest niedostępna | Przekaźnik online przesyła aktualne dane, ale nie przechowuje ich na serwerze |

Limity te dotyczą jedynie ilości utraconych danych, które można odtworzyć za pomocą określonego kanału. Lokalny [archiwum microSD](data-storage.md) nie posiada rocznego limitu przechowywania: jego głębokość ograniczona jest jedynie pojemnością karty, która wystarcza na cały przewidywany okres użytkowania urządzenia. W razie potrzeby dane można także odczytać bezpośrednio z karty microSD.
