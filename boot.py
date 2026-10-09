import storage
import supervisor
DEFAULT_VID = 0x0D28
DEFAULT_PID = 0x0204

def read_usb_id(filename, default):
    try:
        with open("/" + filename, "r") as f:
            value = f.read().strip().lower()

        if value.startswith("0x"):
            value = value[2:]

        number = int(value, 16)

        if 1 <= number <= 65535:
            return number

    except (OSError, ValueError):
        pass

    return default

try:
    with open("/usbmode.txt", "r") as f:
        mode = f.read().strip()
except OSError:
    mode = "1"

if mode == "1":
    vid = read_usb_id("vid.txt", DEFAULT_VID)
    pid = read_usb_id("pid.txt", DEFAULT_PID)
    supervisor.set_usb_identification(
        manufacturer="NotCBCSD",
        product="RP2040",
        vid=vid,
        pid=pid
    )

storage.enable_usb_drive()
storage.remount("/", readonly=True)

try:
    with open("/label.txt", "r") as f:
        name = f.read().strip()
    if name:
        storage.getmount("/").label = name[:11]
except OSError:
    storage.getmount("/").label = "RP2040"
    pass  # no label.txt, keep the default
