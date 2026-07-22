# real time face detection

import cv2

a = cv2.CascadeClassifier(r"C:\Users\Bhargav Ravinutala\Desktop\learn_cv\opencv-learning\scripts\projects\haarcascade_frontalface_default.xml")

cam = cv2.VideoCapture(0)

while True:
    ret,cam_img = cam.read()

    grey = cv2.cvtColor(cam_img,cv2.COLOR_BGR2GRAY)

    face = a.detectMultiScale(grey,1.2,6)

    for(x1,y1,w1,h1) in face:
        cv2.rectangle(cam_img,(x1,y1),(x1+w1,y1+h1),(255,0,0),5)

    cv2.imshow("Detected_Face",cam_img)

    if cv2.waitKey(1) & 0xff == ('a'):
        break


cam.release()
cv2.destroyAllWindows()