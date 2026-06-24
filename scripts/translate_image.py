import cv2 as cv
import numpy as np

img = cv.imread(r"C:\Users\Bhargav Ravinutala\Desktop\learn_cv\images\2.jpg")

cv.imshow('bear',img)

def translation (img,x,y):
    translate_matrix = np.float32([[1,0,x],[0,1,y]])
    dimension= (img.shape[1],img.shape[0])
    return cv.warpAffine(img,translate_matrix,dimension)

translated = translation(img,50,50)

cv.imshow('traslated_bear',translated)
                
cv.waitKey(0)    
