# Jak pobrać archiwum

Zanim zaczniesz, upewnij się, że BeeApiary aplikacja jest aktualna w sklepie Google Play, a wagi do ula mają oprogramowanie sprzętowe wydane w sierpniu 2024 r. lub później. Jeśli zainstalowana wersja jest starsza lub nie jesteś pewien jej daty, postępuj zgodnie z instrukcjami [Zaktualizuj BeeApiary Oprogramowanie wag do ważenia ula](update-device.md).

Ręczne pobieranie archiwum przydaje się w przypadku, gdy waga nie posiada karty SIM, chwilowo nie są dostępne inne metody synchronizacji lub w pomiarach pojawiają się luki. Aplikacja importuje zapisane dane i dodaje je do lokalnej historii.

!!! warning "microSD i ładowanie baterii"
    W wadze musi być zainstalowana działająca karta microSD zawierająca dostępne dane. Bezpośrednie połączenie Wi-Fi utrzymuje wagę w działaniu i zwiększa zużycie energii, dlatego nie wykonuj tej procedury częściej niż raz dziennie, jeśli nie jest to konieczne.

1. [Aktywuj lub uruchom ponownie BeeApiary wagi do ula](../device/installation.md#activation-reset) z kluczem magnetycznym.
2. W dostępnym przedziale czasu, zwykle około jednej minuty, podłącz telefon do `apiary_net` i pozostawać w pobliżu wagi.
3. Otwórz BeeApiary aplikacja.
4. Poczekaj, aż aplikacja automatycznie wykryje pobliskie wagi.
5. w **„Urządzenie w pobliżu. Pobrać archiwum?”** monit, dotknij **Tak**.

    ![BeeApiary aplikacja wyświetli monit o pobranie archiwum z pobliskiego urządzenia](../../assets/en/guides/download-archive/nearby-device-archive-prompt.jpg){ .doc-screenshot }

6. Poczekaj na zakończenie importu, a następnie natychmiast odłącz telefon od `apiary_net`. Po odłączeniu waga może przejść w tryb uśpienia, co pozwala uniknąć niepotrzebnego zużycia baterii.
7. Przeglądaj pobrane dane, korzystając ze standardowych ekranów aplikacji.

    ![BeeApiary ekran główny aplikacji z zaimportowanymi pomiarami](../../assets/en/app/main-screen/app-home-screen.png){ .doc-screenshot }

Po potwierdzeniu aplikacja automatycznie pobiera archiwum i przechowuje lokalną kopię pomiarów. Jeśli inne kanały pominęły jakieś dane, archiwum może wypełnić odpowiednie luki w historii. Format archiwum i okres przechowywania opisano poniżej [Przechowywanie danych](../system/data-storage.md).
