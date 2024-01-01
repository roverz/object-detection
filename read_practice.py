import cv2 as cv
img = cv.imread("C:/Users/User/OneDrive/Desktop/OPEN_CV/solo_pic.jpg")
img = cv.resize(img, (0,0), fx = 0.5, fy = 0.5)
cv.imshow('solo_pic', img)
cv.waitKey(0)