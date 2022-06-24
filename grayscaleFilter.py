import colorsys

def grayscaleFilter(pixel):     
    
    cmax = max(pixel)
    cmin = min(pixel)
    delta = int(cmax) - int(cmin)
    '''    
    if(pixel[0] < 20):
        return True
    else:
        return False
    '''
    if(delta >= 65):
        if(cmin < 220):
            if(cmax > 100):
                return True
        
    
    return False




def main():
    a = hueFilter((199, 200, 204), 240, 15)
    print(a)
    print(colorsys.rgb_to_hsv(0/255, 0/255, 255/255))
    print(colorsys.rgb_to_hsv(60/255, 60/255, 255/255))


if __name__ == '__main__':
    main()
