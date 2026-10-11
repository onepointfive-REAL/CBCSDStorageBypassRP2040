import supervisor
import storage

vid = 0x0D28
pid = 0x0204
manufacturer = "RaspberryPi"
product = "RaspberryPi"
label = "RaspberryPi"

supervisor.set_usb_identification(
    manufacturer=manufacturer,
    product=product,
    vid=vid,
    pid=pid,
)

storage.enable_usb_drive()
storage.getmount("/").label = label
storage.remount("/", readonly=True)
