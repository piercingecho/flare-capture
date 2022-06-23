from PIL import Image
import colorsys
from hueFilter import hueFilter
import cv2
from grayscaleFilter import grayscaleFilter
hran = 179 #huerange

def colorFilter(openImage, center, xradius, yradius, hue):
    
    if type(openImage) == str:
        openImage = cv2.imread(openImage)
    
    imageXlength = openImage.shape[0]
    imageYlength = openImage.shape[1]

    try:
        avg_r = 0
        avg_g = 0
        avg_b = 0
        numPixels = 0 
        if(imageXlength <= 0 or imageYlength <= 0):
            raise(ValueError)
        for i in range(xradius * 2):
            for j in range(yradius * 2):
                #these are the pixel coordinates that are being worked with. Start halfway to the left/above the x/y respectively.
                #int conversion floors them because they're always positive
                tempx = center[0] + i - (int(xradius))
                tempy = center[1] + j - (int(yradius)) 
                if(tempx < imageXlength and tempy < imageYlength and tempx > 0 and tempy > 0): #check bounds
                    pixel = openImage[tempx][tempy]
                    #Hue filter takes hte desired hue and pixel, and finds whether that pixel falls int he desired hue or not.

                    #if(hueFilter(pixel, hue, hran)):
                    
                    if grayscaleFilter(pixel):
                        #These take the previous average, and compute a new average with the newly added value.
                        #multiply by the previous number of data points, add the value of the new data point, then divide by n again.
                        numPixels += 1
                        avg_r = (pixel[0] * (numPixels - 1) + pixel[0]) / (numPixels) 
                        avg_g = (pixel[1] * (numPixels - 1) + pixel[1]) / (numPixels)  
                        avg_b = (pixel[2] * (numPixels - 1) + pixel[2]) / (numPixels)
                        print(avg_r, pixel[0])

        #print(f"Average pixel color (RGB): {avg_r} {avg_g} {avg_b})")
        return avg_r, avg_g, avg_b
                        
    except Exception as e:
        print(e)
        print("Something's wrong with function AverageColor; exiting and returning black.")
        return 0, 0, 0
    
    

    '''
    newstring = photostring[0:len(photostring) - 4]
    print("Converting to png, this may take a bit...")
    im.save(newstring + ".png")
    print("Image saved as png")
    '''

def main():
    value = -1
    im = Image.open('Images/lakePic.jpg')
    t_size = im.size
    print(f"Dimensions: {t_size[0]} {t_size[1]}")
    
    ###
    ###Change these values!
    ###

    x_center = 150  #this is the center of the RANGE TO AVERAGE, *not* the image as a whole!
    y_center = 350
    x_radius = 40 #this is the radius of the range to average, going equally on both sides of the center
    y_radius = 40
    hue = 0
    


    t_pixel = colorFilter(im, (x_center, y_center), t_size[0], t_size[1], x_radius, y_radius, hue) #red
    

if __name__=='__main__':
    main()
