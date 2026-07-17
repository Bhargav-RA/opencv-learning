import cv2
import numpy as np
import time

capture_video = cv2.VideoCapture(0)

# Allow camera to warm up
time.sleep(2)
count = 0
background = 0

# Capture the baseline background frame
print("Capturing background... Please stay out of frame!")
for i in range(60):
    return_val, background = capture_video.read()
    if return_val == False:
        continue

background = np.flip(background, axis=1)

print("Background captured! You can now enter the frame with your Black cloth.")

while (capture_video.isOpened()):
    return_val, img = capture_video.read()
    if not return_val:
        break
    count = count + 1
    img = np.flip(img, axis=1)

    # FIXED: Changed 'mg' to 'img' to fix your NameError typo
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # ----------------------------------------------------
    # BLACK COLOR PARAMETERS (HSV)
    # ----------------------------------------------------
    # Hue: 0-180 (all colors)
    # Saturation: 0-255 (all intensities)
    # Value: 0-50 (Only very dark/shadowy tones)
    # NOTE: If it picks up too much background shadow, lower the '50' value to '40' or '30'
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 50])

    # Generate the black mask
    mask1 = cv2.inRange(hsv, lower_black, upper_black)

    # Clean up the mask using morphological operations
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    
    # FIXED: Wrapped the shape dimensions inside a tuple (3,3) for cv2.dilate
    mask1 = cv2.dilate(mask1, np.ones((3, 3), np.uint8), iterations=1)
    
    # Invert the mask to find everything that is NOT black
    mask2 = cv2.bitwise_not(mask1)

    # Isolate the background where the black cloth is
    res1 = cv2.bitwise_and(background, background, mask=mask1)
    # Isolate the current frame where the black cloth is NOT present
    res2 = cv2.bitwise_and(img, img, mask=mask2)

    # Blend them together for the invisibility illusion
    final_out = cv2.addWeighted(res1, 1, res2, 1, 0)

    cv2.imshow("Invisible T-Shirt (Black)", final_out)
    
    # Press ESC to exit
    k = cv2.waitKey(10)
    if k == 27:
        break

capture_video.release()
cv2.destroyAllWindows()