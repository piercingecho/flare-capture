from PIL import Image
import colorsys
import cv2
import numpy
#Takes each point in an image, and if it's white it creates a box that's 10 pixels wide and 25 height, 
#with the white point in the left center. If there are enough white pixels in that box, the coordinates of the
#initial white coordinate are returned. This can be applied effectively with CV2's canny library for shape detection,
#as white points will cluster around a particular object.

#This uses the numpy library, which has height, width as a tuple, differing from cv2's general method. Careful!

def shapeFinder(image, sentinel, points, y_range = -1, x_range = -1, ymin = 0, ymax = -1, xmin = 0, xmax = -1, x_reverse = False): #as an image object
    init_length = len(points)
    
     

    #please. change variable names. im begging you
    if(type(image) == str):
        image = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
        
    print("Beginning search, this might take a while...")
    
    #x_range is the width of square
    #y_range is the height of square we use to compare against sentinel.

    if(x_range == -1):
        x_range = int((image.shape[1])**(1/2) / 4)
    if(y_range == -1):
        y_range = int((image.shape[0])**(1/2) / 4)

    '''
    print("X range then Y range:", x_range)
    print(y_range)
    '''

    if(sentinel == 30 and x_range * y_range < 30):#forgot what I was thinking when I made this
        #sentinel = 5
        sentinel = 7
    
    if(ymax == -1):
        ymax = image.shape[0] - 1
    
    if(xmax == -1):
        xmax = image.shape[1] - 1
    
    if(ymin < 0):
        ymin = 0

    if(xmin < 0):
        xmin = 0
    
    #generally this looks through the whole image. But with the xmax/xmin and ymax/ymin changed, this changes the area where it will look for a valid point.

    for j in range(xmax - xmin): #width, X VALUE BECAUSE CV2 IS STUPID
        for i in range(ymax - ymin): #height, Y VALUE
            #black and white image, so this can just be a 2d array
            if(x_reverse == True):
                used_j = xmax - j
            else:
                used_j = j + xmin
            used_i = i + ymin


            #was: used_i + ymin, used_j + xmin
            if(image[used_i][used_j] ==255): #check the grayscale color value, if it's 255 then it is definitely white
                count = 1 #number of white pixels found
               
                
                #pixel is white, so check surroundings to right
                #and count number of other white pixels
                for a in range(x_range): #x change
                    for b in range(y_range * 2 + 1): #ychange, this will start at -12
                        #make sure that we only look at pixels that actually exist on the image
                        if(x_reverse == False):
                            if (( used_i - y_range + b) < image.shape[0]) and ((used_j + a) < image.shape[1]) and ((b + used_i - y_range) >= 0):
                                if(image[used_i - y_range + b][used_j + a] == 255):
                                    count += 1
                        else:
                            if ((used_j - a) > 0) and ((used_i - y_range + i) < image.shape[0]) and ((used_i - y_range + i) > 0):
                                if(image[used_i - y_range + b][used_j - a] == 255):
                                    count += 1

                if count >= sentinel:
                    #print(f"[{used_j}, {used_i}]", end = "     ")
                    points.append((used_j,used_i))
                    break
        if(len(points) > init_length):
            break
    
    if(len(points) == init_length):
        print("Didn't find anything, returning the list unchanged.")
        return (-1,-1)
    return points[len(points) - 1]
