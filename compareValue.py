#pixellow and pixelhigh are the two to make comparisons with. pixeltest is the
#new value. These are all RGB values.
def compareValue(pixellow, pixelhigh, pixeltest, conclow, conchigh):
    values[3] = [-1, -1, -1]
    for i in range(3):
        pixel = args[i]
        cmax = max(pixel)
        cmin = min(pixel)
        values[i] = (cmax + cmin) / 2
    
    #points for line to be created
    point1 = (values[0], conclow)
    point2 = (values[1], conchigh)

    #point slope form, taken from point1.
    m = (conchigh - conclow) / (values[1] - values[0])
    sampleconc = conclow + (values[2]-values[0]) * m
    return sampleconc
