# Pedestrian Detection using OpenCV-Python (HOG Descriptor)

import cv2
import imutils

# Initialize HOG Descriptor
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Load Video
cap = cv2.VideoCapture(r"C:\Users\asus\OneDrive\Desktop\Learn_CV\videos\HogRider.mp4")

# Create a resizable window
cv2.namedWindow("Result", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Result", 1280, 720)

while cap.isOpened():

    ret, img = cap.read()

    if not ret:
        break

    # Increase frame size for better detection
    img = imutils.resize(img, width=960)

    # Detect pedestrians
    regions, weights = hog.detectMultiScale(
        img,
        winStride=(4, 4),
        padding=(8, 8),
        scale=1.05
    )

    # Draw bounding boxes
    for (x, y, w, h) in regions:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Display output
    cv2.imshow("Result", img)

    # Press 'q' to quit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()