import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread(r"C:\Users\Hai\OneDrive\Desktop\dog.webp")
cv.imshow("dog", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

LAB = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB", LAB)

plt.imshow(img)
plt.show()