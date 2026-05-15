import cv2 as cv
import numpy as np

img = cv.imread(r"C:\Users\asus\OneDrive\Desktop\Learn_CV\DK.jpg")
#
cv.putText(img, 'Snake kinguu', (50, 50), cv.FONT_HERSHEY_TRIPLEX, 0.6, (0, 0, 0), 1)
cv.imshow('DK', img)

cv.waitKey(0)