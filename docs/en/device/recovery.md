# Restoring the Configuration

This page explains how to replace the microSD card safely, restore the configuration from a backup, and check the XML files after the device starts.

!!! danger "Do not remove the microSD card while the device is active"
    The device has no standard power button. Before removing or installing the microSD card, wait until the device enters sleep mode. First, save a complete copy of the `/setting` directory.

## Automatic Normalization

- the main file is located at `/setting/mset.xml`;
- if the main file is missing, the device can create an initial configuration;
- a missing or incomplete hive file can be saved again using fallback values from the current state;
- a missing `hive`, `thermometer`, or `schedule` section, as well as an incomplete existing `scales` section, triggers normalization of the hive file;
- a completely missing `scales` section is not an error: the scales are simply not created;
- structural errors in the root XML element, the `apairy_set` section, or the `hiveN` attribute can prevent the configuration from being read.

Creating an initial `mset.xml` does not mean that every parameter will have a universal value. `UPLOAD_URL`, FTP credentials, HX711 pins, and some other fields depend on the device configuration or individual setup.

!!! warning "A backup is required"
    Do not rely on automatic recovery as your only backup. Before replacing the microSD card, save the entire `/setting` directory if the card can still be read.

## Replacing the microSD Card Safely

1. Wait for the device to enter sleep mode.
2. Remove the microSD card and, if it is readable, copy all of its contents.
3. Prepare the microSD card according to the requirements of the specific device hardware version.
4. Restore the `/setting` directory from a verified backup.
5. If no backup exists, do not use scale calibration values from another device. First restore a minimal [`mset.xml`](settings-reference.md#minimal-example), then create the hive file without a `scales` section or perform the standard calibration procedure.
6. Install the microSD card while the device is asleep and wait for the next operating cycle.
7. Check the time, network, GSM numbers, available sensors, schedule, and weight.
8. Compare the normalized XML files with the backup: the device may have added fields with fallback values or rewritten sections.

## If the Configuration Cannot Be Read

1. Check that the file has one `<settings>` root element.
2. Check the exact names `apairy_set`, `synchronize`, `sefe_start_interval`, and `pecision` in the three filter fields.
3. Make sure `hive_count` has matching `hive1`…`hiveN` attributes.
4. Make sure every referenced `/setting/<hive>.xml` file exists.
5. Do not try to fix the problem by copying `scales` from another device. Temporarily remove the scales section and check the rest of the configuration.
6. Save the problematic XML files and service logs for diagnostics.

For a complete description of the fields, see the [`mset.xml`](settings-reference.md) and [`HIVE*.XML`](hive-settings-reference.md) references.
