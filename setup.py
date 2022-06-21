import RPi.GPIO as GPIO
from takePic import takePic
import os
from imageProcess import imageProcess
from edgeDetect import edgeDetect
BtnPin=11


def detect(chn):
    print("Button pressed")

    ###
    ###fork
    ###
    

    parent = os.getpid()
    print(parent)
    #kill the child system and the window it created
    os.system("kill " + str(parent + 1))
    os.system("kill " + str(parent + 3))
    os.system("kill " + str(parent + 4))

    
    ###keep

    photoname = takePic() #change to current_img
    print("Camera finished")
    edgeDetect(photoname)
    

    #imageProcess(photoname) #image processing
             

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
        pass
        exit(1)
    elif(pid == 0):
        print("Child", os.getpid())
        os.system("libcamera-hello -t 0")
    else:
        print("Parent", os.getpid())
        
        ###needed
        GPIO.setmode(GPIO.BOARD) # Numbers GPIOs by physical location
        GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set BtnPin's mode is input, and pull up to high level(3.3V)
        GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=detect) #, bouncetime = 2 
        print("Ready for photo! Click button for a still image.")
