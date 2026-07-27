import cv2
import os

# ===========================
# Load Haar Cascade
# ===========================
script_dir = os.path.dirname(os.path.abspath(__file__))

cascade_path = os.path.join(
    script_dir,
    "haarcascade_russian_plate_number (1).xml"
)

plate_cascade = cv2.CascadeClassifier(cascade_path)

if plate_cascade.empty():
    print("Error: Could not load Haar Cascade XML file.")
    print("Expected path:", cascade_path)
    exit()

# ===========================
# Video Path
# ===========================
video_path = r"C:\Users\asus\OneDrive\Desktop\Learn_CV\Videos\Video6.mp4"
# Change this to your actual video path

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

print("Press 'q' to quit.")

while True:
    success, frame = cap.read()

    if not success:
        print("Video Finished.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    plates = plate_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=4,
        minSize=(30, 30)
    )

    for (x, y, w, h) in plates:

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.putText(
            frame,
            "Number Plate",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    cv2.imshow("Number Plate Detection", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()