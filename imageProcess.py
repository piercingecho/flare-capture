from PIL import Image
from findContour import findShape

def imageProcess(photostring):

    x = 500
    y = 1000
    value = -1
    im = Image.open(photostring)
    rgb_im = im.convert('RGB') #curious if this is actually needed
    pix = rgb_im.load()
    print(rgb_im.size)
    
    #find contours and display
    #findShape(photostring)

    while(x > -1 and y > -1):
        try:
            x1 = int(input("X value?"))
            y1 = int(input("Y value?"))
            
            pixel = rgb_im.getpixel((x1, y1))
            r1 = pixel[0]
            g1 = pixel[1]
            b1 = pixel[2]
            print(f"Pixel 1 color (RGB): {r1} {g1} {b1})")
            
            x2 = int(input("X value?"))
            y2 = int(input("Y value?"))

            pixel = rgb_im.getpixel((x2, y2))
            r2 = pixel[0]
            g2 = pixel[1]
            b2 = pixel[2]
            print(f"Pixel 2 color (RGB): {r2} {g2} {b2})")
            print(f"Difference in color (RGB): {abs(r1-r2)} {abs(g1-g2)} {abs(b1-b2)}")

        except:
            print("Something wrong with x and y coordinates given. Sorry!")
    
    

    '''
    newstring = photostring[0:len(photostring) - 4]
    print("Converting to png, this may take a bit...")
    im.save(newstring + ".png")
    print("Image saved as png")
    '''

def main():
    imageProcess('shapes.png')

if __name__=='__main__':
    main()
