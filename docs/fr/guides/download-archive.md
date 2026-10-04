# Comment télécharger l'archive

Avant de commencer, assurez-vous que BeeApiary L'application est à jour via Google Play et les balances pour ruches exécutent un micrologiciel publié en août 2024 ou plus tard. Si la version installée est plus ancienne ou si vous n'êtes pas sûr de sa date, suivez [Mettre à jour le BeeApiary Micrologiciel des balances pour ruches](update-device.md).

Le téléchargement manuel des archives est utile lorsque les balances n'ont pas de carte SIM, que d'autres méthodes de synchronisation sont temporairement indisponibles ou que des lacunes apparaissent dans les mesures. L'application importe les données stockées et les ajoute à l'historique local.

!!! warning "microSD et charge de la batterie"
    Une carte microSD fonctionnelle contenant les données disponibles doit être installée dans la balance. Une connexion Wi-Fi directe maintient la balance active et augmente la consommation d'énergie, n'effectuez donc pas cette procédure plus d'une fois par jour, sauf si cela est nécessaire.

1. [Activez ou redémarrez le BeeApiary balances pour ruches](../device/installation.md#activation-reset) avec la clé magnétique.
2. Dans l'intervalle disponible, généralement environ une minute, connectez le téléphone à `apiary_net` et restez à proximité de la balance.
3. Ouvrez le BeeApiary application.
4. Attendez que l'application détecte automatiquement les balances à proximité.
5. Dans le **"Appareil à proximité. Télécharger l'archive ?"** invite, appuyez sur **Oui**.

    ![BeeApiary invite de l'application pour télécharger l'archive à partir d'un appareil à proximité](../../assets/en/guides/download-archive/nearby-device-archive-prompt.jpg){ .doc-screenshot }

6. Attendez la fin de l'importation, puis déconnectez immédiatement le téléphone de `apiary_net`. Une fois déconnectée, la balance peut passer en mode veille et éviter une décharge inutile de la batterie.
7. Affichez les données téléchargées à l'aide des écrans standard de l'application.

    ![BeeApiary écran d'accueil de l'application avec mesures importées](../../assets/en/app/main-screen/app-home-screen.png){ .doc-screenshot }

Après confirmation, l'application télécharge automatiquement l'archive et stocke une copie locale des mesures. Si d'autres chaînes ont manqué certaines données, l'archive peut combler les lacunes correspondantes dans l'historique. Le format d'archive et la durée de conservation sont décrits sous [Stockage des données](../system/data-storage.md).
