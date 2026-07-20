#CAR DETECTION
import cv2

cascade=r'C:\Users\Hai\OneDrive\Desktop\OPENCV\cars (1).xml'
video = r'C:\Users\Hai\OneDrive\Desktop\OPENCV\learning opencv\Video\car video.mp4'

cap = cv2.VideoCapture(video)

car_cascade = cv2.CascadeClassifier(cascade)

while True:
    success,image = cap.read()
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cars=car_cascade.detectMultiScale(gray,1.1,1)
    
    for(x,y,w,h) in cars:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
        
    cv2.imshow('cars',image)
    
    if cv2.waitKey(33) == 27:
        break
    
cv2.destroyAllWindows()
        
        