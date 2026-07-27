import cv2
import numpy as np
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

def detect_gesture(frame):
    """Detects the number of extended fingers using MediaPipe."""
    # Convert BGR to RGB for MediaPipe processing
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    
    if not results.multi_hand_landmarks:
        return "original"  # Default if no hand is visible

    for hand_landmarks in results.multi_hand_landmarks:
        # Optional: Draw the hand skeleton on screen for feedback
        mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        
        landmarks = hand_landmarks.landmark
        
        # Tip IDs for standard finger counting in MediaPipe
        # Thumb: 4, Index: 8, Middle: 12, Ring: 16, Pinky: 20
        # Pip IDs (joints below the tip)
        # Thumb: 2, Index: 6, Middle: 10, Ring: 14, Pinky: 18
        
        fingers = []
        
        # Check Thumb (Horizontal movement comparison for right/left hand adaptation)
        if landmarks[4].x < landmarks[3].x:
            fingers.append(1)
        else:
            fingers.append(0)
            
        # Check 4 Fingers (Vertical movement comparison: tip higher than lower joint)
        finger_tips = [8, 12, 16, 20]
        finger_pips = [6, 10, 14, 18]
        
        for tip, pip in zip(finger_tips, finger_pips):
            if landmarks[tip].y < landmarks[pip].y:
                fingers.append(1)
            else:
                fingers.append(0)
                
        total_fingers = fingers.count(1)
        
        # Map finger counts to match your original structure strings
        if total_fingers == 1: return "1_fingers"
        if total_fingers == 2: return "2_fingers"
        if total_fingers == 3: return "3_fingers"
        if total_fingers == 4: return "4_fingers"
        if total_fingers >= 5: return "5_fingers"
        
    return "original"

def apply_filter(frame, filter_name):
    """Applies standard OpenCV filters based on the selected string name."""
    if filter_name == "gray":
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
    elif filter_name == "blur":
        return cv2.GaussianBlur(frame, (15, 15), 0)
        
    elif filter_name == "sepia":
        sepia_matrix = np.array([[0.272, 0.534, 0.131],
                                 [0.349, 0.686, 0.168],
                                 [0.393, 0.769, 0.189]])
        sepia_frame = cv2.transform(frame, sepia_matrix)
        return np.clip(sepia_frame, 0, 255).astype(np.uint8)
        
    elif filter_name == "edges":
        return cv2.Canny(frame, 100, 200)
        
    else:
        return frame

# Initialize camera
cap = cv2.VideoCapture(0)
current_filter = "original"

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Mirror the frame for intuitive user interaction
    frame = cv2.flip(frame, 1)
    
    # Process the gesture directly inside this file
    gesture = detect_gesture(frame)
    
    if gesture == "1_fingers":
        current_filter = "original"
    elif gesture == "2_fingers":
        current_filter = "gray"
    elif gesture == "3_fingers":
        current_filter = "blur"
    elif gesture == "4_fingers":
        current_filter = "sepia"
    elif gesture == "5_fingers":
        current_filter = "edges"
        
    # Apply the native filter function built above
    filtered = apply_filter(frame, current_filter)
    
    # Convert single-channel images (gray/edges) back to 3 channels so text colors work
    if len(filtered.shape) == 2:
        filtered = cv2.cvtColor(filtered, cv2.COLOR_GRAY2BGR)
        
    # Display the current state overlay
    cv2.putText(filtered, f"Current Filter: {current_filter}", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow("Gesture Controlled Filters", filtered)
    
    # Exit cleanly if 'ESC' key is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        break
    
cap.release()
cv2.destroyAllWindows()