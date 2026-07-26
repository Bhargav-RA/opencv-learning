# import cv2

# hercescad =r"C:\Users\Bhargav Ravinutala\Desktop\learn_cv\opencv-learning\scripts\projects\haarcascade_russian_plate_number.xml"

# cap = cv2.VideoCapture(0)

# while True:
#     succes, img= cap.read()
    
#     plate_cascade = cv2.CascadeClassifier(hercescad)
    
#     img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
#     plates = plate_cascade.detectMultiScale(img_gray,1.1,4)
    
#     for (x,y,w,h) in plates:
#         cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        
    
#     cv2.imshow("car Plate",img)
    
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
    
# cap.release()
# cv2.destroyAllWindows()






import cv2
import sys

# 1. Load the classifier ONCE outside the loop to keep frame rates smooth
hercescad = r"C:\Users\Bhargav Ravinutala\Desktop\learn_cv\opencv-learning\scripts\projects\haarcascade_russian_plate_number.xml"
plate_cascade = cv2.CascadeClassifier(hercescad)

# 2. Checkpoint: Ensure the XML file path works and reads properly
if plate_cascade.empty():
    print(f"CRITICAL ERROR: Failed to load XML file from path:\n{hercescad}")
    print("Please verify that the file exists and is not empty.")
    sys.exit()

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture frame from webcam.")
        break
        
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detect license plates
    plates = plate_cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=4)
    
    # Draw rectangles around detected boundaries
    for (x, y, w, h) in plates:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
    cv2.imshow("Car Plate Tracker", img)
    
    # Press 'q' to safely exit the stream loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
