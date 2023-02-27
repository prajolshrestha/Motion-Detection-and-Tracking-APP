import cv2, time, pandas
from datetime import datetime

video = cv2.VideoCapture(0)                               #creating object that can capture video using first(0) camera
first_frame = None                                        #create empty variable
motion_status_list = [None,None]                          #empty list to store status of object detection
motion_time = []                                          #empty list to store time of motion detection 
df = pandas.DataFrame(columns= ["Start","End"])           #creating pandas dataframe  

while True:
    #video input 
    check,frame = video.read()                             #capture a frame
    status = 0
    
    ##video processing
    #a)convert to gray image and blur it
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)          #convert frame to gray
    blured_gray = cv2.GaussianBlur(gray,(21,21),0)         #apply gussain blur
    #b)store first frame for later processing using it
    if first_frame is None:
        first_frame = blured_gray                          #storing first frame
        continue
    #c)calculate diffrence between first and current frames
    delta_frame = cv2.absdiff(first_frame,blured_gray)     #difference between first and current frame
    #d)if difference between 1st and current frame is less than 15, show white pixel
    threshold_frame = cv2.threshold(delta_frame,10,255,cv2.THRESH_BINARY)[1]   #apply threshold method to see object as white image
    improved_threshold_frame = cv2.dilate(threshold_frame,None,iterations=10)  #improve threshold frame
    #e)find coordinates of contours>1000 in improved threshold frames and make rectangle in unprocessed current frames 
    (cntrs,_) = cv2.findContours(improved_threshold_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for contour in cntrs:
        if cv2.contourArea(contour) < 1000:              #you can adjust a/c to what you want to capture
            continue                                      #1000 = 100 * 10 window pixel
        status = 1
        (x,y,w,h) = cv2.boundingRect(contour)             #gives coordinates of contours as rectiangle
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)  #make rectangle in unprocessed frame


    #display video
    cv2.imshow('First Frame', first_frame)
    cv2.imshow('Capturing', blured_gray)                          #prints each frame
    cv2.imshow('Delta Frame',delta_frame)
    cv2.imshow('Threshold frame',threshold_frame)
    cv2.imshow('Color Frame',frame)
    key = cv2.waitKey(1)                                   #waits for 1 miliseconds   
    

    #calculate and store object detection period
    motion_status_list.append(status)
    motion_status_list=motion_status_list[-2:]              #just store last two item(improvement for memory storage)
    if motion_status_list[-1]==1 and motion_status_list[-2]==0:
        motion_time.append(datetime.now())
    if motion_status_list[-1]==0 and motion_status_list[-2]==1:
        motion_time.append(datetime.now())

    
    #end video capturing
    #print(blured_gray)     
    #print(delta_frame)   #to calculate threhold value we see its value
    if key == ord('q'):
        if status == 1:
            motion_time.append(datetime.now())       #if there is object at end that is also counted
        break
    

    
#object motion data 
#print(status)                 #1 = object , 0 = no object
print(motion_status_list)
print(motion_time)
for i in range(0,len(motion_time),2):
    df=df.append({"Start":motion_time[i],"End":motion_time[i+1]},ignore_index=True)

df.to_csv("Moton Time Stamp.csv")
video.release()
cv2.destroyAllWindows()