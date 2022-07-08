from picamera2 import *
from datestring import datestring
import os
def takePic():
    
    photostring=datestring()
    os.system("libcamera-jpeg -o "+photostring+" -t 5")

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

    print("Photo taken")
    return photostring


def main():
    takePic()

if __name__ == '__main__':
    main()
