from cv2 import imread, cvtColor, RETR_TREE, threshold, findContours, approxPolyDP, drawContours, moments, arcLength, CHAIN_APPROX_SIMPLE, THRESH_BINARY, COLOR_BGR2GRAY, putText, FONT_HERSHEY_SIMPLEX
from cv2 import imwrite

import numpy as np
from matplotlib import pyplot as plt
import os

def findShape(photostring):

    img = imread(photostring)

    #convert image to grayscale
    
    gray = cvtColor(img, COLOR_BGR2GRAY)

    #setting threshold of gray image
    _, thresholdvar = threshold(gray, 127, 255, THRESH_BINARY)

    #using a findContours() function
    contours, _ = findContours(
            thresholdvar, RETR_TREE, CHAIN_APPROX_SIMPLE)

    i = 0

    #list for storing names of shapes
    for contour in contours:
        i += 1
    print("Contour count:", i)
    
    i = 0
    
    for contour in contours:

        #here we are ignoring first counter because
        #findcontour function detects whole image as shape
        if i == 0:
            i = 1
            continue

        #cv2.approxPloyDP() function to approximate the shape
        approx = approxPolyDP(
                contour, 0.01 * arcLength(contour, True), True)
        
        if i == 1:
            print(approx)

        #using drawContours() function
        #drawContours(img, [contour], -1, (0, 0, 255), 5) #works with -1 as 0 as well?

        #finding center point of shape
        M = moments(contour)
        if M['m00'] != 0.0:
            x = int(M['m10']/M['m00'])
            y = int(M['m01']/M['m00'])

            #putting shape name at center of each shape
            name_array = ['Triangle', 'Quadrilateral', 'Pentagon', 'Hexagon', 'Circle']
            
            index = len(approx) - 3
            if(index > 4):
                index = 4
            if index == 1: #just put a contour where there are squares. Will place all (too many) contours if this isn't present.
                putText(img, name_array[index], (x,y), FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
            i += 1
    
    imwrite(photostring, img)

    os.system('fbi ' + photostring)

def main():
    findShape("shapes.png")

if __name__ == '__main__':
    main()
