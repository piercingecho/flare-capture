import colorsys

def grayscaleFilter(pixel):     
    
    cmax = max(pixel)
    cmin = min(pixel)
    delta = int(cmax) - int(cmin)
    if(delta >= 30):
        if(cmin < 175):
            if(cmax > 100):
                return True
        
    return False




def main():
    pass

if __name__ == '__main__':
    main()
