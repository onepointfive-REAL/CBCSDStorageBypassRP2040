# CBCSDStorageBypass (Waveshare RP2040-Zero version)
### This version is more stable than the flipper zero version, but it's very small if you want to store files. Maybe getting a SD card reader might help with low storage.
\
Bypasses Council Bluffs Community School District Chromebook's external storage restrictions by posing as a micro:bit storage device with a Waveshare RP2040-Zero (using VID and PID). This works because they approved the micro:bits storage vid and pid for computer science.
\
\
Instructions:<br>
1. Download and flash [Circuit Python](https://circuitpython.org/board/waveshare_rp2040_zero/) if you haven't already
2. Download [source code](https://github.com/onepointfive-REAL/CBCSDStorageBypassRP2040/releases)
3. Copy `boot.py` and `code.py` to the `CIRCUITPY` drive
4. Unplug and replug the board
