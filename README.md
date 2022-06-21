This program utilizes a.

Research under Centre College, under Dr. David Toth. 

System Hardware requirements:
- Was tested on a raspberry pi 4, modifications may be necessary for it to work on other systems.

System 


Program Summary

- averageColor: takes a center and radius, and constructs a square of pixels to take in and average.
- hueFilter: returns a boolean, given an RGB pixel, target hue, and range of error. This boolean represents if the RGB pixel's hue is within this range.
- averageColorFilter: uses hueFilter to make the average color only include pixels that are in a target hue.
- compareValue: takes a low, high, and sample pixel, as well as low and high's concentration. Returns the expected concentration of the sample (which is between low and high) through linear interpolation.
- datestring: constructs a unique string for an image file based on the exact date and time.
- edgeDetect: utilizes CV2 library to find shapes through difference in color. Parameters optimized for detecting test slip.
- imageProcess: was formerly used to find a single pixel within an image. Unsure of its current functionality.
- takePic: takes photo on raspberryPi using piCamera2 / libcamera.
- setup: Sets up steps before a GPIO button is pressed, and event handler for when that occurs.
- main: The main function that utilizes all of these.
