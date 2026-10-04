# Comment configurer la synchronisation Bluetooth

!!! danger "Compatibilité des appareils"
    Cette fonctionnalité n'est prise en charge que par les appareils fabriqués après août 2026. Les appareils fabriqués antérieurement peuvent également bénéficier de cette fonctionnalité, mais ils doivent être mis à jour en usine. Il n’existe actuellement aucun correctif simple que vous puissiez installer vous-même.

Cette procédure met en place une récupération automatique des données depuis BeeApiary balances de ruche lorsque le téléphone est à proximité. La synchronisation ne nécessite ni carte SIM ni accès Internet.

## Avant de commencer

1. Assurez-vous que les balances répondent aux exigences de compatibilité ci-dessus.
2. [Synchroniser l'horloge de la balance](../system/time-synchronization.md) avec le téléphone. La différence ne doit pas dépasser deux minutes.
3. Activez Bluetooth sur le téléphone.
4. Accordez à l'application toutes les autorisations demandées, y compris les autorisations Bluetooth.
5. Autorisez l'application à s'exécuter en arrière-plan et à se réveiller à l'heure requise. Revoir le courant [recommandations d'installation d'applications](../app/installation.md).

!!! warning "Vérifiez l'heure avant l'installation"
    Si la différence dépasse deux minutes, la balance peut devenir disponible avant ou après le début de l'écoute du téléphone, empêchant ainsi la synchronisation automatique.

## Activer les informations BLE sur les balances

1. [Connectez-vous au point d'accès de la balance](configure-local-wifi.md).
2. Ouvert `http://192.168.4.1` et sélectionnez **Paramètres supplémentaires**.
3. Sélectionnez **BLE info** et enregistrez les modifications.

Cette option et les autres commutateurs sont expliqués sous [Paramètres supplémentaires de l'appareil](../device/additional-settings.md).

## Activer la synchronisation dans l'application

4. Ouvrez le menu principal de l'application, accédez à **Paramètres**, et ouvrez **Paramètres supplémentaires**.
5. Activer **Rechercher des appareils BLE** afin que l'application puisse trouver des balances à proximité et recevoir des mesures.
6. Activer **Histoire du BLE** afin que l'application récupère également l'historique stocké, y compris les données de la veille.

    ![Options Bluetooth dans les paramètres supplémentaires du BeeApiary Application Android](../../assets/en/app/additional-settings/app-additional-settings.jpg){ .doc-screenshot }

    !!! warning "Activer les options requises"
        La capture d'écran est un exemple général, donc les deux commutateurs Bluetooth sont affichés comme désactivés. **Rechercher des appareils BLE** doit être activé pour la synchronisation. Activation **Histoire du BLE** est également recommandé afin que l'application puisse récupérer l'historique disponible et restaurer les mesures manquées.

    Pour une description complète de cet écran, voir [Paramètres d'application supplémentaires](../app/additional-settings.md).

7. Revenez à l'écran d'accueil de l'application. Gardez le Bluetooth activé et le téléphone à portée Bluetooth fiable pendant le prochain cycle horaire.

## Vérifiez le résultat

La synchronisation se produit uniquement lorsque **BLE info** est activé sur la balance et Bluetooth et les options d'application correspondantes sont activées sur le téléphone. La balance devient disponible pour communiquer lors d'un réveil programmé ou après [activation avec la clé magnétique](../device/installation.md#activation-reset).

L'application peut échanger des données lorsqu'elle est ouverte ou en arrière-plan si Android lui permet de s'exécuter et de se réveiller à l'heure requise.

8. Attendez un message confirmant que les données ont été reçues.

    ![Résultat de la réception des mesures via Bluetooth dans le BeeApiary application](../../assets/en/system/bluetooth/bluetooth-sync-result.jpg){ .doc-screenshot }

    Cette fenêtre affiche :

    - le nom de la ruche et le numéro de la balance ;
    - le dernier ensemble de mesures disponible pour la configuration de la balance ;
    - la date et l’heure de la mesure reçue ;
    - l’heure et le résultat de la synchronisation de l’horloge.

    Lors de la connexion à des balances qui n'ont pas encore été enregistrées, un **Ajouter un appareil** Le bouton peut également apparaître. Utilisez-le pour compléter la norme [procédure d'ajout BeeApiary balances pour ruches](../app/add-device.md) une fois. L’application les reconnaîtra alors automatiquement.

9. Appuyez sur **D'accord**. Si nécessaire, ouvrez à nouveau le dernier message via **BLE Info** dans le menu principal.
10. Assurez-vous que les nouvelles valeurs apparaissent sur l'écran d'accueil et les graphiques de l'application.

Terminé : lorsque le téléphone est à proximité, l'application récupérera automatiquement les données disponibles. Si la connexion était indisponible pendant plusieurs heures, activée **Histoire du BLE** peut restaurer les mesures manquées lors de la prochaine synchronisation réussie, dans la profondeur d'historique disponible d'un jour à une semaine.

Pour plus d'informations sur son fonctionnement, voir [Synchronisation des données Bluetooth](../system/bluetooth.md).
