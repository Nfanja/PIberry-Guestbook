import pifaced
import os
import signal

import urllib.request
import xml.etree.ElementTree as EL

# you can ignore these three lines of code
# they are needed so that you can end the
# program by pressing Ctrl+C
def signal_handler(signal, frame):
	os._exit(0)
signal.signal(signal.SIGINT, signal_handler)

# fetch the data
xml = urllib.request.urlopen("http://192.168.1.100:8080/rest/guestbook/").read()
# parse the data and create a XML tree
root = EL.fromstring(xml)
# we can now iterate over the XML tree
# the greetings are the children of root
# the content tag is the 4th (so index 3)
# child of a greeting

all_greetings = ""
for greeting in root:
	all_greetings += greeting[3].text

cad = pifacecad.PiFaceCAD()
cad.lcd.write(all_greetings)

