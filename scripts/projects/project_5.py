import cv2

cap=cv2.VideoCapture(r"C:\Users\Bhargav Ravinutala\Desktop\learn_cv\videos\1.mp4")

check,vid = cap.read()
counter = 0
frame_list=[]

while(check==True):
    cv2.imwrite("frame%d.jpg" % counter,vid)
    check,vid = cap.read()
    frame_list.append(vid)
    counter += 1


frame_list.pop()
frame_list.reverse()
for frame in frame_list:
    cv2.imshow("Frame",frame)
    if cv2.waitKey(25) and 0xff == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()        