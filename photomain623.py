




def main():
    if(len(sys.argv) == 2):
        photoname = sys.argv[1]
    elif(len(sys.argv) == 1):
        photoname = "testimage.jpg"
    else:
        print("Wrong number of arguments.")

    bwimage = edgeDetect(photoname)
    horiz_edges = []

    points = shapeFinder(bwimage, 30, horiz_edges)
    points = shapeFinder(bwimage, 30, horiz_edges, x_reverse = True)

    l_bulbs = findBulbSections(points)

    xrad = int((l_bulbs[1] - l_bulbs[0]) / 2)
    yrad = int(xrad * 8/7)

    leftColor = colorFilter(photoname, leftCenter, xrad, yrad, 200)
    rightColor = colorFilter(photoname, rightCenter, xrad, yrad, 200)

    print("Left bulb avg color:", leftColor)
    print("Right bulb avg color:", rightColor)

if __name__ == '__main__':
    main()
