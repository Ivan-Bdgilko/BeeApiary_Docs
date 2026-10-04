# Jak skonfigurować synchronizację Bluetooth

!!! danger "Kompatybilność urządzenia"
    Ta funkcja jest obsługiwana tylko przez urządzenia wyprodukowane po sierpniu 2026 roku. Urządzenia wyprodukowane wcześniej również mogą zyskać tę funkcjonalność, ale muszą zostać zaktualizowane fabrycznie. Obecnie nie ma prostej łatki, którą można zainstalować samodzielnie.

Ta procedura konfiguruje automatyczne pobieranie danych z BeeApiary waga do ważenia ula, gdy telefon jest w pobliżu. Synchronizacja nie wymaga karty SIM ani dostępu do Internetu.

## Zanim zaczniesz

1. Upewnij się, że waga spełnia powyższe wymagania dotyczące kompatybilności.
2. [Zsynchronizować zegar wagi](../system/time-synchronization.md) z telefonem. Różnica nie może przekraczać dwóch minut.
3. Włącz Bluetooth w telefonie.
4. Przyznaj aplikacji wszystkie wymagane uprawnienia, w tym uprawnienia Bluetooth.
5. Pozwól aplikacji działać w tle i obudź się o wymaganej godzinie. Przejrzyj bieżący [zalecenia dotyczące instalacji aplikacji](../app/installation.md).

!!! warning "Sprawdź czas przed konfiguracją"
    Jeśli różnica przekracza dwie minuty, waga może stać się dostępna przed lub po rozpoczęciu nasłuchiwania telefonu, uniemożliwiając automatyczną synchronizację.

## Włącz informację BLE na wadze

1. [Połącz się z punktem dostępowym wagi](configure-local-wifi.md).
2. Otwórz `http://192.168.4.1` i wybierz **Dodatkowe ustawienia**.
3. Wybierz **BLE info** i zapisz zmiany.

Ta opcja i inne przełączniki zostały wyjaśnione poniżej [Dodatkowe ustawienia urządzenia](../device/additional-settings.md).

## Włącz synchronizację w aplikacji

4. Otwórz menu główne aplikacji, przejdź do **Ustawienia**i otwarty **Dodatkowe ustawienia**.
5. Włącz **Wyszukaj urządzenia BLE** dzięki czemu aplikacja może znaleźć pobliskie wagi i odebrać pomiary.
6. Włącz **Historia BLE** dzięki czemu aplikacja pobiera również zapisaną historię, w tym dane z poprzedniego dnia.

    ![Opcje Bluetooth w dodatkowych ustawieniach aplikacji BeeApiary Aplikacja na Androida](../../assets/en/app/additional-settings/app-additional-settings.jpg){ .doc-screenshot }

    !!! warning "Włącz wymagane opcje"
        Zrzut ekranu jest przykładem ogólnym, więc oba przełączniki Bluetooth są pokazane jako wyłączone. **Wyszukaj urządzenia BLE** musi być włączona do synchronizacji. Włączanie **Historia BLE** jest również zalecane, aby aplikacja mogła pobrać dostępną historię i przywrócić utracone pomiary.

    Pełny opis tego ekranu można znaleźć w sekcji [Dodatkowe ustawienia aplikacji](../app/additional-settings.md).

7. Wróć do ekranu głównego aplikacji. Utrzymuj funkcję Bluetooth włączoną i telefon w niezawodnym zasięgu Bluetooth przez następny cykl godzinowy.

## Sprawdź wynik

Synchronizacja następuje tylko wtedy, gdy **BLE info** jest włączona na wadze, a w telefonie włączone są Bluetooth i odpowiednie opcje aplikacji. Waga staje się dostępna do komunikacji podczas zaplanowanego przebudzenia lub po nim [aktywacja za pomocą klucza magnetycznego](../device/installation.md#activation-reset).

Aplikacja może wymieniać dane, gdy jest otwarta lub w tle, jeśli Android pozwala na jej uruchomienie i wybudzenie w wymaganym czasie.

8. Poczekaj na wiadomość potwierdzającą odebranie danych.

    ![Wynik odbioru pomiarów przez Bluetooth w BeeApiary aplikacja](../../assets/en/system/bluetooth/bluetooth-sync-result.jpg){ .doc-screenshot }

    To okno pokazuje:

    - nazwę ula i numer wagi;
    - najnowszy dostępny zestaw pomiarów do konfiguracji wag;
    - data i godzina otrzymanego pomiaru;
    - czas i wynik synchronizacji zegara.

    Podczas łączenia się z wagą, która nie została jeszcze zarejestrowana, an **Dodaj urządzenie** może również pojawić się przycisk . Użyj go, aby ukończyć standard [procedura dodawania BeeApiary wagi do ula](../app/add-device.md) raz. Aplikacja rozpozna je wówczas automatycznie.

9. Kliknij **OK**. W razie potrzeby otwórz ponownie najnowszą wiadomość **BLE Info** w menu głównym.
10. Upewnij się, że nowe wartości pojawiają się na ekranie głównym aplikacji i na wykresach.

Gotowe: gdy telefon jest w pobliżu, aplikacja automatycznie pobierze dostępne dane. Jeśli połączenie było niedostępne przez kilka godzin, włącz **Historia BLE** może przywrócić utracone pomiary podczas kolejnej udanej synchronizacji, w ramach dostępnej głębokości historii od jednego dnia do jednego tygodnia.

Więcej informacji o tym, jak to działa, można znaleźć w artykule [Synchronizacja danych Bluetooth](../system/bluetooth.md).
