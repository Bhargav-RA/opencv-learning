import cv2
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

cascade_path = os.path.join(
    script_dir,
    "haarcascade_russian_plate_number (1).xml"
)

plate_cascade = cv2.CascadeClassifier(cascade_path)

if plate_cascade.empty():
    print("Error: Could not load Haar Cascade XML file.")
    exit()

video_path = r"C:\Users\asus\OneDrive\Desktop\Learn_CV\videos\Car.mp4"

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

if fps <= 0:
    fps = 30

scale = 0.6

width = int(original_width * scale)
height = int(original_height * scale)

output_path = os.path.join(
    script_dir,
    "number_plate_output.mp4"
)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")

out = cv2.VideoWriter(
    output_path,
    fourcc,
    fps,
    (width, height)
)

print("Press 'q' to quit.")

while True:

    success, frame = cap.read()

    if not success:
        print("Video Finished.")
        break

    frame = cv2.resize(
        frame,
        (width, height),
        interpolation=cv2.INTER_AREA
    )

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray = cv2.equalizeHist(gray)

    plates = plate_cascade.detectMultiScale(
        gray,
        scaleFactor=1.08,
        minNeighbors=10,
        minSize=(80, 25),
        maxSize=(500, 160)
    )

    for (x, y, w, h) in plates:

        aspect_ratio = w / float(h)

        center_x = x + w // 2
        center_y = y + h // 2

        if not (2.5 <= aspect_ratio <= 6.0):
            continue

        if w < 80 or h < 25:
            continue

        if center_y < height * 0.50:
            continue

        if center_x < width * 0.20:
            continue

        if center_x > width * 0.95:
            continue

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            "Number Plate",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2,
            cv2.LINE_AA
        )

    out.write(frame)

    cv2.imshow(
        "Number Plate Detection",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print("Output saved:")
print(output_path)