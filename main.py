import os
from picamera import PiCamera
import time
from takePic import takePic
from setup import *
import RPi.GPIO as GPIO
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
    setup()
    try:
        while 1==1:
            pass
    except KeyboardInterrupt:
        destroy()

if __name__ == '__main__':
    main()
