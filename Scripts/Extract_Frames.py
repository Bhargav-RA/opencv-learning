import cv2

def FrameCapture(path, target_frame_count=25):
    vidObj = cv2.VideoCapture(path)
    
    # Get the total number of frames in the video
    total_frames = int(vidObj.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Calculate how many frames to skip (e.g., 900 total / 25 target = save every 36th frame)
    step = max(1, total_frames // target_frame_count)
    
    count = 0
    saved_count = 0

    while True:
        success, image = vidObj.read()
        if not success:
            break
        
        # Only save the frame if it lands on our step interval
        if count % step == 0 and saved_count < target_frame_count:
            cv2.imwrite("frame%d.jpg" % saved_count, image)
            saved_count += 1
            
        count += 1

    print(f"Done! Successfully extracted {saved_count} frames.")

if __name__ == "__main__":
    path = "videos/video.mp4" 
    # You can change 25 to any number between 20 and 30
    FrameCapture(path, target_frame_count=25)