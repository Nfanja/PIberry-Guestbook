import pifaced
import os
import signal
import time

import urllib.request
import xml.etree.ElementTree as EL

display_size = [16, 2]

# you can ignore these three lines of code
# they are needed so that you can end the
# program by pressing Ctrl+C
def signal_handler(signal, frame):
	os._exit(0)
signal.signal(signal.SIGINT, signal_handler)

def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

def show_greeting(greeting, sroll_speed):
	for chunk in chunkstring(greeting[3].text, display_size[0] * display_size[1]):
		cad.lcd.write('\n'.join(chunkstring(chunk, display_size[0])
		time.sleep(scroll_speed)

# fetch the data
xml = urllib.request.urlopen("http://192.168.1.100:8080/rest/guestbook/").read()
# parse the data and create a XML tree
root = EL.fromstring(xml)
# we can now iterate over the XML tree
# the greetings are the children of root
# the content tag is the 4th (so index 3)
# child of a greeting

# all_greetings = ""
# for greeting in root:
# 	all_greetings += greeting[3].text
# 
# cad = pifacecad.PiFaceCAD()
# cad.lcd.write(all_greetings)
# 
# for greeting in root:
# 	for chunk in chunkstring(greeting, display_size[0] * display_size[1]):
# 		cad.lcd.write('\n'.join(chunkstring(chunk, display_size[0])
# 		time.sleep(1)

guestbook_len = len(root)
current_greeting = 0
show_greeting(root[current_greeting], 1)

def update_pin_text(event):
	event.chip.lcd.set_cursor(0, 0)
	event.chip.lcd.clear()
	print(str(event.pin_num))
	if event.pin_num == 4:
		current_greeting = (current_greeting + 1) % guestbook_len
		show_greeting(root[current_greeting], 1)

listener = pifacecad.SwitchEventListener(chip=cad)

for i in range(8):
	listener.register(i, pifacecad.IODIR_FALLING_EDGE, update_pin_text)
listener.activate()
