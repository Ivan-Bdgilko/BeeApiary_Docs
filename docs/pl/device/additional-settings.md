# Dodatkowe ustawienia urządzenia

 **Dodatkowe ustawienia** strona należy do interfejsu sieciowego BeeApiary wagi do ula. Określa, jaki dodatkowy sprzęt jest zainstalowany i steruje poszczególnymi kanałami transmisji danych.

## Jak to otworzyć

1. [Połącz się z punktem dostępu urządzenia](../guides/configure-local-wifi.md).
2. Otwórz `http://192.168.4.1`.
3. Na stronie głównej wybierz **Dodatkowe ustawienia**.
4. Przeczytaj ostrzeżenie dotyczące interfejsu internetowego. Postępuj tylko w celu celowego sprawdzenia lub zmiany ustawień.

!!! warning "Nie zmieniaj ustawień losowo"
    Nieprawidłowa wartość może zakłócić pracę urządzenia. Włącz flagi sprzętu tylko wtedy, gdy odpowiedni sprzęt jest fizycznie zainstalowany. Nie zmieniaj niepotrzebnie ustawień sieciowych ani kluczy.

![Dodatkowe ustawienia w interfejsie internetowym programu BeeApiary wagi do ula](../../assets/uk/device/additional-settings/device-additional-settings.jpg){ .doc-screenshot }

Wartości sieciowe na zrzucie ekranu są jedynie przykładowe. Na Twoim urządzeniu będą się one różnić.

## Przełączniki

| Przedmiot | Przeznaczenie | Notatki |
|---|---|---|
| **BLE info** | Umożliwia lokalną synchronizację danych poprzez Bluetooth. | Po włączeniu skonfiguruj [Synchronizacja Bluetooth w aplikacji](../guides/configure-bluetooth-sync.md). |
| **GSM** | Umożliwia moduł GSM i transmisję danych poprzez SMS. | Wyłącz tę opcję, jeśli nie korzystasz z komunikacji GSM, np. podczas zimowego przechowywania bez transmisji danych. |
| **Synchronizacja Wi-Fi** | Umożliwia automatyczną transmisję danych poprzez zewnętrzną sieć Wi-Fi. | Zwykle włączane automatycznie, gdy aplikacja przesyła przygotowane ustawienia Wi-Fi i chmury na urządzenie. Nie włączaj go ręcznie bez poprawnych pól sieciowych. |
| **Ekran** | Informuje urządzenie, że wyświetlacz OLED jest fizycznie zainstalowany i umożliwia jego obsługę. | Włącz tylko wtedy, gdy zainstalowany jest wyświetlacz. |
| **Odwrócony** | Obraca obraz wyświetlacza OLED o 180°. | Istotne tylko wtedy, gdy **Ekran** jest włączony. |
| **Pogoda** | Włącza zainstalowany czujnik pogodowy ciśnienia, wilgotności i dodatkowej temperatury. | Włącz tylko wtedy, gdy czujnik jest zainstalowany. |
| **Zamień T1/T2** | Zamienia przesyłane wartości głównych termometrów T1 i T2. | Przydatne, jeśli czujniki wewnętrzne i zewnętrzne zostały fizycznie zamienione miejscami. Pozostaw nazwy kanałów i ustawienia w aplikacji bez zmian. |
| **Czujnik PIR** | Włącza wejście alarmowe dla czujnika PIR lub innego kompatybilnego czujnika budzenia systemu. | Włącz tylko wtedy, gdy podłączony jest czujnik. |

## Pola sieciowe

| Pole | Przeznaczenie | Notatki |
|---|---|---|
| **Sieć Wi-Fi** | Nazwa zewnętrznej sieci Wi-Fi, z którą urządzenie się połączy. | Musi dokładnie odpowiadać identyfikatorowi SSID sieci dostępnej w pobliżu urządzenia. |
| **Hasło Wi-Fi** | Hasło zewnętrznej sieci Wi-Fi. | Interfejs sieciowy maskuje wartość. |
| **Klucz STA** | Klucz do transmisji usługi uzyskany podczas rejestracji poprzez aplikację. | Nie edytuj ręcznie. |

Bezpieczniej jest ustawić parametry Wi-Fi [ustawienia synchronizacji w aplikacji](../guides/configure-wifi-sync.md). Aplikacja tworzy wymagane dane i przesyła je do urządzenia podczas bezpośredniego połączenia `apiary_net`.
