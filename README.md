# The DDL pi UPS
[![Made in Ukraine](https://img.shields.io/badge/made_in-ukraine-ffd700.svg?labelColor=0057b7)](https://vshymanskyy.github.io/StandWithUkraine)

This repo contains the hardware and *soon TM* software for the ultra efficient raspberry pi UPS.
The reason this was created was because I wasn't satisfied with the things available on the market
that would just lower the incoming voltage to charge the battery and immediately boost it to power the pi. This way efficiencies of around ~80% can be achieved. Don't get me wrong this is not terrible but I wanted to do better, which is why this design incorporates a power MUX.

### Current revision: 0.5

##### Known issues of rev 0.5

| Issue  | Possible fix |
| ------------- |:-------------:|
| Power mux and everything involving the comparator oscilates when trying to shut down. | Use TL431 instead, it combines a voltage reference and a comparator. |
| Turning switch off while plugged in doesn't turn off the output. | Rework the schematic. |
| DW01 chip is acting up (high leakage, not working half of the time). | Replace with BQ2970. |
| BMS turns off when the charger is plugged in. | Try removing diodes going to the fs8205. |

### Pictures
![3D render](https://github.com/diminDDL/PiUPS/blob/main/assets/3D.png)
![Photo in development](https://github.com/diminDDL/PiUPS/blob/main/assets/dev.jpg)
