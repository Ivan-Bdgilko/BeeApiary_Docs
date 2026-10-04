# Utilisation et stockage hivernaux

BeeApiary Les balances pour ruches peuvent rester à l'extérieur et continuer à prendre des mesures en hiver, ou elles peuvent être stockées sans transmettre de données. Choisissez le scénario selon que vous devez ou non surveiller les ruches pendant cette période.

## Fonctionnement en hiver

Quand [installé](installation.md) correctement, la balance fonctionne normalement à l'extérieur dans la plage de température indiquée dans le [spécifications](specifications.md). Les mesures hivernales vous aident à surveiller :

- changements de poids et réserves alimentaires restantes ;
- température à l'intérieur et à l'extérieur de la ruche surveillée ;
- humidité, si le capteur correspondant est installé.

Avant l’hiver, inspectez l’enceinte et les capots de protection, vérifiez la charge de la batterie et assurez-vous que la plateforme est stable. Ne laissez pas l’eau pénétrer dans l’enceinte.

## Stockage sans transmission de données

Si des mesures hivernales ne sont pas nécessaires, vous n'avez pas besoin d'éteindre ou de démonter l'appareil. Pour éviter qu'il ne consomme l'énergie de la batterie et le crédit de communication en raison de tentatives infructueuses d'envoi de messages SMS, utilisez l'une de ces méthodes :

- retirer la carte SIM ou appuyer dessus jusqu'à ce qu'elle se désengage et sorte de sa position de fonctionnement ;
- désactiver le **GSM** basculer dans le [paramètres supplémentaires de l'appareil](additional-settings.md).

Ne laissez pas de carte SIM active sans crédit ni forfait payant dans l'appareil. L'appareil peut détecter la carte mais ne peut pas déterminer l'état du compte ou du forfait. Il continuera donc à essayer d'envoyer des messages SMS et à consommer l'énergie de la batterie.

Chargez complètement la batterie avant le stockage. Avec une transmission normale de données, une charge peut durer 2 à 3 mois. Si le GSM est désactivé dans les paramètres ou si la carte SIM est déplacée hors de sa position de fonctionnement, la durée de vie de la batterie peut dépasser six mois, même à basse température. La durée réelle dépend de l'état et du type de batterie, de la température et de la configuration de l'appareil ; vérifiez périodiquement la charge et [recharger l'appareil](power.md) lorsque cela est nécessaire.

## Ne retirez pas la batterie pour le stockage

L'appareil dispose de deux niveaux intelligents et d'un niveau électronique de protection de la batterie. Lorsque la charge tombe en dessous de 20 %, il entre automatiquement en mode d'économie d'énergie profonde et attend d'être chargé. Dans ce mode, sa consommation électrique est comparable à l'autodécharge de la batterie.

À titre d'estimation, même une charge de 20 % peut fournir près de deux ans d'autonomie en veille en sommeil profond. Ceci ne constitue pas une garantie de la durée de vie de la batterie lors de mesures régulières ou de transmission de données : l'état et le type de la batterie, la température et la configuration de l'appareil affectent tous le résultat.

!!! danger "N'inversez pas la polarité"
    Ne retirez pas la batterie pour un stockage ou un chargement normal. Chaque réinstallation crée un risque d'inversion de polarité et d'endommagement permanent de l'appareil. Les exceptions sont [récupération d'urgence](../troubleshooting/recovery-after-storage.md) lorsque la tension est inférieure `3,5 В`, ou des travaux d'entretien effectués selon une procédure vérifiée.

Après le stockage, vérifiez la charge et l'heure de la batterie de l'appareil. Des recommandations supplémentaires sont disponibles sur le [Entretien](maintenance.md) page.
