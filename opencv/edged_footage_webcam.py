import cv2 as cv                                        #importing opencv package
import numpy as np                                      #importing numpy for matrix calculation of the video footage
cap = cv.VideoCapture(0)                                #displays the footage recorded by your PC's webcam
cap.set(3,640)                                          #adjusts the height of the footage
cap.set(4,480)                                          #adjusts the width of the footage
cap.set(10,100)                                         #setting for proper brightness in the footage 
true = 1
while true:
    istrue, frame = cap.read()                          #reads the footage frame by frame
    cv.imshow("video", frame)                           #displays the original footage as output
    frame_edge = cv.Canny(frame,80,80)                  #converts the original footage into an edged or canny footage  
    lap_edge = cv.Laplacian(frame, cv.CV_64F)           #converts the original footage into a laplacian footage
    lap_edge = np.uint8(lap_edge)                       #converting the float value to integer for matrix calculation
    cv.imshow("Laplacian video", lap_edge)              #displays laplacian footage
    cv.imshow("edged video", frame_edge)                #displays canny footage
    if cv.waitKey(20) & 0xff == ord("d"):               #if the letter "d" is pressed, the footage displaying will stop
        break
