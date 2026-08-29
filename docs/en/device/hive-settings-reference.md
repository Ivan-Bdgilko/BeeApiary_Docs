# `HIVE*.XML`: Hive Settings

The hive configuration is stored in `/setting/<hive>.xml`. The `<hive>` base name is specified by the `hive1`, `hive2`, and subsequent attributes in [`mset.xml`](settings-reference.md); the `.xml` extension is added automatically.

!!! danger "Hardware-dependent values"
    Do not copy the `scales` section from another device. Board pins and calibration values depend on the hardware version and the particular set of weight sensors. Incorrect values can distort measurements or make them unavailable.

See the [safe editing rules](service-reference.md).

## Automatic Rewriting

After reading the file, the device may save it again:

- a missing or damaged file is created from the available current state;
- missing `hive`, `thermometer`, or `schedule` sections enable normalization;
- a missing attribute in an existing `scales` or `thermometer` section is replaced with a fallback value and enables normalization;
- complete `scales`, `booster`, and `range_alarmer` sections are optional;
- normalization also writes the `booster`, `range_alarmer`, `thermometer`, and `schedule` sections even if some of them were absent from the source file.

## `hive`

| Field | Purpose | Requirement | Allowed values / range | Initial value | If omitted | Level |
|---|---|---|---|---|---|---|
| `hive_name` | Internal hive name | Optional | String; up to 8 ASCII characters is recommended for compatibility | Name from `mset.xml`, for example `hive1` | `hive_<index>`; the file is marked for rewriting | `ADVANCED` |
| `bus_number` | Hive number on the internal bus | Optional | Integer; limits are not checked | Instance index, `0` for the first | Instance index; the file is marked for rewriting | `SERVICE` |
| `main_device` | Indicates the main device with local hardware sensors | Optional | `true`, `false` | `true` in a newly created file | The instance does not become the main device; omission alone does not enable rewriting | `SERVICE` |

Support for subordinate devices is obsolete. The value `main_device="false"` is accepted during loading, but after saving, the attribute becomes `main_device="true"`. Do not use `false` as a stable configuration.

## `scales`

If the entire section is absent, no scales object is created and weight measurement is disabled. If the section is present, every missing or invalid field is replaced with a fallback value, after which the entire file may be rewritten.

| Field | Purpose | Requirement | Allowed values / range | Initial value | If omitted | Level |
|---|---|---|---|---|---|---|
| `pin_hc711_data` | HX711 data GPIO | Required in an existing section | GPIO for the particular board | The section is not created automatically; hardware-dependent | Pin for the particular board; the file is rewritten | `SERVICE` |
| `pin_hc711_clk` | HX711 clock GPIO | Required in an existing section | GPIO for the particular board | The section is not created automatically; hardware-dependent | Pin for the particular board; the file is rewritten | `SERVICE` |
| `gain` | HX711 gain mode | Required in an existing section | HX711 gain-mode value | Channel A, gain 128 | Channel A, gain 128; the file is rewritten | `SERVICE` |
| `zero_calibrate_measurement` | Raw ADC value for zero load | Required in an existing section | Signed 32-bit integer | Hardware-dependent | Fallback value `-486050`; the file is rewritten | `SERVICE` |
| `weight_calibrate_measurement` | Raw ADC value with the reference weight | Required in an existing section | Signed 32-bit integer | Hardware-dependent | Fallback value `-498030`; the file is rewritten | `SERVICE` |
| `calibrate_weight` | Calibration reference mass | Required in an existing section | Grams; positive integer; limits are not checked automatically | Hardware-dependent | `500` g; the file is rewritten | `USER` |
| `start_weight` | Tare subtracted from the result | Required in an existing section | Grams; `-100000` to `100000` is recommended; limits are not checked automatically | Hardware-dependent | `0` g; the file is rewritten | `USER` |
| `source_weight` | Filter whose result is used as the primary weight | Required in an existing section | `1` — `immediate`; `2` — `stable`; `3` — `calibration` | The section is not created automatically | `1`; the file is rewritten. Other values are treated as `1` during operation | `SERVICE` |
| `normal_pecision` | Precision parameter of the fast filter | Required in an existing section | Floating-point number; limits are not checked | The section is not created automatically | `0.5`; the file is rewritten | `SERVICE` |
| `normal_desired_deviation` | Desired deviation of the fast filter | Required in an existing section | Floating-point number; limits are not checked | The section is not created automatically | `10`; the file is rewritten | `SERVICE` |
| `stable_pecision` | Precision parameter of the stable filter | Required in an existing section | Floating-point number; limits are not checked | The section is not created automatically | `0.35`; the file is rewritten | `SERVICE` |
| `stable_desired_deviation` | Desired deviation of the stable filter | Required in an existing section | Floating-point number; limits are not checked | The section is not created automatically | `5`; the file is rewritten | `SERVICE` |
| `calibrate_pecision` | Precision parameter of the calibration filter | Required in an existing section | Floating-point number; limits are not checked | The section is not created automatically | `0.25`; the file is rewritten | `SERVICE` |
| `calibrate_desired_deviation` | Desired deviation of the calibration filter | Required in an existing section | Floating-point number; limits are not checked | The section is not created automatically | `3`; the file is rewritten | `SERVICE` |
| `median_window` | Median-filter window size | Required in an existing section | `3`–`100`; out-of-range values are replaced | The section is not created automatically | `100`; the file is rewritten | `SERVICE` |

The identifiers `normal_pecision`, `stable_pecision`, and `calibrate_pecision` contain the historical error `pecision`, which must not be corrected in the XML.

`gain` is loaded from the file, but saving always sets channel A with gain 128. Do not change it manually without data for your particular device.

## `thermometer`

A missing section enables file normalization. The value `sensors_count="0"` disables polling of DS18B20 sensors.

| Field | Purpose | Requirement | Allowed values / range | Initial value | If omitted | Level |
|---|---|---|---|---|---|---|
| `pin_onewire` | 1-Wire bus GPIO | Optional | GPIO for the particular board | `4` | `4`; the file is rewritten | `SERVICE` |
| `sensors_count` | Number of DS18B20 sensors | Optional | `0` disables the sensors; positive integer; upper limit is not checked | `2` | `2`; the file is rewritten | `ADVANCED` |

## `schedule`

The `TimeSlot0`–`TimeSlot23` attributes define the action for the corresponding hour. After minute 30, the action for the next hour is selected; after hour 23, `TimeSlot0` is selected.

| Field | Purpose | Requirement | Allowed values / range | Initial value | If omitted | Level |
|---|---|---|---|---|---|---|
| `TimeSlot0`…`TimeSlot23` | Type of scheduled action for hour `0`–`23` | All attributes are optional, but at least one slot with `2` is required | Integer from `0` to `5`; see below | `5` for hours `0`–`20`; `1` for `21` and `22`; `2` for `23` | A missing slot becomes `0`. If no `2` remains after reading, the entire schedule is reset to the initial schedule | `ADVANCED` |

| Value | Action | Recommendation |
|---:|---|---|
| `0` | No scheduled action | Can be used for an empty slot |
| `1` | Measurement | Supported |
| `2` | Transmission through the primary channel | Required in at least one slot |
| `3` | Reserved for transmission through Wi-Fi | Do not use |
| `4` | Reserved for transmission through BLE | Do not use |
| `5` | Hourly wake-up for synchronization | Used by the initial schedule |

Other integers are not rejected but have no defined behavior. Use only values from the table.

### Initial Schedule

```xml
<schedule
  TimeSlot0="5" TimeSlot1="5" TimeSlot2="5" TimeSlot3="5"
  TimeSlot4="5" TimeSlot5="5" TimeSlot6="5" TimeSlot7="5"
  TimeSlot8="5" TimeSlot9="5" TimeSlot10="5" TimeSlot11="5"
  TimeSlot12="5" TimeSlot13="5" TimeSlot14="5" TimeSlot15="5"
  TimeSlot16="5" TimeSlot17="5" TimeSlot18="5" TimeSlot19="5"
  TimeSlot20="5" TimeSlot21="1" TimeSlot22="1" TimeSlot23="2" />
```

## `booster`

This section sets the interval for additional wake-ups to check critical parameters. If the section is absent, an hourly interval is used during operation; the absence itself does not trigger rewriting.

| Field | Purpose | Requirement | Allowed values / range | Initial value | If omitted | Level |
|---|---|---|---|---|---|---|
| `booster_time_sec` | Additional-check interval | Optional | `180`, `240`, `300`, `360`, `600`, `720`, `900`, `1200`, `1800`, or `3600` s | `3600` s | `3600` s | `ADVANCED` |

A value below `180` s becomes `180`; a value above `3600` s becomes `3600`. Other values within the range are rounded to the nearest supported interval in the table.

## `range_alarmer`

This section is optional. If it is absent, the threshold alarm is not initialized. If `alarm="false"` or the `alarm` attribute is absent, the limits are not read and the background alarm task is not started.

| Field | Purpose | Requirement | Allowed values / range | Initial value | If omitted | Level |
|---|---|---|---|---|---|---|
| `alarm` | Enables threshold alarms | Optional | `true`, `false` | `false` | `false` | `USER` |
| `T1_min` | T1 lower limit | Optional | Floating-point number, °C; physical limits and min/max order are not checked automatically | `-500` °C in a newly created file | With `alarm="true"`, there is no lower limit | `ADVANCED` |
| `T1_max` | T1 upper limit | Optional | Floating-point number, °C; physical limits and min/max order are not checked automatically | `500` °C in a newly created file | With `alarm="true"`, there is no upper limit | `ADVANCED` |
| `T2_min` | T2 lower limit | Optional | Floating-point number, °C; physical limits and min/max order are not checked automatically | `-500` °C in a newly created file | With `alarm="true"`, there is no lower limit | `ADVANCED` |
| `T2_max` | T2 upper limit | Optional | Floating-point number, °C; physical limits and min/max order are not checked automatically | `500` °C in a newly created file | With `alarm="true"`, there is no upper limit | `ADVANCED` |
| `Humidity_min` | Humidity lower limit | Optional | Floating-point number, %; physical limits and min/max order are not checked automatically | `-20` % in a newly created file | With `alarm="true"`, there is no lower limit | `ADVANCED` |
| `Humidity_max` | Humidity upper limit | Optional | Floating-point number, %; physical limits and min/max order are not checked automatically | `200` % in a newly created file | With `alarm="true"`, there is no upper limit | `ADVANCED` |

For each source—T1, T2, or humidity—one limit is sufficient. If no limit is specified for a particular source, it is not added to the check. The order of `_min` and `_max` is not checked automatically.

### One-Sided Alarm Example

In this example, T1 is monitored only from above, T2 only from below, and humidity is not monitored:

```xml
<range_alarmer alarm="true" T1_max="45.0" T2_min="-10.0" />
```

The general SMS frequency and PIR alarm confirmation are configured by `alarm_sms_sec_interval`, `alarm_by_changes_count`, and `alarm_by_long_state` in [`mset.xml`](settings-reference.md#options).

## Structural Example Without Scales

This file uses the initial schedule, two temperature sensors, and disabled threshold alarms. The `scales` section is absent, so no scales object is created.

```xml
<settings>
  <hive hive_name="hive1" bus_number="0" main_device="true" />
  <booster booster_time_sec="3600" />
  <range_alarmer alarm="false"
                 T1_max="500" T1_min="-500"
                 T2_max="500" T2_min="-500"
                 Humidity_max="200" Humidity_min="-20" />
  <thermometer pin_onewire="4" sensors_count="2" />
  <schedule
    TimeSlot0="5" TimeSlot1="5" TimeSlot2="5" TimeSlot3="5"
    TimeSlot4="5" TimeSlot5="5" TimeSlot6="5" TimeSlot7="5"
    TimeSlot8="5" TimeSlot9="5" TimeSlot10="5" TimeSlot11="5"
    TimeSlot12="5" TimeSlot13="5" TimeSlot14="5" TimeSlot15="5"
    TimeSlot16="5" TimeSlot17="5" TimeSlot18="5" TimeSlot19="5"
    TimeSlot20="5" TimeSlot21="1" TimeSlot22="1" TimeSlot23="2" />
</settings>
```

## Complete Scales Section

The following structural example uses fallback values and is provided only for archival reference. **Do not install it on a device:** calibration values and pins must come from a backup of that particular device or be created by the standard calibration procedure.

```xml
<scales pin_hc711_data="27" pin_hc711_clk="26" gain="0"
        zero_calibrate_measurement="-486050"
        weight_calibrate_measurement="-498030"
        calibrate_weight="500" start_weight="0" source_weight="1"
        normal_pecision="0.5" normal_desired_deviation="10"
        stable_pecision="0.35" stable_desired_deviation="5"
        calibrate_pecision="0.25" calibrate_desired_deviation="3"
        median_window="100" />
```

GPIO `27` and `26` are only an example for one device and are not universal. Use values from the backup of your particular device.
