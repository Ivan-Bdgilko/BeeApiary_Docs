# Power Problems

!!! note "Charging"
    The device does not support fast charging, including USB Power Delivery (PD). For testing, use a standard power source with a USB Type-A port and a USB Type-A-to-USB Type-C cable. A USB Type-C-to-USB Type-C cable is not recommended.

1. After long-term storage, check the battery voltage. If it is below `3.5 V`, follow the [recovery procedure after storage](recovery-after-storage.md).
2. In other cases, connect a working standard power source to the USB Type-C port and allow the battery to charge.
3. Make sure the battery installed in the BeeApiary hive scales is intended for the configuration of that particular model. Models that use 18650 cells must have at least one such cell installed.
4. If the battery has been replaced, check its polarity against the markings on the holder.
5. After a critical discharge, allow the battery charge to recover; the device may resume normal operation during the next cycle.
6. After recovery, check the time and synchronize it if necessary.

!!! danger
    Do not attempt to power the device only from external USB without an 18650 cell. Incorrect battery polarity may permanently damage the device.

For details, see [Power](../device/power.md).
