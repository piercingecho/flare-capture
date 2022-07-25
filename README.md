## System Hardware requirements:
- Was tested on a raspberry pi 4, rasbian os version 11(bullseye), modifications may be necessary for it to work on other systems.
- A raspberry pi camera module and ribbon, and a raspberry pi button module. This button should be connected as follows: SIG connects to GPIO17; 3V3 connects to ; GND connects to Ground. A breadboard can also feasibly be used for this.



## System Software Requirements:
We imported:
	- Python
	- Pip 3
	- OpenCV
	- Colorsys
	- Time
	- RPi.GPIO
	- Numpy
	- Matplotlib
	- Math
 
Below is a list of commands that should work to install all of these as needed:

	1. sudo apt-update
	2. sudo apt-install python3
	3. sudo apt-install pip3
	4. pip3 install time
	5. pip3 install math
	6. pip3 install matplotlib
	7. pip3 install RPi.GPIO
	8. pip3 install numpy
	9. pip3 install colorsys
	
	10. sudo pip3 install python-opencv


# Directions for Front-End Use:
After powering on the system, the user will place a completed bulb test sheet under the system(as close to the center as possible). Pull every module from GitHub into a giving directory. 

The user will then run the "main.py" function and wait for a preview of the camera to appear. Once the preview appears, the user is allowed to move the strip however much they want in order for the strip to be alligned with the camera. Make sure that the camera shows the lines going horizontally between each pair of bulbs.

Note: each time an image appears, you must close out of the window before continuing.

When the user is ready, they will push the button and wait for the cannied image, which they can then exit out of. They should then enter the type of test they ran, which for now consists of the three bulb-to-bulb interactions. Later implementation will exist for the one-to-three bulb. 

After waiting for the program to run, they should be met with multiple areas sectionedwith squares, each depicting a bulb. The program ends with giving each bulb's average RGB value, as well as the overall average between the left and right.

They will also be ased which type of substance they are testing for, and they will be prompted to type it in verbatim. For now, type in "Trypsin." This should give the expected concentration of the third bulb..



# Summary of Modules

- main: calls setup and executes the rest of the program.
- photomain630: takes an image, bypassing the need for the camera or button modules (the three programs described below).

- setup: utilizes the button module to take a photo upon pressing the button, and showing a preview display until that point.
- datestring: constructs a unique string for an image file based on the exact date and time.
- takePic: takes photo on raspberryPi using piCamera2 / libcamera.

- edgeDetect: utilizes CV2 library's canny algorithm to find shapes through difference in color. Parameters optimized for detecting test slip.
- inputLoop: Asks which type of image the user submitted. For now, only the three bulb-to-bulb is relevant.

- shapeFinder: takes in the canny image from edgeDetect. Appends a point to a list passed in, then exits. The way this works: it goes through every pixel of a cannied image, top-down then left-to-right. 
  [x reverse boolean makes this search right to left instead]. [it searches within ymin ymax, and xmin xmax]. 
  When it finds a white pixel from the canny, it then creates a "search box", length and width are xrange and yrange. This search box is positioned on the side of the pixel, so that the left side of the square is bisected by the pixel (or the right side, if x reverse is true). In other words, it goes half of yrange up *and* down, while only going to one side for xrange.
  If this search finds enough ('sentinel' or more) white pixels in the search box, the initially found pixel is returned.
  
  
- threeBulbAlg: Uses shapeFinder multiple times to find each part of the three bulbs. Afterwards, it uses the csv file and colors it collected to determine the concentration.

     Further in depth:
	threeBulbAlg uses shapeFinder twice, the second time with x_reverse = True, in order to find what will likely be the top bulb of one side, and the bottom bulb of the opposing side. (If this doesn't make sense, hold the bulb structure at a slight angle and read about shapeFinder). From this, it determines the bulb that has a lower y value, and relocates the other side's bulb with a restricted ymin and ymax. From there, it uses findBulbSections to find the size of each bulb in pixels, then some simple math to find the centers of the top two bulbs. From there, we do a similar algorithm and restrict the y values to a slightly higher amount, so that we will be certain to find the center 2 bulbs then the bottom 2 bulbs.
	
	From there, we use avgColorFilter on each bulb in order to get their color values. We intend to later add in functionality with 
     



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
- findConcentrations: searches a previously updated .csv file to find the lower and higher callibration points' concentrations. Using this in saturationToConc, we can use the saturation of the three bulbs to determine the last one's value.
- input thing (csv): Asks which type of substance to test for. Works with findConcentrations.
