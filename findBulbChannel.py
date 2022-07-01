def findBulbChannel(points):
    leftX = points[0][0]
    rightX = points[1][0]
    fulldistance = rightX - leftX

    ratio = 13

    #bulb should always be on left, if it's on right then that's the user's problem
    unit_distance = int(fulldistance / ratio)

    threeXpoints = []

    threeXpoints.append(leftX);

    #place between bulb and channel
    threeXpoints.append(int(leftX + unit_distance * 6))

    threeXpoints.append(rightX)

    return threeXpoints
