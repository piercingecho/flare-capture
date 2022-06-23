import colorsys

#pixel is a 3-tuple with the RGB values
#hue is an integer of which to find
#huerange is the amount of distance to go, above and below, the center. Code exits if this is over 180.
def hueFilter(pixel, hue, huerange):     
    
    h, s, v = colorsys.rgb_to_hsv(pixel[0]/255, pixel[1]/255, pixel[2]/255)

    #None of the filtering has been modified to account for this :(
   
    #keep it consistent with the code we've written already
    h = h * 360
    #print(h, s, v) 
    
    if(huerange >= 180):
        print("Warning: check hue range, it seems to include all hues.")
        return True

    '''
    h = -1 #hue
    s = -1 #saturate
    v = -1 #value
    
    cmax = max(pixel)
    cmin = min(pixel)
    delta = int(cmax) - int(cmin)

    #Value calc is relatively simple
    v = (int(cmax) + int(cmin)) / 2
    
    if delta == 0:
        h = 0
    else:
        #if you want to understand the rest of this calculation go to google I can't help you
        adj_r = pixel[0]/255
        adj_g = pixel[1]/255
                    if(tempx == center[0] and tempy == center[1]):                    
                        print(center)
        adj_b = pixel[2]/255
        if(cmax == pixel[0]):
            h = (adj_g - adj_b) * 60 / delta 
        elif(cmax == pixel[1]):
            h = (adj_b - adj_r) * 60 / delta + 120
        else:
            h = (adj_r - adj_g) * 60 / delta + 240

        if(h < 0):
            h += 360
        

    #Saturation
    print(colorsys.rgb_to_hsv(0/255, 0/255, 255/255))
    
    if(int(cmax) == 0):
        s = 0
    else:
        s = delta / int(cmax) * 100

    '''

    #convert pixel to hsv
    #if saturation is 0, toss it
    #if hue is outside of the range wanted, toss it  

    if(s <= 0.01):
        return False
    if(v < 0.1):
        return False

    #hueminimum and huemaximum are the lowest and highest values where the hue will be accepted.

    if(hue < huerange): #if the hue - huerange is less than 0, then minimum should be at the overshoot.
        hueminimum = 1 - hue
    else:
        hueminimum = hue - huerange
    if(1-hue < huerange): #if the hue + huerange overshoots 360, then the max should be that overshot distance. 
        huemaximum = huerange + hue - 1
    else:
        huemaximum = hue + huerange
    ###
    ###Below: find whether the pixel's hue is within range. Return True if it is, False if it isn't.
    ###
    
    if(hue < hueminimum): #loops below to high values
        if(h < huemaximum or h > hueminimum):
            #print(pixel)
            return True
        else:
            return False
    elif(hue > huemaximum): #loops above to low values
        if(h > hueminimum or h < huemaximum):
            #print(pixel)
            return True
        else:
            return False
    else: #everything's normal
        if(hueminimum < h and h < huemaximum):
            #print(pixel)
            return True
        else:
            return False

def main():
    a = hueFilter((199, 200, 204), 240, 15)
    print(a)
    print(colorsys.rgb_to_hsv(0/255, 0/255, 255/255))
    print(colorsys.rgb_to_hsv(60/255, 60/255, 255/255))


if __name__ == '__main__':
    main()
