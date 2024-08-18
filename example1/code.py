import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from time import sleep
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS as KeyboardLayout


keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayout(keyboard)

# Script line
keyboard.press(Keycode.GUI)
keyboard.press(Keycode.R)
keyboard.release_all()

sleep(0.1)
layout.write("notepad")
sleep(0.1)

# Script line
keyboard.press(Keycode.ENTER)
keyboard.release_all()

sleep(0.1)
sleep(0.4)
sleep(0.1)
layout.write("Hello World!")
sleep(0.1)
