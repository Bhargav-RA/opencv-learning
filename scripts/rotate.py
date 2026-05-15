import cv2 as cv
import numpy as np

img= cv.imread(r"C:\Users\Bhargav Ravinutala\Desktop\learn_cv\images\3.jpg")

cv.imshow('bear',img)

def rotation(img,angle,rpoint=None):
    (height,width)=img.shape[:2]

    if rpoint is None:
        rpoint=(height//2,width//2)

    rot_matrix=cv.getRotationMatrix2D(rpoint,angle,0.5)
    dimension=(width,height)

    return cv.warpAffine(img,rot_matrix,dimension)

rotated_90=rotation(img,49)
rotated_180=rotation(img,99)
rotated_270=rotation(img,199)
rotated_360=rotation(img,299)

cv.imshow('bear_rotated_90',rotated_90)
cv.imshow('bear_rotated_180',rotated_180)
cv.imshow('bear_rotated_49',rotated_270)
cv.imshow('bear_rotated_299',rotated_360)

cv.waitKey(0)
    