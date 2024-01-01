import cv2 as cv                                          #importing library to read the video
capture = cv.VideoCapture('VIDEO_PATH.mp4')               #enter the video path of the video that is to be read 
true = 1
while true:
    istrue, frame = capture.read()                        #caputure.read reads the video frame by frame and istrue is the boolean which says that the video wast successfully read or not
    cv.imshow('Video', frame)                             #display each frame
    frame = cv.resize(frame, (0,0), fx = 0.5, fy = 0.5)   #this resizes the image into an acceptable format
    if cv.waitKey(20) & 0xff ==ord('d'):                  #to stop the video bascially it says if the letter 'd' is pressed the just break out of the loop
        break
capture.release()                                         #optional command
cv.destroyAllWindows()                                    #optional command
