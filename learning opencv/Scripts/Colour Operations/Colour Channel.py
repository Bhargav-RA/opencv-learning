import cv2 as cv
import numpy as np

img = cv.imread(r"C:\Users\Hai\OneDrive\Desktop\dog.webp")

b, g, r = cv.split(img)

cv.imshow("Blue", b)
cv.imshow("Green", g)
cv.imshow("Red", r)

merged = cv.merge([b, g, r])
cv.imshow("Merged", merged)

cv.waitKey(0)    
    