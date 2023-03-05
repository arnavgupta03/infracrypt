# Infracrypt

<p>
  <a href="https://github.com/arnavgupta03/regionsell/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-purple" alt="License"></a>
  <a href="https://regionsell.azurewebsites.net/?item=something"><img src="https://betteruptime.com/status-badges/v1/monitor/a9kf.svg" alt="Uptime" width=85 height=20></a>
</p>

With [Infracrypt](https://pypi.org/project/infracrypt/), secure your Flask APIs and servers without any hassle! Infracrypt takes a Flask file and replaces any data returned with data encrypted using AES-256. Further, the data needed for decryption is put into an easy-to-access JSON file so that decryption can be done on any frontend or by any user of the API.

The private key for the AES-256 encryption is generated using a password that is created by the near random motion created by the hardware module. This module consists of an ESP32 microcontroller, infrared sensor, ultrasonic sensor, servo motor, as well as LEDs and resistors and a cardboard chassis. When motion is detected, the distance between the ultrasonic sensor and the cardboard is calculated, which is used with a random generator to move the motor again as well as generate a password for the AES-256 procedure.

The Infracrypt package communicates over WiFi to get this password, which is also encrypted using a 256-bit private key known to the Infracrypt package. Infracrypt then uses this to conduct the encryption and replacement procedure.

Here is a video of the random motion of the hardware module:

https://user-images.githubusercontent.com/65367548/222950501-ddcce131-5970-491a-b454-0e9255faa854.mp4

## How to use it

```
python -m infracrypt {flask-file-name}
```

Currently supports string, dict, int, and list return types. Any other types can be put into these types to be encrypted.
