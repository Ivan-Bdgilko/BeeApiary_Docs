# Data Storage

The BeeApiary measuring device records data to microSD whether or not GSM is available. A `YEARxx` directory is created for each year, with CSV files for each month containing the date, time, and available readings.

The CSV file may contain:

- `Date`, `Time`;
- `Weight[Kg]`;
- `T1 [°C]`, `T2 [°C]`, and additional temperatures;
- battery charge;
- pressure and humidity;
- GSM RSSI;
- firmware service metadata.

The columns depend on the device configuration and firmware version. Measurements use approximately 2 MB per year, while service logs use about 40–50 MB per year.

To retrieve the data, see [Download the Archive](../guides/download-archive.md).
