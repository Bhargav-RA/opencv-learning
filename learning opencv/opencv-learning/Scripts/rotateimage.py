import cv2 as cv
import numpy as np

img = cv.imread(r"C:\Users\asus\OneDrive\Desktop\Learn_CV\DK.jpg")

cv.imshow('DK', img)

def rotation(img, angle, rotPoint=None):
    height, width = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    rotation_matrix = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotation_matrix, dimensions)

rotated = rotation(img, 49)
cv.imshow('DK rotation', rotated)

cv.waitKey(0)

