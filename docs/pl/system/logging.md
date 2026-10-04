# Dzienniki

 BeeApiary Wagi do ula dostarczają trzech różnych typów danych:

1. archiwum pomiarów CSV dla użytkownika;
2. dziennik serwisowy urządzenia na karcie microSD;
3. dziennik inżynieryjny w czasie rzeczywistym za pośrednictwem interfejsu internetowego.

Dzienniki serwisowe służą do celów diagnostycznych, a nie do rutynowego przeglądania. Są one dostępne na karcie microSD; interfejs sieciowy udostępnia także adresy usług `/log` i `/tracecontrol`.

!!! warning
    Nie zmieniaj poziomu rejestrowania inżynieryjnego, chyba że jest to konieczne lub zalecane przez programistę. Skorzystaj z [archiwum danych](data-storage.md) do analizy pomiarów.
