import cv2 as cv                                             #importing library to read the image
img = cv.imread('IMAGE_PATH.jpg')                            #reads the image whose path is given
img = cv.resize(img, (0,0), fx= 0.5, fy= 0.5)                #resizes the image into an acceptable format
cv.imshow('IMAGE_NAME', img)                                 #displays the image
cv.waitKey(0)                                                #displays the output for infinite number of seconds
