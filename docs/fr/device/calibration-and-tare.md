# Calibrage et tare

!!! danger "Un nouvel appareil n'a pas besoin d'être calibré"
    L’étalonnage est surtout nécessaire après une réparation ou la perte des données d’étalonnage d’usine. Ne l’utilisez pas comme solution générale à une mesure de poids incorrecte.

<span id="calibration"></span>
## Calibrage

1. Débranchez l'alimentation externe.
2. Placez tous les capteurs de poids sur une surface ferme et plane et laissez la plateforme vide.
3. Connectez-vous au point d'accès de l'appareil et ouvrez **Paramètres généraux → Paramètres de la balance** dans son interface web.

    ![Bouton pour ouvrir les paramètres de la balance](../../assets/en/device/calibration-and-tare/open-scale-settings.png){ .doc-screenshot }

4. Commencer **Étalonnage du zéro** et attendez qu'il se termine sans toucher la plateforme.

    L'écran affiche deux étapes d'étalonnage :

    ![étapes d'étalonnage de la balance](../../assets/en/device/calibration-and-tare/calibration-steps.png){ .doc-screenshot }

    ![Calibrage du zéro en cours](../../assets/en/device/calibration-and-tare/zero-calibration-progress.png){ .doc-screenshot }

5. Sélectionnez un poids de référence disponible de 500, 1 000 ou 5 000 g et placez-le sur la plateforme.

    ![Sélection du poids de référence](../../assets/en/device/calibration-and-tare/reference-weight-selection.png){ .doc-screenshot }

6. Commencer **Étalonnage de référence** et attendez le résultat.

    ![Étalonnage de référence en cours](../../assets/en/device/calibration-and-tare/reference-weight-calibration-progress.png){ .doc-screenshot }

    ![résultat de l'étalonnage de la balance](../../assets/en/device/calibration-and-tare/calibration-result.png){ .doc-screenshot }

Résultat : l’appareil a enregistré les nouvelles valeurs d’étalonnage. Vérifie que le poids de référence est affiché.

<span id="tare"></span>
## Tarer

La tare permet d’exclure le poids de la plateforme ou d’une autre structure permanente.

1. [Connecte-toi à l’interface web de la balance](../guides/configure-local-wifi.md).
2. Ouvre **Paramètres généraux → Paramètres de la balance**.
3. Choisis une méthode :

    - Si le poids de tare est connu, saisis-le en grammes et sélectionne **Définir le poids de tare**.

        ![Saisir une tare connue](../../assets/en/device/calibration-and-tare/known-tare-weight-form.png){ .doc-screenshot }

    - Ou laisse la structure sur les capteurs et accepte la valeur actuelle comme zéro.

        ![Accepter le poids actuel comme zéro](../../assets/en/device/calibration-and-tare/use-current-weight-as-zero.png){ .doc-screenshot }

4. Vérifie la valeur affichée après l’opération.

Résultat : l’appareil soustrait la tare des mesures suivantes. La tare ne modifie pas le coefficient d’étalonnage d’usine.
