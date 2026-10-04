# Jak skonfigurować nową wagę pasieczną BeeApiary

1. Naładuj urządzenie przez USB typu C.

    !!! note "Wybór ładowarki i kabla"
        Urządzenie nie obsługuje szybkiego ładowania, w tym USB Power Delivery (PD). Użyj standardowego źródła zasilania z portem USB Type-A i kabla USB Type-A–USB Type-C. Kabel USB Type-C–USB Type-C nie jest zalecany do ładowania.

2. Zamontować urządzenie i czujniki zgodnie z pkt [wytyczne dotyczące rozmieszczenia](../device/placement.md).
3. Włóż kartę micro-SIM z wyłączoną ochroną PIN.

    Użyj formatu micro-SIM:

    ![Porównanie formatów kart SIM](../../assets/en/quick-start/gsm/micro-sim-format-comparison.png){ .doc-photo }

    Poprawnie zainstalowana karta:

    ![Prawidłowo zainstalowany micro-SIM](../../assets/common/device/installation/micro-sim-insertion-orientation.jpeg){ .doc-photo }

    Włóż kartę SIM i delikatnie wciśnij ją prawie całkowicie do gniazda, aż usłyszysz delikatne kliknięcie potwierdzające, że karta została zablokowana na swoim miejscu:

    ![micro-SIM zablokowany w gnieździe](../../assets/common/device/installation/micro-sim-locked-in-slot.jpeg){ .doc-photo }

4. Aktywuj lub uruchom ponownie urządzenie: krótko przytrzymaj klucz magnetyczny przy znaku firmowym z tyłu jednostki głównej.

    ![BeeApiary klucz magnetyczny](../../assets/common/device/installation/magnetic-key.png){ .doc-photo }

    ![Markowy celownik z kluczem magnetycznym](../../assets/common/device/installation/magnetic-key-target.png){ .doc-photo }

    Aby uzyskać więcej informacji, zobacz [Aktywacja i ponowne uruchomienie](../device/installation.md#activation-reset).

5. Połącz się z `apiary_net` i otwarte `http://192.168.4.1`.
6. Wpisz numer telefonu właściciela w formacie międzynarodowym.
7. Odłącz od `apiary_net` i sprawdź pierwszą wiadomość SMS.

Wynik: urządzenie zbiera pomiary, wysyła je do właściciela i przechowuje archiwum.
