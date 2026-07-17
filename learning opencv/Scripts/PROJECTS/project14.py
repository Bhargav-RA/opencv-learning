#background subtraction using opencv

import cv2
fgbg1 = cv2.createBackgroundSubtractorMOG2()
fgbg2 = cv2.createBackgroundSubtractorKNN()

cap = cv2.VideoCapture(0)

while True:
    ret,img = cap.read()
    
    if not ret:
        break
    
    fgmask1 = fgbg1.apply(img)
    fgmask2 = fgbg2.apply(img)
    
    cv2.imshow('Original',img)
    cv2.imshow('MOG2',fgmask1)
    cv2.imshow('KNN',fgmask2)
    
    k = cv2.waitKey(30)& 0XFF
    
    if k==27:
        break

cap.release()
cv2.destroyAllWindows