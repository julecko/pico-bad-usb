import argparse

def getDuckyFile():
    parser = argparse.ArgumentParser(description='Python script which converts ducky files into python scripts for raspberry pi pico')
    parser.add_argument('-i', type=str, help='Input file')
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
    )
    file.write(imports)

def main():
    inFile = getDuckyFile()
    outFile = open("code.py", "w")
    
    addImports(outFile)

if __name__ == "__main__":
    main()