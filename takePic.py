from picamera2 import Picamera2
from datestring import datestring
import os

def takePic():
    picam2 = Picamera2()
    photostring = datestring()
    
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

    print("Photo taken and photocopy created")
    return photostring


def main():
    takePic()

if __name__ == '__main__':
    main()
