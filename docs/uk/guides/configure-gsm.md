# Як налаштувати GSM

1. Переконайтеся, що micro-SIM активна, має покриття й не захищена PIN-кодом.
2. Підключіться до [локальної мережі Wi-Fi](configure-local-wifi.md).

    На сторінці загальних налаштувань доступні кнопки основного й додаткового номера:

    ![Номери користувача в загальних налаштуваннях](../../assets/uk/guides/configure-gsm/user-phone-number-settings.png){ .doc-screenshot }

3. Відкрийте налаштування **Основний номер** або **Додатковий номер**.

    ![Форма основного номера](../../assets/uk/guides/configure-gsm/primary-phone-number-form.png){ .doc-screenshot }

    ![Форма додаткового номера](../../assets/uk/guides/configure-gsm/additional-phone-number-form.png){ .doc-screenshot }

4. Введіть номер у форматі `+380XXXXXXXXX`.
5. Виберіть звичайний або стислий формат SMS.
6. Відкрийте розклад, виберіть години й натисніть **Створити та зберегти**.
7. Від'єднайтеся від `apiary_net` і дочекайтеся першого SMS.

    Після збереження номер відображається у вебінтерфейсі:

    ![Збережений номер у вебінтерфейсі](../../assets/uk/guides/configure-gsm/saved-primary-phone-number.png){ .doc-screenshot }

    ![Номер пристрою у вебінтерфейсі](../../assets/uk/guides/configure-gsm/device-phone-number.png){ .doc-screenshot }

Щоб прибрати номер, задайте `+000000000000`. Формати й розклад описані на сторінці [GSM та SMS](../system/gsm-and-sms.md).
