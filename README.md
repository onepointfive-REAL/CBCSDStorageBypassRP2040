# Circuit Python Custom Mass Storage

### A customizable mass storage app for the RP2040 and Raspberry Pi Zero 2W with a serial terminal

**Raspberry Pi Zero 2 W notes:**
- The experimental CircuitPython port is unstable, so the serial terminal is not available.
- Use `pizeroboot.py` and `pizerocode.py` instead of `boot.py` and `code.py`.
- Rename `pizeroboot.py` to `boot.py` and `pizerocode.py` to `code.py` before using them.
- `pizeroboot.py` must be configured manually (by editing the file) before use.
- Attempting to use the RP2040 `code.py` with the Raspberry Pi Zero 2W WILL result in a crash.

## Instructions
**If using Waveshare RP2040-Zero:**
1. Download and flash [CircuitPython for the Waveshare RP2040-Zero](https://circuitpython.org/board/waveshare_rp2040_zero/) if you haven't already.
2. Download the [latest source code](https://github.com/onepointfive-REAL/RP2040-Custom-Mass-Storage/releases).
3. Copy `boot.py` and `code.py` to the `CIRCUITPY` drive.
4. Unplug and reconnect the board.

**If using Raspberry Pi Zero 2W:**
1. Download and flash [CircuitPython for the Raspberry Pi Zero 2W](https://circuitpython.org/board/raspberrypi_zero2w/) with balenaEtcher to your SD card if you haven't already.
2. Download the [latest source code](https://github.com/onepointfive-REAL/RP2040-Custom-Mass-Storage/releases).
3. Copy `pizeroboot.py` and `pizerocode.py` to the `CIRCUITPY` drive.
4. Rename `pizeroboot.py` to `boot.py` and `pizerocode.py` to `code.py`
5. Unplug and reconnect the board.

## Serial Commands (RP2040 Exclusive)

Connect to the board's serial console and enter one of the following commands. You might need to press `Ctrl+D` first if the `USB>` prompt hasn't appeared yet.

| Command | Description |
|---|---|
| `help` | Lists available commands and usage instructions. |
| `customusbid` | Switches to Custom USB VID/PID mode and restarts the device. |
| `normalusbid` | Switches to Normal USB VID/PID mode and restarts the device. |
| `setvidpid` | Sets a custom USB Vendor ID (VID) and Product ID (PID) using hexadecimal values. |
| `status` | Displays USB settings and storage statistics, including total and free space. |
| `label` | Changes the USB drive's volume label. Enter up to 11 characters, or leave blank to delete the saved label. |
| `ls` | Lists files and folders in a directory, including file sizes. Enter a directory path when prompted, or leave blank to list the root directory. |
| `cat` | Displays the contents of a text file. |
| `write` | Creates a text file or overwrites an existing file after confirmation. |
| `mkdir` | Creates a directory at the specified path. |
| `rm` | Deletes a file or folder after confirmation. Can recursively delete folders and their contents. |
| `uptime` | Displays how long the device has been running. |
| `reset` | Restarts the microcontroller. |
| `version` | Displays the CircuitPython version information. |
| `device` | Displays information about the microcontroller and its platform. |
| `resetsettings` | Resets all settings to their defaults by deleting the saved configuration files. |
| `boardrng` | Generates a SHA-256 hash using urandom, the board UID, temperature, and available RAM. |
| `boarduid` | Displays the board's unique identifier. |
| `safemode` | Restarts the board in CircuitPython safe mode. |
| `bootloader` | Restarts the board into the bootloader. |
| `ram` | Displays available RAM and optionally cleans up unused objects. |

### Usage Notes

- Commands do not accept arguments directly. Enter the command first, then follow the prompts.
- For `ls`, leave the directory path blank to list `/`, or enter a path such as `/sd` or `/lib`.
- For `rm`, confirm the deletion when prompted. The root directory `/` cannot be deleted.
- For `setvidpid`, enter the VID and PID in hexadecimal format, such as `0x0D28`.
- For `label`, leave the label blank to remove the saved label.

### What RP2040-Zero clone board I recommend on a budget

[DWEII RP2040 Zero on Amazon](https://www.amazon.com/DWEII-RP2040-Zero-Microcontroller-Development-MicroPython/dp/B0H3Z4BBFG/)

This is a clone Waveshare RP2040 Zero, but I'm using it and it works fine.

[Waveshare RP2040-Zero Case with Keyring on Makerworld](https://makerworld.com/en/models/577171-waveshare-rp2040-zero-case-with-keyring)

This is the 3D printed case I'm using for my clone Waveshare. I think it's a different size than the official one so I had to scale the bottom part to 102% and the top part 100.75%.

EDIT: [Fixed STL with adjusted sizes](https://github.com/onepointfive-REAL/RP2040-Custom-Mass-Storage/blob/main/rp2040_clone_case.stl)

