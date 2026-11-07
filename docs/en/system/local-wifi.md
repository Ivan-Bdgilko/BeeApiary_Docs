---
title: "Wi-Fi Beehive Scales — Direct and Network Connections"
description: "Connect BeeApiary beehive scales over Wi-Fi: a direct access point for your phone and remote transmission through the apiary network."
---

# Wi-Fi Beehive Scales — Direct and Network Connections { #device-wi-fi-connection }

BeeApiary beehive scales with Wi-Fi support two ways to receive data: a direct phone connection to the device access point (AP) and transmission through the apiary Wi-Fi network (STA). The first method works near the scales; the second provides remote data access when Internet connectivity is available.

## Direct Connection to the Device { #direct-access-point }

After activation with the magnetic key, the device temporarily creates a local access point. It is usually available for about one minute, but this interval can be changed in the settings.

Default settings:

```text
SSID: apiary_net
Password: apiary_wifi
Web interface: http://192.168.4.1
```

Through the local connection, you can:

- allow the app to retrieve the measurement archive;
- open the web interface;
- configure the owner's phone number and the schedule;
- view the charge level and firmware version;
- use FTP to access files on the microSD card.

After the phone connects to `apiary_net`, the app finds the device and displays the prompt **“Device nearby. Retrieve archive?”**. Data is downloaded only after the user confirms the request.

!!! warning "Change the password"
    The default password is publicly known. After the first check, set your own password of up to 32 characters.

Detailed procedures:

- [Connect to the Device Access Point](../guides/configure-local-wifi.md);
- [download the archive to the app](../guides/download-archive.md);
- [view additional device settings](../device/additional-settings.md).

## Routing Through the Apiary Wi-Fi Network { #apiary-wifi-routing }

The device can connect to an existing Wi-Fi network at the apiary and automatically send data over the Internet to the owner's app. The phone can be anywhere with Internet access.

This method does not require a separate SIM card in every device, but a configured Wi-Fi network with Internet access must be available near the device.

### How Setup Works

Register a device already known to the app: the service creates identifiers and keys. Then transfer the apiary network settings from the phone through the device's `apiary_net` access point.

After a restart with the magnetic key or during the next scheduled hourly cycle, the device uses the configured network for automatic transmission. The phone no longer needs to be nearby.

### Requirements

- the device has already been added to the app;
- the app has received its data at least once through SMS or a direct archive download;
- the phone has Internet access during registration;
- a Wi-Fi network with Internet access is available near the device;
- the user knows the name and password of that network.

The online relay is not permanent storage: data remains on the scales and phone. The service may become unstable or paid; device compatibility and other conditions are described in the guide.

For the step-by-step procedure, see [Set Up Synchronization Through the Apiary Wi-Fi Network](../guides/configure-wifi-sync.md).
