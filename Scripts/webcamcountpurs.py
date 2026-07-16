import cv2 as cv
import numpy as np

# Initialize the webcam (0 is usually the default camera)
capture = cv.VideoCapture(0)

while True:
    # Capture frame-by-frame
    isTrue, frame = capture.read()
    
    # If the frame wasn't read successfully, break the loop
    if not isTrue:
        break

    # Create a blank image based on the frame size for drawing contours
    blank = np.zeros(frame.shape, dtype='uint8')

    # 1. Convert to Grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # 2. Blur the image slightly to reduce noise (helps with better contour detection)
    blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)

    # 3. Thresholding (Adjust 125 if the room is too dark/bright)
    ret, thresh = cv.threshold(blur, 125, 255, cv.THRESH_BINARY)

    # 4. Find Contours
    contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

    # 5. Draw Contours on the blank image
    cv.drawContours(blank, contours, -1, (0, 0, 255), 2)

    # Display the results
    cv.imshow('Live Webcam', frame)
    cv.imshow('Thresh', thresh)
    cv.imshow('Contours', blank)

    # Break the loop if 'd' is pressed
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

# Release the capture and close windows
capture.release()
cv.destroyAllWindows()