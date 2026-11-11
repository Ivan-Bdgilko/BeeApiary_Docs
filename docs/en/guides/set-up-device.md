# How to Set Up BeeApiary Beehive Scales

1. Charge the device through USB Type-C.

    !!! note "Choosing a charger and cable"
        The device does not support fast charging, including USB Power Delivery (PD). Use a standard power source with a USB Type-A port and a USB Type-A–USB Type-C cable. A USB Type-C–USB Type-C cable is not recommended for charging.

2. Install the device and sensors according to the [placement guidelines](../device/placement.md).
3. Insert a micro-SIM with PIN protection disabled.

    Use the micro-SIM format:

    ![Comparison of SIM card formats](../../assets/en/quick-start/gsm/micro-sim-format-comparison.png){ .doc-photo }

    Correctly installed card:

    The GSM module is in a different location on older boards made before 2026 and newer boards from 2026 onward.

    **Older board (before 2026):**

    ![Correctly installed micro-SIM](../../assets/common/device/installation/micro-sim-insertion-orientation.jpeg){ .doc-photo }

    **Newer board (from 2026):**

    ![micro-SIM orientation on the newer board](../../assets/common/device/installation/micro-sim-new-board-orientation.png){ .doc-photo }

    Insert the SIM card and gently press it almost completely into the slot until you hear a soft click confirming that it is locked in place:

    **Older board (before 2026):**

    ![micro-SIM locked in the slot](../../assets/common/device/installation/micro-sim-locked-in-slot.jpeg){ .doc-photo }

    **Newer board (from 2026):**

    ![micro-SIM locked on the newer board](../../assets/common/device/installation/micro-sim-new-board-locked.png){ .doc-photo }

4. <span id="activation-reset"></span>Activate or restart the device: briefly hold the magnetic key against the branded mark on the back of the main unit.

    ![BeeApiary magnetic key](../../assets/common/device/installation/magnetic-key.png){ .doc-photo }

    ![Branded magnetic-key target](../../assets/common/device/installation/magnetic-key-target.png){ .doc-photo }

5. If you need to check or change settings, [connect to `apiary_net`](configure-local-wifi.md) and open `http://192.168.4.1`. Otherwise, skip this step.
6. The owner's number is usually configured by the manufacturer. Only if necessary, [check, change or remove the number in the GSM settings](configure-gsm.md).
7. If you connected to `apiary_net`, disconnect. Wait for the first SMS: it usually arrives before the device goes to sleep, about one minute after disconnection or activation.

    After changing transmission settings, calibration or other settings, you may need to wait for the device to sleep and activate it again with the magnetic key, without reconnecting to `apiary_net`.

Result: the device collects measurements, sends them to the owner, and stores an archive.
