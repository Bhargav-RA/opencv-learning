import cv2

def FrameCapture(path):
    # Use the 'path' variable passed into the function
    vidobj = cv2.VideoCapture(path)
    
    count = 0
    
    while True:
        succes, image = vidobj.read()
        
        # If the video is over or the frame couldn't be read, break out of the loop
        if not succes:
            break
            
        # Only save if we actually have a valid image frame
        cv2.imwrite("frame%d.jpg" % count, image)
        count += 1  
        
    # It's good practice to release the video file when you're finished
    vidobj.release()
    print(f"Successfully extracted {count} frames!")
        
if __name__ == "__main__":
    video_path = r"C:\Users\asus\OneDrive\Desktop\Learn_CV\videos\video.mp4"
    FrameCapture(video_path)