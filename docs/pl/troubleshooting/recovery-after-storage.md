# Odzyskaj urządzenie po długotrwałym przechowywaniu

Po długotrwałym przechowywaniu bateria może zostać całkowicie rozładowana, a urządzenie może nie reagować na normalne podłączenie do zasilania. Jeśli napięcie ogniwa 18650 jest niższe `3,5 В`, odzyskaj urządzenie w następującej kolejności.

!!! danger "Polaryzacja baterii"
    Przed wyjęciem akumulatora należy zlokalizować `+` i `-` oznaczenia na ogniwie i uchwycie. Zapamiętaj lub sfotografuj prawidłową orientację. Zakładanie baterii z odwróconą polaryzacją może spowodować trwałe uszkodzenie urządzenia.

1. Wyjmij baterię z urządzenia.
2. Naładuj go w osobnej ładowarce przeznaczonej na ogniwa 18650.
3. Po naładowaniu sprawdź napięcie akumulatora. Instaluj go w urządzeniu tylko wtedy, gdy napięcie jest `4,0 В` lub wyższy.
4. Zamontuj baterię, zwracając szczególną uwagę na zaznaczoną polaryzację.
5. Podłącz standardowe zewnętrzne źródło zasilania do portu USB typu C urządzenia bez szybkiego ładowania Power Delivery (PD). Użyj ładowarki z portem USB typu A i kablem USB typu A do USB typu C; nie zaleca się stosowania kabla USB Type-C na USB Type-C.
6. Po zainstalowaniu akumulatora i podłączeniu zewnętrznego źródła zasilania, [aktywuj urządzenie za pomocą klucza magnetycznego](../device/installation.md#activation-reset).
7. Zsynchronizuj czas na jeden z następujących sposobów:

    - [połącz się z punktem dostępowym urządzenia przez Wi-Fi](../guides/configure-local-wifi.md) i otwórz jego stronę główną — ta metoda jest domyślnie dostępna;
    - [skonfiguruj synchronizację Bluetooth](../guides/configure-bluetooth-sync.md), otwórz BeeApiary aplikacji i zostaw telefon w pobliżu urządzenia — ta metoda działa tylko wtedy, gdy włączone są odpowiednie ustawienia zarówno na urządzeniu, jak i w aplikacji.

8. Upewnij się, że data i godzina są prawidłowe, a znacznik czasu ostatniej synchronizacji został zaktualizowany.

Urządzenie jest gotowe do normalnej pracy po przywróceniu zasilania i czasu.

Zobacz także [Zasilanie i ładowanie](../device/power.md) i [Synchronizacja czasu](../system/time-synchronization.md).
