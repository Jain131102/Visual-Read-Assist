#click_image.py this program clicks the image
# of the text through the raspberry pi camera

import time
import libcamera # importing the libraries 
import os
from picamera2 import Picamera2
speak=" VisualRead Assist Powering On "
os.popen('espeak "'+speak+'" --stdout | aplay 2>/dev/null').read()
speak=" "
os.popen('espeak "'+speak+'" --stdout | aplay 2>/dev/null').read()
speak=" Clicking Picture "
os.popen('espeak "'+speak+'" --stdout | aplay 2>/dev/null').read()

picam=Picamera2()
picam.brightness = 150 # Adjusting camera settings
picam.contrast = 90

config = picam.create_preview_configuration(main={"size": (512, 512)}) 
config["transform"] = libcamera.Transform(hflip=1, vflip=1)

picam.start() 
time.sleep(2)

picam.capture_file("img.png") # clicking picture

picam.close()

speak=" Picture clicked "
os.popen('espeak "'+speak+'" --stdout | aplay 2>/dev/null').read()
