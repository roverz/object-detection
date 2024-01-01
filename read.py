import cv2 as cv
img = cv.imread('C:/Users/User/OneDrive/Desktop/OPEN_CV/south_city.jpg')
img = cv.resize(img, (0,0), fx= 0.5, fy= 0.5)
cv.imshow('south_city', img)
cv.waitKey(0)