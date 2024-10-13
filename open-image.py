import cv2 as cv

img = cv.imread("/Users/ivandimitrov/Downloads/IMG_20240914_151624.jpg")

cv.imshow("Display window", img)
k = cv.waitKey(0) # Wait for a keystroke in the window
