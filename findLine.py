import os

import cv2

import numpy as np
import matplotlib.pyplot as plt

def findImage(photostring):
    image = cv2.imread(photostring)

    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(grayscale, 30, 100)

    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 60, np.array([]), 50, 5)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(image, (x1,y1), (x2,y2), (20, 220, 20), 3)
    
    cv2.imwrite("shapes2.png", image)
    #plt.imshow(image)
    #plt.show()

    os.system('fbi ' + "shapes2.png")
def main():
    findImage("shapes.png")

if(__name__=='__main__'):
    main()
