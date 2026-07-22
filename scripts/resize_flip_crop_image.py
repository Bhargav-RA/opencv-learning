import cv2 as cv

img=cv.imread(r"C:\Users\Bhargav Ravinutala\Desktop\learn_cv\images\2.jpg")
cv.imshow('bear',img)

def resizedFrame(frame,scale=2.5):
    width = int(frame.shape[0] *scale)
    height = int(frame.shape[0] *scale)

    dimensions= (width,height)
    return cv.resize(frame,dimensions, interpolation=cv.INTER_CUBIC)

resized_image=resizedFrame(img)
cv.imshow('bear_resized',resized_image)

flip=cv.flip(img,0)
flip_1=cv.flip(img,1)
flip_2=cv.flip(img,-1)

cropped=img[100:250,100:190]

cv.imshow('bear',flip)
cv.imshow('bear_cropped',cropped)
cv.imshow('bear_1',flip_1)
cv.imshow('bear_2',flip_2)

cv.waitKey(0)

