from picamera2 import *
#from qt_gl_preview import *

from datestring import datestring
import os
import time

def takePic():
    
    '''a'''
    picam2 = Picamera2()
    photostring = datestring()
    
    #preview_config = picam2.preview_configuration()
    

    '''b'''
    still_config = picam2.still_configuration()
    
    #picam2.start_preview(Preview.QTGL)
    #picam2.configure(preview_config)
    
    '''c'''
    picam2.configure(still_config)
    picam2.start()
    
    #time.sleep(2)
    #picam2.switch_mode_and_capture_file(still_config, photostring)
    
    '''d'''
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
