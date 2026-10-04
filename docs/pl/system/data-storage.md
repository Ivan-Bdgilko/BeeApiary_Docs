# Przechowywanie danych

 BeeApiary wagi do ula zapisują dane na karcie microSD niezależnie od dostępności sieci GSM. A `YEARxx` katalog tworzony jest dla każdego roku, a pliki CSV dla każdego miesiąca zawierają datę, godzinę i dostępne odczyty.

Plik CSV może zawierać:

- `Date`, `Time`;
- `Weight[Kg]`;
- `T1 [°C]`, `T2 [°C]`i dodatkowe temperatury;
- ładowanie akumulatora;
- ciśnienie i wilgotność;
- RSSI GSM;
- metadane usługi oprogramowania sprzętowego.

Kolumny zależą od konfiguracji urządzenia i wersji oprogramowania sprzętowego. Measurements use approximately 2 MB per year, while service logs use about 40–50 MB per year.

Aby odzyskać dane, zobacz [Pobierz archiwum](../guides/download-archive.md).
