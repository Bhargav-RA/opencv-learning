import cv2 as cv
import numpy as np

img=cv.imread(r"C:\Users\Bhargav Ravinutala\Desktop\learn_cv\images\2.jpg")

blank = np.zeros(img.shape,dtype='uint8')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

ret,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)

cv.imshow('bear_thresh',thresh)

contours, hirearchy = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)

cv.drawContours(blank,contours,-1,(0,0,255),2)

cv.imshow('bear_contour',blank)

cv.waitKey(0)
