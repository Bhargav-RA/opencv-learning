import os
import cv2
import mediapipe as mp

# ==========================
# Model Path
# ==========================
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(SCRIPT_DIR, "hand_landmarker.task")

if not os.path.exists(MODEL_PATH):
    print("ERROR: hand_landmarker.task not found!")
    print("Expected location:")
    print(MODEL_PATH)
    exit()

# ==========================
# MediaPipe Hand Landmarker
# ==========================
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=MODEL_PATH),
    running_mode=VisionRunningMode.VIDEO,
    num_hands=2
)

landmarker = HandLandmarker.create_from_options(options)

# ==========================
# Open Webcam
# ==========================
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot open webcam.")
    exit()

timestamp = 0

while True:
    success, frame = cap.read()

    if not success:
        print("Failed to grab frame.")
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb
    )

    result = landmarker.detect_for_video(mp_image, timestamp)

    h, w, _ = frame.shape

    if result.hand_landmarks:

        for hand_landmarks in result.hand_landmarks:

            # Draw landmarks
            for point in hand_landmarks:
                x = int(point.x * w)
                y = int(point.y * h)

                cv2.circle(frame, (x, y), 6, (0, 255, 0), -1)

            # Draw connections
            connections = [
                (0,1),(1,2),(2,3),(3,4),
                (0,5),(5,6),(6,7),(7,8),
                (5,9),(9,10),(10,11),(11,12),
                (9,13),(13,14),(14,15),(15,16),
                (13,17),(17,18),(18,19),(19,20),
                (0,17)
            ]

            for start, end in connections:
                x1 = int(hand_landmarks[start].x * w)
                y1 = int(hand_landmarks[start].y * h)

                x2 = int(hand_landmarks[end].x * w)
                y2 = int(hand_landmarks[end].y * h)

                cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

    cv2.imshow("MediaPipe Hand Tracking - Python 3.13", frame)

    timestamp += 33

    key = cv2.waitKey(1)

    if key == 27 or key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()