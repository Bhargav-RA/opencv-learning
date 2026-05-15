import cv2 as cv
import numpy as np

img = cv.imread(r"C:\Users\asus\OneDrive\Desktop\Learn_CV\DK.jpg")

blank = np.zeros(img.shape, dtype='uint8')

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grey', grey)

ret , thresh = cv.threshold(grey, 125, 255, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)

countours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

cv.drawContours(blank, countours, -1, (0,0,255), 1)
cv.imshow('countours', blank)
cv.waitKey(1)


