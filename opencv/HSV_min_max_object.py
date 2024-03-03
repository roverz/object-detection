import cv2 as cv
import numpy as np
capture = cv.VideoCapture(0)
capture.set(3,640)
capture.set(4,480)
capture.set(10,100)
def empty(e):
    pass
cv.namedWindow("HSV")
cv.resizeWindow("HSV", 640,240)
cv.createTrackbar("HUE Min", "HSV", 0,179,empty)
cv.createTrackbar("HUE Max", "HSV", 255,255,empty)
cv.createTrackbar("SAT Min","HSV", 0,255,empty)
cv.createTrackbar("SAT Max", "HSV", 255,255,empty)
cv.createTrackbar("VALUE Min","HSV", 0,255,empty)
cv.createTrackbar("VALUE Max", "HSV", 255,255,empty)


true = 1
while true:
    istrue, img = capture.read()
    imgHSV = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    h_min = cv.getTrackbarPos("HUE Min", "HSV")
    h_max = cv.getTrackbarPos("HUE Max", "HSV")
    s_min = cv.getTrackbarPos("SAT Min", "HSV")
    s_max = cv.getTrackbarPos("SAT Max", "HSV")
    v_min = cv.getTrackbarPos("VALUE Min", "HSV")
    v_max = cv.getTrackbarPos("VALUE Max", "HSV")
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_min])
    mask = cv.inRange(imgHSV, lower, upper)
    result = cv.bitwise_and(img,img, mask = mask)
   # hstack = np.hstack([img, mask, result])
    mask = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)
    cv.imshow("original", img)
    cv.imshow("HSV color space", imgHSV)
    cv.imshow("Mask", mask)
    cv.imshow("Result", result)

    #cv.imshow("Horizontal Stack", hstack)

    if cv.waitKey(1) & 0xff == ord('d'):
        break
#capture.release()
#cv.waitKey(0)
#cv.destroyAllWindows()
