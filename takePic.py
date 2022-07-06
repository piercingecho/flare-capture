from picamera2 import *
#from picamera import PiCamera
#from qt_gl_preview import *

from datestring import datestring
import os
import time
import cv2
from picamera2 import Picamera2
from picamera import PiCamera
def takePic():
    
    '''
    photostring="test.jpg" #datestring()
    cam=cv2.VideoCapture()
    print(cam.read())

    result, image =cam.read()
    if result:
        print("A")
        cv2.imshow("Preview", image)
        cv2.waitKey(2)
        cv2.imwrite(photostring,image)

    else:
        print("No image detected, try again")
        photostring = takePic()
    '''
    
    '''
    photostring=datestring()
    picam=PiCamera()
    picam.start_preview()
    time.sleep(5)
    picam.capture(photostring)
    picam.stop_preview()
    '''

    #before everything broke
    
    picam2 = Picamera2()
    photostring = datestring()
    
    #preview_config = picam2.preview_configuration()
    
    still_config = picam2.still_configuration()
    
    #picam2.start_preview(Preview.QTGL)
    #picam2.configure(preview_config)
    
    picam2.configure(still_config)
    picam2.start()
    
    #time.sleep(2)
    #picam2.switch_mode_and_capture_file(still_config, photostring)
    
    picam2.capture_file( photostring)
    



    '''
    picam2.start_preview(alpha = 192)
    picam2.capture(datestring + ".jpg")
    picam2.stop_preview()

    #image = picam2.capture_image()
    

    ##test this and see what you broke

    request = picam2.capture_request()
    #this request has been taken by the application and can now be used for example
    request.save("main", "test.jpg")
    #once done, the request must be returned
    request.release

    #camera.capture(photostring)
    #camera.close()
    
    #below is creating a duplicate file with the same photo
    
    newstring = photostring[0:len(photostring)-4]
    newstring += "_orig.jpg"
    os.system('cp ' + photostring + " " + newstring)
    '''
    print("Photo taken")
    return photostring


def main():
    takePic()

if __name__ == '__main__':
    main()
