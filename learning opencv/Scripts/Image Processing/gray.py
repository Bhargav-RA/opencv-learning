import cv2 as cv
import numpy as np

img = cv.imread(r"C:\Users\Hai\OneDrive\Desktop\dog.webp")

#cv.imshow('dog', img)

blank = np.zeros(img.shape,dtype='uint8')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

ret,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)

cv.imshow('dog_thresh',thresh)


contours,hierarchise = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)

cv.drawContours(blank,contours,-1,(0,0,255),2)
cv.imshow('dog_contour',blank)
cv.waitKey(0)