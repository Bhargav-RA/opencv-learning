import cv2 

img = cv2.imread(r"C:\Users\asus\OneDrive\Desktop\Learn_CV\images\Puppy.jpg")

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Hello World")
        cv2.circle(img, (x, y), 50, (0, 255, 0), -1)
        
cv2.namedWindow(winname="Draw Circle")
cv2.setMouseCallback("Draw Circle", draw_circle)

while True:
    cv2.imshow("Draw Circle", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break   
    
cv2.destroyAllWindows()
