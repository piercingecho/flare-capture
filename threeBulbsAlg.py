from edgeDetect import edgeDetect
from shapeFinder import *
from placePoint import *
from findBulbs import *
from placeSections import *
from avgColorFilter import avgColorFilter

import math


def threeBulbsAlg(photoname):
    bwimage = edgeDetect(photoname)
    print(bwimage.shape);
    top_edges = [];
    
    topLeftEdge = shapeFinder(bwimage, 30, top_edges, ymin = 10);
    
    #some conditional to find whether it's top left or top right

    topRightEdge = shapeFinder(bwimage, 30, top_edges, ymin = 10, x_reverse = True);
    
    #it found either top left and bottom right, or top right and bottom left. This makes it redo the wrok for the bottom
    #part, with bounds so it recognizes only the top bulb.
    

    halfofrange = int(bwimage.shape[1] / 10)
    #this was 125 when workign with gigantic images, it's crashing the program when it's tiny. So we're reducing its size proportionally based on the image size as a whole lol    

    if(abs(topLeftEdge[1] - topRightEdge[1]) > bwimage.shape[1] / 5):
        top_edges = [];
        if(topLeftEdge[1] > topRightEdge[1]): #right is top
            topLeftEdge = shapeFinder(bwimage, 30, top_edges, ymin = topRightEdge[1] - halfofrange, ymax = topRightEdge[1] + halfofrange)
            top_edges.append(topLeftEdge);
            top_edges.append(topRightEdge);
        else: #left was top
            top_edges = []
            top_edges.append(topLeftEdge);
            topRightEdge = shapeFinder(bwimage, 30, top_edges, x_reverse = True, ymin = topLeftEdge[1] - halfofrange, ymax = topLeftEdge[1] + halfofrange);
            top_edges.append(topRightEdge);
    
    l_topbulbs = findBulbSections(top_edges)

    xrad = int((l_topbulbs[1] - l_topbulbs[0]) / 2)
    yrad = int(xrad * 8/7)

    #top left center, top rigth center.
    tlCenter = (l_topbulbs[0] + xrad, top_edges[0][1])
    trCenter = (l_topbulbs[2] + xrad, top_edges[1][1])
    
    placeSects(photoname, [tlCenter, trCenter], xrad, yrad);


    #We have the top two bulb locations at this point
   
    fullXDist = l_topbulbs[3] - l_topbulbs[0]

    

    #1.25 is the real distance (in cm) between bulb sectors, and 2.75 is the real distance from left bulb to rigth bulb.
    #Using that and the pixel values, we find the number of pixels to go down to repeat the process.


    effectiveDist = int(fullXDist * 2 / 7)


    middleLeftEdge = shapeFinder(bwimage, 30, top_edges, ymin = tlCenter[1] + effectiveDist - halfofrange, ymax = tlCenter[1] + effectiveDist + 150)
    middleRightEdge = shapeFinder(bwimage, 30, top_edges, ymin = trCenter[1] + effectiveDist - halfofrange, ymax = trCenter[1]  + effectiveDist + halfofrange, x_reverse = True)
    
    mid_edges = [middleLeftEdge, middleRightEdge]
    l_midbulbs = findBulbSections(mid_edges)

    mlCenter = (l_midbulbs[0] + xrad, mid_edges[0][1])
    mrCenter = (l_midbulbs[2] + xrad, mid_edges[1][1])

    #debug line
    placeSects(photoname, [tlCenter, trCenter, mlCenter, mrCenter], xrad, yrad);

    bottomLeftEdge = shapeFinder(bwimage, 30, top_edges, ymin = mlCenter[1] + effectiveDist - halfofrange, ymax = mlCenter[1] + effectiveDist + halfofrange)
    bottomRightEdge = shapeFinder(bwimage, 30, top_edges, ymin = mrCenter[1] + effectiveDist - halfofrange, ymax = mrCenter[1]  + effectiveDist + halfofrange, x_reverse = True)
    print("Types:", type(bottomLeftEdge), type(bottomLeftEdge[1])) 
    bot_edges = [bottomLeftEdge, bottomRightEdge]
    l_botbulbs = findBulbSections(bot_edges)


    blCenter = (l_botbulbs[0] + xrad, bot_edges[0][1])
    brCenter = (l_botbulbs[2] + xrad, bot_edges[1][1])
    
    l_centers = [tlCenter, trCenter, mlCenter, mrCenter, blCenter, brCenter]
    
    placeSects(photoname, l_centers, xrad, yrad);
    
    l_avgcolor = []

    for center in l_centers:
        corner = (center[0] - xrad, center[1] - yrad) #top left corner
        l_avgcolor.append(avgColorFilter(photoname, corner, xrad * 2, yrad * 2))

    for color in l_avgcolor:
        print(color)





    #failed attempt at finding the other four by using trig lol
    '''
    yDiff = trCenter[1] - tlCenter[1]
    xDiff = trCenter[0] - tlCenter[0]

    pixDist =((yDiff)**2 + xDiff**2)**1/2 #this is dist from left to right, but also from top to bottom since we lucked out
    
    blYval = tlCenter[1] + math.tan(yDiff / xDiff) * yDiff

    #mlYval = tlCenter[0] + math.tan(yDiff / xDiff) * xDiff

    mlCenter = (tlCenter[0], tlCenter[1])
    mrCenter = (trCenter[0], trCenter[1])

    blCenter = (tlCenter[0] + 300, blYval)
    brCenter = (trCenter[0], trCenter[1])
    '''
