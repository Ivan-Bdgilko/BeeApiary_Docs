# Installing the BeeApiary App

## Installation

!!! note "App permissions"
    We recommend granting **all permissions** requested by the app during the first launch. If you deny some of them, certain features may not work or may work incorrectly; behavior for every possible combination of restrictions has not been tested. To avoid making setup and troubleshooting unnecessarily difficult, grant all requested permissions.

!!! warning "SMS permission is required for GSM"
    If you use BeeApiary hive scales and plan to receive data via GSM, permission to process SMS messages is required. Without it, the app cannot read messages from the scales, so measurements will not arrive via GSM.

    If you use the app without BeeApiary hive scales as a standalone notebook and apiary journal, SMS permission is not required.

1. Open the [app page on Google Play](https://play.google.com/store/apps/details?id=com.beeapiary).
2. Install and launch the app.
3. Grant all permissions requested by the app.

!!! info "Automatic synchronization via Bluetooth"
    Make sure the app has Bluetooth permissions and that the system allows it to run in the background and wake up at the required time. Full procedure: [Configure synchronization via Bluetooth](../guides/configure-bluetooth-sync.md).

## Next Steps

After installation, choose the scenario you need:

- [Add BeeApiary hive scales](add-device.md) to receive automatic measurements.
- [Add a hive](add-hive.md) to keep its description, condition, notes, and events even without a physical device.

Earlier APKs in the [Android_Apk repository](https://github.com/Ivan-Bdgilko/Android_Apk) are outdated. Use Google Play for the current installation.
