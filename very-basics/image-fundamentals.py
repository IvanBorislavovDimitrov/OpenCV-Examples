import cv2
import random

img = cv2.imread("/Users/ivandimitrov/projects/opencv/assets/img1.jpg", cv2.IMREAD_UNCHANGED)

for i in range(600):
    for j in range(img.shape[1]):
       img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

cv2.imshow('picname', img)
cv2.waitKey(0)
cv2.destroyAllWindows()