import cv2 as cv
import numpy as np

img=cv.imread(r"C:\Users\Bhargav Ravinutala\Desktop\learn_cv\images\2.jpg")

## average blurr

averge=cv.blur(img,(7,7))
cv.imshow('average',averge)

## gaussian
gauss=cv.GaussianBlur(img,(7,7),0)

cv.imshow('gauss',gauss)

## median blurr

median=cv.medianBlur(img,9)

cv.imshow('median',median)

## bilateral blurr

bilateral=cv.bilateralFilter(img,5,15,15)

cv.imshow('bilateral',bilateral)

cv.waitKey(0)
