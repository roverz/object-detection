import cv2 as cv                                    #importing the package required for opencv
img = cv.imread("your image path.jpg")              #this will read the image who's path is given
img = cv.resize(img, (0,0), fx = 0.5, fy = 0.5)     #this will resize the image to an acceptable form and fx , fy values can be changed accordingly to meet the output image's criteria
imgGrey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)       #here the original colour of the image changes to grey
cv.imshow("grey image", imgGrey)                    #this will display the grey image
cv.waitKey(0)                                       #this will help the image wait on your screen for infinite amount of time
