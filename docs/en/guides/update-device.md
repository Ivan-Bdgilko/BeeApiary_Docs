# How to Update the BeeApiary Measuring Device Firmware

Before updating, select firmware that matches the device generation and the required interface language.

## Select the firmware generation

| Device | Update source | Development status |
|---|---|---|
| Manufactured before August 2026 | [Hive_Controller](https://github.com/Ivan-Bdgilko/Hive_Controller) | Feature development for the previous version is no longer supported |
| Manufactured after August 2026 | [Hive_Controller_Ble](https://github.com/Ivan-Bdgilko/Hive_Controller_Ble) | The new version continues to receive updates and new functionality |

!!! danger "Migrating an older device to the new version"
    Any previously manufactured device can be migrated to the new software version, but this requires a factory update. There is currently no simple patch for a self-service migration, so the standard procedure on this page does not migrate a device between generations.

## Select the firmware language

Both generations provide multilingual builds. The suffix in the version name identifies the language:

| Suffix | Language |
|---|---|
| `-de` | German |
| `-en` | English |
| `-es` | Spanish |
| `-fr` | French |
| `-pl` | Polish |
| `-uk` | Ukrainian |

Select the language by downloading and flashing the corresponding file. The language builds are publicly available in the repositories listed above, and more languages may be added later if needed.

## Update the device using microSD

1. Wait until the device enters sleep mode, then remove the microSD card.
2. Create the `/fm` directory in the root of the card if it does not already exist.
3. Place the `Apiary.bin` update file in `/fm`.
4. Reinsert the microSD card into the device.
5. [Activate or restart the device](../device/installation.md#activation-reset) with the magnetic key.
6. Wait for a regular SMS message containing measurements; the update usually takes up to two minutes.
7. At the bottom of the web interface home page, check the firmware version, language suffix, build date and time, and unique device number.

![Firmware version, language suffix, build time, and unique ID in the device web interface](../../assets/common/guides/update-device/device-version-build-time-and-id.png){ .doc-screenshot }

The full version string includes the localization suffix, for example `-uk`. Compare it with the corresponding update version in the repository for your device generation. The same page also shows the build date and time and the unique device identifier.

!!! warning "Check the file before updating"
    Make sure `Apiary.bin` is intended for your device generation and required language. Service update methods over FTP or a server are outside the scope of this procedure.
