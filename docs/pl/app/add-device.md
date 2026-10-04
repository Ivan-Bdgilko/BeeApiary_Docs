# Dodawanie wagi pasiecznej BeeApiary

Dodaj BeeApiary Wagi do ważenia uli umożliwiające połączenie profilu ula ze sprzętem fizycznym i otrzymywanie automatycznych odczytów. Dostępne kanały danych i ich wymagania opisano poniżej [Odbieranie danych w aplikacji](../system/connectivity.md).

## Dodaj wagę

1. Otwórz **Menu główne → Dodaj urządzenie lub ul**.
2. Na **Urządzenia i ule** ekranie, dotknij **Dodaj urządzenie**.
3. Wpisz czytelną nazwę ula lub wagi do ula.
4. Jeżeli planujesz odbierać dane poprzez sieć GSM, wprowadź numer karty SIM zainstalowanej w wadze ula.

    ![Formularz dodawania BeeApiary wagi do ula](../../assets/en/app/add-device/add-scales-form.jpg){ .doc-screenshot }

5. Kliknij **Wstaw**.

Po zapisaniu profil pojawi się na liście urządzeń i uli. Dane z wag fizycznych pojawią się po skonfigurowaniu i pierwszej udanej wymianie przez jedną z wag [obsługiwane kanały](../system/connectivity.md).

## Dodaj za pomocą karty NFC

Możesz dodać wagę do ula, gdy aplikacja rozpozna kartę NFC. W tym przypadku aplikacja tworzy profil i jednocześnie łączy z nim kartę.

1. Przytrzymaj kartę NFC w pobliżu telefonu.
2. Na pytanie, czy chcesz używać karty jako identyfikatora ula, wybierz żądaną czynność:
   - **Link do istniejącego** — wybierz profil, który został już utworzony;
   - **Dodaj nowe** — utwórz nowy profil za pomocą tego łącza NFC.

    ![Wybór sposobu połączenia rozpoznanej karty NFC](../../assets/en/app/add-device/nfc-card-binding-choice.jpg){ .doc-screenshot }

3. Po wybraniu **Dodaj nowe**, wpisz nazwę oraz, w przypadku GSM, numer karty SIM zainstalowanej w wadze ula.
4. Kliknij **Wstaw**.

    ![Dodawanie BeeApiary waga ula z łączem do karty NFC](../../assets/en/app/add-device/add-scales-with-nfc-form.jpg){ .doc-screenshot }

Więcej informacji na temat identyfikacji ula i dostępnych akcji znajdziesz w artykule [Tagi i akcje NFC](nfc-settings.md).
