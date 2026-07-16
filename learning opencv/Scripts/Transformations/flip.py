import cv2 as cv
import numpy as np

img = cv.imread(r"C:\Users\Hai\OneDrive\Desktop\dog.webp")

cv.imshow('dog', img)

resized =cv.resize(img,(300,300),interpolation=cv.INTER_CUBIC)

flip =cv.flip(img,-1)

cv.imshow('dog',flip)

cropped=img[190:200,190:260]

cv.waitKey(0)

                   