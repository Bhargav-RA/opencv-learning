import cv2 as cv
import numpy as np

img = cv.imread(r"C:\Users\asus\OneDrive\Desktop\Learn_CV\DK.jpg")


cv.imshow('DK', img)

# translation
def translation(img, x, y):
    translation_matrix = np.float32([[1, 0, x],[0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, translation_matrix, dimensions)

translate = translation(img, 100, 100)
cv.imshow('DK translation', translate)

cv.waitKey(0)
cv.destroyAllWindows()

