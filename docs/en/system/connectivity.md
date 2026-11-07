---
title: "Apiary Monitoring Through GSM, Wi-Fi and Bluetooth"
description: "Compare GSM, direct Wi-Fi, the apiary network and Bluetooth for receiving measurements in BeeApiary: connection requirements and available history."
---

# Apiary Monitoring Through GSM, Wi-Fi and Bluetooth { #receiving-data-in-the-app }

For apiary monitoring, data from the BeeApiary beehive scales can reach the app in four ways: through GSM/SMS, a direct Wi-Fi connection, the apiary Wi-Fi network or Bluetooth. The choice between local and remote monitoring depends on the phone’s location and the connection available near the scales.

| Channel | Phone location | Requirements | How data reaches the app |
|---|---|---|---|
| [GSM and SMS](gsm-and-sms.md) | Anywhere with mobile coverage | A SIM card in the device with a basic SMS plan; SMS permission for the app | The app automatically processes compact SMS; mobile Internet is not needed. [Set up GSM](../guides/configure-gsm.md) |
| [Direct connection to the device access point](local-wifi.md#direct-access-point) | Near the device | Activate the device with the magnetic key and connect to `apiary_net` within the available interval, usually about one minute; no SIM or Internet needed | The app finds the device, asks for permission to retrieve the archive, and imports the data after confirmation. [Download archive](../guides/download-archive.md) |
| [Routing through the apiary Wi-Fi network](local-wifi.md#apiary-wifi-routing) | Anywhere with Internet access | A configured Wi-Fi network with Internet access must be available near the device | Data is routed to the app automatically; a separate SIM card for every device is not required. [Set up Wi-Fi](../guides/configure-wifi-sync.md) |
| [Bluetooth](bluetooth.md) | Nearby, within Bluetooth range | **BLE info**, BLE scanning, and app background operation are enabled; the time is synchronized; no SIM card or Internet is required | The app automatically synchronizes current data and can restore available history. [Set up Bluetooth](../guides/configure-bluetooth-sync.md) |

## GSM and SMS

Ordinary SMS can be read without the app; the app stores compact messages as measurements. [SMS formats](gsm-and-sms.md).

## Direct Connection to the Device

The connected phone receives the archive only after user confirmation. [Connect to the access point](../guides/configure-local-wifi.md).

## Routing Through the Apiary Wi-Fi Network

Before setup, the app must have received device data at least once through SMS or a direct archive download. The relay is not permanent storage: copies stay on the scales and phone. It may be unstable or become paid; check [compatibility and service conditions](../guides/configure-wifi-sync.md).

## Bluetooth

When history retrieval is enabled, gaps may be filled at the next successful connection. [How it works and compatibility](bluetooth.md).

## Operation Without a Connection

A temporary or complete loss of any communication channel does not stop measurements: the device continues recording them to microSD. Once the connection is restored, the app can retrieve missed data, but the available history depth depends on the selected channel.

| Channel | Available history after the connection is restored | Note |
|---|---|---|
| GSM and SMS | 2 to 12 hours | Depends on the configured SMS transmission schedule |
| Direct connection to the device access point | Up to 1 year | Data can be downloaded if the corresponding records are present in the local archive |
| Bluetooth | 1 day to 1 week | Depends on the history retrieval setting and the available records |
| Routing through the apiary Wi-Fi network | History is unavailable | The online relay transfers current data but does not store it on the server |

These limits apply only to the amount of missed data that can be restored through a particular channel. The local [microSD archive](data-storage.md) has no one-year storage limit: its depth is limited only by the card capacity, which is sufficient for the device's entire expected service life. If necessary, the data can also be read directly from the microSD card.
