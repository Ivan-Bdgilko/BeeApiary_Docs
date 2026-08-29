# Recover the Device After Long-Term Storage

After long-term storage, the battery may be completely discharged and the device may not respond to a normal power connection. If the voltage of the 18650 cell is below `3.5 V`, recover the device in the following order.

!!! danger "Battery polarity"
    Before removing the battery, locate the `+` and `-` markings on the cell and holder. Remember or photograph the correct orientation. Installing the battery with reversed polarity may permanently damage the device.

1. Remove the battery from the device.
2. Charge it in a separate charger designed for 18650 cells.
3. After charging, check the battery voltage. Install it in the device only when the voltage is `4.0 V` or higher.
4. Install the battery, carefully following the marked polarity.
5. Connect a standard external power source to the device's USB Type-C port without Power Delivery (PD) fast charging. Use a charger with a USB Type-A port and a USB Type-A-to-USB Type-C cable; a USB Type-C-to-USB Type-C cable is not recommended.
6. With the battery installed and external power connected, [activate the device with the magnetic key](../device/installation.md#activation-reset).
7. Synchronize the time in one of these ways:

    - [connect to the device access point over Wi-Fi](../guides/configure-local-wifi.md) and open its home page — this method is available by default;
    - [set up Bluetooth synchronization](../guides/configure-bluetooth-sync.md), open the BeeApiary app, and leave the phone near the device — this method works only when the corresponding settings are enabled on both the device and in the app.

8. Make sure the date and time are correct and the last synchronization timestamp has been updated.

The device is ready for normal operation after power and time have been restored.

See also [Power and Charging](../device/power.md) and [Time Synchronization](../system/time-synchronization.md).
