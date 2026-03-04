# Treadmill2D
Scripts for reading velocity from 2D treadmill ball using Raspberry Pi. Adapted from https://github.com/HanLabBU/movement_recording/mouse_relay_voltage.py. Reads the x- and y-velocity from the optical mouse, and transmits it as a voltage via the raspberry pi output pins to be converted through the DAC MCP4725 and then read into Matlab via the NiDaq card

## NOTES
- Put these scripts on the Raspberry Pi
- Python 2.7
- Install: https://github.com/adafruit/Adafruit_Python_MCP4725
- The sign (+/-) of the data may need to be adjusted, based on the positioning of the sensors, specifically the sensor on the side reading the yaw/roll.

## Scripts
### mouse_display_mouse0.py
- reads in mouse activity from /dev/input/mouse0 and displays dx and dy to the command prompt

### mouse_display_mouse1.py
- reads in mouse activity from /dev/input/mouse1 and displays dx and dy to the command prompt

### mouse_relayVoltage2_mouse0.py
- reads in mouse activity from /dev/input/mouse0 and sends out voltage using the I2C buses (to output to digital-to-analog converter MCP4725). Note that this uses the Raspberry Pi's I2C built-in I2C bus, as well as an added one on GPIO17 and GPIO27. Output is 0-3.3V, absolute value of velocity multipled by a conversion factor to convert to voltage. The sign (+/-) gets output separately via a digital pin (0=neg, 1=pos).

### mouse_relayVoltage2_mouse1.py
- reads in mouse activity from /dev/input/mouse1 and sends out voltage using the I2C buses (to output to digital-to-analog converter MCP4725). Note that this uses the Raspberry Pi's I2C built-in I2C bus, as well as an added one on GPIO17 and GPIO27. Output is 0-3.3V, absolute value of velocity multipled by a conversion factor to convert to voltage. The sign (+/-) gets output separately via a digital pin (0=neg, 1=pos).


## License and Citation

This repository is released under the MIT License - see the LICENSE file for details.

## Acknowledgements
This work was supported by Aligning Science Across Parkinson’s (ASAP-020370) through the Michael J. Fox Foundation for Parkinson’s Research (MJFF), National Institute of Mental Health (R01 MH125835), Whitehall Foundation Fellowship, Klingenstein-Simons Foundation Fellowship, and Parkinson’s Foundation (Stanley Fahn Junior Faculty Award, PF-SF-JFA-836662) to M.W.H.; NIMH F32MH120894 to M.-A.T.V.

