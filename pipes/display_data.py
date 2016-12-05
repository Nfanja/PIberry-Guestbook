#!/usr/bin/env python3

import sys
import io
import pifacecad
import time
import argparse

display_size = [16, 2]
cad = pifacecad.PiFaceCAD()

def chunckstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

def show_greeting(greeting, scroll_speed):
    cad.lcd.set_cursor(0,0)
    cad.lcd.write(greeting)
    for i in range(len(greeting)):
        time.sleep(scroll_speed)
        cad.lcd.move_left()

def main():
    parser = argparse.ArgumentParser(description="Displays messages on PI")
    parser.add_argument("messages", nargs='?', help="String of messages", default=sys.stdin)
    parser.add_argument("-s", "--speed", help="Delay between move_left commands in ms", default=0.5)
    args = parser.parse_args()


    for line in args.messages:
        show_greeting(line, float(args.speed))

#    for line in sys.stdin:
#        show_greeting(line,0.5)
        
if __name__ == '__main__':
    main()
