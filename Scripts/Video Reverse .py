import cv2

# Use a raw string to avoid invalid escape sequence warnings on Windows paths
video_path = r"C:\Users\asus\OneDrive\Desktop\Learn_CV\videos\video.mp4"

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    raise FileNotFoundError(f"Could not open video: {video_path}")

frame_list = []

while True:
    check, frame = cap.read()
    if not check:
        break
    frame_list.append(frame)

cap.release()

# Reverse playback
frame_list.reverse()

for frame in frame_list:
    cv2.imshow("Video", frame)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()

