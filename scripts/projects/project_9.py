# converting image into cartoon image
import cv2

img = cv2.imread(r"C:\Users\Bhargav Ravinutala\Desktop\learn_cv\images\2.jpg")
# img = cv2.imread(r"C:\Users\Bhargav Ravinutala\Desktop\learn_cv\frame50.jpg")


color = cv2.bilateralFilter(img,d=9,sigmaColor=90,sigmaSpace=60)

grey =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

grey_blur = cv2.medianBlur(grey,5)

edges = cv2.adaptiveThreshold(grey_blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)

cartoon = cv2.bitwise_and(color,color,mask=edges)

cv2.imshow("image",cartoon)

cv2.waitKey(0)
cv2.destroyAllWindows