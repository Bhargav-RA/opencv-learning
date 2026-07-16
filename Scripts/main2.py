import cv2 as cv

#img = cv.imread(r"C:\Users\asus\OneDrive\Desktop\Learn_CV\DK.jpg")

#cv.imshow('DK', img)
capture = cv.VideoCapture(r"C:\Users\asus\OneDrive\Desktop\Learn_CV\Bhoomi.mp4.mp4")
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
    
capture.release
cv.destroyWindow
