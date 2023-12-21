import cv2 as cv
capture = cv.VideoCapture(0)               #captures your PC's webcam
capture.set(3,640)
capture.set(4,480)
capture.set(10,100)
true = 1
while true:
    istrue, frame = capture.read()         #this reads the captured video frame by frame
    cv.imshow('Video', frame)              #displays each frame of the video
    if cv.waitKey(0) & 0xff('d'):           #on pressing the letter "d" the webcam recording would stop immediately
        break
capture.release()                            #optional
