#pixellow and pixelhigh are the two to make comparisons with. pixeltest is the
#new value. These are all RGB values.
import colorsys

def saturation_to_conc(pixellow, pixelhigh, pixeltest, conclow, conchigh):
    saturations = []
    
    #get saturations: the second element rgb_to_hsv returns

    saturations.append(colorsys.rgb_to_hsv(pixellow[0], pixellow[1], pixellow[2])[1])
    saturations.append(colorsys.rgb_to_hsv(pixelhigh[0], pixelhigh[1], pixelhigh[2])[1])
    saturations.append(colorsys.rgb_to_hsv(pixeltest[0], pixeltest[1], pixeltest[2])[1])

    print(saturations)

    
    #points for line to be created
    point1 = (saturations[0], conclow)
    point2 = (saturations[1], conchigh)

    #point slope form, taken from point1.
    if(conchigh - conclow != 0):
        m = (conchigh - conclow) / (saturations[1] - saturations[0])
    else:
        m = 0
        print("Same color for two samples; something is likely wrong. Is your test turned the right way?")

    #y - y1 = m(x - x1)
    sampleconc = conclow + (saturations[2]-saturations[0]) * m
    
    return sampleconc

def main():
    lowpix = (111, 128, 90) #30 satur.
    highpix = (78, 128, 13) #90 satur.
    #samplepix = (86,128,38) #60 satur.
    samplepix = (120, 118, 60) #50 satur.
    highc = 100
    lowc = 0
    print("Low concentration:", lowc);
    print("High concentration:", highc);
    print("Test:",saturation_to_conc(lowpix, highpix, samplepix, lowc, highc))

if __name__ == '__main__':
    main()
