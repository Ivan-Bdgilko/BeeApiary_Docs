# Añadir balanzas para colmenas BeeApiary

Añadir BeeApiary básculas de pesaje de colmena para vincular un perfil de colmena a un equipo físico y recibir lecturas automáticas. Los canales de datos disponibles y sus requisitos se describen en [Recibir datos en la aplicación](../system/connectivity.md).

## Añadir las básculas

1. Abierto **Menú principal → Agregar dispositivo o colmena**.
2. en el **Dispositivos y colmenas.** pantalla, toque **Agregar dispositivo**.
3. Introduzca un nombre claro para la báscula para colmenas o colmena.
4. Si planea recibir datos vía GSM, ingrese el número de la tarjeta SIM instalada en la báscula para colmenas.

    ![Formulario para agregar BeeApiary balanzas de colmena](../../assets/en/app/add-device/add-scales-form.jpg){ .doc-screenshot }

5. Toque **Insertar**.

Después de guardar, el perfil aparece en la lista de dispositivos y colmenas. Los datos de las básculas físicas aparecerán después de la configuración y del primer intercambio exitoso a través de uno de los [canales soportados](../system/connectivity.md).

## Agregar usando una tarjeta NFC

Puede agregar la báscula para colmenas cuando la aplicación reconozca una tarjeta NFC. En este caso, la aplicación crea el perfil y vincula la tarjeta al mismo al mismo tiempo.

1. Sostenga la tarjeta NFC cerca del teléfono.
2. Cuando se le pregunte si desea utilizar la tarjeta como identificador de colmena, seleccione la acción requerida:
   - **Enlace a existente** — seleccione un perfil que ya haya sido creado;
   - **Agregar nuevo** — crea un nuevo perfil con este enlace NFC.

    ![Seleccionar cómo vincular una tarjeta NFC reconocida](../../assets/en/app/add-device/nfc-card-binding-choice.jpg){ .doc-screenshot }

3. Después de seleccionar **Agregar nuevo**, introduzca un nombre y, para GSM, el número de la tarjeta SIM instalada en la báscula para colmenas.
4. Toque **Insertar**.

    ![Añadiendo BeeApiary Balanzas para colmenas con enlace de tarjeta NFC](../../assets/en/app/add-device/add-scales-with-nfc-form.jpg){ .doc-screenshot }

Para obtener más información sobre la identificación de colmenas y las acciones disponibles, consulte [Etiquetas y acciones NFC](nfc-settings.md).
