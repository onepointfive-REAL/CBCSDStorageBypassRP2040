import os
import sys
import time
import microcontroller
import storage

while True:
    command = input("USB> ").strip().lower()

    if command == "help":
	print("Available commands:")
	print("")
        print("customusb, normalusb, setvidpid, status, label, ls, reset, version, device, repl, uptime, cat, write, mkdir, rm, help")
	print("")
	print("Commands do not accept arguments directly. Enter the command first, then follow the prompts.")

    elif command == "repl":
        sys.exit()

    elif command == "uptime":
        elapsed = int(time.monotonic())
        hours = elapsed // 3600
        minutes = (elapsed % 3600) // 60
        seconds = elapsed % 60
        print("Uptime: {:02}:{:02}:{:02}".format(hours, minutes, seconds))

    elif command == "cat":
        filename = input("File path: ").strip()

        try:
            with open(filename, "r") as f:
                print(f.read())
        except OSError:
            print("Could not open file.")

    elif command == "mkdir":
        path = input("Directory path: ").strip()
        storage.unsafe_disable_usb_drive()

        try:
            os.mkdir(path)
            print("Directory created!")
        except OSError as e:
            print("Error:", e)
        finally:
            storage.enable_usb_drive()

    elif command == "rm":
        path = input("File or folder path: ").strip().rstrip("/")

        if not path:
            path = "/"

        if path == "/":
            print("Error: Cannot delete the root directory.")
            continue

        confirm = input("Delete " + path + "? (y/n): ").strip().lower()

        if confirm == "y":
            storage.unsafe_disable_usb_drive()

            def delete_all(folder):
                for name in os.listdir(folder):
                    item = folder.rstrip("/") + "/" + name
                    mode = os.stat(item)[0]

                    if mode & 0x4000:
                        delete_all(item)
                        os.rmdir(item)
                    else:
                        os.remove(item)

            try:
                mode = os.stat(path)[0]

                if mode & 0x4000:
                    delete_all(path)
                    os.rmdir(path)
                else:
                    os.remove(path)

                print("Deleted successfully!")

            except OSError as e:
                print("Error:", e)

            finally:
                storage.enable_usb_drive()
        else:
            print("Cancelled.")

    elif command == "write":
        path = input("File path: ").strip()
        confirm = "y"

        try:
            with open(path, "r") as f:
                f.read()
            confirm = input("File exists. Overwrite? (y/n): ").strip().lower()
        except OSError:
            pass

        if confirm == "y":
            content = input("Text to write: ")
            storage.unsafe_disable_usb_drive()

            try:
                with open(path, "w") as f:
                    f.write(content)
                print("File saved!")
            except OSError as e:
                print("Error:", e)
            finally:
                storage.enable_usb_drive()
        else:
            print("Cancelled.")

    elif command == "status":
        s = os.statvfs("/")
        try:
            with open("/usbmode.txt", "r") as f:
                mode = "Custom USB" if f.read().strip() == "1" else "Normal USB"
        except OSError:
            mode = "Custom USB (default)"

        try:
            with open("/vid.txt", "r") as f:
                vid = f.read().strip()
        except OSError:
            vid = "Default"

        try:
            with open("/pid.txt", "r") as f:
                pid = f.read().strip()
        except OSError:
            pid = "Default"

        try:
            with open("/label.txt", "r") as f:
                label = f.read().strip()
        except OSError:
            label = "Default"

        print("USB Mode:", mode)
        print("VID:", vid)
        print("PID:", pid)
        print("Label:", label)
        print("Block size:", s[0])
        print("Total blocks:", s[2])
        print("Free blocks:", s[3])
        print("Total bytes:", s[0] * s[2])
        print("Free bytes:", s[0] * s[3])

    elif command == "":
        pass
       
    elif command == "label":
        name = input("New drive label (blank to delete): ").strip()[:11]
        storage.unsafe_disable_usb_drive()

        try:
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

        except OSError as e:
            print("Error:", e)

    elif command == "ls":
        path = input("Directory path (blank for /): ").strip()

        if not path:
            path = "/"

        try:
            print("\n Directory listing for " + path + "\n")

            items = os.listdir(path)

            for name in items:
                item = path.rstrip("/") + "/" + name
                try:
                    info = os.stat(item)
                    if info[0] & 0x4000:
                        print("<DIR>       " + name)
                    else:
                        print("{:>10}  {}".format(info[6], name))
                except OSError:
                    print("            " + name)

            print("\n{} item(s)".format(len(items)))

        except OSError as e:
            print("Error:", e)

    elif command == "version":
        print(os.uname().version)
       
    elif command == "device":
        print(os.uname().machine)

    elif command == "reset":
        microcontroller.reset()

    elif command == "customusb":
        storage.unsafe_disable_usb_drive()
        try:
            with open("/usbmode.txt", "w") as f:
                f.write("1")
            print("Switching to Custom USB...")
            microcontroller.reset()
        except OSError as e:
            print("Error:", e)

    elif command == "normalusb":
        storage.unsafe_disable_usb_drive()
        try:
            with open("/usbmode.txt", "w") as f:
                f.write("0")
            print("Switching to Normal USB...")
            microcontroller.reset()
        except OSError as e:
            print("Error:", e)
       
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

                try:
                    with open("/vid.txt", "w") as f:
                        f.write("0x{:04X}".format(vid_num))

                    with open("/pid.txt", "w") as f:
                        f.write("0x{:04X}".format(pid_num))

                    print("VID saved: 0x{:04X}".format(vid_num))
                    print("PID saved: 0x{:04X}".format(pid_num))

                    microcontroller.reset()

                except OSError as e:
                    print("Error:", e)

        except ValueError:
            print("Invalid input. Use hexadecimal digits (0-9, A-F).")

    else:
        print("Unknown command. Type help.")
