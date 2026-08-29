# Service Documentation

This section is a technical configuration archive for the BeeApiary measuring device. It is intended for service technicians and experienced users who need to restore or inspect XML files manually.

The initial values of some hardware and network parameters depend on the configuration and setup of the particular device.

!!! danger "Manual editing"
    Incorrect hardware pins, calibration values, or service intervals can disrupt measurements or device operation. Use the web interface for ordinary changes. Always create a backup of the `/setting` directory before editing files manually.

## Safe Procedure

1. Wait until the device enters sleep mode. The device has no standard power button: during operation, it is either active or in hibernation.
2. Remove the microSD card and save a complete copy of the `/setting` directory.
3. Edit the XML in a text editor without changing section or attribute names.
4. Make sure the XML has one `<settings>` root element and that all quotation marks and closing tags are present.
5. Reinsert the microSD card while the device is asleep. Updated settings are applied the next time the configuration is loaded normally; some changes made through the web interface also take effect only after a restart.
6. Check measurements, communication, and the service log. Keep the backup until verification is complete.

When saving, the device may normalize the file: add missing sections or attributes, substitute fallback values, and rewrite the element order.

## Files

- [`/setting/mset.xml`](settings-reference.md) — network, GSM, time, hardware options, general alarms, and BLE.
- [`/setting/<hive>.xml`](hive-settings-reference.md) — sensors for a particular hive, weight, schedule, check frequency, and threshold alarms.
- [Restoring the Configuration](recovery.md) — safe microSD replacement, restoration from a backup, and XML verification.

The hive filename is specified by the `hive1`, `hive2`, and subsequent attributes without an extension. The `.xml` extension is added automatically.

## Access Levels

| Label | Meaning |
|---|---|
| `USER` | The value can be changed through the standard interface. |
| `ADVANCED` | An understanding of its effect on communication or operating logic is required. |
| `SERVICE` | Manual changes can make the device inoperable or distort data. |

In the tables, `—` means that limits do not apply to the field. **Initial value** is the value in a newly created configuration, not in the XML of a particular device. **If omitted** describes the value used when the attribute is absent, which may differ from the initial value.

## Historical Names

Exact XML identifiers are not corrected even when they contain mistakes: `apairy_set`, `sefe_start_interval`, `normal_pecision`, and `calibrate_pecision` must remain exactly as written. The spelling `synсhronize` with the Cyrillic letter `с` is incorrect; use `synchronize`.
