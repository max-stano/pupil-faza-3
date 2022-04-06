import cv2
import numpy as np
img = cv2.imread('face.jpg', 0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_deafult.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_deafult.xml')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x + w, y+ h), (255, 0, 0), 5)
    roi_gray = gray[y:y+w, x:x+w]
    roi_color = img[y:y+w, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)
cv2.imshow('tvar', img)


cv2.waitKey(0)
cv2.destroyAllWindows()