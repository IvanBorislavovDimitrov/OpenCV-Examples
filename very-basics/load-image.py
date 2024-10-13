import cv2

img = cv2.imread("/Users/ivandimitrov/projects/opencv/assets/img1.jpg", cv2.IMREAD_UNCHANGED)

#img = cv2.resize(img, (600, 900)) # by exact pixels
img = cv2.resize(img, (0, 0), fx=0.2, fy=0.2)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow('pic', img)

# cv2.imwrite('filename.jpg', img) # writes the file

k = cv2.waitKey(0)
cv2.destroyAllWindows()
 