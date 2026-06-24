import cv2 as cv

capture = cv.VideoCapture(r"C:\Users\Bhargav Ravinutala\Desktop\learn_cv\videos\1.mp4")

while True:
    isTrue, frame = capture.read()
    cv.imshow('video',frame)
    if cv.waitKey(24) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()    