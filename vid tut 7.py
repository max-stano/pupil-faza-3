import cv2
import numpy as np
img = cv2.imread('pupil2.jpg', 0)
template = cv2.imread('pupil2-5.jpg', 0)
height, width = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
           cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()
    #kopirujeme lebo kreslime kým hladame
    result = cv2.matchTemplate(img2, template, method)
    #(W - w + 1, H - h +1)
    #width of base img, - width of template
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + width, location[1] + height)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()