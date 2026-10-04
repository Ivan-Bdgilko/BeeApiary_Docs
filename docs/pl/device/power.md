# Zasilanie i ładowanie

Urządzenie jest zasilane z jednego lub dwóch ogniw 18650 i ładowane przez USB Type-C. Źródłem zasilania może być ładowarka, power bank lub opcjonalny panel słoneczny.

!!! note "Wybór ładowarki i kabla"
    Urządzenie nie obsługuje szybkiego ładowania, w tym USB Power Delivery (PD). Użyj standardowego źródła zasilania z portem USB Type-A i kabla USB Type-A–USB Type-C. Kabel USB Type-C–USB Type-C nie jest zalecany do ładowania.

![Otwórz port zasilania USB typu C](../../assets/common/device/power/open-usb-type-c-port.jpeg){ .doc-photo }

Po naładowaniu zamknij osłonę portu ochronnego:

![Zamknięta osłona ochronna nad portem zasilania](../../assets/common/device/power/closed-usb-type-c-cover.jpeg){ .doc-photo }

- niebieski wskaźnik pozostaje zapalony, gdy akumulator jest w pełni naładowany, a zasilanie zewnętrzne jest nadal podłączone;
- poziom naładowania widoczny jest w wiadomościach SMS oraz w ogólnych ustawieniach interfejsu internetowego;

  ![Ładowanie baterii w interfejsie internetowym](../../assets/en/device/power/battery-charge-status.png){ .doc-screenshot }

- poniżej 20% urządzenie przechodzi w tryb oszczędzania energii, przerywa regularne pomiary i wysyłanie wiadomości SMS oraz okresowo sprawdza poziom naładowania;
- po krytycznym rozładowaniu akumulator odłącza się automatycznie i [synchronizacja czasu](../system/time-synchronization.md) może być wymagane po naładowaniu.

!!! warning "Po długotrwałym przechowywaniu"
    Jeśli napięcie akumulatora jest niższe `3,5 В`, nie próbuj przywracać urządzenia, korzystając wyłącznie z jego portu USB. Postępuj zgodnie z [procedura odzyskiwania po długotrwałym przechowywaniu](../troubleshooting/recovery-after-storage.md).

!!! danger
    Nie używaj urządzenia bez zainstalowanego ogniwa 18650. Podczas wymiany należy ściśle przestrzegać polaryzacji: niewłaściwa polaryzacja spowoduje uszkodzenie urządzenia.
