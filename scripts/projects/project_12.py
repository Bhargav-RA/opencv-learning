import cv2
import numpy as np

# Initialize webcam
cap = cv2.VideoCapture(0)

def nothing(x):
    pass

# Create control window
cv2.namedWindow("Tracker")

# Set initial default values so the screen isn't completely black at start
# Lower bounds start at 0, Upper bounds start at maximum values
cv2.createTrackbar("LH", "Tracker", 0, 179, nothing)   # OpenCV HSV Hue max is 179
cv2.createTrackbar("LS", "Tracker", 0, 255, nothing)   # Saturation max is 255
cv2.createTrackbar("LV", "Tracker", 0, 255, nothing)   # Value max is 255
cv2.createTrackbar("HH", "Tracker", 179, 179, nothing)
cv2.createTrackbar("HS", "Tracker", 255, 255, nothing)
cv2.createTrackbar("HV", "Tracker", 255, 255, nothing)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Get current trackbar positions
    l_h = cv2.getTrackbarPos("LH", "Tracker")
    l_s = cv2.getTrackbarPos("LS", "Tracker")
    l_v = cv2.getTrackbarPos("LV", "Tracker")
    h_h = cv2.getTrackbarPos("HH", "Tracker")
    h_s = cv2.getTrackbarPos("HS", "Tracker")
    h_v = cv2.getTrackbarPos("HV", "Tracker")

    # Create numpy arrays for limits
    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([h_h, h_s, h_v])

    # Create mask and apply it
    mask = cv2.inRange(hsv, l_b, u_b)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # ----------------------------------------------------
    # DEMONSTRATION TABS: Splitting into individual channels
    # ----------------------------------------------------
    # Split the original HSV frame into its standalone components
    h_channel, s_channel, v_channel = cv2.split(hsv)

    # Display all individual processing states in separate windows
    cv2.imshow("1. Original Frame", frame)
    cv2.imshow("2. Hue (Color Tone) Channel", h_channel)
    cv2.imshow("3. Saturation (Intensity) Channel", s_channel)
    cv2.imshow("4. Value (Brightness) Channel", v_channel)
    cv2.imshow("5. Generated Binary Mask", mask)
    cv2.imshow("6. Final Filtered Result", res)

    # FIX: Corrected bitwise condition to properly listen for the 'q' key
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

# Clean cleanup
cap.release()
cv2.destroyAllWindows()
