# Użytkowanie i przechowywanie w zimie

BeeApiary Wagi do ula mogą pozostać na zewnątrz i kontynuować pomiary w zimie lub można je przechowywać bez przesyłania danych. Wybierz scenariusz w oparciu o to, czy w tym okresie musisz monitorować ule.

## Operacja zimą

Kiedy [zainstalowany](installation.md) prawidłowo, waga działa normalnie na zewnątrz w zakresie temperatur podanym w pkt [specyfikacje](specifications.md). Pomiary zimowe pomagają monitorować:

- zmiany masy ciała i pozostałe rezerwy żywności;
- temperatura wewnątrz i na zewnątrz monitorowanego ula;
- wilgotność, jeśli zainstalowany jest odpowiedni czujnik.

Przed zimą sprawdź obudowę i osłony ochronne, sprawdź poziom naładowania akumulatora i upewnij się, że platforma jest stabilna. Nie dopuścić do przedostania się wody do obudowy.

## Przechowywanie bez transmisji danych

Jeżeli pomiary zimowe nie są potrzebne, nie trzeba wyłączać ani demontować urządzenia. Aby zapobiec zużywaniu energii baterii i środków komunikacyjnych w przypadku nieudanych prób wysłania wiadomości SMS, użyj jednej z następujących metod:

- wyjmij kartę SIM lub naciśnij ją, aż odłączy się i wyjdzie z pozycji roboczej;
- wyłącz **GSM** przełącznik w [dodatkowe ustawienia urządzenia](additional-settings.md).

Nie zostawiaj w urządzeniu aktywnej karty SIM bez środków lub płatnego planu. Urządzenie może wykryć kartę, ale nie może określić stanu konta ani planu, więc będzie kontynuować próby wysyłania wiadomości SMS i zużywać energię baterii.

Przed przechowywaniem całkowicie naładuj akumulator. Przy normalnej transmisji danych jedno ładowanie może wystarczyć na 2–3 miesiące. Jeśli w ustawieniach wyłączono funkcję GSM lub kartę SIM przesunięto z pozycji roboczej, żywotność baterii może przekroczyć sześć miesięcy nawet w niskich temperaturach. Rzeczywisty okres zależy od stanu i rodzaju baterii, temperatury i konfiguracji urządzenia; okresowo sprawdzaj ładowanie i [naładuj urządzenie](power.md) kiedy to konieczne.

## Nie wyjmuj akumulatora w celu przechowywania

Urządzenie posiada dwa inteligentne i jeden elektroniczny poziom ochrony baterii. Gdy poziom naładowania spadnie poniżej 20%, automatycznie przechodzi w tryb głębokiego oszczędzania energii i czeka na ładowanie. W tym trybie pobór mocy jest porównywalny z samorozładowaniem akumulatora.

Szacuje się, że nawet 20% naładowania może zapewnić prawie dwa lata czuwania w głębokim śnie. Nie gwarantuje to żywotności baterii podczas regularnych pomiarów lub transmisji danych: stan i typ baterii, temperatura i konfiguracja urządzenia mają wpływ na wynik.

!!! danger "Nie odwracaj polaryzacji"
    Nie wyjmuj akumulatora w celu normalnego przechowywania lub ładowania. Każda ponowna instalacja stwarza ryzyko odwrócenia polaryzacji i trwałego uszkodzenia urządzenia. Wyjątkami są [odzyskiwanie awaryjne](../troubleshooting/recovery-after-storage.md) gdy napięcie jest niższe `3,5 В`lub prace serwisowe wykonane według sprawdzonej procedury.

Po przechowywaniu sprawdź poziom naładowania baterii urządzenia i czas. Dodatkowe rekomendacje są dostępne na stronie [Konserwacja](maintenance.md) strona.
