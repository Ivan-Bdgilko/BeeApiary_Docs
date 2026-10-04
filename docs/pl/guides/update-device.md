# Jak zaktualizować oprogramowanie wagi pasiecznej BeeApiary

Przed aktualizacją wybierz oprogramowanie sprzętowe odpowiadające generacji urządzenia i wymaganemu językowi interfejsu.

## Wybierz generację oprogramowania sprzętowego

| Urządzenie | Aktualizuj źródło | Stan rozwoju |
|---|---|---|
| Wyprodukowano przed sierpniem 2026 r | [Hive_Controller](https://github.com/Ivan-Bdgilko/Hive_Controller) | Rozwój funkcji poprzedniej wersji nie jest już obsługiwany |
| Wyprodukowano po sierpniu 2026 r | [Hive_Controller_Ble](https://github.com/Ivan-Bdgilko/Hive_Controller_Ble) | Nowa wersja nadal otrzymuje aktualizacje i nowe funkcje |

!!! danger "Migracja starszego urządzenia do nowej wersji"
    Każde wcześniej wyprodukowane urządzenie można migrować do nowej wersji oprogramowania, ale wymaga to aktualizacji fabrycznej. Obecnie nie ma prostej łatki umożliwiającej samoobsługową migrację, więc standardowa procedura na tej stronie nie powoduje migracji urządzenia pomiędzy generacjami.

## Wybierz język oprogramowania sprzętowego

Obie generacje zapewniają wersje wielojęzyczne. Sufiks w nazwie wersji identyfikuje język:

| Przyrostek | Język |
|---|---|
| `-de` | niemiecki |
| `-en` | Angielski |
| `-es` | Hiszpański |
| `-fr` | Francuski |
| `-pl` | Polski |
| `-uk` | ukraiński |

Wybierz język, pobierając i flashując odpowiedni plik. Kompilacje językowe są publicznie dostępne w repozytoriach wymienionych powyżej, a w razie potrzeby można później dodać więcej języków.

## Zaktualizuj urządzenie za pomocą karty microSD

1. Poczekaj, aż urządzenie przejdzie w tryb uśpienia, a następnie wyjmij kartę microSD.
2. Utwórz `/fm` katalogu w katalogu głównym karty, jeśli jeszcze nie istnieje.
3. Umieść `Apiary.bin` zaktualizuj plik w `/fm`.
4. Włóż ponownie kartę microSD do urządzenia.
5. [Aktywuj lub uruchom ponownie urządzenie](../device/installation.md#activation-reset) z kluczem magnetycznym.
6. Poczekaj na zwykłą wiadomość SMS zawierającą pomiary; aktualizacja trwa zwykle do dwóch minut.
7. Na dole strony głównej interfejsu internetowego sprawdź wersję oprogramowania sprzętowego, przyrostek języka, datę i godzinę kompilacji oraz unikalny numer urządzenia.

![Wersja oprogramowania sprzętowego, przyrostek języka, czas kompilacji i unikalny identyfikator w interfejsie internetowym urządzenia](../../assets/common/guides/update-device/device-version-build-time-and-id.png){ .doc-screenshot }

Ciąg pełnej wersji zawiera na przykład przyrostek lokalizacji `-uk`. Porównaj ją z odpowiednią wersją aktualizacji w repozytorium generacji urządzenia. Na tej samej stronie wyświetlana jest także data i godzina kompilacji oraz unikalny identyfikator urządzenia.

!!! warning "Sprawdź plik przed aktualizacją"
    Upewnij się `Apiary.bin` jest przeznaczony do generacji Twojego urządzenia i wymaganego języka. Metody aktualizacji usług za pośrednictwem protokołu FTP lub serwera wykraczają poza zakres tej procedury.
