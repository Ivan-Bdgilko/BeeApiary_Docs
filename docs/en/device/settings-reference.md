# `mset.xml`: Device Settings

The main configuration is stored in `/setting/mset.xml` on the microSD card and has a `<settings>` root element.

!!! warning "The current file is not a list of factory values"
    Values in the XML of a particular device may have been changed by the user, the web interface, or automatically. For example, `sefe_start_interval="60000"` and `alarm_sms_sec_interval="10"` are not initial values: a new configuration uses `120000` ms and `180` s respectively.

See also the [safe editing rules](service-reference.md). Do not change `SERVICE` parameters without a backup and an understanding of their effect on the device.

## `net_settings`

This section stores parameters for the device access point, connection to an external Wi-Fi network, data transmission, and FTP. An `SSID`/`PASSWORD` or `SSID_STA`/`PASSWORD_STA` pair is applied only when both values are present and nonempty.

| Field | Purpose | Requirement | Allowed values / range | Initial value | If omitted | Level |
|---|---|---|---|---|---|---|
| `SSID` | Name of the device's local access point | Conditionally required with `PASSWORD` | String; up to 32 characters | `apiary_net` | The new access-point pair is not applied | `USER` |
| `PASSWORD` | Password for the local access point | Conditionally required with `SSID` | String; up to 32 characters | `apiary_wifi` | The new access-point pair is not applied | `USER` |
| `SSID_STA` | SSID of the external Wi-Fi network | Optional | Nonempty string; maximum length is not specified | `-` | New STA parameters are not applied | `ADVANCED` |
| `PASSWORD_STA` | Password for the external Wi-Fi network | Conditionally required with `SSID_STA` | String; maximum length is not specified | `-` | New STA parameters are not applied | `ADVANCED` |
| `STA_KEY` | Authentication key used during transmission | Optional | String; format depends on the authentication method | `-` | The Wi-Fi parameter is not changed | `SERVICE` |
| `UPLOAD_URL` | Address of the Wi-Fi data receiver | Optional | URL; maximum length is not specified | Depends on device configuration | Set to a single space; transmission is effectively not configured | `SERVICE` |
| `wifi_sync` | Enables synchronization through an external Wi-Fi network | Optional | `true`, `false` | `false` | `false` | `ADVANCED` |
| `FTP_USER` | Username for local FTP | Optional as part of a pair | String; up to 32 characters | Depends on device configuration | If either FTP field is missing, the initial FTP settings are used | `ADVANCED` |
| `FTP_PASSWORD` | Password for local FTP | Optional as part of a pair | String; up to 32 characters | Depends on device configuration | If either FTP field is missing, the initial FTP settings are used | `ADVANCED` |

!!! note "The `-` value"
    For `SSID_STA`, `PASSWORD_STA`, and `STA_KEY`, the hyphen is a literal initial value. It is processed as a nonempty string, so do not use it as a reliable indication that a setting is “not configured.”

Change the initial password `apiary_wifi` after the first device check.

## `apairy_set`

The section name contains a historical error and must remain `apairy_set`. This section is required to create the list of hives.

| Field | Purpose | Requirement | Allowed values / range | Initial value | If omitted | Level |
|---|---|---|---|---|---|---|
| `hive_count` | Number of hive configuration files | Optional field in a required section | Integer; `1` or more is recommended; limits are not checked automatically | `1` | `1` | `ADVANCED` |
| `hive1`…`hiveN` | Base names of hive files without `.xml` | Required for every number up to `hive_count` | String; up to 8 ASCII characters is recommended for compatibility | `hive1` | Attribute read error; the corresponding hive is not created | `SERVICE` |

The path has the form `/setting/<value>.xml`. The name uses an internal 24-byte buffer, so do not use long names or path separators.

## `GSM`

This section describes two recipients. If the section is absent, the GSM structure is cleared. The section itself should therefore be considered required even when operating without a SIM card.

| Field | Purpose | Requirement | Allowed values / range | Initial value | If omitted | Level |
|---|---|---|---|---|---|---|
| `sms_format1` | SMS format for `number1` | Optional | `1` — text; `2` — compact app format | `2` | `2` | `USER` |
| `sms_format2` | SMS format for `number2` | Optional | `1` — text; `2` — compact app format | `2` | `2` | `USER` |
| `number1` | Primary recipient number | Optional | International format; internal 15-byte buffer | Empty string | No recipient is configured on the first load | `USER` |
| `number2` | Additional recipient number | Optional | International format; internal 15-byte buffer | Empty string | No recipient is configured on the first load | `USER` |
| `sms_wait_to_send_sec` | Time to wait before sending an SMS on a weak network | Optional | Integer number of seconds; no fixed limits | `50` s | `50` s | `ADVANCED` |
| `alarm_call_wait_sec` | Interval between repeated alarm-call attempts | Optional | Integer number of seconds; no fixed limits | `80` s | `80` s | `ADVANCED` |

Specify an empty number as `number1=""` or `number2=""`. Do not include real phone numbers in published examples.

## `NTP`

This section belongs to the same internal structure as GSM. If `NTP` is completely absent, the GSM parameters that were just read are also reset. The section must therefore remain present even when synchronization is disabled.

| Field | Purpose | Requirement | Allowed values / range | Initial value | If omitted | Level |
|---|---|---|---|---|---|---|
| `synchronize` | Automatic time synchronization through an available network mechanism | Optional field in a required section | `true`, `false` | `false` | `false` | `USER` |
| `time_zone` | Time-zone offset specified in whole hours in the XML | Optional | Integer; `-11` to `12` is recommended; limits are not checked automatically | `2` | `3` | `ADVANCED` |
| `ntp1` | Primary time server | Optional | Hostname; internal buffer up to 30 bytes | `0.europe.pool.ntp.org` | Empty on the first load | `ADVANCED` |
| `ntp2` | Secondary time server | Optional | Hostname; internal buffer up to 30 bytes | `1.europe.pool.ntp.org` | Empty on the first load | `ADVANCED` |
| `ntp3` | Third time server | Optional | Hostname; internal buffer up to 30 bytes | `2.europe.pool.ntp.org` | Empty on the first load | `ADVANCED` |

`time_zone` has different values in the two cases: a new file receives `2`, while a missing attribute results in `3`. Account for this difference before changing the initial configuration.

The spelling `synсhronize` contains the Cyrillic letter `с` and is not recognized. Use only `synchronize`.

## `options`

Individual attributes are optional and have fallback values. **Do not remove the entire section:** if it is absent, the section parameters are cleared instead of receiving the initial values shown below.

| Field | Purpose | Requirement | Allowed values / range | Initial value | If omitted | Level |
|---|---|---|---|---|---|---|
| `meteo` | Indicates the presence of a pressure and humidity sensor | Optional | `true`, `false` | `false` | `false` | `SERVICE` |
| `pir_sensor` | Indicates the presence of a PIR motion sensor | Optional | `true`, `false` | `false` | `false` | `SERVICE` |
| `temperature_twist` | Swaps the logical T1 and T2 values | Optional | `true`, `false` | `false` | `false` | `ADVANCED` |
| `oled` | Indicates the presence of an OLED display | Optional | `true`, `false` | `false` | `false` | `SERVICE` |
| `oled_invert` | Inverts the OLED image | Optional | `true`, `false` | `false` | `false` | `SERVICE` |
| `sefe_start_interval` | Duration of the active window after startup | Optional | Milliseconds; limits are not checked automatically | `120000` ms | `120000` ms | `SERVICE` |
| `alarm_sms_sec_interval` | Minimum interval between alarm SMS messages | Optional | Unsigned integer number of seconds | `180` s | `180` s | `ADVANCED` |
| `alarm_by_changes_count` | Number of PIR state changes required to confirm an alarm | Optional | Unsigned integer; practical value depends on placement | `3` | `3` | `ADVANCED` |
| `alarm_by_long_state` | Duration of an active PIR state required for an alarm | Optional | Unsigned integer number of seconds | `10` s | `10` s | `ADVANCED` |
| `time_ms_compensate` | Daily clock-rate compensation | Optional | Signed 32-bit number of milliseconds | `0` ms | `0` ms | `SERVICE` |
| `sync_time_sec` | Service timestamp for manual synchronization | Optional | Signed 64-bit number of seconds | `0` | `0` | `SERVICE` |

`sefe_start_interval` is the exact historical field name. Its initial value is `120000` ms; the range is not checked automatically, so reducing it arbitrarily is dangerous.

Hardware flags changed through the web interface are saved immediately, but the operating configuration applies them after the settings are read again.

## `BLE`

The entire section is optional for compatibility with older files. If it is absent, BLE is disabled, and the current values and standard intervals are used.

| Field | Purpose | Requirement | Allowed values / range | Initial value | If omitted | Level |
|---|---|---|---|---|---|---|
| `ble_enable` | Enables BLE | Optional | `true`, `false` | `false` | `false`; an invalid value also disables BLE | `USER` |
| `static_values` | Selects static values instead of current values | Optional | `true`, `false` | `false` | `false` | `SERVICE` |
| `update_time_sec` | BLE data update interval | Optional | `3`–`60` s; lower values are normalized to `3`, higher values to `60` | `30` s | `30` s | `ADVANCED` |
| `advertising_time_sec` | BLE advertising duration | Optional | `0` or `10`–`60` s; values from `1` to `9` are normalized to `0`, values above `60` to `60` | `20` s | `20` s | `ADVANCED` |

For `static_values`, only the selection of static instead of current values is described; no other effect of the parameter is defined.

## Minimal Example { #minimal-example }

This example leaves STA, FTP, and BLE at their initial values. An empty but present `<options />` section activates the fallback value of each attribute instead of clearing the entire structure.

```xml
<settings>
  <net_settings SSID="apiary_net" PASSWORD="apiary_wifi" />
  <apairy_set hive_count="1" hive1="hive1" />
  <GSM sms_format1="2" sms_format2="2"
       number1="" number2=""
       sms_wait_to_send_sec="50" alarm_call_wait_sec="80" />
  <NTP synchronize="false" time_zone="2"
       ntp1="0.europe.pool.ntp.org"
       ntp2="1.europe.pool.ntp.org"
       ntp3="2.europe.pool.ntp.org" />
  <options />
</settings>
```

## Complete Sanitized Example { #full-example }

The values `SITE_WIFI`, `WIFI_PASSWORD`, `DEVICE_KEY`, `FTP_USER`, `FTP_PASSWORD`, and the URL are placeholders, not data from an operating device.

```xml
<settings>
  <net_settings SSID="apiary_net" PASSWORD="apiary_wifi"
                SSID_STA="SITE_WIFI" PASSWORD_STA="WIFI_PASSWORD"
                STA_KEY="DEVICE_KEY"
                UPLOAD_URL="https://example.invalid/beeapiary"
                wifi_sync="false"
                FTP_USER="FTP_USER" FTP_PASSWORD="FTP_PASSWORD" />
  <apairy_set hive_count="1" hive1="hive1" />
  <GSM sms_format1="2" sms_format2="2"
       number1="+380XXXXXXXXX" number2=""
       sms_wait_to_send_sec="50" alarm_call_wait_sec="80" />
  <NTP synchronize="false" time_zone="2"
       ntp1="0.europe.pool.ntp.org"
       ntp2="1.europe.pool.ntp.org"
       ntp3="2.europe.pool.ntp.org" />
  <options meteo="false" pir_sensor="false"
           temperature_twist="false" oled="false" oled_invert="false"
           sefe_start_interval="120000"
           alarm_sms_sec_interval="180"
           alarm_by_changes_count="3" alarm_by_long_state="10"
           time_ms_compensate="0" sync_time_sec="0" />
  <BLE ble_enable="false" static_values="false"
       update_time_sec="30" advertising_time_sec="20" />
</settings>
```
