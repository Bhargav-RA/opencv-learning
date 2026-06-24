import cv2 as cv

import numpy as np

# img=cv.imread(r"C:\Users\Bhargav Ravinutala\Desktop\learn_cv\images\7.jpg")
# img_2=cv.imread(r"C:\Users\Bhargav Ravinutala\Desktop\learn_cv\images\7.jpg")

blank = np.zeros((400,400),dtype='uint8')

img=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)

img_2=cv.circle(blank.copy(),(200,200),200,255,-1)

bitwise_and=cv.bitwise_and(img,img_2)

cv.imshow('and',bitwise_and)

## bitwise or

bitwise_or=cv.bitwise_or(img,img_2)
cv.imshow('or',bitwise_or)

## bitwise xor

bitwise_xor=cv.bitwise_xor(img,img_2)
cv.imshow('xor',bitwise_xor)

## bitwise not

bitwise_not=cv.bitwise_not(img,img_2)
cv.imshow('not',bitwise_not)

cv.waitKey(0)