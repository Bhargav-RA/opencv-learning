import cv2

cascade = r"C:\Users\Bhargav Ravinutala\Desktop\learn_cv\opencv-learning\scripts\projects\cars.xml"
video = r"C:\Users\Bhargav Ravinutala\Desktop\learn_cv\opencv-learning\scripts\projects\cars.mp4"

cap= cv2.VideoCapture(video)

car_cascade = cv2.CascadeClassifier(cascade)

while True:
    success,image = cap.read()

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cars =car_cascade.detectMultiScale(gray,1.1,1)

    for(x,y,w,h) in cars:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),1)

    cv2.imshow("car detector",image)

    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()