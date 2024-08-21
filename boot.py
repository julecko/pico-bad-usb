from board import *
import board
import digitalio
import storage

noStorage = False
noStoragePin = digitalio.DigitalInOut(GP18)
noStoragePin.switch_to_input(pull=digitalio.Pull.UP)
noStorageStatus = noStoragePin.value

if(board.board_id == 'raspberry_pi_pico'):
    # On Pi Pico, default to USB visible unless GP18 is connected to GND
    noStorage = not noStorageStatus
elif(board.board_id == 'raspberry_pi_pico_w'):
    # On Pi Pico W, default to USB hidden, unless GP18 is connected to GND
    noStorage = noStorageStatus

if(noStorage == True):
    # don't show USB drive to host PC
    storage.disable_usb_drive()
else:
    # show USB drive to host PC
    storage.enable_usb_drive()