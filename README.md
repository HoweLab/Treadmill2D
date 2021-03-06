# Treadmill2D
Scripts for reading velocity from 2D treadmill ball using Raspberry Pi. Adapted from https://github.com/HanLabBU/movement_recording/mouse_relay_voltage.py. Reads the x- and y-velocity from the optical mouse, and transmits it as a voltage via the raspberry pi output pins to be converted through the DAC MCP4725 and then read into Matlab via the NiDaq card

## NOTES
- Put these scripts on the Raspberry Pi
- Python 2.7
- Install: https://github.com/adafruit/Adafruit_Python_MCP4725

## Scripts
### mouse_display_mouse0.py
- reads in mouse activity from /dev/input/mouse0 and displays dx and dy to the command prompt

### mouse_display_mouse1.py
- reads in mouse activity from /dev/input/mouse1 and displays dx and dy to the command prompt

### mouse_relayVoltage2_mouse0.py
- reads in mouse activity from /dev/input/mouse0 and sends out voltage using the I2C buses (to output to digital-to-analog converter MCP4725). Note that this uses the Raspberry Pi's I2C built-in I2C bus, as well as an added one on GPIO17 and GPIO27. Output is 0-3.3V, absolute value of velocity multipled by a conversion factor to convert to voltage. The sign (+/-) gets output separately via a digital pin (0=neg, 1=pos).

### mouse_relayVoltage2_mouse1.py
- reads in mouse activity from /dev/input/mouse1 and sends out voltage using the I2C buses (to output to digital-to-analog converter MCP4725). Note that this uses the Raspberry Pi's I2C built-in I2C bus, as well as an added one on GPIO17 and GPIO27. Output is 0-3.3V, absolute value of velocity multipled by a conversion factor to convert to voltage. The sign (+/-) gets output separately via a digital pin (0=neg, 1=pos).



