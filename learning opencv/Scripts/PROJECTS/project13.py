#pedestrain detection 

import cv2
import imutils

hog=cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cap = cv2.VideoCapture(r"C:\Users\Hai\OneDrive\Desktop\OPENCV\learning opencv\Video\video2.mp4")

while cap.isOpened():
    ret,img=cap.read()
    if ret:
        img=imutils.resize(img,width=min(400,img.shape[1]))
        (regions,_) = hog.detectMultiScale(img,winStride=(4,4),padding=(4,4),scale=1.05)
        for(x,y,w,h)in regions:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255,2))
        cv2.imshow('img',img)
        if cv2.waitKey(250) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
        