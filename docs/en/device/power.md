# Power and Charging

The device operates from one or two 18650 cells and charges through USB Type-C. The power source can be a charger, a power bank, or an optional solar panel.

!!! note "Choosing a charger and cable"
    The device does not support fast charging, including USB Power Delivery (PD). Use a standard power source with a USB Type-A port and a USB Type-A–USB Type-C cable. A USB Type-C–USB Type-C cable is not recommended for charging.

![Open USB Type-C power port](../../assets/common/device/power/open-usb-type-c-port.jpeg){ .doc-photo }

Close the protective port cover after charging:

![Closed protective cover over the power port](../../assets/common/device/power/closed-usb-type-c-cover.jpeg){ .doc-photo }

- the blue indicator remains lit when the battery is fully charged and external power is still connected;
- the charge level is shown in SMS messages and in the general settings of the web interface;

  ![Battery charge in the web interface](../../assets/en/device/power/battery-charge-status.png){ .doc-screenshot }

- below 20%, the device enters power-saving mode, stops regular measurements and SMS messages, and periodically checks the charge level;
- after a critical discharge, the battery disconnects automatically, and [time synchronization](../system/time-synchronization.md) may be required after charging.

!!! warning "After long-term storage"
    If the battery voltage is below `3.5 V`, do not try to restore the device using only its USB port. Follow the [recovery procedure after long-term storage](../troubleshooting/recovery-after-storage.md).

!!! danger
    Do not use the device without an installed 18650 cell. Observe the polarity strictly when replacing it: incorrect polarity will damage the device.
