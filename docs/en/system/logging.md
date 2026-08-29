# Logs

The BeeApiary measuring device provides three different types of data:

1. a CSV measurement archive for the user;
2. a device service log on the microSD card;
3. a real-time engineering log through the web interface.

Service logs are intended for diagnostics, not routine viewing. They are available on the microSD card; the web interface also provides the service addresses `/log` and `/tracecontrol`.

!!! warning
    Do not change the engineering logging level unless necessary or recommended by the developer. Use the [data archive](data-storage.md) to analyze measurements.
