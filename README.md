This program utilizes a.

Research under Centre College, under Dr. David Toth. 

System Hardware requirements:
- Was tested on a raspberry pi 4, modifications may be necessary for it to work on other systems.

System Software Requirements:








Summary of Modules

- avgColorFilter: uses grayscaleFilter, a given image, and a rectangular section to find the average color while excluding unsaturated (grayscale) pixels.
- datestring: constructs a unique string for an image file based on the exact date and time.
- edgeDetect: utilizes CV2 library's canny algorithm to find shapes through difference in color. Parameters optimized for detecting test slip.
- findBulbSections: uses the proportions of the test slip to locate two pairs of x coordinates that each bound a test section.
- grayscaleFilter: Returns a boolean as to whether avgColorFilter will accept a given pixel or not. This has been made to ensure colors too black, too white, and too unsaturated (where all 3 color values are around the same) will not be counted.
- placePoint and placeSection: uses matplotlib to show a list of points or a center with x and y radii to plot a point or rectangle, respectively. Primarily used in debugging.
- README.md: hi!
- resize-and-display: alters canny output image then displays it to help with debugging (previously it was massive).
- shapeFinder: takes a canny image and list of points and reviews it from left to right. When it finds the first cluster of white points, it appends it to a passed-in list (empty or not) and then exits. Can go right to left using the variable x\_reverse, and can be passed in a non-empty list.

- takePic: takes photo on raspberryPi using piCamera2 / libcamera.
- setup: Sets up steps before a GPIO button is pressed, and event handler for when that occurs.
- main: The main function that utilizes all of these.




For Later Use

- compareValue: takes a low, high, and sample pixel, as well as low and high's concentration. Returns the expected concentration of the sample (which is between low and high) through linear interpolation.
