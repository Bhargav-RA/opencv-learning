"""
bitwise_and: Applies a logical AND operation to each pixel of two images or an image and a mask.
bitwise_or: Applies a logical OR operation.
bitwise_xor: Applies a logical XOR operation.
bitwise_not: Inverts the pixels (logical NOT).
"""

import cv2 as cv
import numpy as np
blank = np.zeros((400,400),dtype='uint8')

rect =cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle =cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('Rectangle',rect)
cv.imshow('circle',circle)
# Bitwise And
bitwise_and =cv.bitwise_and(rect,circle)
# cv.imshow("bitwise_and",bitwise_and)

#Bitwise Or
bitwise_or = cv.bitwise_or(rect,circle)
# cv.imshow("bitwise_or",bitwise_or)

#bitwise Xor
bitwise_Xor = cv.bitwise_xor(rect,circle)
# cv.imshow('bitwise_Xor',bitwise_Xor)

#bitwise Not
bitwise_not = cv.bitwise_not(circle)
cv.imshow('bitwise_not',bitwise_not)



cv.waitKey(0)