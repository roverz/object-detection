import cv2 as cv                                                              #import opencv package
img = cv.imread("IMAGE PATH.filetype")                                        #location of the image has to be read
img = cv.resize(img,(0,0), fx = 0.5, fy = 0.5)                                #resizing the image as per your requirement
blur_image = cv.GaussianBlur(img,(7,7),sigmaX = 5, sigmaY = 7)                #funtion used to blur the image and and remember to given odd numbers in the required places
cv.imshow("original image", img)                                              #displays the original image
cv.imshow("Blur image", blur_image)                                           #displays the blurred image along with original image
cv.waitKey(0)                                                                 #this will display the output for infinite milliseconds
