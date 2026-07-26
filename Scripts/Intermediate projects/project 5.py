import cv2

# Path to the Haar Cascade XML file
hercescad = cv2.data.haarcascades + "haarcascade_russian_plate_number.xml"

# Load the cascade only once
plate_cascade = cv2.CascadeClassifier(hercescad)

if plate_cascade.empty():
    print("Error: Could not load Haar Cascade XML file.")
    exit()

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    if not success:
        break

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plates = plate_cascade.detectMultiScale(
        img_gray,
        scaleFactor=1.1,
        minNeighbors=4
    )

    for (x, y, w, h) in plates:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(img, "Plate", (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                    (0, 255, 0), 2)

    cv2.imshow("Car Plate Detection", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()