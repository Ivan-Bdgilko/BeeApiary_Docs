# Alimentation et chargement

L'appareil fonctionne à partir d'une ou deux cellules 18650 et se charge via USB Type-C. La source d'alimentation peut être un chargeur, une banque d'alimentation ou un panneau solaire en option.

!!! note "Choisir un chargeur et un câble"
    L'appareil ne prend pas en charge la charge rapide, y compris USB Power Delivery (PD). Utilisez une source d'alimentation standard avec un port USB Type-A et un câble USB Type-A – USB Type-C. Un câble USB Type-C – USB Type-C n’est pas recommandé pour le chargement.

![Port d'alimentation USB Type-C ouvert](../../assets/common/device/power/open-usb-type-c-port.jpeg){ .doc-photo }

Fermez le couvercle du port de protection après le chargement :

![Capot de protection fermé sur le port d'alimentation](../../assets/common/device/power/closed-usb-type-c-cover.jpeg){ .doc-photo }

- le voyant bleu reste allumé lorsque la batterie est complètement chargée et que l'alimentation externe est toujours connectée ;
- le niveau de charge est affiché dans les messages SMS et dans les paramètres généraux de l'interface web ;

  ![Charge de la batterie dans l'interface web](../../assets/en/device/power/battery-charge-status.png){ .doc-screenshot }

- en dessous de 20 %, l'appareil passe en mode d'économie d'énergie, arrête les mesures régulières et les messages SMS et vérifie périodiquement le niveau de charge ;
- après une décharge critique, la batterie se déconnecte automatiquement, et [synchronisation de l'heure](../system/time-synchronization.md) peut être nécessaire après le chargement.

!!! warning "Après un stockage à long terme"
    Si la tension de la batterie est inférieure `3,5 В`, n'essayez pas de restaurer l'appareil en utilisant uniquement son port USB. Suivez le [procédure de récupération après un stockage à long terme](../troubleshooting/recovery-after-storage.md).

!!! danger
    N'utilisez pas l'appareil sans une cellule 18650 installée. Respectez strictement la polarité lors du remplacement : une polarité incorrecte endommagera l'appareil.
