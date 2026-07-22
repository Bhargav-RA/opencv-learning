# pointing coordinates in an image

import cv2

def click_event(event,x,y,flags,params):
    # print("working")

    if event == cv2.EVENT_LBUTTONDOWN:
        print(x," ",y)
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(img,str(x)+','+str(y),(x,y),font,1,(255,0,0),2)
        cv2.imshow('image',img)


    if event == cv2.EVENT_RBUTTONDOWN:
        print(x," ",y)
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(img,str(x)+','+str(y),(x,y),font,1,(255,0,0),2)
        cv2.imshow('image',img)

if __name__=="__main__":

    img=cv2.imread(r"C:\Users\Bhargav Ravinutala\Desktop\learn_cv\Frame0.jpg")

    cv2.imshow('image',img)

    cv2.setMouseCallback('image',click_event)

    cv2.waitKey(0)

    cv2.destroyAllWindows