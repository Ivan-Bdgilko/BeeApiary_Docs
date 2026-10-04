---
title: "Jak dane z ula trafiają do telefonu"
description: "Jak BeeApiary mierzy, przechowuje i przesyła dane dotyczące ula do telefonu w celu przeglądania bieżących odczytów, historii i wykresów."
---

# Jak dane z ula trafiają do telefonu { #_1 }

BeeApiary monitoring ula obejmuje pomiary, lokalne przechowywanie i transmisję danych do aplikacji. Poniższe kroki pokazują ścieżkę od pomiaru na urządzeniu do bieżących odczytów, historii i wykresów w telefonie.

1. Na początku każdej godziny, BeeApiary Wagi do ula wykonują skonfigurowane pomiary.
2. Wynik jest zapisywany w lokalnym archiwum microSD, jeśli karta jest dostępna.
3. Urządzenie udostępnia dane przez skonfigurowany kanał:

    - wysyła wiadomość SMS zwykłą lub kompaktową zgodnie z harmonogramem;
    - kieruje dane przez pasieczną sieć Wi-Fi;
    - [przesyła dostępne dane przez Bluetooth](bluetooth.md) gdy telefon jest w pobliżu;
    - udostępnia archiwum aplikacji za pośrednictwem własnego punktu dostępu po potwierdzeniu przez użytkownika.

4. Aplikacja rozpoznaje otrzymane wartości i dodaje je do lokalnej pamięci telefonu.
5. Użytkownik przegląda aktualne wartości, historię i wykresy.

Brak sieci GSM, Wi-Fi, Bluetooth lub pobliskiego telefonu nie wstrzymuje procesu pomiaru rdzenia. Dane można przesłać do aplikacji, gdy połączenie stanie się dostępne.

Gdy dane są przesyłane zdalnie przez Wi-Fi, przekaźnik online ich nie przechowuje. Stałe kopie pozostają w BeeApiary w pamięci wagi ula oraz w telefonie użytkownika.

Aby zapoznać się z porównaniem kanałów, zobacz [Odbieranie danych w aplikacji](connectivity.md).

Aby skonfigurować kanał zdalny, zobacz [Synchronizacja poprzez pasieczną sieć Wi-Fi](../guides/configure-wifi-sync.md).

Aby skonfigurować lokalny kanał automatyczny, patrz [Synchronizacja Bluetooth](../guides/configure-bluetooth-sync.md).
