# Przywracanie konfiguracji

Na tej stronie opisano, jak bezpiecznie wymienić kartę microSD, przywrócić konfigurację z kopii zapasowej i sprawdzić pliki XML po uruchomieniu urządzenia.

!!! danger "Nie wyjmuj karty microSD, gdy urządzenie jest aktywne"
    Urządzenie nie posiada standardowego przycisku zasilania. Przed wyjęciem lub zainstalowaniem karty microSD należy poczekać, aż urządzenie przejdzie w tryb uśpienia. Najpierw zapisz pełną kopię pliku `/setting` informator.

## Automatyczna normalizacja

- plik główny znajduje się w `/setting/mset.xml`;
- jeśli brakuje głównego pliku, urządzenie może utworzyć konfigurację wstępną;
- brakujący lub niekompletny plik ula można ponownie zapisać, korzystając z wartości zastępczych z bieżącego stanu;
- zaginiony `hive`, `thermometer`lub `schedule` sekcji, jak również istniejącej niekompletnej `scales` sekcja, uruchamia normalizację pliku ula;
- całkowicie brak `scales` sekcja nie jest błędem: wagi po prostu nie są tworzone;
- błędy strukturalne w głównym elemencie XML, `apairy_set` sekcja lub `hiveN` atrybut może uniemożliwić odczytanie konfiguracji.

Tworzenie inicjału `mset.xml` nie oznacza, że każdy parametr będzie miał wartość uniwersalną. `UPLOAD_URL`, dane uwierzytelniające FTP, piny HX711 i niektóre inne pola zależą od konfiguracji urządzenia lub indywidualnej konfiguracji.

!!! warning "Wymagana jest kopia zapasowa"
    Nie polegaj na automatycznym odzyskiwaniu jako jedynej kopii zapasowej. Przed wymianą karty microSD zapisz całość `/setting` katalogu, jeśli kartę można jeszcze odczytać.

## Bezpieczna wymiana karty microSD

1. Poczekaj, aż urządzenie przejdzie w tryb uśpienia.
2. Wyjmij kartę microSD i, jeśli można ją odczytać, skopiuj całą jej zawartość.
3. Przygotuj kartę microSD zgodnie z wymaganiami konkretnej wersji sprzętowej urządzenia.
4. Przywróć `/setting` katalog ze zweryfikowanej kopii zapasowej.
5. Jeżeli nie istnieje kopia zapasowa, nie należy wykorzystywać wartości kalibracyjnych wagi z innego urządzenia. Najpierw przywróć plik minimalny [`mset.xml`](settings-reference.md#minimal-example), a następnie utwórz plik ula bez `scales` sekcji lub wykonaj standardową procedurę kalibracji.
6. Włóż kartę microSD, gdy urządzenie jest w stanie uśpienia i poczekaj na kolejny cykl pracy.
7. Sprawdź godzinę, sieć, numery GSM, dostępne czujniki, harmonogram i wagę.
8. Porównaj znormalizowane pliki XML z kopią zapasową: urządzenie mogło mieć dodane pola z wartościami zastępczymi lub przepisanymi sekcjami.

## Jeśli nie można odczytać konfiguracji

1. Sprawdź, czy plik go zawiera `<settings>` element główny.
2. Sprawdź dokładne nazwy `apairy_set`, `synchronize`, `sefe_start_interval`, i `pecision` w trzech polach filtrów.
3. Upewnij się `hive_count` ma dopasowanie `hive1`…`hiveN` atrybuty.
4. Upewnij się, że wszystkie odniesienia `/setting/<hive>.xml` plik istnieje.
5. Nie próbuj naprawiać problemu poprzez kopiowanie `scales` z innego urządzenia. Tymczasowo usuń sekcję wagi i sprawdź resztę konfiguracji.
6. Zapisz problematyczne pliki XML i dzienniki usług do celów diagnostycznych.

Pełny opis pól znajduje się w sekcji [`mset.xml`](settings-reference.md) i [`HIVE*.XML`](hive-settings-reference.md) referencje.
