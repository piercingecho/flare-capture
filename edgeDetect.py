import cv2
import numpy

def edgeDetect(string):
    img =cv2.imread(string)
    print("Dimensions:", img.shape)

    imgCanny=cv2.Canny(img, 90, 90) #50 low, 70 high maybe
    cv2.imshow("Shapes", imgCanny)
    cv2.waitKey(0)

def main():
    edgeDetect("shapes.png")

if __name__ == '__main__':
    main()
