#!/usr/bin/env python3

import sys
import io
import pifacecad
import time

display_size = [16, 2]
cad = pifacecad.PiFaceCAD()

def chunckstring(string, length):
	return (string[0+i:length+i] for i in range(0, len(string), length))

# def show_greeting(greeting, scroll_speed):
# 	for chunk in chunckstring(greeting[3], display_size[0] * display_size[1]):
# 		cad.lcd.write('\n'.join(chunckstring(chunk, display_size[0])))
# 		time.sleep(scroll_speed)
def show_greeting(greeting, scroll_speed):
	cad.lcd.set_cursor(0,0)
	cad.lcd.write(greeting)
	for i in range(len(greeting)):
		time.sleep(scroll_speed)
		cad.lcd.move_left()

def main():
	for line in sys.stdin:
		show_greeting(line,0.5)
		
if __name__ == '__main__':
	main()
#    sys.stdout.write(main())
