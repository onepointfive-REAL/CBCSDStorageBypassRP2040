import supervisor
import storage

supervisor.set_usb_identification(
    manufacturer="notamicrobit",
    product="RP2040",
    vid=0x0D28,
    pid=0x0204,
)

storage.enable_usb_drive()
