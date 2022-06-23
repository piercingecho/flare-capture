from PIL import Image
import colorsys
import cv2
import numpy
#Takes each point in an image, and if it's white it creates a box that's 10 pixels wide and 25 height, 
#with the white point in the left center. If there are enough white pixels in that box, the coordinates of the
#initial white coordinate are returned. This can be applied effectively with CV2's canny library for shape detection,
#as white points will cluster around a particular object.

#This uses the numpy library, which has height, width as a tuple, differing from cv2's general method. Careful!

def shapeFinder(image, sentinel, points, x_reverse = False): #as an image object
    init_length = len(points)

    #please. change variable names. im begging you
    print(type(image))
    if(type(image) == str):
        image = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
        
    print("Beginning search, this might take a while...")

    for j in range(image.shape[1] - 1): #width, X VALUE BECAUSE CV2 IS STUPID
        for i in range(image.shape[0] - 1): #height, Y VALUE
            #black and white image, so this can just be a 2d array
            if(x_reverse == True):
                used_j = image.shape[1] - 1 - j
            else:
                used_j = j
            used_i = i



            if(image[used_i][used_j] ==255): #check the grayscale color value, if it's 255 then it is definitely white

                count = 1 #number of white pixels found
                
                #pixel is white, so check surroundings to right
                #and count number of other white pixels
                for a in range(10):
                    for b in range(25): #this will start at -12
                        #make sure that we only look at pixels that actually exist on the image
                        if ((a + used_i) < image.shape[0]) and ((b + used_j - 12) < image.shape[1]) and ((b + used_j - 12) >= 0):
                            if(image[used_i + a][used_j + b - 12] ==255):
                                count += 1
                if count >= sentinel:
                    points.append((used_j,used_i))
                    break
        if(len(points) > init_length):
            break
    
    if(len(points) == init_length):
        print("Didn't find anything, returning the list unchanged.")
    return (points)
