from  matplotlib import pyplot as plt
from matplotlib import image

def placeSect(imgstring, points):
    data = image.imread(imgstring)
    for point in points:
        plt.plot(point[0], point[1], marker='v', color="red")
    plt.imshow(data)
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
