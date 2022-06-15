from picamera import PiCamera
import RPi.GPIO as GPIO
from takePic import *
import os
from imageProcess import imageProcess

BtnPin=11

#current_img=0

def detect(chn):
    print("Button pressed")
    
    try:
        camera = PiCamera() #load camera

        photoname = takePic(camera, 0) #change to current_img
        print("Camera finished")
        os.system('fbi '+ photoname) #display photo to screen

        imageProcess(photoname) #image processing
         
        #current_img=current_img+1
        #GPIO.remove_event_detect(BtnPin)
        #GPIO.add_event_detect(BtnPin, GPIO.RISING, callback=prepare, bouncetime=2)
    except Exception as e:
        if(e == TypeError):
            print("Fork error on photo.")
        else:
            print(e)


def destroy():
	GPIO.cleanup()                     # Release button resource

def prepare(chn):
    print("Push the button when you're ready!")
    GPIO.remove_event_detect(BtnPin)
    GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=detect, bouncetime=2)

def setup(): 
    print("A!")
    prev_state = 0 #previous state of the button: checks for change
    GPIO.setmode(GPIO.BOARD) # Numbers GPIOs by physical location
    GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set BtnPin's mode is input, and pull up to high level(3.3V)
    GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=detect) #, bouncetime = 2
    print("Ready!")
