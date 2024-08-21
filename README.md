# Introduction
When i first bought my raspberry pi pico and wanted to make it a bad usb, I tried to look up tutorials, youtube videos, even some github repositories. Sadly, none of them worked and I saw people in the comments having same problem as me, it just didnt work. Thats why I decided to create this project, which simplifies transformation of raspberry pi pico into bad usb.

### So what is "bad usb"?
Because you are on this page you probably know what it is, but let me explain just for clarification
Bad usb is usb device, which looks like normal usb, but isnt. In every a bit complex piece of electronics are little computer called microcontrollers. Theese microcontrollers do small operation to make sure, entire device works. For example you can find microcontrollers in microwaves, TV remotes or even you keyboard or mouse. When connecting microcontrollers to PC, you either use specific cable to connect to it, for example HDMI, ethernet, etc... but when you connect standard usb device, it can be many things. In modern age, electronics are starting to use usb ports a lot more than before, so there wont be need for special ports. When usb is connected to the computer, it send a signal about what it is going to be. Is it going to be mouse, keyboard, headhpones, microphone, mass storage, etc...? This information sends microcontroller from inside our electronics and here is where bad usb was created. Bad usb is simple microcontroller, usually packed in usb-like case, but when connected to the computer, it doesnt send signal about being mass storage, but a HID (Human Interface Device). This allows our bad usb to act as keyboar, mouse or even game controller, all thoose are also identified as HID. And you probably already know where this is going. Our bad usb is going to act as a keyboard. With theese capabilities, you can preprogramm simple script into your microcontroller which after connecting to computer will execute and start typing. Using this you can troll someone, for example open Rickroll on their device, simply shut it down, write secret message to desktop or even start typing CMD command by which you can get reverse shell into device withing few second.

# Installation
Have your bad usb working in 5-10 minutes

1. Clone the repository to get a local copy of the files, which you will be needing later `git clone https://github.com/dbisu/pico-ducky.git`
2. Download CircuitPython version 8.* or 9.*, for easy setup just download first one on top
    * [CircuitPython for the Raspberry Pi Pico](https://circuitpython.org/board/raspberry_pi_pico/)
    * [CircuitPython for the Raspberry Pi Pico W](https://circuitpython.org/board/raspberry_pi_pico_w/)
3. Plug the device into a USB port while holding the boot button. It will show up as a removable media device named `RPI-RP2`
4. Copy downloaded `.uf2` file to the root of the Pico (`RPI-RP2`). Device should disconnect and connect back after few seconds as `CIRCUITPYTHON`
5. Install adafruit package `adafruit-circuitpython-bundle-8/9.x-mpy-YYYYMMDD.zip`, which will allow Pico to identify as HID from [here](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/latest) with `version` corresponding to version of your CircuitPython and extract files outside of Pico
6. Navigate to `lib` folder of recently extracted package and copy `adafruit_hid` to `lib` folder on your Pico device
7. Choose ducky script you want from [here](https://github.com/hak5/usbrubberducky-payloads) or create your own, you can inspier yourself by [this](https://docs.hak5.org/hak5-usb-rubber-ducky/ducky-script-basics/hello-world) tutorial and save somewhere, recommended to save in cloned git repository
8. Now just convert ducky script file into raspberry pi pico python script using tool `main.py` which is located in cloned repository ([this one](https://github.com/julecko/pico-bad-usb/blob/master/main.py)) using command `python main.py -i \<DuckyScriptPath>` for example `python main.py -i payload.ds`
9. You should see file `code.py` appear inside cloned repository. Now just copy this file into Pico root. As soon as file is coppied, script will start executing. It executes every time change is made to it and every time Pico connects to computer
10. Thats it, you should have by now working bad usb made from Pico, amazing

## USB enable/disable mode
Pico is in default mode of storage, but what if you want to change it?
○ Pico: The default mode is USB mass storage `enabled`
○ Pico W: The default mode is USB mass storage `disabled`
Its very practical, to be able to switch mass storage mode, either if you want to edit files or want to be more stealthy by not acting as HID and mass storage at once (which can also disrupt ducky script if not waited long enough for PC to load mass storage)

To do this:
1. Copy `boot.py` from cloned repository into the root of Pico
2. Connect jumper wire between pin 24 (`GP18`) and pin 23 (`GND`) to switch default mode, so Pico will have mass storage `disabled` and Pico w will have mass storage `enabled`
3. Thats it, next time you connect Pico it will have its default mode switched

![USB enable/disable mode](images/pico-pinout.svg)

> Optionally what I recommed is soldering simple switch into ports 24, 23, 22, so you can simply turn on, off storage mode

## Final Words
Well, thats it, i hope this tutorial helped. Later (probably) i will add bigger ducky script support. Like other tutorials, i havent programmed program, which runs ducky script at runtime but program which basicly translates ducky script into python script runnable by Pico. I choose this, because i believe it can be time saving, just a little bit, but if you want to use this thing in serious stuff, every moment matters.

## Usefull links and resources
How to reset Pico in case of corruption or doesnt boot [here](https://github.com/dbisu/pico-ducky/blob/main/RESET.md)

[CircuitPython](https://circuitpython.readthedocs.io/en/6.3.x/README.html)

[CircuitPython HID](https://learn.adafruit.com/circuitpython-essentials/circuitpython-hid-keyboard-and-mouse)

[Ducky Script](https://github.com/hak5darren/USB-Rubber-Ducky/wiki/Duckyscript)

[Pico-Ducky Repository](https://github.com/dbisu/pico-ducky)
