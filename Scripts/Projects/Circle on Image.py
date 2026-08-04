import cv2

img = cv2.imread(r"C:\Users\asus\OneDrive\Desktop\Learn_CV\images\Ironman.jpg")

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Hello")
        cv2.circle(img,(x,y),100,(0,0,255),-1)
        
cv2.namedWindow(winname = "My Panda")
cv2.setMouseCallback("My Panda",draw_circle)

while True:
    cv2.imshow("My Panda",img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
    
cv2.destroyAllWindows()
