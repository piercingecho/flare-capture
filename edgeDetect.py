import cv2
import numpy
from resize_and_display import *

def edgeDetect(string):
    img =cv2.imread(string)

    imgCanny=cv2.Canny(img, 120,80) #50 low, 70 high maybe
    

    if(img.shape[0] > 1300 or img.shape[1] > 1300):
        resize_and_display(imgCanny, 0.25)
    else:
        resize_and_display(imgCanny, 0.5)


    cv2.waitKey(0)
    cv2.imwrite('blackwhiteimg.jpg', imgCanny)
    return imgCanny

def main():
    edgeDetect("shapes.png")

if __name__ == '__main__':
    main()
