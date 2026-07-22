import cv2 as cv
import numpy as np

img = cv.imread(r"C:\Users\Bhargav Ravinutala\Desktop\learn_cv\images\5.jpg")

b,g,r=cv.split(img)

cv.imshow('blue',b)
cv.imshow('green',g)
cv.imshow('red',r)

merged =cv.merge([b,g,r])

cv.imshow('merged',merged)

cv.waitKey(0)
