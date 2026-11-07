---
title: "Balances de ruche avec Wi-Fi — connexion directe et par réseau"
description: "Se connecter BeeApiary balance pour ruches en Wi-Fi : accès direct à votre téléphone et transmission à distance via le réseau rucher."
---

# Balances de ruche avec Wi-Fi — connexion directe et par réseau { #wi-fi- }

BeeApiary Les balances pour ruches avec Wi-Fi prennent en charge deux manières de recevoir des données : une connexion téléphonique directe au point d'accès de l'appareil (AP) et la transmission via le réseau Wi-Fi du rucher (STA). La première méthode fonctionne à proximité des balances ; le second fournit un accès aux données à distance lorsque la connectivité Internet est disponible.

## Connexion directe à l'appareil { #direct-access-point }

Après activation avec la clé magnétique, l'appareil crée temporairement un point d'accès local. Il est généralement disponible pendant environ une minute, mais cet intervalle peut être modifié dans les paramètres.

Paramètres par défaut :

```text
SSID: apiary_net
Mot de passe: apiary_wifi
Interface web: http://192.168.4.1
```

Grâce à la connexion locale, vous pouvez :

- permettre à l'application de récupérer les archives de mesures ;
- ouvrez l'interface Web ;
- configurer le numéro de téléphone du propriétaire et l'horaire ;
- afficher le niveau de charge et la version du micrologiciel ;
- utilisez FTP pour accéder aux fichiers sur la carte microSD.

Une fois le téléphone connecté à `apiary_net`, l'application trouve l'appareil et affiche l'invite **"Appareil à proximité. Récupérer les archives ?"**. Les données ne sont téléchargées qu'après que l'utilisateur a confirmé la demande.

!!! warning "Changer le mot de passe"
    Le mot de passe par défaut est connu publiquement. Après la première vérification, définissez votre propre mot de passe pouvant contenir jusqu'à 32 caractères.

Procédures détaillées :

- [Connectez-vous au point d'accès de l'appareil](../guides/configure-local-wifi.md);
- [téléchargez l'archive sur l'application](../guides/download-archive.md);
- [afficher les paramètres supplémentaires de l'appareil](../device/additional-settings.md).

## Routage via le réseau Wi-Fi Apiary { #apiary-wifi-routing }

L'appareil peut se connecter à un réseau Wi-Fi existant au niveau du rucher et envoyer automatiquement des données via Internet à l'application du propriétaire. Le téléphone peut être n’importe où avec accès à Internet.

Cette méthode ne nécessite pas une carte SIM distincte dans chaque appareil, mais un réseau Wi-Fi configuré avec accès à Internet doit être disponible à proximité de l'appareil.

### Comment fonctionne la configuration

Enregistre un appareil déjà connu de l’application : le service crée des identifiants et des clés. Transfère ensuite les paramètres du réseau du rucher depuis le téléphone via le point d’accès `apiary_net` de l’appareil.

Après un redémarrage avec la clé magnétique ou lors du prochain cycle horaire programmé, l'appareil utilise le réseau configuré pour la transmission automatique. Le téléphone n'a plus besoin d'être à proximité.

### Exigences

- le dispositif a déjà été ajouté à l’application ;
- l'application a reçu ses données au moins une fois par SMS ou par téléchargement direct d'archives ;
- le téléphone a accès à Internet lors de l'inscription ;
- un réseau Wi-Fi avec accès Internet est disponible à proximité de l'appareil ;
- l'utilisateur connaît le nom et le mot de passe de ce réseau.

Le relais en ligne n’est pas un stockage permanent : les données restent sur la balance et le téléphone. Le service peut devenir instable ou payant ; la compatibilité et les autres conditions figurent dans le guide.

Pour la procédure étape par étape, voir [Configurer la synchronisation via le réseau Wi-Fi Apiary](../guides/configure-wifi-sync.md).
