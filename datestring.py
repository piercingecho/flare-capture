from datetime import datetime

def datestring():
    curr_date = datetime.now()
    
    datetime_string = curr_date.strftime("%Y%m%d_%H%M%S")
    photostring = "/home/pi/Research2022/Images/" + datetime_string + ".jpg"
    return photostring
