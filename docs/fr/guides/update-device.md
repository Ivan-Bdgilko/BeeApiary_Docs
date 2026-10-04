# Comment mettre à jour le micrologiciel des balances BeeApiary

Avant la mise à jour, sélectionnez le micrologiciel correspondant à la génération de l'appareil et à la langue d'interface requise.

## Sélectionnez la génération du firmware

| Appareil | Source de mise à jour | État de développement |
|---|---|---|
| Fabriqué avant août 2026 | [Hive_Controller](https://github.com/Ivan-Bdgilko/Hive_Controller) | Le développement de fonctionnalités pour la version précédente n'est plus pris en charge |
| Fabriqué après août 2026 | [Hive_Controller_Ble](https://github.com/Ivan-Bdgilko/Hive_Controller_Ble) | La nouvelle version continue de recevoir des mises à jour et de nouvelles fonctionnalités |

!!! danger "Migration d'un ancien appareil vers la nouvelle version"
    Tout appareil fabriqué précédemment peut être migré vers la nouvelle version du logiciel, mais cela nécessite une mise à jour d'usine. Il n'existe actuellement aucun correctif simple pour une migration en libre-service, donc la procédure standard sur cette page ne migre pas un appareil entre les générations.

## Sélectionnez la langue du firmware

Les deux générations proposent des versions multilingues. Le suffixe dans le nom de la version identifie la langue :

| Suffixe | Langue |
|---|---|
| `-de` | Allemand |
| `-en` | Anglais |
| `-es` | Espagnol |
| `-fr` | Français |
| `-pl` | Polonais |
| `-uk` | Ukrainien |

Sélectionnez la langue en téléchargeant et en flashant le fichier correspondant. Les versions de langue sont accessibles au public dans les référentiels répertoriés ci-dessus, et d'autres langues peuvent être ajoutées ultérieurement si nécessaire.

## Mettre à jour l'appareil à l'aide de microSD

1. Attendez que l'appareil passe en mode veille, puis retirez la carte microSD.
2. Créer le `/fm` répertoire à la racine de la carte s'il n'existe pas déjà.
3. Placez le `Apiary.bin` mettre à jour le fichier dans `/fm`.
4. Réinsérez la carte microSD dans l'appareil.
5. [Activer ou redémarrer l'appareil](../device/installation.md#activation-reset) avec la clé magnétique.
6. Attendez un message SMS régulier contenant des mesures ; la mise à jour prend généralement jusqu'à deux minutes.
7. Au bas de la page d'accueil de l'interface Web, vérifiez la version du micrologiciel, le suffixe de langue, la date et l'heure de construction et le numéro unique de l'appareil.

![Version du micrologiciel, suffixe de langue, heure de construction et identifiant unique dans l'interface Web de l'appareil](../../assets/common/guides/update-device/device-version-build-time-and-id.png){ .doc-screenshot }

La chaîne de version complète inclut le suffixe de localisation, par exemple `-uk`. Comparez-le avec la version de mise à jour correspondante dans le référentiel pour la génération de votre appareil. La même page affiche également la date et l'heure de construction ainsi que l'identifiant unique de l'appareil.

!!! warning "Vérifiez le fichier avant de mettre à jour"
    Assurez-vous `Apiary.bin` est destiné à la génération de votre appareil et à la langue requise. Les méthodes de mise à jour du service via FTP ou un serveur sortent du cadre de cette procédure.
