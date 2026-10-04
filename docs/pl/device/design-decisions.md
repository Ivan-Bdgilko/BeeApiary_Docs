# Dlaczego BeeApiary działa w ten sposób

## Z BeeApiary Twórcy

BeeApiary został zaprojektowany jako samodzielne narzędzie, które przechowuje dane i kluczowe decyzje pod kontrolą pszczelarza. Na tej stronie objaśniono kilka opcji dotyczących projektu i oprogramowania, które mogą nie być od razu oczywiste.

## Dlaczego okładki są przezroczyste?

Przezroczysta pokrywa pozwala zobaczyć, kiedy urządzenie pracuje i czy do obudowy nie dostała się wilgoć, owady lub brud. Ułatwia to kontrolę bez niepotrzebnego otwierania obudowy.

Projekt jest otwarty na uwagi i sugestie: jego konstrukcja nie ukrywa przed właścicielem stanu głównych podzespołów.

## Dlaczego nie ma obowiązkowej pamięci serwerowej?

Podstawowe działanie wagi do ula i aplikacji nie jest uzależnione od stałego działania BeeApiary przechowywanie na serwerze zewnętrznym. Pomiary zapisywane są na [kartę microSD urządzenia](../system/data-storage.md) oraz lokalnie na telefonie użytkownika. System nie wymaga scentralizowanego przechowywania lokalizacji właściciela ani historii jego aktywności.

Można skorzystać z opcjonalnej usługi przekaźnika [synchronizacja poprzez pasieczną sieć Wi-Fi](../system/local-wifi.md#apiary-wifi-routing). Przesyła dane do aplikacji, ale nie stanowi trwałego przechowywania i nie jest wymagany w przypadku innych kanałów komunikacji.

## Dlaczego GSM korzysta z SMS-ów?

W terenie lub podczas przenoszenia pasieki SMS jest często dostępny tam, gdzie mobilny dostęp do Internetu jest zawodny. Wystarczy minimalny plan SMS, a aplikacja odbiera dane bez osobnej subskrypcji serwera.

Przy odpowiednim formacie wiadomości, dwie wiadomości SMS dziennie mogą dostarczyć wyniki wszystkich pomiarów godzinowych zebranych w ciągu danego dnia. Aplikacja działa bezpośrednio na telefonie właściciela i w typowej konfiguracji może obsłużyć do pięciu urządzeń; w razie potrzeby liczbę tę można zwiększyć.

Aby uzyskać szczegółowe informacje, zobacz [GSM i SMS-y](../system/gsm-and-sms.md).

## Dlaczego pomiary są wykonywane co godzinę?

Historia godzinowa pomaga ujawnić poranne odloty pszczół i wieczorne powroty, zmiany masy ciała podczas suszenia nektaru oraz dzienne wahania temperatury. Dane te stanowią podstawę do dalszej analizy siły rodziny, zapasów pożywienia i innych procesów zachodzących w ulu.

## Dlaczego wiadomości SMS nie są wysyłane co godzinę?

Częsta transmisja nie poprawia samych pomiarów, ale zużywa energię baterii i kredyt komunikacyjny. Wysyłanie kilku wiadomości dziennie pozwala znacznie efektywniej przesyłać zgromadzone dane godzinowe.

Praktyczny szacunek dla dwóch wiadomości SMS dziennie to co najmniej 160 dni działania na jednym ładowaniu. To jest wskazówka, a nie gwarancja: żywotność baterii zależy od baterii, konfiguracji urządzenia, temperatury, zasięgu GSM i włączonych kanałów transmisji.

Jeśli zainstalowany jest czujnik alarmowy, zdarzenie awaryjne lub próba przeniesienia ula może oddzielnie wywołać połączenie i SMS-a, bez czekania na normalny harmonogram.

## Dlaczego nie należy wyjmować akumulatora?

Urządzenie ma trzy poziomy ochrony baterii i przy niskim poziomie naładowania automatycznie przechodzi w tryb głębokiego oszczędzania energii. Nie trzeba wyjmować baterii na czas przechowywania, a nieprawidłowa polaryzacja przy ponownym montażu może trwale uszkodzić elektronikę.

Wyjątki i zasady przechowywania zimowego opisano w [Zasilanie i ładowanie](power.md) i [Użytkowanie i przechowywanie w zimie](winter-use-and-storage.md).

## Dlaczego aktualizacje oprogramowania sprzętowego nie są automatyczne?

Właściciel decyduje, kiedy zaktualizować urządzenie i czy potrzebne będą funkcje nowej wersji. Kontrolowana aktualizacja zmniejsza ryzyko nieoczekiwanych zmian w zachowaniu systemu autonomicznego.

Waga ula może pracować bez telefonu jako samodzielna waga i rejestrator danych pogodowych. Aplikacja na Androida rozszerza funkcje przeglądania, dziennika pasiecznego i synchronizacji, ale nie jest wymagana do pomiarów. Procedura: [Zaktualizuj urządzenie](../guides/update-device.md).

## Jak długo przechowywane są pomiary?

Archiwum na karcie microSD nie jest ograniczone do jednego roku. Okres przechowywania zależy od pojemności i stanu karty; przy normalnej liczbie pomiarów wystarcza ona na przewidywany okres użytkowania urządzenia.

## Dwa rodzaje SMS-ów i elastyczny harmonogram. Dlaczego?

Istnieje wiele opinii na temat tego, kiedy, jak i gdzie rozpocząć pomiary; Aby rozwiązać ten problem, użytkownicy mogą dowolnie konfigurować format wiadomości SMS i czas wysyłania zgodnie ze swoimi preferencjami. Istnieją jednak pewne zalecenia dotyczące liczby wiadomości dziennie w celu oszczędzania energii.
