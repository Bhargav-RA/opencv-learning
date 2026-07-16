import cv2 as cv

img = cv.imread(r"C:\Users\asus\OneDrive\Desktop\Learn_CV\DK.jpg")
cv.imshow('DK', img)

def rescaleFrame(frame, scale=2.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)
    return cv.resize(frame,dimensions, interpolation=cv.INTER_CUBIC)

resized_image = rescaleFrame(img)

flip = cv.flip(resized_image, 1)
cv.imshow('DK flip', flip)

cropped = resized_image[100:200, 100:200]
cv.imshow('DK cropped', cropped)

cv.imshow('DK resized', resized_image)
cv.waitKey(0)

