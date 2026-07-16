import cv2 as cv

img = cv.imread(r"C:\Users\Hai\OneDrive\Desktop\dog.webp")
cv.imshow('Dog', img)

def rescaleFrame(frame, scale=2.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)
    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Dog resized', resized_image)
cv.waitKey(0)