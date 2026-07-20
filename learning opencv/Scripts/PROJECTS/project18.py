import cv2
import imutils

gun_cascad = cv2.CascadeClassifier(
    r"C:\Users\Hai\OneDrive\Desktop\OPENCV\gun_cascad (1).xml"
)

camera = cv2.VideoCapture(0)

while True:
    success, frame = camera.read()

    if not success:
        break

    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gun = gun_cascad.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(100, 100)
    )

    gun_exist = False

    if len(gun) > 0:
        gun_exist = True

    for (x, y, w, h) in gun:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("security", frame)

    if gun_exist:
        print("Gun Detected")
    else:
        print("Gun not found")

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()