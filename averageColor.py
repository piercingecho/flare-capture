from PIL import Image
from findContour import findShape

def averageColor(openImage, center, imageXlength, imageYlength, xradius, yradius):

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
    x = 500
    y = 1000
    value = -1
    im = Image.open('shapes.png')
    rgb_im = im.convert('RGB') #curious if this is actually needed
    pix = rgb_im.load()
    t_size = rgb_im.size
    sizex = t_size[0]
    sizey = t_size[1]

    t_pixel = averageColor(rgb_im, (100,100), 50, 50, sizex, sizey)
    

if __name__=='__main__':
    main()
