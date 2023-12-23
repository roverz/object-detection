import cv2 as cv                                       #importing opencv package
import numpy as np                                     #importing numpy for matrix calculation
img = cv.imread("IMAGE PATH.filetype")                 #image location
img = cv.resize(img, (0,0), fx = 0.5, fy = 0.5)        #resizing the image as per the demanding criteria
img_canny = cv.Canny(img,150,200)                      #this will show canny or sharped edges in the given image and the given values can be altered as per requirement
img_lap = cv.Laplacian(img, cv.CV_64F)                 #this will show a little less sharped image
img_lap = np.uint8(img_lap)                            #converting the previous float value into integer so as to be considered while matrix calculation
cv.imshow("edged pic", img_canny)                      #displays canny image 
cv.imshow("laplacian pic", img_lap)                    #displays laplacian image
cv.imshow("original image", img)                       #displays original image along with them
cv.waitKey(0)                                          #displays the output for infinite milliseconds of time
