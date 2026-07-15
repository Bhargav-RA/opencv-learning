import cv2 as cv

img = cv.imread(r"C:\Users\Hai\OneDrive\Desktop\dog.webp")
cv.imshow('Dog', img)

def rescaleFrame(frame, scale=2.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)
    return cv.resize(frame,dimensions, interpolation=cv.INTER_CUBIC)

resized_image = rescaleFrame(img)

flip = cv.flip(resized_image, 1)
cv.imshow('Dog flip', flip)

cropped = resized_image[100:200, 100:200]
cv.imshow('Dog cropped', cropped)

cv.imshow('Dog resized', resized_image)
cv.waitKey(0)