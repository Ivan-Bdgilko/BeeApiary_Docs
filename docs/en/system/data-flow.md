# Data Flow

1. At the start of each hour, the BeeApiary measuring device takes the configured measurements.
2. The result is saved to the local microSD archive when the card is available.
3. The device makes the data available through the configured channel:

    - sends a regular or compact SMS message according to the schedule;
    - routes data through the apiary Wi-Fi network;
    - [transmits available data over Bluetooth](bluetooth.md) when the phone is nearby;
    - provides the archive to the app through its own access point after user confirmation.

4. The app recognizes the received values and adds them to the phone's local storage.
5. The user views current values, history, and charts.

The absence of GSM, Wi-Fi, Bluetooth, or a nearby phone does not stop the core measurement process. The data can be transferred to the app when a connection becomes available.

When data is routed remotely through Wi-Fi, the online relay does not store it. Permanent copies remain on the measuring device and the user's phone.

For a channel comparison, see [Receiving Data in the App](connectivity.md).

To configure the remote channel, see [Synchronization Through the Apiary Wi-Fi Network](../guides/configure-wifi-sync.md).

To configure the local automatic channel, see [Bluetooth Synchronization](../guides/configure-bluetooth-sync.md).
