# Journaux

Le BeeApiary Les balances pour ruches fournissent trois types de données différents :

1. une archive de mesures CSV pour l'utilisateur ;
2. un journal de service de l'appareil sur la carte microSD ;
3. un journal d'ingénierie en temps réel via l'interface Web.

Les journaux de service sont destinés au diagnostic et non à l'affichage de routine. Ils sont disponibles sur la carte microSD ; l'interface web fournit également les adresses de service `/log` et `/tracecontrol`.

!!! warning
    Ne modifiez pas le niveau de journalisation technique sauf si cela est nécessaire ou recommandé par le développeur. Utilisez le [archives de données](data-storage.md) pour analyser les mesures.
