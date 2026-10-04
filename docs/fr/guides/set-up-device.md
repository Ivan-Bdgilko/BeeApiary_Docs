# Comment configurer une nouvelle balance BeeApiary

1. Chargez l'appareil via USB Type-C.

    !!! note "Choisir un chargeur et un câble"
        L'appareil ne prend pas en charge la charge rapide, y compris USB Power Delivery (PD). Utilisez une source d'alimentation standard avec un port USB Type-A et un câble USB Type-A – USB Type-C. Un câble USB Type-C – USB Type-C n’est pas recommandé pour le chargement.

2. Installez l'appareil et les capteurs conformément aux [directives de placement](../device/placement.md).
3. Insérez une micro-SIM avec la protection PIN désactivée.

    Utilisez le format micro-SIM :

    ![Comparaison des formats de cartes SIM](../../assets/en/quick-start/gsm/micro-sim-format-comparison.png){ .doc-photo }

    Carte correctement installée :

    ![Micro-SIM correctement installée](../../assets/common/device/installation/micro-sim-insertion-orientation.jpeg){ .doc-photo }

    Insérez la carte SIM et enfoncez-la doucement presque complètement dans la fente jusqu'à ce que vous entendiez un léger clic confirmant qu'elle est verrouillée en place :

    ![micro-SIM verrouillée dans l'emplacement](../../assets/common/device/installation/micro-sim-locked-in-slot.jpeg){ .doc-photo }

4. Activez ou redémarrez l'appareil : maintenez brièvement la clé magnétique contre le marquage au dos de l'unité principale.

    ![BeeApiary clé magnétique](../../assets/common/device/installation/magnetic-key.png){ .doc-photo }

    ![Cible à clé magnétique de marque](../../assets/common/device/installation/magnetic-key-target.png){ .doc-photo }

    Pour plus d'informations, voir [Activation et redémarrage](../device/installation.md#activation-reset).

5. Connectez-vous à `apiary_net` et ouvert `http://192.168.4.1`.
6. Saisissez le numéro de téléphone du propriétaire au format international.
7. Se déconnecter de `apiary_net` et vérifiez le premier message SMS.

Résultat : l'appareil collecte les mesures, les envoie au propriétaire et stocke une archive.
