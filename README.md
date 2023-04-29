# The DDL pi UPS
[![Made in Ukraine](https://img.shields.io/badge/made_in-ukraine-ffd700.svg?labelColor=0057b7)](https://vshymanskyy.github.io/StandWithUkraine)

# Terms of use
### The following conditions should be met if you want to use any part of this repository:

By using this project or its parts, for any purpose and in any shape or form, you grant your **implicit agreement** to all the following statements:

- You **condemn Russia and its military aggression against Ukraine**
- You **recognize that Russia is an occupant that unlawfully invaded a sovereign state**
- You **support Ukraine's territorial integrity, including its claims over temporarily occupied territories of Crimea and Donbas**
- You **reject false narratives perpetuated by Russian state propaganda**

To learn more about the war and how you can help, [click here](https://u24.gov.ua/). Glory to Ukraine! 🇺🇦

### AND

## CERN Open Hardware Licence v2 (CERN-OHL-W) TL;DR

- **Can:**
  - *Use*: You are free to use the hardware design in any way.
  - *Modify*: You can make modifications to the design.
  - *Distribute*: You can share the original or modified design with others.
  - *Commercial Use*: You can use the design in commercial projects.

- **Can't:**
  - *Hold Liable*: The original author is not liable for any damages or consequences resulting from the use of the design.

- **Conditions:**
  - *Attribution*: You must give appropriate credit to the original author, including a copyright notice, a link to the license, and an indication of any changes made.
  - *ShareAlike*: If you modify the design, you must distribute your contributions under the same license as the original.
  - *License Notice*: You must include a copy of the CERN-OHL-W v2 with the distributed design or provide a clear link to the license.

Disclaimer: This summary is not a legal document and does not provide legal advice. Please read the full license text for a complete understanding of its terms and conditions.

## Info

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
