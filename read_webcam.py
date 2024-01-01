import cv2 as cv
capture = cv.VideoCapture(0)
capture.set(3,640)
capture.set(4,480)
capture.set(10,100)
true = 1
while true:
    istrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(0) & 0xff('d'):
        break
#capture.release()    