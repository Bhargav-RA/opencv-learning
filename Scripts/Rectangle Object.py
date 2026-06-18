import cv2

drawing = False
ix, iy = -1, -1

# Load image
image = cv2.imread(r"C:\Users\asus\OneDrive\Desktop\Learn_CV\images\Panda.jpg")

if image is None:
    print("Error: Could not load image.")
    exit()

clone = image.copy()

def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, image, clone

    # Mouse button pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    # Mouse moving while button is pressed
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            image = clone.copy()
            cv2.rectangle(image, (ix, iy), (x, y), (0, 255, 0), 2)

    # Mouse button released
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        image = clone.copy()
        cv2.rectangle(image, (ix, iy), (x, y), (0, 255, 0), 2)
        clone = image.copy()  # Keep rectangle permanently

cv2.namedWindow("Panda")
cv2.setMouseCallback("Panda", draw_rectangle)

while True:
    cv2.imshow("Panda", image)

    key = cv2.waitKey(1) & 0xFF

    # Reset image
    if key == ord('r'):
        image = cv2.imread(r"C:\Users\asus\OneDrive\Desktop\Learn_CV\images\Panda.jpg")
        clone = image.copy()

    # Quit
    elif key == ord('q'):
        break

cv2.destroyAllWindows()