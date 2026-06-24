import cv2 as cv

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    cv.imshow('video',frame)
    if cv.waitKey(100) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()    