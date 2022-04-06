import cv2
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('pupil.jpg', 0)
kernel = np.ones((5, 5), np.uint8)
img = cv.medianBlur(img, 5)
img = cv2.erode(img, kernel, iterations=1)
edges = cv.Canny(img,100,200)
img = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv.THRESH_BINARY,11,2)


plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.show()
cv2.imwrite('new_img.jpg', img)

cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
cv.imshow('detected circles',cimg)