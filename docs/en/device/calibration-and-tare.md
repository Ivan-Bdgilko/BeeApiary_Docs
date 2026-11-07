# Calibration and Tare

!!! danger "A new device does not need calibration"
    Calibration is primarily required after a repair or loss of factory calibration data. Do not use it as a general way to troubleshoot an incorrect weight reading.

<span id="calibration"></span>
## Calibration

1. Disconnect the external power supply.
2. Place all weight sensors on a firm, level surface and leave the platform empty.
3. Connect to the device access point and open **General Settings → Scale Settings** in its web interface.

    ![Button for opening scale settings](../../assets/en/device/calibration-and-tare/open-scale-settings.png){ .doc-screenshot }

4. Start **Zero Calibration** and wait for it to finish without touching the platform.

    The screen shows two calibration stages:

    ![Scale calibration stages](../../assets/en/device/calibration-and-tare/calibration-steps.png){ .doc-screenshot }

    ![Zero calibration in progress](../../assets/en/device/calibration-and-tare/zero-calibration-progress.png){ .doc-screenshot }

5. Select an available reference weight of 500, 1000, or 5000 g and place it on the platform.

    ![Selecting the reference weight](../../assets/en/device/calibration-and-tare/reference-weight-selection.png){ .doc-screenshot }

6. Start **Reference Calibration** and wait for the result.

    ![Reference calibration in progress](../../assets/en/device/calibration-and-tare/reference-weight-calibration-progress.png){ .doc-screenshot }

    ![Scale calibration result](../../assets/en/device/calibration-and-tare/calibration-result.png){ .doc-screenshot }

Result: the device has saved the new calibration values. Check that the reference weight is displayed.

<span id="tare"></span>
## Tare

Taring excludes the weight of the platform or another permanent structure.

1. [Connect to the scales' web interface](../guides/configure-local-wifi.md).
2. Open **General Settings → Scale Settings**.
3. Choose one method:

    - If the tare weight is known, enter it in grams and select **Set Tare Weight**.

        ![Entering a known tare weight](../../assets/en/device/calibration-and-tare/known-tare-weight-form.png){ .doc-screenshot }

    - Alternatively, leave the structure on the sensors and accept the current value as zero.

        ![Accepting the current weight as zero](../../assets/en/device/calibration-and-tare/use-current-weight-as-zero.png){ .doc-screenshot }

4. Check the reading when finished.

Result: the device subtracts the tare from subsequent measurements. Taring does not change the factory calibration factor.
