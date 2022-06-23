def findBulbSections(points):
    #first, take out the 
    leftX = points[0][0]
    rightX = points[1][0]
    fulldistance = rightX - leftX

    #left bulb is 6. middle is 7. right bulb is 6.
    #sum is 19

    ratio = 19

    unit_distance = int(fulldistance / ratio)
    
    fourXpoints = []
    
    #left bulb
    fourXpoints.append(leftX)
    fourXpoints.append(leftX + unit_distance * 6)

    #right bulb
    fourXpoints.append(rightX - unit_distance * 6)
    fourXpoints.append(rightX)
    
    return fourXpoints
