import cv2 as cv
import numpy as np

img=cv.imread(r"C:\Users\Bhargav Ravinutala\Desktop\learn_cv\images\2.jpg")

# cv.line(img,(0,0),(256,192),(255,255,255),thickness=5)

cv.putText(img,'nenu pandi',(0,25),cv.FONT_HERSHEY_TRIPLEX, 1.0,(0,255,0),2)

blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)

grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

canny= cv.Canny(img,125,175)

dialted= cv.dilate(canny,(3,3),iterations=5)

resize = cv.resize(img,(250,450))

cropped = resize[20:200,25:250]

# cv.circle(img,(125,75),40,(203,192,255),thickness=15)



cv.imshow('bear',img)
cv.imshow('bear_black_and_white',grey)
cv.imshow('bear_with_his_vision',blur)
cv.imshow('bear_with_his_borders',canny)
cv.imshow('bear_with_dialted',dialted)
cv.imshow('bear_resize',resize)
cv.imshow('bear_cropped',cropped)





cv.waitKey(0)