import os
import cv2
import face_recognition
import numpy as np

# -----------------------------
# Load Known Faces
# -----------------------------

KNOWN_FACES_DIR = r"C:\Users\Hai\Downloads\known_faces"

known_face_encodings = []
known_face_names = []

if not os.path.exists(KNOWN_FACES_DIR):
    print("Folder not found:", KNOWN_FACES_DIR)
    exit()

for filename in os.listdir(KNOWN_FACES_DIR):

    path = os.path.join(KNOWN_FACES_DIR, filename)

    # Ignore non-image files
    if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    image = face_recognition.load_image_file(path)
    encodings = face_recognition.face_encodings(image)

    if len(encodings) > 0:
        known_face_encodings.append(encodings[0])
        known_face_names.append(os.path.splitext(filename)[0])

print("Loaded Faces:", known_face_names)

# -----------------------------
# Start Webcam
# -----------------------------

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Unable to open webcam.")
    exit()

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Mirror the webcam
    frame = cv2.flip(frame, 1)

    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(
        rgb_frame,
        face_locations
    )

    # Compare faces
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

        name = "Unknown"
        color = (0, 0, 255)  # Red

        if len(known_face_encodings) > 0:

            matches = face_recognition.compare_faces(
                known_face_encodings,
                face_encoding,
                tolerance=0.5
            )

            face_distances = face_recognition.face_distance(
                known_face_encodings,
                face_encoding
            )

            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                color = (0, 255, 0)  # Green

        # Draw Rectangle
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)

        # Filled Label Background
        cv2.rectangle(frame,
                      (left, bottom - 30),
                      (right, bottom),
                      color,
                      cv2.FILLED)

        # Display Name
        cv2.putText(frame,
                    name,
                    (left + 6, bottom - 8),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (255, 255, 255),
                    2)

    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# -----------------------------
# Cleanup
# -----------------------------

cap.release()
cv2.destroyAllWindows()