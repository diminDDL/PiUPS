# The DDL pi UPS
This repo contains the hardware and *soon TM* software for the ultra efficient raspberry pi UPS.
The reason this was created was because I wasn't satisfied with the things available on the market
that would just lower the incoming voltage to charge the battery and immediately boost it to power the pi. This way efficiencies of around ~80% can be achieved. Don't get me wrong this is not terrible but I wanted to do better, which is why this design incorporates a power MUX.

### Current revision: 0.2

##### Known issues of rev 0.2

| Issue  | Possible fix |
| ------------- |:-------------:|
| Battery voltage leaking on to the output line even with switch in OFF position| Have SW1 turn off VSYS to everything thus closing the MOSFTEs |
| After over-discharge protection turns off the load, it turns back on after reaching ~3V causing hysteresis    | Add dw01 and corresponding MOSFETs to enable battery protections  |
| quiescent power consumption quite high (5mA) when SW1 is off     | Same as for first issue     |
| No direct way to check battery voltage in the BQ25601    | Use the VSYS status to get an inderect measurement/replace battary managment chip     |
