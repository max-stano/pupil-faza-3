import numpy as np
import cv2 as cv
import cv2
#import matplotlib as plt

img = cv.imread('pupil.jpg', 0)
kernel = np.ones((5, 5), np.uint8)
img = cv.medianBlur(img, 5)
#img = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
            #cv.THRESH_BINARY,11,2)
img = cv.erode(img, kernel, iterations=1)
edges = cv.Canny(img,200,200)
cv.imwrite('pupil-canny.jpg', edges)

#cv.imshow('daco', edges)

img2 = cv.imread('pupil-canny.jpg')
circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    cv.circle(img2,(i[0],i[1]),i[2],(0,255,0),2)
    cv.circle(img2,(i[0],i[1]),2,(0,0,255),3)
cv.imshow('detected circles',img2)




cv.waitKey(0)
cv.destroyAllWindows()

