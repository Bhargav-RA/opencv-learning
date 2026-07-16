import cv2 as cv
import numpy as np

img = cv.imread(r"C:\Users\Hai\OneDrive\Desktop\dog.webp")

cv.imshow('dog', img)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)

    dimension = (width, height)

    return cv.warpAffine(img, rotMat, dimension)

rotated = rotate(img, 270)

cv.imshow("rotated_dog", rotated)

cv.waitKey(0)
