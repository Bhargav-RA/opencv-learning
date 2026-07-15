import cv2

def FrameCapture(path):
    vidobj =cv2.VideoCapture(path)

    count=0
    success = 1

    while success:
        success,image= vidobj.read()
        cv2.imwrite("Frame%d.jpg" % count,image)
        count+=1






if __name__== '__main__':
    FrameCapture(r"C:\Users\Hai\Downloads\video.mp4")
    
    
    
    
    
    
    
    
 
