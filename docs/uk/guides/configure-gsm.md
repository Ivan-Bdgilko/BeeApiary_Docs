---
translation_status: not_ready
---

# Як налаштувати GSM

!!! attention "Зверніть увагу"
    Номер користувача зазвичай уже налаштований виробником. Ця інструкція допоможе перевірити, змінити або видалити його за потреби.

1. Переконайтеся, що micro-SIM активна, має покриття й не захищена PIN-кодом.
2. [Підключіться до точки доступу пристрою](configure-local-wifi.md) і відкрийте його вебінтерфейс.

    На сторінці загальних налаштувань вебінтерфейсу пристрою доступні кнопки основного й додаткового номера:

    ![Номери користувача в загальних налаштуваннях вебінтерфейсу пристрою](../../assets/uk/guides/configure-gsm/user-phone-number-settings.png){ .doc-screenshot }

3. Відкрийте налаштування **Основний номер** або **Додатковий номер**.

    ![Форма основного номера у вебінтерфейсі пристрою](../../assets/uk/guides/configure-gsm/primary-phone-number-form.png){ .doc-screenshot }

    ![Форма додаткового номера у вебінтерфейсі пристрою](../../assets/uk/guides/configure-gsm/additional-phone-number-form.png){ .doc-screenshot }

4. Введіть номер у форматі `+380XXXXXXXXX`.
5. Виберіть **Для людини** для звичайних SMS або **Для Android** для стислих SMS у застосунку.

    ![Вибір формату SMS Для Android у вебінтерфейсі пристрою](../../assets/uk/system/gsm-and-sms/android-message-format.png){ .doc-screenshot }

    ![Вибір формату SMS Для людини у вебінтерфейсі пристрою](../../assets/uk/system/gsm-and-sms/human-message-format.png){ .doc-screenshot }

6. Відкрийте **Переглянути розклад відправки**, виберіть години й натисніть **Створити та зберегти**.

    ![Перехід до розкладу відправки у вебінтерфейсі пристрою](../../assets/uk/system/gsm-and-sms/open-sending-schedule.png){ .doc-screenshot }

    ![Вибір годин відправки SMS у вебінтерфейсі пристрою](../../assets/uk/system/gsm-and-sms/sending-hours-selection.png){ .doc-screenshot }

    ![Збережений розклад із відправкою кожні чотири години у вебінтерфейсі пристрою](../../assets/uk/system/gsm-and-sms/saved-four-hour-schedule.png){ .doc-screenshot }

    Після збереження номер відображається у вебінтерфейсі:

    ![Збережений номер у вебінтерфейсі](../../assets/uk/guides/configure-gsm/saved-primary-phone-number.png){ .doc-screenshot }

    ![Номер пристрою у вебінтерфейсі](../../assets/uk/guides/configure-gsm/device-phone-number.png){ .doc-screenshot }

7. Від'єднайтеся від `apiary_net` і дочекайтеся першого SMS.

Щоб прибрати номер, задайте `+000000000000`. Формати й розклад описані на сторінці [GSM та SMS](../system/gsm-and-sms.md).
