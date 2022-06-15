from picamera import PiCamera
import time
from datetime import datetime
from datestring import datestring
import os

def takePic(camera, num):
    #camera = PiCamera()
    photostring = datestring()
    camera.capture(photostring)
    camera.close()
    
    #below is creating a duplicate file with the same photo

    newstring = photostring[0:len(photostring)-4]
    newstring += "_orig.jpg"
    os.system('cp ' + photostring + " " + newstring)

    print("Photo taken and photocopy created")
    return photostring
