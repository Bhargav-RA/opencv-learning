import cv2

img= cv2.imread(r"C:\Users\Bhargav Ravinutala\Desktop\learn_cv\frame52.jpg")

def draw_circle(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:

        print("Hi")
        cv2.circle(img,(x,y),50,(0,0,255),2)

cv2.namedWindow(winname="popup window")
cv2.setMouseCallback("popup window",draw_circle)


while True:
    cv2.imshow("popup window",img)
    if cv2.waitKey(10) & 0xFF == 27:
        break

    cv2.destroyAllWindows