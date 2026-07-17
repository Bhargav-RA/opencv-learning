# Template matching

import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Bhargav Ravinutala\Desktop\learn_cv\opencv-learning\bhargav\img.jpg",0)
template = cv2.imread(r"C:\Users\Bhargav Ravinutala\Desktop\learn_cv\opencv-learning\bhargav\football.jpg",0)

h,w = template.shape

methods = [cv2.TM_CCOEFF,cv2.TM_CCOEFF_NORMED,cv2.TM_CCORR,cv2.TM_CCORR,cv2.TM_CCORR_NORMED,cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]

for meathod in methods:
    img2=img.copy()
    result=cv2.matchTemplate(img2,template,meathod)

    min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(result)

    if meathod in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
        location=min_loc
    else:
        location= max_loc

    bottom_right=(location[0]+w,location[1]+h)
    cv2.rectangle(img2,location,bottom_right,255,5)

    cv2.imshow("result",img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

