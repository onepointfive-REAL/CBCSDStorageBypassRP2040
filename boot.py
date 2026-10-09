# boot.py
import supervisor
import storage

supervisor.set_usb_identification(
    manufacturer="NotCBCSD",
    product="RP2040",
    vid=0x0D28,
    pid=0x0204,
)

storage.enable_usb_drive()

try:
    with open("/label.txt", "r") as f:
        name = f.read().strip()
    if name:
        storage.getmount("/").label = name[:11]
except OSError:
    storage.getmount("/").label = "RP2040"
    pass  # no label.txt, keep the default

# put your other code here if you want it, this is just to get around the storage restrictions
