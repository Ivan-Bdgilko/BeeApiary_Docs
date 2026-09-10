# Why BeeApiary Works This Way

## From the BeeApiary Creators

BeeApiary was designed as a self-contained tool that keeps data and key decisions under the beekeeper's control. This page explains several design and software choices that may not be immediately obvious.

## Why Are the Covers Transparent?

The transparent cover lets you see when the device is operating and whether condensation, insects, or dirt have entered the enclosure. This makes inspection easier without opening the enclosure unnecessarily.

The project is open to feedback and suggestions: its construction does not hide the condition of the main components from the owner.

## Why Is There No Mandatory Server Storage?

The core operation of the hive scales and the app does not depend on permanent BeeApiary storage on an external server. Measurements are stored on the [device's microSD card](../system/data-storage.md) and locally on the user's phone. The system does not require centralized storage of the owner's location or activity history.

An optional relay service can be used for [synchronization through the apiary Wi-Fi network](../system/local-wifi.md#apiary-wifi-routing). It transfers data to the app but is not permanent storage and is not required for the other communication channels.

## Why Does GSM Use SMS?

In the field or while moving an apiary, SMS is often available where mobile Internet access is unreliable. A minimal SMS plan is sufficient, and the app receives data without a separate server subscription.

With the appropriate message format, two SMS messages per day can deliver the results of all hourly measurements collected during that day. The app works directly on the owner's phone and, in a typical configuration, can handle up to five devices; this number can be increased if necessary.

For details, see [GSM and SMS](../system/gsm-and-sms.md).

## Why Are Measurements Taken Every Hour?

An hourly history helps reveal morning bee departures and evening returns, weight changes while nectar is drying, and daily temperature variations. These data provide a basis for further analysis of colony strength, food reserves, and other processes inside the hive.

## Why Are SMS Messages Not Sent Every Hour?

Frequent transmission does not improve the measurements themselves, but it consumes battery power and communication credit. Sending several messages per day transfers the accumulated hourly data much more efficiently.

A practical estimate for two SMS messages per day is at least 160 days of operation on one charge. This is a guideline, not a guarantee: battery life depends on the battery, device configuration, temperature, GSM coverage, and enabled transmission channels.

If an alarm sensor is installed, an emergency event or an attempt to move the hive can separately trigger a call and an SMS without waiting for the regular schedule.

## Why Should the Battery Not Be Removed?

The device has three levels of battery protection and automatically enters a deep power-saving mode when the charge is low. The battery does not need to be removed for storage, while incorrect polarity during reinstallation can permanently damage the electronics.

Exceptions and winter storage rules are described in [Power and Charging](power.md) and [Winter Use and Storage](winter-use-and-storage.md).

## Why Are Firmware Updates Not Automatic?

The owner decides when to update the device and whether the features of a new version are needed. A controlled update reduces the risk of unexpected changes in the behavior of an autonomous system.

The hive scales can operate without a phone as self-contained scales and a weather-data logger. The Android app extends the viewing, apiary journal, and synchronization features, but is not required for measurements. Procedure: [Update the Device](../guides/update-device.md).

## How Long Are Measurements Stored?

The archive on the microSD card is not limited to one year. The storage period depends on the card's capacity and condition; with a normal volume of measurements, it is sufficient for the expected service life of the device.

## Two Types of SMS and a Flexible Schedule. Why?

There are many opinions on when, how, and where to begin taking measurements; to address this, users can freely configure the SMS format and sending time according to their preferences. However, there are certain recommendations regarding the number of messages per day in order to conserve power.
