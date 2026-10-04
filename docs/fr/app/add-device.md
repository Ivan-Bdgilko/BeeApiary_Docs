# Ajouter une balance de ruche BeeApiary

Ajouter BeeApiary balances de pesée pour ruches pour relier un profil de ruche à un équipement physique et recevoir des lectures automatiques. Les canaux de données disponibles et leurs exigences sont décrits sous [Réception de données dans l'application](../system/connectivity.md).

## Ajouter la balance

1. Ouvert **Menu principal → Ajouter un appareil ou une ruche**.
2. Sur le **Appareils et ruches** écran, appuyez sur **Ajouter un appareil**.
3. Saisissez un nom clair pour la ruche ou la balance de ruche.
4. Si vous prévoyez de recevoir des données via GSM, saisissez le numéro de la carte SIM installée dans la balance pour ruche.

    ![Formulaire d'ajout BeeApiary balances pour ruches](../../assets/en/app/add-device/add-scales-form.jpg){ .doc-screenshot }

5. Appuyez sur **Insérer**.

Après enregistrement, le profil apparaît dans la liste des appareils et des ruches. Les données des balances physiques apparaîtront après la configuration et le premier échange réussi via l'un des [chaînes prises en charge](../system/connectivity.md).

## Ajouter à l'aide d'une carte NFC

Vous pouvez ajouter la balance pour ruche lorsque l'application reconnaît une carte NFC. Dans ce cas, l’application crée le profil et y associe en même temps la carte.

1. Tenez la carte NFC à proximité du téléphone.
2. Lorsqu'on vous demande si vous souhaitez utiliser la carte comme identifiant de ruche, sélectionnez l'action requise :
   - **Lien vers l'existant** — sélectionnez un profil déjà créé ;
   - **Ajouter un nouveau** — créez un nouveau profil avec ce lien NFC.

    ![Sélection de la manière de lier une carte NFC reconnue](../../assets/en/app/add-device/nfc-card-binding-choice.jpg){ .doc-screenshot }

3. Après avoir sélectionné **Ajouter un nouveau**, saisissez un nom et, pour le GSM, le numéro de la carte SIM installée dans la balance pour ruches.
4. Appuyez sur **Insérer**.

    ![Ajout BeeApiary balances pour ruches avec liaison par carte NFC](../../assets/en/app/add-device/add-scales-with-nfc-form.jpg){ .doc-screenshot }

Pour plus d'informations sur l'identification des ruches et les actions disponibles, voir [Balises et actions NFC](nfc-settings.md).
