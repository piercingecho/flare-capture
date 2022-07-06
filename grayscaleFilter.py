import colorsys

def grayscaleFilter(pixel):     
    
    cmax = max(pixel)
    cmin = min(pixel)
    delta = int(cmax) - int(cmin)
    return True
    if(delta >= 30):
        if(cmin < 170):
            if(cmax > 100):
                return True
        
        
    return False




def main():
    pass

if __name__ == '__main__':
    main()
