import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    image = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    crossed_out_image = cv2.line(image, (0, 0), (width, height), (255, 0, 0), 10)
    crossed_out_image = cv2.line(crossed_out_image, (0,  ), (width, 0), (0, 255, 0), 1000)
    crossed_out_image = cv2.rectangle(crossed_out_image, (0, 0), (200, 200), (255, 255, 0), 20)
    cv2.imshow('frame', crossed_out_image)
    if cv2.waitKey(1) == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()