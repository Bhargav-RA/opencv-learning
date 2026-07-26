import cv2

hercescad =r"C:\Users\Hai\OneDrive\Desktop\OPENCV\learning opencv\Scripts\PROJECTS\haarcascade_frontalface_default (1) (1).xml"

cap = cv2.VideoCapture(0)

while True:
    succes, img= cap.read()
    
    plate_cascade = cv2.CascadeClassifier(hercescad)
    
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    plates = plate_cascade.detectMultiScale(img_gray,1.1,4)
    
    for (x,y,w,h) in plates:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        
    
    cv2.imshow("car Plate",img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()