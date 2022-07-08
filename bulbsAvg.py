def colorAverage(color_list):
    leftAvg=[0,0,0]
    rightAvg=[0,0,0]
    for i in range(len(color_list)):
        if i%2==0:
            rightAvg[0]+=color_list[i][0]
            rightAvg[1]+=color_list[i][1]
            rightAvg[2]+=color_list[i][2]
        else:
            leftAvg[0]+=color_list[i][0]   
            leftAvg[1]+=color_list[i][1]
            leftAvg[2]+=color_list[i][2]
    for i in range(3):
        leftAvg[i]=leftAvg[i]/3
        rightAvg[i]=rightAvg[i]/3
    print("The average color for the bulbs were\nLeft: "+str(leftAvg)+"\nRight: "+str(rightAvg))

