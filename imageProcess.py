from PIL import Image
from findContour import findShape

def imageProcess(photostring):

    x = 500
    y = 1000
    value = -1
    im = Image.open(photostring)
    pix = im.load()
    print(im.size)
    
    #find contours and display
    findShape(photostring)

    while(x > -1 and y > -1):
        try:
            x = int(input("X value?"))
            y = int(input("Y value?"))

            print(pix[x,y])
            pix[x,y] = value
        except:
            print("Something wrong with x and y coordinates given. Sorry!")
    
    

    '''
    newstring = photostring[0:len(photostring) - 4]
    print("Converting to png, this may take a bit...")
    im.save(newstring + ".png")
    print("Image saved as png")
    '''
