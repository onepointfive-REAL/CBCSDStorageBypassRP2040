# CBCSDStorageBypass (Waveshare RP2040-Zero version)
### This version is more stable than the flipper zero version, but it's very small if you want to store files. Maybe getting a SD card reader might help with low storage.

Bypasses Council Bluffs Community School District Chromebook's external storage restrictions by posing as a micro:bit storage device with a Waveshare RP2040-Zero (using VID and PID). This works because they approved the micro:bits storage vid and pid for computer science.

## Instructions

1. Download and flash [CircuitPython for the Waveshare RP2040-Zero](https://circuitpython.org/board/waveshare_rp2040_zero/) if you haven't already.
2. Download the [latest source code](https://github.com/onepointfive-REAL/CBCSDStorageBypassRP2040/releases).
3. Copy `boot.py` and `code.py` to the `CIRCUITPY` drive.
4. Unplug and reconnect the board.

## Serial Commands

Connect to the board's serial console and enter one of the following commands. (you might need to do ctrl+d first if the prompt `USB>` haven't shown yet)

| Command     | Description                                                                                                   |
| ----------- | ------------------------------------------------------------------------------------------------------------- |
| `help`      | Lists all available commands.                                                                                 |
| `customusb` | Switches to Custom USB VID/PID mode and restarts the device.                                                  |
| `normalusb` | Switches to Normal USB VID/PID mode and restarts the device.                                                  |
| `setvidpid` | Sets a custom USB Vendor ID (VID) and Product ID (PID) using hexadecimal values.                              |
| `status`    | Displays the currently selected USB VID/PID mode.                                                             |
| `label`     | Changes the USB drive's volume label. Enter up to 11 characters, or leave it blank to delete the saved label. |
| `files`     | Lists files and folders in the root directory.                                                                |
| `stat`      | Displays storage statistics, including total and free space.                                                  |
| `reset`     | Restarts the microcontroller.                                                                                 |
| `version`   | Displays the CircuitPython version information.                                                               |
| `device`    | Displays information about the microcontroller and its platform.                                              |
| `repl`      | Exits the command interface and returns to the CircuitPython REPL.                                            |
