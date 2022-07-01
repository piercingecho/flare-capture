from edgeDetect import edgeDetect
from shapeFinder import *
from placePoint import *
from findBulbs import *
from placeSections import *
from avgColorFilter import avgColorFilter

def bulbBulbAlg(photoname):
    bwimage = edgeDetect(photoname)
    horiz_edges = []
    
    #points has 2 values: leftmost and rightmost. Both are tuples
    leftPoint = shapeFinder(bwimage, 30, horiz_edges)  #"bwimage.jpg"
    rightPoin = shapeFinder(bwimage, 30, horiz_edges, x_reverse = True)
    
    #placePoint("bwimage.jpg", horiz_edges)
    #placePoint(photoname, horiz_edges)
    
    #THIS FINDS THE SECTIONS
    #four X values: first 2 are the left bulb, second 2 are the right bulb
    l_bulbs = findBulbSections(horiz_edges)
   


    #now that we have our four x coordinates, we can find the centers & radii
    #of the two bulbs
    


    xrad = int((l_bulbs[1] - l_bulbs[0]) / 2) #half of the distance between these 2
    yrad = int(xrad * 8/7)  #take into account the likely error with vertical positioning

    leftCenter = (l_bulbs[0] + (xrad), horiz_edges[0][1]) 
    rightCenter = (l_bulbs[2] + (xrad), horiz_edges[1][1])


    leftTopLeft = (leftCenter[0] - xrad, leftCenter[1] - yrad)
    rightTopLeft = (rightCenter[0] - xrad, rightCenter[1] - yrad)

    placeSects(photoname, [leftCenter, rightCenter], xrad, yrad);
    

    #change the values here
    leftColor = avgColorFilter(photoname, leftTopLeft, xrad * 2, yrad * 2) 
    rightColor = avgColorFilter(photoname, rightTopLeft, xrad * 2, yrad * 2)

    print("Left bulb average color:", leftColor)
    print("Right bulb average color:`", rightColor)
