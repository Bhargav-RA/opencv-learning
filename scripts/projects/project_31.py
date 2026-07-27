import cv2
import numpy as np
import zxingcpp

# Initialize webcam
cap = cv2.VideoCapture(0)

print("Scanner active. Press 'q' or 'ESC' to exit.")

while True:
    success, frame = cap.read()
    if not success:
        break

    # Read barcodes or QR codes out of the frame
    results = zxingcpp.read_barcodes(frame)
    
    for code in results:
        data = code.text
        if not data:
            continue
            
        # Extract the specialized Position object
        pos = code.position
        
        if pos:
            # Map the exact corner structures from the zxingcpp object layout
            pts = np.array([
                [pos.top_left.x, pos.top_left.y],
                [pos.top_right.x, pos.top_right.y],
                [pos.bottom_right.x, pos.bottom_right.y],
                [pos.bottom_left.x, pos.bottom_left.y]
            ], np.int32)
            
            # Format shape for OpenCV polygon drawer
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(frame, [pts], True, (0, 255, 0), 2)

            # Extract a safe position overlay anchor coordinate point
            x_min = int(min(pos.top_left.x, pos.bottom_left.x))
            y_min = int(min(pos.top_left.y, pos.top_right.y))
            
            # Draw the classification text tracking overlay tag string 
            cv2.putText(frame, data, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 
                        0.7, (255, 0, 0), 2)

        print(f"Detected Code: {data}")

    # Show video frame feed window
    cv2.imshow('Barcode/QR Code Scanner', frame)

    # Clean exit triggers ('q' key or 'ESC' key code)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:
        break

cap.release()
cv2.destroyAllWindows()
