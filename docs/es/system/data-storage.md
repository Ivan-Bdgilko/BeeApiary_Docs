# Almacenamiento de datos

El BeeApiary Las básculas para colmenas registran datos en microSD, independientemente de que GSM esté disponible o no. un `YEARxx` Se crea un directorio para cada año, con archivos CSV para cada mes que contienen la fecha, hora y lecturas disponibles.

El archivo CSV puede contener:

- `Date`, `Time`;
- `Weight[Kg]`;
- `T1 [°C]`, `T2 [°C]`y temperaturas adicionales;
- carga de la batería;
- presión y humedad;
- RSSI GSM;
- metadatos del servicio de firmware.

Las columnas dependen de la configuración del dispositivo y la versión del firmware. Las mediciones utilizan aproximadamente 2 MB por año, mientras que los registros de servicio utilizan entre 40 y 50 MB por año.

Para recuperar los datos, consulte [Descargar el archivo](../guides/download-archive.md).
