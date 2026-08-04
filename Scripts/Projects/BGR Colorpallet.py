import cv2 
import numpy as np

def emptyFunction(x):
    pass

img = np.zeros((300, 512, 3), np.uint8)
window_name = "BGR Color Palette"
cv2.namedWindow(window_name)

cv2.createTrackbar("B", window_name, 0, 255, emptyFunction)
cv2.createTrackbar("G", window_name, 0, 255, emptyFunction)
cv2.createTrackbar("R", window_name, 0, 255, emptyFunction)

while True:
    cv2.imshow(window_name, img)
    if cv2.waitKey(1) == 27:
        break
    
    b = cv2.getTrackbarPos("B", window_name)
    g = cv2.getTrackbarPos("G", window_name)
    r = cv2.getTrackbarPos("R", window_name)
    
    # Update the image color based on trackbar positions
    img[:] = [b, g, r]
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    