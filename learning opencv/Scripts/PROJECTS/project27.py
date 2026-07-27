import cv2
import mediapipe as mp
import pyautogui

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# Open Webcam
cap = cv2.VideoCapture(0)

# Get Screen Resolution
screen_width, screen_height = pyautogui.size()

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    # Flip the frame
    frame = cv2.flip(frame, 1)

    # Frame dimensions
    frame_height, frame_width, _ = frame.shape

    # Convert to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process hand landmarks
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:

            # Draw landmarks
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            # Index finger tip (Landmark 8)
            index_tip = hand_landmarks.landmark[8]

            # Convert camera coordinates to screen coordinates
            x = int(index_tip.x * screen_width)
            y = int(index_tip.y * screen_height)

            # Move mouse
            pyautogui.moveTo(x, y)

            # Draw a circle on the fingertip
            cx = int(index_tip.x * frame_width)
            cy = int(index_tip.y * frame_height)

            cv2.circle(frame, (cx, cy), 10, (0, 255, 0), -1)

    # Display webcam
    cv2.imshow("Virtual Mouse", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()