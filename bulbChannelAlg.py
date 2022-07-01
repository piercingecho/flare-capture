from edgeDetect import edgeDetect
from shapeFinder import *
from placePoint import *
from findBulbChannel import *
from placeSections import *
from avgColorFilter import *

def bulbChannelAlg(photoname):
    bwimage = edgeDetect(photoname)
    horiz_edges = []

    #points has 2 values: leftmost and rightmost. Both are tuples
    points = shapeFinder(bwimage, 30, horiz_edges)
    points = shapeFinder(bwimage, 30, horiz_edges, x_reverse = True)

    l_sections = findBulbChannel(horiz_edges)

    #can now find center and radii of two sections

    bulbXlen = l_sections[1] - l_sections[0]
    bulbYlen = int(bulbXlen * 8/7)
    bulbCenter = (int(l_sections[0] + bulbXlen / 2), horiz_edges[0][1])
    bulbTopLeft = (l_sections[0], horiz_edges[0][1] - int(bulbYlen / 2))

    rectXlen = l_sections[2] - l_sections[1]
    rectYlen = int(rectXlen / 2)
    rectCenter = (l_sections[1] + int(rectXlen / 2), horiz_edges[0][1])
    rectTopLeft = (l_sections[1], horiz_edges[0][1] - int(rectYlen / 2))

    placeSects(photoname, bulbCenter, bulbXlen / 2, bulbYlen / 2)
    placeSects(photoname, rectCenter, rectXlen / 2, rectYlen / 2)

    leftColor = avgColorFilter(photoname, bulbTopLeft, bulbXlen, bulbYlen)
    rightColor = avgColorFilter(photoname, rectTopLeft, rectXlen, rectYlen)

    print("Bulb avg color:", leftColor)
    print("Rect avg color:", rightColor)
