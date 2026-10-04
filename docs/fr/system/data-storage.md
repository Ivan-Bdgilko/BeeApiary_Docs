# Stockage des données

Le BeeApiary Les balances pour ruches enregistrent les données sur microSD, que le GSM soit disponible ou non. Un `YEARxx` Un répertoire est créé pour chaque année, avec des fichiers CSV pour chaque mois contenant la date, l'heure et les lectures disponibles.

Le fichier CSV peut contenir :

- `Date`, `Time`;
- `Weight[Kg]`;
- `T1 [°C]`, `T2 [°C]`, et températures supplémentaires ;
- charge de la batterie ;
- pression et humidité ;
- GSM RSSI ;
- métadonnées du service du micrologiciel.

Les colonnes dépendent de la configuration de l'appareil et de la version du micrologiciel. Les mesures utilisent environ 2 Mo par an, tandis que les journaux de service utilisent environ 40 à 50 Mo par an.

Pour récupérer les données, voir [Téléchargez les archives](../guides/download-archive.md).
