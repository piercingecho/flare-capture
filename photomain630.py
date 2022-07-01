import sys
from inputLoop import inputLoop
from bulbBulbAlg import bulbBulbAlg
from bulbChannelAlg import bulbChannelAlg
from threeBulbsAlg import threeBulbsAlg

def main():
    if(len(sys.argv) == 1):
        photoname = "bulbbulkimages1.jpg"
    else:
        photoname = sys.argv[1]

    choice = inputLoop()
    #try:
    if(choice == 1):
        bulbBulbAlg(photoname)
    elif(choice == 2):
        bulbChannelAlg(photoname)
    elif(choice == 3):
        threeBulbsAlg(photoname)
    #except Exception as e:
    #    print("Invalid filename.")
    #    print(e)
    sys.exit()

if __name__ == '__main__':
    main()
