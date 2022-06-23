import RPi.GPIO as GPIO
import os

from takePic import takePic
from imageProcess import imageProcess
from edgeDetect import edgeDetect
from shapeFinder import *
from placePoint import *
from findBulbSections import *
from placeSections import *
from averageColorFilter import *
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
    bwimage = edgeDetect(photoname)
    horiz_edges = []
    
    #points has 2 values: leftmost and rightmost. Both are tuples
    points = shapeFinder(bwimage, 30, horiz_edges)  #"bwimage.jpg"
    points = shapeFinder(bwimage, 30, horiz_edges, x_reverse = True)
    
    #placePoint("bwimage.jpg", horiz_edges)
    #placePoint(photoname, horiz_edges)
    
    #THIS FINDS THE SECTIONS
    #four X values: first 2 are the left bulb, second 2 are the right bulb
    l_bulbs = findBulbSections(points)
   


    #this is plotting four!
    '''
    l_points_to_plot = []
    for i in range(4):
        l_points_to_plot.append((l_bulbs[i], points[0][1]))
    
    placeSect(photoname, l_points_to_plot)
    '''

    #now that we have our four x coordinates, we can find the centers & radii
    #of the two bulbs
    
    xrad = int((l_bulbs[1] - l_bulbs[0]) / 2) #half of the distance between these 2
    yrad = int(xrad * 8/7)  #take into account the likely error with vertical positioning

    leftCenter = (l_bulbs[0] + xrad, points[0][1]) 
    rightCenter = (l_bulbs[2] + xrad, points[1][1])
    
    leftColor = colorFilter(photoname, leftCenter, xrad, yrad, 200) 
    rightColor = colorFilter(photoname, rightCenter, xrad, yrad, 200)

    print("Left bulb average color:", leftColor)
    print("Right bulb average color:", rightColor)


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
