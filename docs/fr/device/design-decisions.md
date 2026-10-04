# Pourquoi BeeApiary fonctionne ainsi

## De la BeeApiary Créateurs

BeeApiary a été conçu comme un outil autonome qui garde les données et les décisions clés sous le contrôle de l'apiculteur. Cette page explique plusieurs choix de conception et de logiciels qui peuvent ne pas être immédiatement évidents.

## Pourquoi les couvertures sont-elles transparentes ?

Le couvercle transparent vous permet de voir quand l'appareil fonctionne et si de la condensation, des insectes ou de la saleté sont entrés dans le boîtier. Cela facilite l’inspection sans ouvrir inutilement le boîtier.

Le projet est ouvert aux retours d'expérience et aux suggestions : sa construction ne cache pas l'état des principaux composants au propriétaire.

## Pourquoi n’y a-t-il pas de stockage obligatoire sur le serveur ?

Le fonctionnement principal de la balance pour ruches et de l'application ne dépend pas d'une BeeApiary stockage sur un serveur externe. Les mesures sont stockées sur le [la carte microSD de l'appareil](../system/data-storage.md) et localement sur le téléphone de l'utilisateur. Le système ne nécessite pas de stockage centralisé de la localisation ou de l'historique des activités du propriétaire.

Un service de relais optionnel peut être utilisé pour [synchronisation via le réseau Wi-Fi du rucher](../system/local-wifi.md#apiary-wifi-routing). Il transfère les données vers l'application mais ne constitue pas un stockage permanent et n'est pas nécessaire pour les autres canaux de communication.

## Pourquoi le GSM utilise-t-il les SMS ?

Sur le terrain ou lors du déplacement d'un rucher, les SMS sont souvent disponibles là où l'accès à l'Internet mobile n'est pas fiable. Un forfait SMS minimal suffit et l'application reçoit des données sans abonnement au serveur séparé.

Avec le format de message approprié, deux messages SMS par jour peuvent fournir les résultats de toutes les mesures horaires collectées au cours de cette journée. L'application fonctionne directement sur le téléphone du propriétaire et, dans une configuration typique, peut gérer jusqu'à cinq appareils ; ce nombre peut être augmenté si nécessaire.

Pour plus de détails, voir [GSM et SMS](../system/gsm-and-sms.md).

## Pourquoi les mesures sont-elles prises toutes les heures ?

Un historique horaire permet de révéler les départs des abeilles le matin et leurs retours le soir, les changements de poids pendant le séchage du nectar et les variations de température quotidiennes. Ces données fournissent une base pour une analyse plus approfondie de la force de la colonie, des réserves alimentaires et d'autres processus à l'intérieur de la ruche.

## Pourquoi les messages SMS ne sont-ils pas envoyés toutes les heures ?

Une transmission fréquente n’améliore pas les mesures elles-mêmes, mais consomme de l’énergie de la batterie et du crédit de communication. L'envoi de plusieurs messages par jour transfère les données horaires accumulées beaucoup plus efficacement.

Une estimation pratique pour deux messages SMS par jour est d'au moins 160 jours de fonctionnement avec une seule charge. Il s'agit d'une ligne directrice et non d'une garantie : la durée de vie de la batterie dépend de la batterie, de la configuration de l'appareil, de la température, de la couverture GSM et des canaux de transmission activés.

Si un capteur d'alarme est installé, un événement d'urgence ou une tentative de déplacement de la ruche peut déclencher séparément un appel et un SMS sans attendre l'horaire habituel.

## Pourquoi la batterie ne doit-elle pas être retirée ?

L'appareil dispose de trois niveaux de protection de la batterie et passe automatiquement en mode d'économie d'énergie lorsque la charge est faible. La batterie n'a pas besoin d'être retirée pour le stockage, tandis qu'une polarité incorrecte lors de la réinstallation peut endommager définitivement l'électronique.

Les exceptions et les règles d'entreposage hivernal sont décrites dans [Alimentation et chargement](power.md) et [Utilisation et stockage hivernaux](winter-use-and-storage.md).

## Pourquoi les mises à jour du micrologiciel ne sont-elles pas automatiques ?

Le propriétaire décide quand mettre à jour l'appareil et si les fonctionnalités d'une nouvelle version sont nécessaires. Une mise à jour contrôlée réduit le risque de changements inattendus dans le comportement d'un système autonome.

Les balances pour ruches peuvent fonctionner sans téléphone comme balances autonomes et enregistreur de données météorologiques. L'application Android étend les fonctionnalités de visualisation, de journal du rucher et de synchronisation, mais n'est pas requise pour les mesures. Procédure : [Mettre à jour l'appareil](../guides/update-device.md).

## Combien de temps les mesures sont-elles conservées ?

L'archive sur la carte microSD n'est pas limitée à un an. La durée de conservation dépend de la capacité et de l'état de la carte ; avec un volume de mesures normal, il est suffisant pour la durée de vie attendue de l'appareil.

## Deux types de SMS et un horaire flexible. Pourquoi?

Il existe de nombreuses opinions sur quand, comment et où commencer à prendre des mesures ; pour résoudre ce problème, les utilisateurs peuvent configurer librement le format des SMS et l'heure d'envoi selon leurs préférences. Cependant, il existe certaines recommandations concernant le nombre de messages par jour afin d'économiser de l'énergie.
