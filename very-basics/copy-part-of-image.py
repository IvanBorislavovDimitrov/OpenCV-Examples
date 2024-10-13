import cv2
import random

img = cv2.imread("/Users/ivandimitrov/projects/opencv/assets/img1.jpg", cv2.IMREAD_UNCHANGED)

tag = img[1500:1700, 1600:1900]
img[1100:1300, 1650:1950] = tag

cv2.imshow('picname', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('tag', tag)
cv2.waitKey(0)
cv2.destroyAllWindows()