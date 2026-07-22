# colour pallate tracebar

import cv2
import numpy as np

def empty_Function():
    pass


image = np.zeros((512,512,3),np.uint8)
WindowName="open cv colour pallate"

cv2.namedWindow(WindowName)

cv2.createTrackbar('Blue',WindowName,0,255,empty_Function)
cv2.createTrackbar('Green',WindowName,0,255,empty_Function)
cv2.createTrackbar('Red',WindowName,0,255,empty_Function)

while(True):
    cv2.imshow(WindowName,image)
    if cv2.waitKey(1) == 27:
        break

    blue = cv2.getTrackbarPos('Blue',WindowName)
    green = cv2.getTrackbarPos('Green',WindowName)
    red = cv2.getTrackbarPos('Red',WindowName)

    image[:] = [blue,green,red]
    print(blue,green,red)

