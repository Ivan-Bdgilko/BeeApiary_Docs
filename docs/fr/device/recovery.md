# Restauration de la configuration

Cette page explique comment remplacer la carte microSD en toute sécurité, restaurer la configuration à partir d'une sauvegarde et vérifier les fichiers XML après le démarrage de l'appareil.

!!! danger "Ne retirez pas la carte microSD lorsque l'appareil est actif"
    L'appareil n'a pas de bouton d'alimentation standard. Avant de retirer ou d'installer la carte microSD, attendez que l'appareil passe en mode veille. Tout d'abord, enregistrez une copie complète du `/setting` annuaire.

## Normalisation automatique

- le fichier principal se trouve à `/setting/mset.xml`;
- si le fichier principal est manquant, l'appareil peut créer une configuration initiale ;
- un fichier de ruche manquant ou incomplet peut être à nouveau enregistré en utilisant les valeurs de repli de l'état actuel ;
- un disparu `hive`, `thermometer`, ou `schedule` section, ainsi qu'un existant incomplet `scales` section, déclenche la normalisation du fichier de la ruche ;
- un complètement disparu `scales` La section n'est pas une erreur : les balances ne sont tout simplement pas créées ;
- erreurs structurelles dans l'élément XML racine, le `apairy_set` section, ou la `hiveN` L'attribut peut empêcher la lecture de la configuration.

Création d'une initiale `mset.xml` ne signifie pas que chaque paramètre aura une valeur universelle. `UPLOAD_URL`, les informations d'identification FTP, les broches HX711 et certains autres champs dépendent de la configuration de l'appareil ou de la configuration individuelle.

!!! warning "Une sauvegarde est requise"
    Ne comptez pas sur la récupération automatique comme seule sauvegarde. Avant de remplacer la carte microSD, enregistrez l'intégralité `/setting` répertoire si la carte est encore lisible.

## Remplacer la carte microSD en toute sécurité

1. Attendez que l'appareil passe en mode veille.
2. Retirez la carte microSD et, si elle est lisible, copiez tout son contenu.
3. Préparez la carte microSD conformément aux exigences de la version matérielle spécifique de l'appareil.
4. Restaurer le `/setting` répertoire à partir d’une sauvegarde vérifiée.
5. S'il n'existe aucune sauvegarde, n'utilisez pas les valeurs d'étalonnage de la balance provenant d'un autre appareil. Restaurez d’abord un minimum [`mset.xml`](settings-reference.md#minimal-example), puis créez le fichier ruche sans `scales` ou effectuez la procédure d'étalonnage standard.
6. Installez la carte microSD pendant que l'appareil est en veille et attendez le prochain cycle de fonctionnement.
7. Vérifiez l'heure, le réseau, les numéros GSM, les capteurs disponibles, le calendrier et le poids.
8. Comparez les fichiers XML normalisés avec la sauvegarde : l'appareil peut avoir ajouté des champs avec des valeurs de repli ou des sections réécrites.

## Si la configuration ne peut pas être lue

1. Vérifiez que le fichier en possède un `<settings>` élément racine.
2. Vérifiez les noms exacts `apairy_set`, `synchronize`, `sefe_start_interval`, et `pecision` dans les trois champs de filtre.
3. Assurez-vous `hive_count` a une correspondance `hive1`…`hiveN` attributs.
4. Assurez-vous que chaque référence `/setting/<hive>.xml` le fichier existe.
5. N'essayez pas de résoudre le problème en copiant `scales` depuis un autre appareil. Retirez temporairement la section balance et vérifiez le reste de la configuration.
6. Enregistrez les fichiers XML et les journaux de service problématiques à des fins de diagnostic.

Pour une description complète des champs, voir le [`mset.xml`](settings-reference.md) et [`HIVE*.XML`](hive-settings-reference.md) références.
