from PIL import Image
from findContour import findShape
import colorsys
from hueFilter import hueFilter

def colorFilter(openImage, center, imageXlength, imageYlength, xradius, yradius, hue):

    try:
        avg_r = 0
        avg_g = 0
        avg_b = 0
        
        if(imageXlength <= 0 or imageYlength <= 0):
            raise(ValueError)

        for i in range(xradius):
            for j in range(yradius):
                #these are the pixel coordinates that are being worked with. Start halfway to the left/above the x/y respectively.
                #int conversion floors them because they're always positive
                tempx = center[0] + i - (int(xradius / 2))
                tempy = center[1] + j - (int(yradius / 2)) 
                if(tempx < imageXlength and tempy < imageYlength and tempx > 0 and tempy > 0): #check bounds
                    pixel = openImage.getpixel((tempx, tempy))
                    r1 = pixel[0]
                    g1 = pixel[1]
                    b1 = pixel[2]
                    #These take the previous average, and compute a new average with the newly added value.
                    #multiply by the previous number of data points, add the value of the new data point, then divide by n again.
                    avg_r = (avg_r * (i*xradius + j) + r1) / (i*xradius + j + 1) 
                    avg_g = (avg_g * (i*xradius + j) + g1) / (i*xradius + j + 1)  
                    avg_b = (avg_b * (i*xradius + j) + b1) / (i*xradius + j + 1) 

        print(f"Average pixel color (RGB): {avg_r} {avg_g} {avg_b})")
        
        return avg_r, avg_g, avg_b
                        
    except:
        print("Something's wrong with function AverageColor; exiting and returning black.")
        return 0, 0, 0
    
    

    '''
    newstring = photostring[0:len(photostring) - 4]
    print("Converting to png, this may take a bit...")
    im.save(newstring + ".png")
    print("Image saved as png")
    '''

def main():
    x = 150
    y = 50
    value = -1
    im = Image.open('shapes.png')
    t_size = im.size
    print(f"Dimensions: {t_size[0]} {t_size[1]}")
    
    ###
    ###Change these values!
    ###

    x_center = 130 #this is the center of the RANGE TO AVERAGE, *not* the image as a whole!
    y_center = 160
    x_radius = 1 #this is the radius of the range to average, going equally on both sides of the center
    y_radius = 1
    hue = 0
    


    t_pixel = colorFilter(im, (x_center, y_center), t_size[0], t_size[1], x_radius, y_radius, hue) #red
    

if __name__=='__main__':
    main()
