# Documents de service

Cette section est une archive de configuration technique pour le BeeApiary balances pour ruches. Il est destiné aux techniciens de service et aux utilisateurs expérimentés qui doivent restaurer ou inspecter manuellement des fichiers XML.

Les valeurs initiales de certains paramètres matériels et réseau dépendent de la configuration et de l'installation de l'appareil particulier.

!!! danger "Édition manuelle"
    Des broches matérielles, des valeurs d'étalonnage ou des intervalles d'entretien incorrects peuvent perturber les mesures ou le fonctionnement de l'appareil. Utilisez l'interface Web pour les modifications ordinaires. Créez toujours une sauvegarde du `/setting` répertoire avant de modifier les fichiers manuellement.

## Procédure sécuritaire

1. Attendez que l'appareil passe en mode veille. L'appareil n'a pas de bouton d'alimentation standard : pendant le fonctionnement, il est soit actif, soit en hibernation.
2. Retirez la carte microSD et enregistrez une copie complète du `/setting` annuaire.
3. Modifiez le XML dans un éditeur de texte sans modifier les noms de section ou d'attribut.
4. Assurez-vous que le XML en a un `<settings>` élément racine et que tous les guillemets et balises fermantes sont présents.
5. Réinsérez la carte microSD pendant que l'appareil est en veille. Les paramètres mis à jour sont appliqués lors du prochain chargement normal de la configuration ; certaines modifications apportées via l'interface Web ne prennent également effet qu'après un redémarrage.
6. Vérifiez les mesures, la communication et le journal d'entretien. Conservez la sauvegarde jusqu'à ce que la vérification soit terminée.

Lors de l'enregistrement, l'appareil peut normaliser le fichier : ajouter des sections ou des attributs manquants, remplacer les valeurs de repli et réécrire l'ordre des éléments.

## Fichiers

- [`/setting/mset.xml`](settings-reference.md) — réseau, GSM, heure, options matérielles, alarmes générales et BLE.
- [`/setting/<hive>.xml`](hive-settings-reference.md) — des capteurs pour une ruche particulière, le poids, le calendrier, la fréquence de contrôle et les alarmes de seuil.
- [Restauration de la configuration](recovery.md) - remplacement sécurisé de la microSD, restauration à partir d'une sauvegarde et vérification XML.

Le nom du fichier de la ruche est spécifié par le `hive1`, `hive2`, et les attributs suivants sans extension. Le `.xml` L’extension est ajoutée automatiquement.

## Niveaux d'accès

| Étiquette | Signification |
|---|---|
| `USER` | La valeur peut être modifiée via l'interface standard. |
| `ADVANCED` | Une compréhension de son effet sur la communication ou la logique de fonctionnement est nécessaire. |
| `SERVICE` | Les modifications manuelles peuvent rendre l'appareil inutilisable ou fausser les données. |

Dans les tableaux, `—` signifie que les limites ne s'appliquent pas au champ. **Valeur initiale** est la valeur dans une configuration nouvellement créée, et non dans le XML d'un périphérique particulier. **Si non défini** décrit la valeur utilisée lorsque l'attribut est absent, qui peut différer de la valeur initiale.

## Noms historiques

Les identifiants XML exacts ne sont pas corrigés même lorsqu'ils contiennent des erreurs : `apairy_set`, `sefe_start_interval`, `normal_pecision`, et `calibrate_pecision` doit rester exactement tel qu’écrit. L'orthographe `synсhronize` avec la lettre cyrillique `с` est incorrect ; utiliser `synchronize`.
