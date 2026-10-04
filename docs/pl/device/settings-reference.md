# `mset.xml`: Ustawienia urządzenia

Główna konfiguracja jest przechowywana w `/setting/mset.xml` na karcie microSD i posiada `<settings>` element główny.

!!! warning "Bieżący plik nie jest listą wartości fabrycznych"
    Wartości w formacie XML konkretnego urządzenia mogły zostać zmienione przez użytkownika, interfejs sieciowy lub automatycznie. Na przykład `sefe_start_interval="60000"` i `alarm_sms_sec_interval="10"` nie są wartościami początkowymi: używana jest nowa konfiguracja `120000` milisekundy i `180` odpowiednio.

Zobacz także [zasady bezpiecznego edytowania](service-reference.md). Nie zmieniaj `SERVICE` parametrów bez tworzenia kopii zapasowej i zrozumienia ich wpływu na urządzenie.

## `net_settings`

W tej sekcji przechowywane są parametry punktu dostępu urządzenia, połączenia z zewnętrzną siecią Wi-Fi, transmisji danych i protokołu FTP. An `SSID`/`PASSWORD` lub `SSID_STA`/`PASSWORD_STA` pair jest stosowana tylko wtedy, gdy obie wartości są obecne i niepuste.

| Pole | Przeznaczenie | Wymagalność | Dopuszczalne wartości / granice | Wartość początkowa | Jeśli nie podano | Poziom |
|---|---|---|---|---|---|---|
| `SSID` | Nazwa lokalnego punktu dostępu urządzenia | Warunkowo wymagane z `PASSWORD` | Ciąg znaków; do 32 znaków | `apiary_net` | Nowa para punktów dostępowych nie jest stosowana | `USER` |
| `PASSWORD` | Hasło do lokalnego punktu dostępu | Warunkowo wymagane z `SSID` | Ciąg znaków; do 32 znaków | `apiary_wifi` | Nowa para punktów dostępowych nie jest stosowana | `USER` |
| `SSID_STA` | SSID zewnętrznej sieci Wi-Fi | Opcjonalne | Niepusty ciąg znaków; nie określono maksymalnej długości | `-` | Nowe parametry STA nie są stosowane | `ADVANCED` |
| `PASSWORD_STA` | Hasło do zewnętrznej sieci Wi-Fi | Warunkowo wymagane z `SSID_STA` | Ciąg znaków; nie określono maksymalnej długości | `-` | Nowe parametry STA nie są stosowane | `ADVANCED` |
| `STA_KEY` | Klucz uwierzytelniający używany podczas transmisji | Opcjonalne | Ciąg znaków; format zależy od metody uwierzytelniania | `-` | Parametr Wi-Fi nie ulega zmianie | `SERVICE` |
| `UPLOAD_URL` | Adres odbiornika danych Wi-Fi | Opcjonalne | Adres URL; maksymalna długość nie jest określona | Zależy od konfiguracji urządzenia | Ustaw na pojedynczą spację; transmisja nie jest faktycznie skonfigurowana | `SERVICE` |
| `wifi_sync` | Umożliwia synchronizację poprzez zewnętrzną sieć Wi-Fi | Opcjonalne | `true`, `false` | `false` | `false` | `ADVANCED` |
| `FTP_USER` | Nazwa użytkownika lokalnego FTP | Opcjonalnie jako część pary | Ciąg znaków; do 32 znaków | Zależy od konfiguracji urządzenia | Jeśli brakuje któregokolwiek pola FTP, używane są początkowe ustawienia FTP | `ADVANCED` |
| `FTP_PASSWORD` | Hasło do lokalnego FTP | Opcjonalnie jako część pary | Ciąg znaków; do 32 znaków | Zależy od konfiguracji urządzenia | Jeśli brakuje któregokolwiek pola FTP, używane są początkowe ustawienia FTP | `ADVANCED` |

!!! note " `-` wartość"
    Dla `SSID_STA`, `PASSWORD_STA`, i `STA_KEY`, łącznik jest dosłowną wartością początkową. Jest przetwarzany jako niepusty ciąg znaków, więc nie używaj go jako wiarygodnego wskazania, że ​​ustawienie jest „nieskonfigurowane”.

Zmień początkowe hasło `apiary_wifi` po pierwszym sprawdzeniu urządzenia.

## `apairy_set`

Nazwa sekcji zawiera błąd historyczny i musi pozostać `apairy_set`. Ta sekcja jest wymagana do utworzenia listy uli.

| Pole | Przeznaczenie | Wymagalność | Dopuszczalne wartości / granice | Wartość początkowa | Jeśli nie podano | Poziom |
|---|---|---|---|---|---|---|
| `hive_count` | Liczba plików konfiguracyjnych ula | Pole opcjonalne w wymaganej sekcji | Liczba całkowita; `1` lub więcej jest zalecane; limity nie są sprawdzane automatycznie | `1` | `1` | `ADVANCED` |
| `hive1`…`hiveN` | Nazwy podstawowe plików ula bez `.xml` | Wymagane dla każdego numeru do `hive_count` | Ciąg znaków; dla zgodności zaleca się do 8 znaków ASCII | `hive1` | Błąd odczytu atrybutu; odpowiedni ul nie jest tworzony | `SERVICE` |

Ścieżka ma formę `/setting/<значення>.xml`. Nazwa korzysta z wewnętrznego bufora 24-bajtowego, dlatego nie należy używać długich nazw ani separatorów ścieżek.

## `GSM`

W tej sekcji opisano dwóch odbiorców. Jeżeli sekcja jest nieobecna, struktura GSM zostaje wyczyszczona. Dlatego samą sekcję należy uznać za wymaganą nawet w przypadku pracy bez karty SIM.

| Pole | Przeznaczenie | Wymagalność | Dopuszczalne wartości / granice | Wartość początkowa | Jeśli nie podano | Poziom |
|---|---|---|---|---|---|---|
| `sms_format1` | Format SMS-a dla `number1` | Opcjonalne | `1` — tekst; `2` — kompaktowy format aplikacji | `2` | `2` | `USER` |
| `sms_format2` | Format SMS-a dla `number2` | Opcjonalne | `1` — tekst; `2` — kompaktowy format aplikacji | `2` | `2` | `USER` |
| `number1` | Główny numer odbiorcy | Opcjonalne | Format międzynarodowy; wewnętrzny bufor 15-bajtowy | Pusty ciąg | Przy pierwszym ładowaniu nie skonfigurowano żadnego odbiorcy | `USER` |
| `number2` | Dodatkowy numer odbiorcy | Opcjonalne | Format międzynarodowy; wewnętrzny bufor 15-bajtowy | Pusty ciąg | Przy pierwszym ładowaniu nie skonfigurowano żadnego odbiorcy | `USER` |
| `sms_wait_to_send_sec` | Czas poczekać przed wysłaniem SMS-a w słabej sieci | Opcjonalne | Całkowita liczba sekund; brak ustalonych limitów | `50` s | `50` s | `ADVANCED` |
| `alarm_call_wait_sec` | Odstęp między powtarzającymi się próbami wywołania alarmu | Opcjonalne | Całkowita liczba sekund; brak ustalonych limitów | `80` s | `80` s | `ADVANCED` |

Podaj pustą liczbę jako `number1=""` lub `number2=""`. W publikowanych przykładach nie należy podawać prawdziwych numerów telefonów.

## `NTP`

Sekcja ta należy do tej samej struktury wewnętrznej co GSM. Jeśli `NTP` jest całkowicie nieobecny, resetowane są także właśnie odczytane parametry GSM. Dlatego sekcja musi pozostać obecna nawet wtedy, gdy synchronizacja jest wyłączona.

| Pole | Przeznaczenie | Wymagalność | Dopuszczalne wartości / granice | Wartość początkowa | Jeśli nie podano | Poziom |
|---|---|---|---|---|---|---|
| `synchronize` | Automatyczna synchronizacja czasu poprzez dostępny mechanizm sieciowy | Pole opcjonalne w wymaganej sekcji | `true`, `false` | `false` | `false` | `USER` |
| `time_zone` | Przesunięcie strefy czasowej określone w formacie XML w pełnych godzinach | Opcjonalne | Liczba całkowita; `-11` do `12` jest zalecane; limity nie są sprawdzane automatycznie | `2` | `3` | `ADVANCED` |
| `ntp1` | Podstawowy serwer czasu | Opcjonalne | nazwa hosta; bufor wewnętrzny do 30 bajtów | `0.europe.pool.ntp.org` | Opróżnij przy pierwszym załadunku | `ADVANCED` |
| `ntp2` | Dodatkowy serwer czasu | Opcjonalne | nazwa hosta; bufor wewnętrzny do 30 bajtów | `1.europe.pool.ntp.org` | Opróżnij przy pierwszym załadunku | `ADVANCED` |
| `ntp3` | Trzeci serwer czasu | Opcjonalne | nazwa hosta; bufor wewnętrzny do 30 bajtów | `2.europe.pool.ntp.org` | Opróżnij przy pierwszym załadunku | `ADVANCED` |

`time_zone` ma różne wartości w obu przypadkach: otrzymuje nowy plik `2`, podczas gdy brakujący atrybut skutkuje `3`. Należy uwzględnić tę różnicę przed zmianą konfiguracji początkowej.

Pisownia `synсhronize` zawiera literę cyrylicy `с` i nie jest rozpoznawany. Używaj tylko `synchronize`.

## `options`

Poszczególne atrybuty są opcjonalne i mają wartości zastępcze. **Nie usuwaj całej sekcji:** w przypadku jego braku parametry sekcji są kasowane zamiast przyjmować wartości początkowe pokazane poniżej.

| Pole | Przeznaczenie | Wymagalność | Dopuszczalne wartości / granice | Wartość początkowa | Jeśli nie podano | Poziom |
|---|---|---|---|---|---|---|
| `meteo` | Wskazuje obecność czujnika ciśnienia i wilgotności | Opcjonalne | `true`, `false` | `false` | `false` | `SERVICE` |
| `pir_sensor` | Wskazuje obecność czujnika ruchu PIR | Opcjonalne | `true`, `false` | `false` | `false` | `SERVICE` |
| `temperature_twist` | Zamienia logiczne wartości T1 i T2 | Opcjonalne | `true`, `false` | `false` | `false` | `ADVANCED` |
| `oled` | Wskazuje obecność wyświetlacza OLED | Opcjonalne | `true`, `false` | `false` | `false` | `SERVICE` |
| `oled_invert` | Odwraca obraz OLED | Opcjonalne | `true`, `false` | `false` | `false` | `SERVICE` |
| `sefe_start_interval` | Czas trwania aktywnego okna po uruchomieniu | Opcjonalne | milisekundy; limity nie są sprawdzane automatycznie | `120000` milisekundy | `120000` milisekundy | `SERVICE` |
| `alarm_sms_sec_interval` | Minimalny odstęp pomiędzy alarmowymi wiadomościami SMS | Opcjonalne | Całkowita liczba sekund bez znaku | `180` s | `180` s | `ADVANCED` |
| `alarm_by_changes_count` | Liczba zmian stanu PIR wymagana do potwierdzenia alarmu | Opcjonalne | Liczba całkowita bez znaku; Wartość praktyczna zależy od umiejscowienia | `3` | `3` | `ADVANCED` |
| `alarm_by_long_state` | Czas trwania aktywnego stanu PIR wymagany do wystąpienia alarmu | Opcjonalne | Całkowita liczba sekund bez znaku | `10` s | `10` s | `ADVANCED` |
| `time_ms_compensate` | Dzienna kompensacja częstotliwości zegara | Opcjonalne | Podpisana 32-bitowa liczba milisekund | `0` milisekundy | `0` milisekundy | `SERVICE` |
| `sync_time_sec` | Znacznik czasu usługi do ręcznej synchronizacji | Opcjonalne | Podpisana 64-bitowa liczba sekund | `0` | `0` | `SERVICE` |

`sefe_start_interval` to dokładna historyczna nazwa pola. Jego wartość początkowa wynosi `120000` milisekundy; zasięg nie jest sprawdzany automatycznie, dlatego arbitralne jego zmniejszanie jest niebezpieczne.

Flagi sprzętowe zmienione poprzez interfejs WWW są zapisywane natychmiast, ale konfiguracja operacyjna stosuje je po ponownym wczytaniu ustawień.

## `BLE`

Cała sekcja jest opcjonalna ze względu na zgodność ze starszymi plikami. Jeśli jej nie ma, BLE jest wyłączone, a urządzenie używa bieżących wartości i standardowych interwałów.

| Pole | Przeznaczenie | Wymagalność | Dopuszczalne wartości / granice | Wartość początkowa | Jeśli nie podano | Poziom |
|---|---|---|---|---|---|---|
| `ble_enable` | Włącza BLE | Opcjonalne | `true`, `false` | `false` | `false`; nieprawidłowa wartość również wyłącza BLE | `USER` |
| `static_values` | Wybiera wartości statyczne zamiast wartości bieżących | Opcjonalne | `true`, `false` | `false` | `false` | `SERVICE` |
| `update_time_sec` | Interwał aktualizacji danych BLE | Opcjonalne | `3`–`60` S; niższe wartości są normalizowane do `3`, wyższe wartości do `60` | `30` s | `30` s | `ADVANCED` |
| `advertising_time_sec` | Czas trwania reklamy BLE | Opcjonalne | `0` lub `10`–`60` s; wartości z `1` do `9` są znormalizowane `0`, wartości powyżej `60` do `60` | `20` s | `20` s | `ADVANCED` |

Dla `static_values`opisano jedynie wybór wartości statycznych zamiast bieżących; nie zdefiniowano żadnego innego efektu parametru.

## Minimalny przykład { #minimal-example }

W tym przykładzie wartości początkowe STA, FTP i BLE są pozostawione. Puste, ale obecne `<options />` sekcja aktywuje wartość rezerwową każdego atrybutu zamiast czyszczenia całej struktury.

```xml
<settings>
  <net_settings SSID="apiary_net" PASSWORD="apiary_wifi" />
  <apairy_set hive_count="1" hive1="hive1" />
  <GSM sms_format1="2" sms_format2="2"
       number1="" number2=""
       sms_wait_to_send_sec="50" alarm_call_wait_sec="80" />
  <NTP synchronize="false" time_zone="2"
       ntp1="0.europe.pool.ntp.org"
       ntp2="1.europe.pool.ntp.org"
       ntp3="2.europe.pool.ntp.org" />
  <options />
</settings>
```

## Kompletny, oczyszczony przykład { #full-example }

Wartości `SITE_WIFI`, `WIFI_PASSWORD`, `DEVICE_KEY`, `FTP_USER`, `FTP_PASSWORD`i adres URL są obiektami zastępczymi, a nie danymi z urządzenia operacyjnego.

```xml
<settings>
  <net_settings SSID="apiary_net" PASSWORD="apiary_wifi"
                SSID_STA="SITE_WIFI" PASSWORD_STA="WIFI_PASSWORD"
                STA_KEY="DEVICE_KEY"
                UPLOAD_URL="https://example.invalid/beeapiary"
                wifi_sync="false"
                FTP_USER="FTP_USER" FTP_PASSWORD="FTP_PASSWORD" />
  <apairy_set hive_count="1" hive1="hive1" />
  <GSM sms_format1="2" sms_format2="2"
       number1="+380XXXXXXXXX" number2=""
       sms_wait_to_send_sec="50" alarm_call_wait_sec="80" />
  <NTP synchronize="false" time_zone="2"
       ntp1="0.europe.pool.ntp.org"
       ntp2="1.europe.pool.ntp.org"
       ntp3="2.europe.pool.ntp.org" />
  <options meteo="false" pir_sensor="false"
           temperature_twist="false" oled="false" oled_invert="false"
           sefe_start_interval="120000"
           alarm_sms_sec_interval="180"
           alarm_by_changes_count="3" alarm_by_long_state="10"
           time_ms_compensate="0" sync_time_sec="0" />
  <BLE ble_enable="false" static_values="false"
       update_time_sec="30" advertising_time_sec="20" />
</settings>
```
