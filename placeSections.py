from  matplotlib import pyplot as plt
from matplotlib import image
from matplotlib import patches as patches

def placeSects(imgstring, center, xrad, yrad):
    
    if(type(imgstring) == str):
        img_sect = image.imread(imgstring)
    else:
        img_sect = imgstring

    fig, ax = plt.subplots()

    ax.imshow(img_sect)
    if(type(center) == list):
        for bulb in center: #loop over, if "center" is a list of centers.
            print("Bulb x, y:", bulb[0], bulb[1])
            topLeft = (bulb[0] - xrad, bulb[1] - yrad)
            rect = patches.Rectangle(topLeft, xrad * 2, yrad * 2, linewidth=1, edgecolor = 'r', facecolor = 'none')
            ax.add_patch(rect)
    else:
            topLeft = (center[0] - xrad, center[1] - yrad)
            rect = patches.Rectangle(topLeft, xrad * 2, yrad * 2, linewidth=1, edgecolor = 'r', facecolor = 'none')
            topLeft = (center[0] - xrad, center[1] - yrad)
            rect = patches.Rectangle(topLeft, xrad * 2, yrad * 2, linewidth=1, edgecolor = 'r', facecolor = 'none')
            ax.add_patch(rect)


    plt.show()

'''
    image = cv2.imread(imgstring)
    print(type(image))
    plt.rcParams["figure.figsize"] = [1000, 1000]
    plt.rcParams["figure.autolayout"] = True
    x = point[0]
    y = point[1]
#    plt.xlim(0, image.size[0])
#    plt.ylim(0, image.size[1])
    plt.grid()
    plt.plot(x, y, marker = "o", markersize = 20, markeredgecolor = "red", markerfacecolor = "green")
    plt.show()
'''
def main():
    placePoint("shapes.png", [5, 10])

if __name__ == '__main__':
    main()
