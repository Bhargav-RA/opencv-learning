import cv2
import mediapipe as mp
import math

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1)
mp_drawing = mp.solutions.drawing_utils

def calculate_angle(p1,p2):
    delta_y = p2[1] - p1[1]
    delta_x = p2[0] - p1[0]
    return math.degrees(math.atan2(delta_y, delta_x))

cap = cv2.VideoCapture(0)

while cap.isOpened():
    succrss, frame = cap.read()
    if not succrss:
        print("Ignoring empty camera frame.")
        continue


    h, w, _ = frame.shape
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(frame_rgb)
    
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            
            right_eye_outer = face_landmarks.landmark[33]
            left_eye_outer = face_landmarks.landmark[263]
            
            right_eye =(int(right_eye_outer.x * w), int(right_eye_outer.y * h))
            left_eye =(int(left_eye_outer.x * w), int(left_eye_outer.y * h))
            
            cv2.circle(frame, right_eye, 5, (0,255,0), -1)
            cv2.circle(frame, left_eye, 5, (0,255,0), -1)
            
            angel = calculate_angle(right_eye, left_eye)
            
            cv2.putText(frame,f"Head Tilt Angle: {angel:.2f} degrees",(30,40),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0),2)
            
    cv2.imshow("Real-time Head Tilt Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()