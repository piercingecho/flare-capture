from takePic import takePic
from setup import *
import os
BtnPin = 11
'''
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imshow, imread
from skimage.color import rgb2hsv, hsv2rgb #for hue saturation value, rgb
from skimage.io import imshow, imread
import cv2
'''

def main():
    #os.system("export PYTHONPATH=/home/centrepi/Research2022/bulbDetect")
    setup()
    try:
        while 1==1:
            pass
    except KeyboardInterrupt:
        destroy()

if __name__ == '__main__':
    main()
