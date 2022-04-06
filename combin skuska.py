

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

fig = plt.figure()


x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)


line1, = plt.plot(x1, y1, 'ko-')        # so that we can update data later

for i in range(1000):
    # update data
    line1.set_ydata(np.cos(2 * np.pi * (x1+i*3.14/2) ) * np.exp(-x1) )

    # redraw the canvas
    fig.canvas.draw()

    # convert canvas to image
    img = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8,
            sep='')
    img  = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))

    # img is rgb, convert to opencv's default bgr
    img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)


    # display image with opencv or any operation you like
    cv2.imshow("plot",img)

    # display camera feed
    #ret,frame = img.read()
    #cv2.imshow("cam",frame)

    k = cv2.waitKey(33) & 0xFF
    if k == 27:
        break