# extracting frames from the video 

import cv2
def FrameCapture(path):
    videoj=cv2.VideoCapture(r"C:\Users\Bhargav Ravinutala\Desktop\learn_cv\videos\1.mp4")

    count =0
    success= 1

    while success:
        success,image=videoj.read()
        cv2.imwrite("frame%d.jpg" % count, image)
        count+=1


if __name__=="__main__":
    FrameCapture(r"C:\Users\Bhargav Ravinutala\Desktop\learn_cv\videos\1.mp4")