# The DDL pi UPS
[![Made in Ukraine](https://img.shields.io/badge/made_in-ukraine-ffd700.svg?labelColor=0057b7)](https://vshymanskyy.github.io/StandWithUkraine)

This repo contains the hardware and *soon TM* software for the ultra efficient raspberry pi UPS.
The reason this was created was because I wasn't satisfied with the things available on the market
that would just lower the incoming voltage to charge the battery and immediately boost it to power the pi. This way efficiencies of around ~80% can be achieved. Don't get me wrong this is not terrible but I wanted to do better, which is why this design incorporates a power MUX.

### Current revision: 0.5

##### Known issues of rev 0.2

| Issue  | Possible fix |
| ------------- |:-------------:|
| Battery voltage leaking on to the output line even with switch in OFF position| Turn the below protection off |
| After over-discharge protection turns off the load, it turns back on after reaching ~3V causing hysteresis    | Use unused compatrator for under voltage protection  |
| quiescent power consumption quite high (10-20uA) when SW1 is off     | Same as for second issue     |

### Pictures
![3D render](https://github.com/diminDDL/PiUPS/blob/main/assets/3D.png)
![Photo in development](https://github.com/diminDDL/PiUPS/blob/main/assets/dev.jpg)
