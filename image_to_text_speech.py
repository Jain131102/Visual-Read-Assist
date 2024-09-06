#image_to_text_speech.py this program performs
# image to text and text to speech.

import os
from PIL import Image # importing the libraries
import pytesseract

img=Image.open('img.png')
text=pytesseract.image_to_string(img,config='') # Image to Text

# Text to speech
speak=" Reading Text "
os.popen('espeak "'+speak+'" --stdout | aplay 2>/dev/null').read()

speak=" "
os.popen('espeak "'+speak+'" --stdout | aplay 2>/dev/null').read()

speak = text
print(speak)
os.popen('espeak "'+speak+'" --stdout | aplay 2>/dev/null').read()

speak="DONE"
os.popen('espeak "'+speak+'" --stdout | aplay 2>/dev/null').read()
print(speak)
