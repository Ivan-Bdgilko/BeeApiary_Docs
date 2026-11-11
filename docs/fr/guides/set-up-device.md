# Comment configurer la balance BeeApiary

1. Chargez l'appareil via USB Type-C.

    !!! note "Choisir un chargeur et un câble"
        L'appareil ne prend pas en charge la charge rapide, y compris USB Power Delivery (PD). Utilisez une source d'alimentation standard avec un port USB Type-A et un câble USB Type-A – USB Type-C. Un câble USB Type-C – USB Type-C n’est pas recommandé pour le chargement.

2. Installez l'appareil et les capteurs conformément aux [directives de placement](../device/placement.md).
3. Insérez une micro-SIM avec la protection PIN désactivée.

    Utilisez le format micro-SIM :

    ![Comparaison des formats de cartes SIM](../../assets/fr/quick-start/gsm/micro-sim-format-comparison.png){ .doc-photo }

    Carte correctement installée :

    L’emplacement du module GSM diffère entre les cartes antérieures à 2026 et les cartes plus récentes à partir de 2026.

    **Ancienne carte (avant 2026) :**

    ![Micro-SIM correctement installée](../../assets/common/device/installation/micro-sim-insertion-orientation.jpeg){ .doc-photo }

    **Carte plus récente (à partir de 2026) :**

    ![Orientation de la micro-SIM sur la carte plus récente](../../assets/common/device/installation/micro-sim-new-board-orientation.png){ .doc-photo }

    Insérez la carte SIM et enfoncez-la doucement presque complètement dans la fente jusqu'à ce que vous entendiez un léger clic confirmant qu'elle est verrouillée en place :

    **Ancienne carte (avant 2026) :**

    ![micro-SIM verrouillée dans l'emplacement](../../assets/common/device/installation/micro-sim-locked-in-slot.jpeg){ .doc-photo }

    **Carte plus récente (à partir de 2026) :**

    ![micro-SIM verrouillée sur la carte plus récente](../../assets/common/device/installation/micro-sim-new-board-locked.png){ .doc-photo }

4. <span id="activation-reset"></span>Activez ou redémarrez l'appareil : maintenez brièvement la clé magnétique contre le marquage au dos de l'unité principale.

    ![BeeApiary clé magnétique](../../assets/common/device/installation/magnetic-key.png){ .doc-photo }

    ![Cible à clé magnétique de marque](../../assets/common/device/installation/magnetic-key-target.png){ .doc-photo }

5. Pour vérifier ou modifier les paramètres, [connecte-toi à `apiary_net`](configure-local-wifi.md) et ouvre `http://192.168.4.1`. Sinon, passe cette étape.
6. Le numéro du propriétaire est généralement configuré par le fabricant. Si nécessaire seulement, [vérifie, modifie ou supprime ce numéro dans les paramètres GSM](configure-gsm.md).
7. Si tu étais connecté à `apiary_net`, déconnecte-toi. Attends le premier SMS : il arrive généralement avant la mise en veille, environ une minute après la déconnexion ou l’activation.

    Après une modification de la transmission, de l’étalonnage ou d’autres paramètres, il peut être nécessaire d’attendre la mise en veille puis de réactiver l’appareil avec la clé magnétique, sans se reconnecter à `apiary_net`.

Résultat : l'appareil collecte les mesures, les envoie au propriétaire et stocke une archive.
