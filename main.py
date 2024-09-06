import argparse
import sys

#GLOBAL VARIABLES

#In miliseconds
defaultDelay = 0.1
duckyCommands = {
    "WINDOWS": "Keycode.WINDOWS", "GUI": "Keycode.GUI",
    "APP": "Keycode.APPLICATION", "MENU": "Keycode.APPLICATION", "SHIFT": "Keycode.SHIFT",
    "ALT": "Keycode.ALT", "CONTROL": "Keycode.CONTROL", "CTRL": "Keycode.CONTROL",
    "DOWNARROW": "Keycode.DOWN_ARROW", "DOWN": "Keycode.DOWN_ARROW", "LEFTARROW": "Keycode.LEFT_ARROW",
    "LEFT": "Keycode.LEFT_ARROW", "RIGHTARROW": "Keycode.RIGHT_ARROW", "RIGHT": "Keycode.RIGHT_ARROW",
    "UPARROW": "Keycode.UP_ARROW", "UP": "Keycode.UP_ARROW", "BREAK": "Keycode.PAUSE",
    "PAUSE": "Keycode.PAUSE", "CAPSLOCK": "Keycode.CAPS_LOCK", "DELETE": "Keycode.DELETE",
    "END": "Keycode.END", "ESC": "Keycode.ESCAPE", "ESCAPE": "Keycode.ESCAPE", "HOME": "Keycode.HOME",
    "INSERT": "Keycode.INSERT", "NUMLOCK": "Keycode.KEYPAD_NUMLOCK", "PAGEUP": "Keycode.PAGE_UP",
    "PAGEDOWN": "Keycode.PAGE_DOWN", "PRINTSCREEN": "Keycode.PRINT_SCREEN", "ENTER": "Keycode.ENTER",
    "SCROLLLOCK": "Keycode.SCROLL_LOCK", "SPACE": "Keycode.SPACE", "TAB": "Keycode.TAB",
    "BACKSPACE": "Keycode.BACKSPACE",
    'A': "Keycode.A", 'B': "Keycode.B", 'C': "Keycode.C", 'D': "Keycode.D", 'E': "Keycode.E",
    'F': "Keycode.F", 'G': "Keycode.G", 'H': "Keycode.H", 'I': "Keycode.I", 'J': "Keycode.J",
    'K': "Keycode.K", 'L': "Keycode.L", 'M': "Keycode.M", 'N': "Keycode.N", 'O': "Keycode.O",
    'P': "Keycode.P", 'Q': "Keycode.Q", 'R': "Keycode.R", 'S': "Keycode.S", 'T': "Keycode.T",
    'U': "Keycode.U", 'V': "Keycode.V", 'W': "Keycode.W", 'X': "Keycode.X", 'Y': "Keycode.Y",
    'Z': "Keycode.Z", "F1": "Keycode.F1", "F2": "Keycode.F2", "F3": "Keycode.F3",
    "F4": "Keycode.F4", "F5": "Keycode.F5", "F6": "Keycode.F6", "F7": "Keycode.F7",
    "F8": "Keycode.F8", "F9": "Keycode.F9", "F10": "Keycode.F10", "F11": "Keycode.F11",
    "F12": "Keycode.F12",
}
special_chars = {
    ' ': "Keycode.SPACE",
    '.': "Keycode.PERIOD",
    ',': "Keycode.COMMA",
    '!': "Keycode.EXCLAIM",
    '@': "Keycode.AT",
    '#': "Keycode.NUMBER_SIGN",
    '$': "Keycode.DOLLAR",
    '%': "Keycode.PERCENT",
    '^': "Keycode.CARET",
    '&': "Keycode.AMPERSAND",
    '*': "Keycode.ASTERISK",
    '(': "Keycode.LEFT_PAREN",
    ')': "Keycode.RIGHT_PAREN",
    '-': "Keycode.MINUS",
    '=': "Keycode.EQUALS",
    '[': "Keycode.LEFT_BRACKET",
    ']': "Keycode.RIGHT_BRACKET",
    '\\':" Keycode.BACKSLASH",
    ';': "Keycode.SEMICOLON",
    '\'':"Keycode.QUOTE",
    '/': "84",
    '`': "Keycode.GRAVE_ACCENT",
    '"': "Keycode.SHIFT, Keycode.QUOTE",
    "0": "Keycode.ZERO",
    "1": "Keycode.ONE",
    "2": "Keycode.TWO",
    "3": "Keycode.THREE",
    "4": "Keycode.FOUR",
    "5": "Keycode.FIVE",
    "6": "Keycode.SIX",
    "7": "Keycode.SEVEN",
    "8": "Keycode.EIGHT",
    "9": "Keycode.NINE",
    "|": "Keycode.SHIFT, Keycode.BACKSLASH"
}
def getDuckyFile():
    parser = argparse.ArgumentParser(description="Python script which converts ducky files into python scripts for raspberry pi pico")
    parser.add_argument("-i", type=str, help="Input file")
    args = parser.parse_args()
    if args.i is None:
        print("No file specified")
        exit(1)
    else:
        return args.i

def addImports(file):
    imports = (
    "import usb_hid\n"
    "from adafruit_hid.keyboard import Keyboard\n"
    "from adafruit_hid.keycode import Keycode\n"
    "from time import sleep\n"
    "from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS as KeyboardLayout\n"
    "\n"
    "\n"
    "keyboard = Keyboard(usb_hid.devices)\n"
    "layout = KeyboardLayout(keyboard)\n"
    )
    file.write(imports)

def editText(text):
    newText = ""
    for char in text:
        if char == "\"" or char == "\'" or char == "\\":
            newText += "\\"
        newText += char
    return newText

def addScriptLine(file, line):
    file.write("\n# Script line\n")
    for key in filter(None, line.split(" ")):
        key = key.upper()
        command_keycode = duckyCommands.get(key, None)
        # If command key is found
        if command_keycode is not None:
            file.write(f"keyboard.press({command_keycode})\n")
        else:
            unknow_key = f"Unknown key: <{key}>"
            file.write(f"# {unknow_key}\n")
            print(unknow_key, sys.stderr)
    file.write("keyboard.release_all()\n\n")

def processLine(file, line):
    global defaultDelay

    if (line[0:3] == "REM" or line == ""):
        return
    elif (line[0:5] == "DELAY" or line[0:5] == "SLEEP"):
        file.write(f"sleep({float(line[6:])/1000})\n")
    elif(line[0:6] == "STRING"):
        text = line[7:]
        for char in text:
            if char in special_chars:
                file.write(f"keyboard.press({special_chars[char]})\nkeyboard.release_all()\n")
            else:
                file.write(f"keyboard.press(Keycode.{char.upper()})\nkeyboard.release_all()\n")
    elif (line[0:5] == "WRITE"):
        text = editText(line[6:])
        file.write(f"layout.write(\"{text}\")\n")
    elif(line[0:5] == "PRINT"):
        file.write("print(\"[SCRIPT]: \" + line[6:])\n")
    elif(line[0:6] == "IMPORT"):
        convertScript(line[7:])
    elif(line[0:12] == "DEFAULTDELAY"):
        defaultDelay = float(line[13:])/1000
        # Just to not add delay, because this command is script creator specific
        return
    else:
        addScriptLine(file, line)
    file.write(f"sleep({defaultDelay})\n")

def convertScript(inFile, outFile):
    while (line := inFile.readline()):
        line = line.rstrip()
        if(line[0:6] == "REPEAT"):
            for i in range(int(line[7:])):
                #repeat the last command
                processLine(outFile, previous_line)
        else:
            processLine(outFile, line)
            previousLine = line

def main():
    inFilePath = getDuckyFile()
    inFile = open(inFilePath, "r", encoding='utf-8')
    outFile = open("code.py", "w", encoding='utf-8')
    
    addImports(outFile)
    convertScript(inFile, outFile)


if __name__ == "__main__":
    main()