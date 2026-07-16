import cv2 as cv

img = cv.imread(r"C:\Users\Hai\OneDrive\Desktop\dog.webp")
# cv.imshow("dog",img)

gary = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gary)

#Simple Thresholding
threshold, thresh = cv.threshold(gary,120,255,cv.THRESH_BINARY)
# cv.imshow('Simple Threshold',thresh)

threshold, thresh_inv = cv.threshold(gary,120,255,cv.THRESH_BINARY_INV)
# cv.imshow('Simple Threshold inv',thresh_inv)

#Adaptive Thresholding
a_thresh = cv.adaptiveThreshold(gary,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('a_thresh',a_thresh)


cv.waitKey(0)