import cv2 as cv
import numpy as np

img = cv.imread(r"C:\Users\Hai\OneDrive\Desktop\dog.webp")

cv.imshow('dog',img)

def translation(img,x,y):
    translate_matrix = np.float32([[1,0,x],[0,1,y]])
    dimension = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,translate_matrix,dimension)

translated = translation(img,-100,-100)

cv.imshow('translated_puppy',translated)

cv.waitKey(0)