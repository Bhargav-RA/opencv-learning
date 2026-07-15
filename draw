import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow('blank', blank)

# paint the image in certain colors
# blank[200:300, 300:400]= 0,0,255
# cv.imshow('green', blank)

#draw a rectangle
# cv.rectangle(blank,(0,0),(250,500),(0,255,0), thickness=cv.FILLED)
# cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//3),(0,255,0), thickness=cv.FILLED)
# cv.imshow('rectangle',blank)

#draw a Circle
# cv.circle(blank,(250,250),40,(0,0,255),thickness=-1)
# cv.imshow('circle',blank)

#Draw a line
# cv.line(blank,(20,20),(blank.shape[1]//2,blank.shape[0]//3),(255,255,255), thickness=3)
# cv.imshow('line',blank)

#Write text on image
cv.putText(blank,'heyy guyyzz',(225,225),cv.FONT_HERSHEY_TRIPLEX, 1.0,(0,255,0), 2 )
cv.imshow('message',blank)

cv.waitKey(0)