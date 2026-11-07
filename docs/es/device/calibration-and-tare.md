# Calibración y Tara

!!! danger "Un dispositivo nuevo no necesita calibración"
    La calibración se requiere principalmente después de una reparación o pérdida de datos de calibración de fábrica. No lo utilice como una forma general de solucionar problemas de una lectura de peso incorrecta.

<span id="calibration"></span>
## Calibración

1. Desconecte la fuente de alimentación externa.
2. Coloque todos los sensores de peso en una superficie firme y nivelada y deje la plataforma vacía.
3. Conéctese al punto de acceso del dispositivo y abra **Ajustes generales → Ajustes de báscula** en su interfaz web.

    ![Botón para abrir la configuración de la báscula.](../../assets/en/device/calibration-and-tare/open-scale-settings.png){ .doc-screenshot }

4. Empezar **Calibración cero** y espera a que termine sin tocar la plataforma.

    La pantalla muestra dos etapas de calibración:

    ![Etapas de calibración de básculas.](../../assets/en/device/calibration-and-tare/calibration-steps.png){ .doc-screenshot }

    ![Calibración cero en progreso](../../assets/en/device/calibration-and-tare/zero-calibration-progress.png){ .doc-screenshot }

5. Seleccione un peso de referencia disponible de 500, 1000 o 5000 g y colóquelo en la plataforma.

    ![Seleccionar el peso de referencia](../../assets/en/device/calibration-and-tare/reference-weight-selection.png){ .doc-screenshot }

6. Empezar **Calibración de referencia** y espera el resultado.

    ![Calibración de referencia en curso](../../assets/en/device/calibration-and-tare/reference-weight-calibration-progress.png){ .doc-screenshot }

    ![resultado de la calibración de la balanza](../../assets/en/device/calibration-and-tare/calibration-result.png){ .doc-screenshot }

Resultado: el dispositivo guardó los nuevos valores de calibración. Comprueba que se muestra el peso de referencia.

<span id="tare"></span>
## tara

La tara excluye el peso de la plataforma u otra estructura permanente.

1. [Conéctate a la interfaz web de la báscula](../guides/configure-local-wifi.md).
2. Abre **Configuración general → Configuración de la báscula**.
3. Elige un método:

    - Si conoces el peso de la tara, introdúcelo en gramos y selecciona **Establecer peso de tara**.

        ![Introducir una tara conocida](../../assets/en/device/calibration-and-tare/known-tare-weight-form.png){ .doc-screenshot }

    - O deja la estructura sobre los sensores y acepta el valor actual como cero.

        ![Aceptar el peso actual como cero](../../assets/en/device/calibration-and-tare/use-current-weight-as-zero.png){ .doc-screenshot }

4. Comprueba la lectura al terminar.

Resultado: el dispositivo resta la tara de las mediciones posteriores. La tara no cambia el factor de calibración de fábrica.
