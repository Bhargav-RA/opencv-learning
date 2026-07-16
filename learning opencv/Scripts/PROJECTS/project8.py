import cv2

# Read the image
img = cv2.imread(r"Images/dog.webp")

# Mouse callback function
def draw_circle(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Hi")
        cv2.circle(img, (x, y), 50, (0, 0, 255), 2)

# Create a window
cv2.namedWindow("popup window")

# Set mouse callback
cv2.setMouseCallback("popup window", draw_circle)

# Display the image
while True:
    cv2.imshow("popup window", img)

    # Press 'c' to close the window
    if cv2.waitKey(1) & 0xFF == ord('c'):
        break

cv2.destroyAllWindows()