import cv2 as cv

import matplotlib.pyplot as plt

img = cv.imread(r"C:\Users\Bhargav Ravinutala\Desktop\learn_cv\images\1.jpg")

cv.imshow('bear',img)

##### conversions #######

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow('grey',gray)

hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

cv.imshow('hsv',hsv)

lab = cv.cvtColor(img,cv.COLOR_BGR2Lab)

cv.imshow('lab',lab)

plt.imshow(img)

plt.show()



