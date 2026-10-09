# terminal for managing USB stuff
import os
import sys
import time
import microcontroller
import supervisor
import storage

while True:
    command = input("USB> ").strip().lower()

    if command == "help":
        print("customusb, normalusb, setvidpid, status, label, files, stat, reset, version, device, repl, help")

    elif command == "repl":
        sys.exit()

    elif command == "":
       pass
       
    elif command == "status":
        try:
            with open("/usbmode.txt", "r") as f:
                print("Custom USB VID/PID" if f.read().strip() == "1" else "Normal USB VID/PID")
        except OSError:
            print("You haven't set the mode yet. The mode automatically defaults to Custom USB VID/PID")

    elif command == "label":
        name = input("New drive label (blank to delete): ").strip()[:11]
        storage.unsafe_disable_usb_drive()

        if name:
            with open("/label.txt", "w") as f:
                f.write(name)
            print("Label saved!")
        else:
            try:
                os.remove("/label.txt")
                print("Label deleted!")
            except OSError:
                print("No label file to delete.")

        microcontroller.reset()

    elif command == "files":
        print(os.listdir("/"))

    elif command == "stat":
        s = os.statvfs("/")
        print("Block size:", s[0])
        print("Total blocks:", s[2])
        print("Free blocks:", s[3])
        print("Total bytes:", s[0] * s[2])
        print("Free bytes:", s[0] * s[3])

    elif command == "version":
        print(os.uname().version)
       
    elif command == "device":
        print(os.uname().machine)

    elif command == "reset":
        microcontroller.reset()

    elif command == "customusb":
        storage.unsafe_disable_usb_drive()
        with open("/usbmode.txt", "w") as f:
            f.write("1")
        print("Switching to Custom USB...")
        microcontroller.reset()

    elif command == "normalusb":
        storage.unsafe_disable_usb_drive()
        with open("/usbmode.txt", "w") as f:
            f.write("0")
        print("Switching to Normal USB...")
        microcontroller.reset()
       
    elif command == "setvidpid":
        vid = input("Enter VID (hex, e.g. 0x0D28): ").strip().lower()
        pid = input("Enter PID (hex, e.g. 0x0204): ").strip().lower()

        if vid.startswith("0x"):
            vid = vid[2:]
        if pid.startswith("0x"):
            pid = pid[2:]

        try:
            vid_num = int(vid, 16)
            pid_num = int(pid, 16)

            if not (1 <= vid_num <= 65535 and 1 <= pid_num <= 65535):
                print("Invalid VID/PID. Use values from 0x0001 to 0xFFFF.")
            else:
                storage.unsafe_disable_usb_drive()
                with open("/vid.txt", "w") as f:
                    f.write("0x{:04X}".format(vid_num))

                with open("/pid.txt", "w") as f:
                    f.write("0x{:04X}".format(pid_num))

                print("VID saved: 0x{:04X}".format(vid_num))
                print("PID saved: 0x{:04X}".format(pid_num))
                microcontroller.reset()

        except ValueError:
            print("Invalid input. Use hexadecimal digits (0-9, A-F).")
    else:
        print("Unknown command. Type help.")
