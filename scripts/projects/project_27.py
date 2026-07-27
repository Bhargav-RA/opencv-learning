import cv2
import mediapipe as mp
import pyautogui
import numpy as np

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)


cap = cv2.VideoCapture(0)
screen_width, screen_height = pyautogui.size()

while cap.isOpened():
    ret,frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame,1)
    h, w, c =frame.shape
    
    rgb_frame =cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            
            x = int(index_finger_tip.x * w)
            y = int(index_finger_tip.y * h)
            
            screen_x = np.interp(x, [0, w], [0, screen_width])
            screen_y = np.interp(y, [0, h], [0, screen_height])

            pyautogui.moveTo(screen_x, screen_y)  
            
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
    cv2.imshow("DEMO", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
    
    
