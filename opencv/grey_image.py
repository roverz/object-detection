import cv2 as cv                                    #importing the package required for opencv
res = float(input("Resize Image (0.1 to 1.0): "))   #storing user input into a variable for later use
img = cv.imread("your image path.jpg")              #this will read the image who's path is given
imgGrey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)       #here the original colour of the image changes to grey
imgGrey = cv.resize(imgGrey, (0,0), fx = res, fy = res) #this will resize the image to the user's given input
cv.imshow("grey image", imgGrey)                    #this will display the grey image
cv.waitKey(0)                                       #this will help the image wait on your screen for infinite amount of time
