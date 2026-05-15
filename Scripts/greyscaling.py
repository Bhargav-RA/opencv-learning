import cv2 as cv
img = cv.imread(r"C:\Users\asus\OneDrive\Desktop\Learn_CV\DK.jpg")

cv.imshow('DK', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('DK gray', gray)

blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Dk blur', blur)

canny = cv.Canny(img, 125,175)
cv.imshow('DK canny', canny)

dilated = cv.dilate(img, (7,7),iterations=3)
cv.imshow('dilated', dilated)

resized = cv.resize(img, (500,500))
cv.imshow('DK resized', resized)

cropped = img[20:200, 20:200]
cv.imshow('DK cropped', cropped)
cv.waitKey(0)
