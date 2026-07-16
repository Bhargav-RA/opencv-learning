import cv2 as cv
import numpy as np

img = cv.imread(r"C:\Users\Hai\OneDrive\Desktop\dog.webp")
cv.imshow("dog", img)

# average blur
Average =cv.blur(img, (15, 15))
cv.imshow("Average Blur", Average)

# gaussian blur
Gaussian = cv.GaussianBlur(img, (15, 15), 0)
cv.imshow("Gaussian Blur", Gaussian)

# median blur
Median = cv.medianBlur(img , 15)
cv.imshow("Median blur", Median)

#Bilateral blur
Bilateral = cv.bilateralFilter(img, 5,15,15)
cv.imshow("Bilateral Blur", Bilateral)

cv.waitKey(0)