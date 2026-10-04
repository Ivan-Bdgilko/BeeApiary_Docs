# Dokumentacja serwisowa

Ta sekcja zawiera archiwum konfiguracji technicznej dla programu BeeApiary wagi do ula. Jest przeznaczony dla techników serwisowych i doświadczonych użytkowników, którzy muszą ręcznie przywrócić lub sprawdzić pliki XML.

Początkowe wartości niektórych parametrów sprzętowych i sieciowych zależą od konfiguracji i konfiguracji konkretnego urządzenia.

!!! danger "Edycja ręczna"
    Nieprawidłowe styki sprzętowe, wartości kalibracji lub okresy międzyobsługowe mogą zakłócać pomiary lub działanie urządzenia. Do zwykłych zmian użyj interfejsu internetowego. Zawsze twórz kopię zapasową pliku `/setting` katalogu przed ręczną edycją plików.

## Bezpieczna procedura

1. Poczekaj, aż urządzenie przejdzie w tryb uśpienia. Urządzenie nie posiada standardowego przycisku zasilania: podczas pracy jest albo aktywne, albo znajduje się w stanie hibernacji.
2. Wyjmij kartę microSD i zapisz pełną kopię pliku `/setting` informator.
3. Edytuj plik XML w edytorze tekstu bez zmiany nazw sekcji i atrybutów.
4. Upewnij się, że plik XML go posiada `<settings>` element główny i że obecne są wszystkie cudzysłowy i znaczniki zamykające.
5. Włóż ponownie kartę microSD, gdy urządzenie jest w trybie uśpienia. Zaktualizowane ustawienia zostaną zastosowane przy następnym normalnym załadowaniu konfiguracji; niektóre zmiany dokonane za pośrednictwem interfejsu internetowego zaczną obowiązywać dopiero po ponownym uruchomieniu.
6. Sprawdź pomiary, komunikację i dziennik serwisowy. Zachowaj kopię zapasową do czasu zakończenia weryfikacji.

Podczas zapisywania urządzenie może znormalizować plik: dodać brakujące sekcje lub atrybuty, zastąpić wartości zastępcze i zmienić kolejność elementów.

## Pliki

- [`/setting/mset.xml`](settings-reference.md) — sieć, GSM, czas, opcje sprzętowe, alarmy ogólne i BLE.
- [`/setting/<hive>.xml`](hive-settings-reference.md) — czujniki dla konkretnego ula, wagi, harmonogramu, częstotliwości kontroli i progów alarmowych.
- [Przywracanie konfiguracji](recovery.md) — bezpieczna wymiana karty microSD, przywracanie z kopii zapasowej i weryfikacja XML.

Nazwa pliku ula jest określona przez rozszerzenie `hive1`, `hive2`, i kolejnych atrybutach, bez rozszerzenia. `.xml` rozszerzenie jest dodawane automatycznie.

## Poziomy dostępu

| Etykieta | Znaczenie |
|---|---|
| `USER` | Wartość można zmienić za pomocą standardowego interfejsu. |
| `ADVANCED` | Wymagane jest zrozumienie jego wpływu na komunikację lub logikę działania. |
| `SERVICE` | Ręczne zmiany mogą spowodować, że urządzenie nie będzie działać lub zniekształcić dane. |

W tabelach, `—` oznacza, że ​​limity nie dotyczą danego pola. **Wartość początkowa** to wartość w nowo utworzonej konfiguracji, a nie w kodzie XML konkretnego urządzenia. **Jeśli nie podano** opisuje wartość używaną w przypadku braku atrybutu, która może różnić się od wartości początkowej.

## Nazwy historyczne

Dokładne identyfikatory XML nie są poprawiane nawet wtedy, gdy zawierają błędy: `apairy_set`, `sefe_start_interval`, `normal_pecision`, i `calibrate_pecision` musi pozostać dokładnie tak, jak napisano. Pisownia `synсhronize` z literą cyrylicy `с` jest nieprawidłowe; używać `synchronize`.
