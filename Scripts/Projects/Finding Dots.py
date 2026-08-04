import cv2
#path = r"C:\Users\asus\OneDrive\Desktop\Learn_CV\images\Blackdot.jpeg"
path = r"C:\Users\asus\OneDrive\Desktop\Learn_CV\images\Whitedot.jpeg"

gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

#th,threshed = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
th,threshed = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU) 

#Counters

cnts = cv2.findContours(threshed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]

#Filter contours based on area

s1 = 3
s2 = 20
xcnts = []

for cnt in cnts:
    if s1<cv2.contourArea(cnt) < s2:
        xcnts.append(cnt)

print(f"total no of White dot is {len(xcnts)}")