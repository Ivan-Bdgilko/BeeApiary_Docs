# `HIVE*.XML`: Ustawienia ula

Konfiguracja ula jest przechowywana w `/setting/<hive>.xml`. `<hive>` nazwa bazowa jest określona przez `hive1`, `hive2`i kolejne atrybuty w [`mset.xml`](settings-reference.md); `.xml` rozszerzenie jest dodawane automatycznie.

!!! danger "Wartości zależne od sprzętu"
    Nie kopiuj `scales` sekcję z innego urządzenia. Piny płytki i wartości kalibracyjne zależą od wersji sprzętu i konkretnego zestawu czujników wagowych. Nieprawidłowe wartości mogą zniekształcić pomiary lub spowodować ich niedostępność.

Zobacz [zasady bezpiecznego edytowania](service-reference.md).

## Automatyczne przepisywanie

Po odczytaniu pliku urządzenie może go ponownie zapisać:

- z dostępnego stanu bieżącego tworzony jest brakujący lub uszkodzony plik;
- brak `hive`, `thermometer`lub `schedule` sekcje umożliwiają normalizację;
- brakujący atrybut w istniejącym `scales` lub `thermometer` sekcja zostaje zastąpiona wartością rezerwową i umożliwia normalizację;
- kompletny `scales`, `booster`, i `range_alarmer` sekcje są opcjonalne;
- normalizacja pisze również `booster`, `range_alarmer`, `thermometer`, i `schedule` sekcji, nawet jeśli niektórych z nich nie było w pliku źródłowym.

## `hive`

| Pole | Przeznaczenie | Wymagalność | Dopuszczalne wartości / granice | Wartość początkowa | Jeśli nie podano | Poziom |
|---|---|---|---|---|---|---|
| `hive_name` | Wewnętrzna nazwa ula | Opcjonalne | Ciąg znaków; dla zgodności zaleca się do 8 znaków ASCII | Imię od `mset.xml`, na przykład `hive1` | `hive_<індекс>`; plik jest oznaczony do ponownego zapisu | `ADVANCED` |
| `bus_number` | Numer ula na wewnętrznej magistrali | Opcjonalne | Liczba całkowita; granice nie są sprawdzane | Indeks instancji, `0` po raz pierwszy | Indeks instancji; plik jest oznaczony do ponownego zapisu | `SERVICE` |
| `main_device` | Wskazuje główne urządzenie z lokalnymi czujnikami sprzętowymi | Opcjonalne | `true`, `false` | `true` w nowo utworzonym pliku | Instancja nie staje się głównym urządzeniem; Samo pominięcie nie pozwala na przepisanie | `SERVICE` |

Obsługa urządzeń podrzędnych jest przestarzała. Wartość `main_device="false"` jest akceptowany podczas ładowania, ale po zapisaniu atrybut staje się `main_device="true"`. Nie używać `false` jako stabilna konfiguracja.

## `scales`

Jeśli cała sekcja jest nieobecna, obiekt wagi nie jest tworzony, a pomiar masy jest wyłączony. Jeśli sekcja istnieje, każde brakujące lub nieprawidłowe pole zostaje zastąpione wartością zastępczą, po czym cały plik może zostać ponownie zapisany.

| Pole | Przeznaczenie | Wymagalność | Dopuszczalne wartości / granice | Wartość początkowa | Jeśli nie podano | Poziom |
|---|---|---|---|---|---|---|
| `pin_hc711_data` | GPIO danych HX711 | Wymagane w istniejącej sekcji | GPIO dla konkretnej płyty | Sekcja nie jest tworzona automatycznie; zależne od sprzętu | Pin do konkretnej tablicy; plik jest przepisywany | `SERVICE` |
| `pin_hc711_clk` | GPIO zegara HX711 | Wymagane w istniejącej sekcji | GPIO dla konkretnej płyty | Sekcja nie jest tworzona automatycznie; zależne od sprzętu | Pin do konkretnej tablicy; plik jest przepisywany | `SERVICE` |
| `gain` | Tryb wzmocnienia HX711 | Wymagane w istniejącej sekcji | Wartość trybu wzmocnienia HX711 | Kanał A, zyskaj 128 | Kanał A, wzmocnienie 128; plik jest przepisywany | `SERVICE` |
| `zero_calibrate_measurement` | Surowa wartość ADC dla zerowego obciążenia | Wymagane w istniejącej sekcji | 32-bitowa liczba całkowita ze znakiem | Zależne od sprzętu | Wartość rezerwowa `-486050`; plik jest przepisywany | `SERVICE` |
| `weight_calibrate_measurement` | Surowa wartość ADC z masą referencyjną | Wymagane w istniejącej sekcji | 32-bitowa liczba całkowita ze znakiem | Zależne od sprzętu | Wartość rezerwowa `-498030`; plik jest przepisywany | `SERVICE` |
| `calibrate_weight` | Masa referencyjna do kalibracji | Wymagane w istniejącej sekcji | gramy; dodatnia liczba całkowita; limity nie są sprawdzane automatycznie | Zależne od sprzętu | `500` G; plik jest przepisywany | `USER` |
| `start_weight` | Tara odjęta od wyniku | Wymagane w istniejącej sekcji | gramy; `-100000` do `100000` jest zalecane; limity nie są sprawdzane automatycznie | Zależne od sprzętu | `0` G; plik jest przepisywany | `USER` |
| `source_weight` | Filtr, którego wynik jest używany jako waga podstawowa | Wymagane w istniejącej sekcji | `1` — `immediate`; `2` — `stable`; `3` — `calibration` | Sekcja nie jest tworzona automatycznie | `1`; plik jest przepisywany. Inne wartości są traktowane jako `1` podczas pracy | `SERVICE` |
| `normal_pecision` | Parametr dokładności filtra szybkiego | Wymagane w istniejącej sekcji | Liczba zmiennoprzecinkowa; limity nie są sprawdzane | Sekcja nie jest tworzona automatycznie | `0.5`; plik jest przepisywany | `SERVICE` |
| `normal_desired_deviation` | Pożądane odchylenie filtra szybkiego | Wymagane w istniejącej sekcji | Liczba zmiennoprzecinkowa; limity nie są sprawdzane | Sekcja nie jest tworzona automatycznie | `10`; plik jest przepisywany | `SERVICE` |
| `stable_pecision` | Parametr dokładności filtra stabilnego | Wymagane w istniejącej sekcji | Liczba zmiennoprzecinkowa; limity nie są sprawdzane | Sekcja nie jest tworzona automatycznie | `0.35`; plik jest przepisywany | `SERVICE` |
| `stable_desired_deviation` | Pożądane odchylenie filtra stabilnego | Wymagane w istniejącej sekcji | Liczba zmiennoprzecinkowa; limity nie są sprawdzane | Sekcja nie jest tworzona automatycznie | `5`; plik jest przepisywany | `SERVICE` |
| `calibrate_pecision` | Parametr dokładności filtra kalibracyjnego | Wymagane w istniejącej sekcji | Liczba zmiennoprzecinkowa; limity nie są sprawdzane | Sekcja nie jest tworzona automatycznie | `0.25`; plik jest przepisywany | `SERVICE` |
| `calibrate_desired_deviation` | Pożądane odchylenie filtra kalibracyjnego | Wymagane w istniejącej sekcji | Liczba zmiennoprzecinkowa; limity nie są sprawdzane | Sekcja nie jest tworzona automatycznie | `3`; plik jest przepisywany | `SERVICE` |
| `median_window` | Rozmiar okna filtra mediany | Wymagane w istniejącej sekcji | `3`–`100`; Wartości spoza zakresu są zastępowane | Sekcja nie jest tworzona automatycznie | `100`; plik jest przepisywany | `SERVICE` |

Identyfikatory `normal_pecision`, `stable_pecision`, i `calibrate_pecision` zawierają błąd historyczny `pecision`, których nie wolno poprawiać w formacie XML.

`gain` jest ładowany z pliku, ale zapisanie zawsze ustawia kanał A ze wzmocnieniem 128. Nie zmieniaj go ręcznie bez danych dla konkretnego urządzenia.

## `thermometer`

Brakująca sekcja umożliwia normalizację pliku. Wartość `sensors_count="0"` wyłącza odpytywanie czujników DS18B20.

| Pole | Przeznaczenie | Wymagalność | Dopuszczalne wartości / granice | Wartość początkowa | Jeśli nie podano | Poziom |
|---|---|---|---|---|---|---|
| `pin_onewire` | Magistrala 1-Wire GPIO | Opcjonalne | GPIO dla konkretnej płyty | `4` | `4`; plik jest przepisywany | `SERVICE` |
| `sensors_count` | Liczba czujników DS18B20 | Opcjonalne | `0` wyłącza czujniki; dodatnia liczba całkowita; górny limit nie jest sprawdzany | `2` | `2`; plik jest przepisywany | `ADVANCED` |

## `schedule`

 `TimeSlot0`–`TimeSlot23` atrybuty definiują akcję dla odpowiedniej godziny. Po 30 minucie wybierana jest akcja na następną godzinę; po godzinie 23, `TimeSlot0` jest wybrany.

| Pole | Przeznaczenie | Wymagalność | Dopuszczalne wartości / granice | Wartość początkowa | Jeśli nie podano | Poziom |
|---|---|---|---|---|---|---|
| `TimeSlot0`…`TimeSlot23` | Typ zaplanowanej akcji na godzinę `0`–`23` | Wszystkie atrybuty są opcjonalne, ale przynajmniej jedno miejsce posiada `2` jest wymagane | Liczba całkowita od `0` do `5`; patrz poniżej | `5` godzinami `0`–`20`; `1` dla `21` i `22`; `2` dla `23` | Brakujące miejsce staje się `0`. Jeśli nie `2` pozostanie po odczytaniu, cały harmonogram zostanie zresetowany do harmonogramu początkowego | `ADVANCED` |

| Wartość | Akcja | Zalecenie |
|---:|---|---|
| `0` | Brak zaplanowanych działań | Można zastosować do pustego gniazda |
| `1` | Pomiar | Obsługiwane |
| `2` | Transmisja poprzez kanał główny | Wymagane w co najmniej jednym gnieździe |
| `3` | Zarezerwowane do transmisji przez Wi-Fi | Nie używać |
| `4` | Zarezerwowane do transmisji poprzez BLE | Nie używać |
| `5` | Budzenie co godzinę w celu synchronizacji | Używany w pierwotnym harmonogramie |

Inne liczby całkowite nie są odrzucane, ale nie mają określonego zachowania. Używaj tylko wartości z tabeli.

### Wstępny harmonogram

```xml
<schedule
  TimeSlot0="5" TimeSlot1="5" TimeSlot2="5" TimeSlot3="5"
  TimeSlot4="5" TimeSlot5="5" TimeSlot6="5" TimeSlot7="5"
  TimeSlot8="5" TimeSlot9="5" TimeSlot10="5" TimeSlot11="5"
  TimeSlot12="5" TimeSlot13="5" TimeSlot14="5" TimeSlot15="5"
  TimeSlot16="5" TimeSlot17="5" TimeSlot18="5" TimeSlot19="5"
  TimeSlot20="5" TimeSlot21="1" TimeSlot22="1" TimeSlot23="2" />
```

## `booster`

W tej sekcji ustawia się częstotliwość dodatkowych wybudzeń w celu sprawdzenia parametrów krytycznych. Jeśli sekcja jest nieobecna, podczas pracy stosowana jest przerwa godzinowa; sama nieobecność nie powoduje przepisywania.

| Pole | Przeznaczenie | Wymagalność | Dopuszczalne wartości / granice | Wartość początkowa | Jeśli nie podano | Poziom |
|---|---|---|---|---|---|---|
| `booster_time_sec` | Dodatkowy okres kontroli | Opcjonalne | `180`, `240`, `300`, `360`, `600`, `720`, `900`, `1200`, `1800`lub `3600` s | `3600` s | `3600` s | `ADVANCED` |

Wartość poniżej `180` staje się `180`; wartość powyżej `3600` staje się `3600`. Pozostałe wartości w zakresie są zaokrąglane do najbliższego obsługiwanego przedziału w tabeli.

## `range_alarmer`

Ta sekcja jest opcjonalna. Jeżeli go nie ma, alarm progowy nie jest inicjowany. Jeśli `alarm="false"` lub `alarm` brak atrybutu, limity nie są odczytywane i nie jest uruchamiane zadanie alarmu tła.

| Pole | Przeznaczenie | Wymagalność | Dopuszczalne wartości / granice | Wartość początkowa | Jeśli nie podano | Poziom |
|---|---|---|---|---|---|---|
| `alarm` | Włącza alarmy progowe | Opcjonalne | `true`, `false` | `false` | `false` | `USER` |
| `T1_min` | Dolna granica T1 | Opcjonalne | Liczba zmiennoprzecinkowa, °C; limity fizyczne i kolejność min/max nie są sprawdzane automatycznie | `-500` °C w nowo utworzonym pliku | Z `alarm="true"`, nie ma dolnej granicy | `ADVANCED` |
| `T1_max` | Górna granica T1 | Opcjonalne | Liczba zmiennoprzecinkowa, °C; limity fizyczne i kolejność min/max nie są sprawdzane automatycznie | `500` °C w nowo utworzonym pliku | Z `alarm="true"`, nie ma górnej granicy | `ADVANCED` |
| `T2_min` | Dolna granica T2 | Opcjonalne | Liczba zmiennoprzecinkowa, °C; limity fizyczne i kolejność min/max nie są sprawdzane automatycznie | `-500` °C w nowo utworzonym pliku | Z `alarm="true"`, nie ma dolnej granicy | `ADVANCED` |
| `T2_max` | Górna granica T2 | Opcjonalne | Liczba zmiennoprzecinkowa, °C; limity fizyczne i kolejność min/max nie są sprawdzane automatycznie | `500` °C w nowo utworzonym pliku | Z `alarm="true"`, nie ma górnej granicy | `ADVANCED` |
| `Humidity_min` | Dolna granica wilgotności | Opcjonalne | Liczba zmiennoprzecinkowa,%; limity fizyczne i kolejność min/max nie są sprawdzane automatycznie | `-20` % w nowo utworzonym pliku | Z `alarm="true"`, nie ma dolnej granicy | `ADVANCED` |
| `Humidity_max` | Górna granica wilgotności | Opcjonalne | Liczba zmiennoprzecinkowa,%; limity fizyczne i kolejność min/max nie są sprawdzane automatycznie | `200` % w nowo utworzonym pliku | Z `alarm="true"`, nie ma górnej granicy | `ADVANCED` |

Dla każdego źródła — T1, T2 lub wilgotności — wystarczy jeden limit. Jeżeli dla danego źródła nie określono limitu, nie jest on dodawany do czeku. Kolejność `_min` i `_max` nie jest sprawdzane automatycznie.

### Przykład alarmu jednostronnego

W tym przykładzie T1 jest monitorowane tylko od góry, T2 tylko od dołu, a wilgotność nie jest monitorowana:

```xml
<range_alarmer alarm="true" T1_max="45.0" T2_min="-10.0" />
```

Ogólną częstotliwość SMS-ów i potwierdzanie alarmów PIR konfiguruje się za pomocą `alarm_sms_sec_interval`, `alarm_by_changes_count`, i `alarm_by_long_state` w [`mset.xml`](settings-reference.md#options).

## Przykład konstrukcyjny bez wagi

Ten plik używa początkowego harmonogramu, dwóch czujników temperatury i wyłączonych alarmów progowych. `scales` sekcja jest nieobecna, dlatego nie jest tworzony obiekt wagi.

```xml
<settings>
  <hive hive_name="hive1" bus_number="0" main_device="true" />
  <booster booster_time_sec="3600" />
  <range_alarmer alarm="false"
                 T1_max="500" T1_min="-500"
                 T2_max="500" T2_min="-500"
                 Humidity_max="200" Humidity_min="-20" />
  <thermometer pin_onewire="4" sensors_count="2" />
  <schedule
    TimeSlot0="5" TimeSlot1="5" TimeSlot2="5" TimeSlot3="5"
    TimeSlot4="5" TimeSlot5="5" TimeSlot6="5" TimeSlot7="5"
    TimeSlot8="5" TimeSlot9="5" TimeSlot10="5" TimeSlot11="5"
    TimeSlot12="5" TimeSlot13="5" TimeSlot14="5" TimeSlot15="5"
    TimeSlot16="5" TimeSlot17="5" TimeSlot18="5" TimeSlot19="5"
    TimeSlot20="5" TimeSlot21="1" TimeSlot22="1" TimeSlot23="2" />
</settings>
```

## Sekcja wag kompletnych

Poniższy przykład strukturalny wykorzystuje wartości rezerwowe i jest udostępniany wyłącznie w celach archiwalnych. **Nie instaluj go na urządzeniu:** wartości kalibracyjne i piny muszą pochodzić z kopii zapasowej tego konkretnego urządzenia lub zostać utworzone w drodze standardowej procedury kalibracji.

```xml
<scales pin_hc711_data="27" pin_hc711_clk="26" gain="0"
        zero_calibrate_measurement="-486050"
        weight_calibrate_measurement="-498030"
        calibrate_weight="500" start_weight="0" source_weight="1"
        normal_pecision="0.5" normal_desired_deviation="10"
        stable_pecision="0.35" stable_desired_deviation="5"
        calibrate_pecision="0.25" calibrate_desired_deviation="3"
        median_window="100" />
```

GPIO `27` i `26` stanowią jedynie przykład dla jednego urządzenia i nie są uniwersalne. Użyj wartości z kopii zapasowej konkretnego urządzenia.
