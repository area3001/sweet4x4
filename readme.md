# Sweet4x4 keyboard macropad
This repository branches off from https://github.com/phyx-be/Fri3d_Sweet4x4 - for all contextual and hardware info please check the Phyx-be repository.
## About this repo
The Sweet4x4 macropad can also be controlled by a XIAO module. This repository contains example code for loading the KMI firmware on a sweet4x4 board.
Based on https://github.com/KMKfw/kmk_firmware

 # Installation steps   
## Firmware
 0) download & install CircuitPython 7.0+ on a compatible controller. Recommended is the XIAO RP2040.
 1) copy the contents of the kmk directory to the mcu's root
 ### Contents
 * code.py (insde the kmk folder) : basic example to test hardware
 * code_layers.py : more advanced example working with color reactive RGB based on selected layers
 ## Hardware
 Because the XIAO footprint is limited regardin I/O pins, we can only use one rotary encoder. In order to do so, the rotary encoder pins must be bridged to the XIAO (as the original board and rotary encoder circuits were designed to function using a micro:bit comptabile header).
 ### Bridges to be made
 * Rotary encoder top pin -> XIAO P6
 * Rotary enconder bottom pin -> XIAO P7