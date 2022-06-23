import cv2
import numpy
from resize_and_display import *

def edgeDetect(string):
    img =cv2.imread(string)
    print("Dimensions:", img.shape)

    imgCanny=cv2.Canny(img, 65, 65) #50 low, 70 high maybe
    
    resize_and_display(imgCanny, 0.25)

    cv2.waitKey(0)
    cv2.imwrite('blackwhiteimg.jpg', imgCanny)
    return imgCanny

def main():
    edgeDetect("shapes.png")

if __name__ == '__main__':
    main()
