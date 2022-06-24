import colorsys
import cv2
import numpy as np
from grayscaleFilter import *

def avgColorFilter(image, topLeftPoint, xLength, yLength):
    if(type(image) == str):
        openImage = cv2.cvtColor(cv2.imread(image), cv2.COLOR_BGR2RGB)
    else:
        openImage = image #this expects it to be in type RGB, tread with care
    
    sum_r = 0
    sum_g = 0
    sum_b = 0

    numPix = 0
    
    for x in range(xLength):
        for y in range(yLength):
            
            #openImage.shape gives (y,x) so that's why its indexes are reversed from the passed point
            if(x + topLeftPoint[0] < openImage.shape[1] and y + topLeftPoint[1] < openImage.shape[0]):
                pixel = openImage[topLeftPoint[1] + y][topLeftPoint[0] + x]
                
                if grayscaleFilter(pixel): #if a valid pixel:
                    numPix += 1
                    sum_r += pixel[0]
                    sum_g += pixel[1]
                    sum_b += pixel[2]
    if(numPix == 0):
        return (0,0,0)
    else:
        avg_r = sum_r / numPix
        avg_g = sum_g / numPix
        avg_b = sum_b / numPix
        return (avg_r, avg_g, avg_b)


def main():
    point = (225,400) #x by y
    color = avgColorFilter("coloredshapes.png", (200,400), 300,300)
    print(color)

if __name__ == '__main__':
    main()
