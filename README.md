##System Hardware requirements:
- Was tested on a raspberry pi 4, rasbian os version 11(bullseye), modifications may be necessary for it to work on other systems.
- A raspberry pi camera module and ribbon, and a raspberry pi button module. This button should be connected as follows: SIG connects to GPIO17; 3V3 connects to ; GND connects to Ground. A breadboard can also feasibly be used for this.



##System Software Requirements:
We imported:
	- OpenCV
	- Colorsys
	- Time
	- RPi.GPIO
	- Numpy
	- Matplotlib
	- Math

## Directions for Front-End Use:
After powering on the system, the user will place a completed bulb test sheet under the system(as close to the center as possible). Pull every module from GitHub into a giving directory. 

The user will then run the "main.py" function and wait for a preview of the camera to appear. Once the preview appears, the user is allowed to move the strip however much they want in order for the strip to be alligned with the camera. 

When the user is ready, they will push the button and wait for the cannied image, which they can then exit out of. They should then enter the type of test they ran, which for now consists of the three bulb-to-bulb interactions. Later implementation will exist for the one-to-three bulb. 

After waiting for the program to run, they should be met with multiple areas sectionedwith squares, each depicting a bulb. The program ends with giving each bulb's average RGB value, as well as the overall average between the left and right.


##Directions for Download, etc:


##Summary of Modules

- main: calls setup and executes the rest of the program.
- photomain630: takes an image, bypassing the need for the camera or button modules.
- setup: utilizes the button module to take a photo upon pressing the button, and showing a preview display until that point.

- datestring: constructs a unique string for an image file based on the exact date and time.
- takePic: takes photo on raspberryPi using piCamera2 / libcamera.

- edgeDetect: utilizes CV2 library's canny algorithm to find shapes through difference in color. Parameters optimized for detecting test slip.

-  findBulbSections: uses the proportions of the test slip to locate two pairs of x coordinates that each bound a test section.
- resize-and-display: alters canny output image then displays it to help with debugging (previously it was massive).

- placePoint and placeSection: uses matplotlib to show a list of points or a center with x and y radii to plot a point or rectangle, respectively. Primarily used in debugging.
- avgColorFilter: uses grayscaleFilter, a given image, and a rectangular section to find the average color while excluding unsaturated (grayscale) pixels.
- grayscaleFilter: Returns a boolean as to whether avgColorFilter will accept a given pixel or not. This has been made to ensure colors too black, too white, and too unsaturated (where all 3 color values are around the same) will not be counted.
- README.md: hi!
- shapeFinder: takes a canny image and list of points and reviews it from left to right. When it finds the first cluster of white points, it appends it to a passed-in list (empty or not) and then exits. Can go right to left using the variable x\_reverse, and can be passed in a non-empty list.

- setup: Sets up steps before a GPIO button is pressed, and event handler for when that occurs.
- main: The main function that utilizes all of these.




For Later Use

- saturationToConc: takes a low, high, and sample pixel, as well as low and high's concentration. Returns the expected concentration of the sample (which is between low and high) through linear interpolation.
- findConcentrations: searches a previously updated .csv file to 
