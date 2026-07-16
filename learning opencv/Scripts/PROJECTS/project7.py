# Saving video from webcam using OpenCV

import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
while True:
    ret, frame = cap.read()

    if not ret:
        break
    out.write(frame)

    cv2.imshow("Live", frame)
    if cv2.waitKey(1) & 0xFF == ord('c'):
        break


cap.release()
out.release()
cv2.destroyAllWindows()