# counting black and white dots

import cv2
path = r"C:\Users\Bhargav Ravinutala\Downloads\white-dot.png"

gray = cv2.imread(path,0)

# th,threshed = cv2.threshold(gray,100,255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
th,threshed = cv2.threshold(gray,100,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)


# countors

cnts=cv2.findContours(threshed,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[-2]

# filter contour by area

s1=3
s2=20
xcnts=[]

for cnt in cnts:
    if s1<cv2.contourArea(cnt) <s2:
        xcnts.append(cnt)

print(f"total no of black dots is {len(xcnts)}")