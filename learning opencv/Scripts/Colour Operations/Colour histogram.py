import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread(r"C:\Users\Hai\OneDrive\Desktop\dog.webp")
cv.imshow('dog', img)

plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
colors = ('b','g','r')

for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],None,[256],[0,255])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
    
plt.show()



cv.waitKey(0)