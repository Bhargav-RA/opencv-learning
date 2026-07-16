import cv2 as cv

img = cv.imread(r"C:\Users\asus\OneDrive\Desktop\Learn_CV\DK.jpg")

cv.imshow('DK', img)

cv.waitKey(0)