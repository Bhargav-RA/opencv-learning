# White and black dot detection using OpenCV | Python

import cv2

path = r"C:\Users\Hai\Downloads\black-dot1.jpg"
#path = r"C:\Users\Hai\Downloads\white-dot.png"

gray= cv2.imread(path,0)


# threshold 

# th,threshed = cv2.threshold(gray,100,255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
th,threshed = cv2.threshold(gray,100,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)

# findcontours 
cnts = cv2.findContours(threshed, cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[-2]

# filter by area

s1 = 3
s2 = 20
xcnts = []

for cnt in cnts:
    if s1<cv2.contourArea(cnt) <s2:
        xcnts.append(cnt)


print(f"Total Number of white dot is {len(xcnts)}")