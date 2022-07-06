import RPi.GPIO as GPIO
import os
import sys

from takePic import takePic
from inputLoop import inputLoop
from bulbBulbAlg import bulbBulbAlg
from bulbChannelAlg import bulbChannelAlg
from threeBulbsAlg import threeBulbsAlg
from picamera import PiCamera

BtnPin=11


def detect(chn):
    parent = os.getpid()
    GPIO.remove_event_detect(BtnPin)

    print("Button pressed")
    os.system("kill " + str(parent + 1))
    #kill the child system and the window it created
    os.system("killall libcamera-hello")

     

    photoname = takePic()
    print("Camera finished")
    
    choice = inputLoop()
    if(choice == 1):
        bulbBulbAlg(photoname)
    elif(choice == 2):
        bulbChannelAlg(photoname)
    elif(choice == 3):
        threeBulbsAlg(photoname)
    sys.exit()


def destroy():
    GPIO.cleanup()                     # Release button resource
    os.system("killall -9 python")
    
def setup():
    ###
    ###fork
    ###
    pid = os.fork()
    if(pid < 0):
        #error, set up later
        exit(1)
    elif(pid == 0):
        
        os.system("libcamera-hello -t 0")
    else:
        
        ###needed
        GPIO.setmode(GPIO.BOARD) # Numbers GPIOs by physical location
        GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set BtnPin's mode is input, and pull up to high level(3.3V)
        GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=detect) #, bouncetime = 2 
        print("Ready for photo! Click button for a still image.")
        
        
