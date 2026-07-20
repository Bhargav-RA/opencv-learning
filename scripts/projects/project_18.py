import cv2
import imutils

gun_cascad = cv2.CascadeClassifier(r"C:\Users\Bhargav Ravinutala\Desktop\learn_cv\opencv-learning\scripts\projects\gun_cascad.xml")

camera = cv2.VideoCapture(0)

first_frame = None
gun_exist = None


while True:
    success,frame = camera.read()

    frame=imutils.resize(frame,width=500)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gun=gun_cascad.detectMultiScale(gray,1.3,5,minSize=(100,100))

    if len(gun) >0:
        gun_exist=True

    for(x,y,h,w) in gun:
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    cv2.imshow("gunt_detector",frame)
    key=cv2.waitKey(1) & 0xff
    if key==ord('w'):
        break

if gun_exist:
    print("gun detected")
else:
    print("not detected")

camera.release()
cv2.destroyAllWindows()    