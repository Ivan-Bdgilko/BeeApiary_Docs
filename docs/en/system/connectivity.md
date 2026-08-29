# Receiving Data in the App

Data from the BeeApiary measuring device can reach the app in four ways. The right choice depends on the phone's location and the connection available near the device.

| Channel | Phone location | Requirements | How data reaches the app |
|---|---|---|---|
| [GSM and SMS](gsm-and-sms.md) | Anywhere with mobile coverage | A SIM card in the device with a basic SMS plan | The app processes SMS messages automatically; mobile Internet is not required |
| [Direct connection to the device access point](local-wifi.md#direct-access-point) | Near the device | Activate the device with the magnetic key and connect to `apiary_net` within the available interval, usually about one minute | The app finds the device, asks for permission to retrieve the archive, and imports the data after confirmation |
| [Routing through the apiary Wi-Fi network](local-wifi.md#apiary-wifi-routing) | Anywhere with Internet access | A configured Wi-Fi network with Internet access must be available near the device | Data is routed to the app automatically; a separate SIM card for every device is not required |
| [Bluetooth](bluetooth.md) | Nearby, within Bluetooth range | **BLE info**, BLE scanning, and app background operation are enabled; the time is synchronized; no SIM card or Internet is required | The app automatically synchronizes current data and can restore available history |

## GSM and SMS

The device sends regular or compact SMS messages without mobile Internet. The app recognizes compact messages and automatically adds the measurements to the phone's local storage.

## Direct Connection to the Device

After activation with the magnetic key, the device temporarily creates the `apiary_net` access point. A phone connected to it does not need a SIM card or Internet access. The app finds the device automatically but downloads the archive only after the user confirms the request.

For the detailed procedure, see [Download the Archive](../guides/download-archive.md).

## Routing Through the Apiary Wi-Fi Network

The device can use an existing Wi-Fi network with Internet access at the apiary. The owner receives data remotely in the app without a separate SIM card for every device.

Before initial setup, the app must have received data from the device at least once through SMS or a direct archive download. Registration is completed on a phone with Internet access, and the prepared Wi-Fi and cloud settings are then transferred to the device through its `apiary_net` access point.

The online relay does not store data. Permanent copies remain on the measuring device and the user's phone.

For the detailed procedure, see [Set Up Synchronization Through the Apiary Wi-Fi Network](../guides/configure-wifi-sync.md).

## Bluetooth

When the phone is within Bluetooth range, the app automatically synchronizes available data. This does not require a SIM card, mobile Internet, or activation of the `apiary_net` access point. When history retrieval is enabled, temporary gaps can be filled during the next successful connection.

For an explanation, see [Bluetooth Data Synchronization](bluetooth.md). For the practical procedure, see [Set Up Bluetooth Synchronization](../guides/configure-bluetooth-sync.md).

## Operation Without a Connection

A temporary or complete loss of any communication channel does not stop measurements: the device continues recording them to microSD. Once the connection is restored, the app can retrieve missed data, but the available history depth depends on the selected channel.

| Channel | Available history after the connection is restored | Note |
|---|---|---|
| GSM and SMS | 2 to 12 hours | Depends on the configured SMS transmission schedule |
| Direct connection to the device access point | Up to 1 year | Data can be downloaded if the corresponding records are present in the local archive |
| Bluetooth | 1 day to 1 week | Depends on the history retrieval setting and the available records |
| Routing through the apiary Wi-Fi network | History is unavailable | The online relay transfers current data but does not store it on the server |

These limits apply only to the amount of missed data that can be restored through a particular channel. The local [microSD archive](data-storage.md) has no one-year storage limit: its depth is limited only by the card capacity, which is sufficient for the device's entire expected service life. If necessary, the data can also be read directly from the microSD card.
