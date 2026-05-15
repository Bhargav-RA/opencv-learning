import cv2 as cv

def rescaleFrame(Frame, scale=0.5):
    width=int(frame.shape[0]*scale)
    height=int(frame.shape[1]*scale)

    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def rescaleFrame_1(Frame, scale=0.5):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimensions_1 = (width,height)
    return cv.resize(frame,dimensions_1,interpolation=cv.INTER_AREA)


# capture = cv.VideoCapture(r"C:\Users\Bhargav Ravinutala\Desktop\learn_cv\videos\1.mp4")
capture = cv.VideoCapture(0)


while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    frame_resized_1 = rescaleFrame_1(frame)

    cv.imshow('video',frame)
    cv.imshow('video_resized',frame_resized)
    cv.imshow('video_resized_1',frame_resized_1)
    if cv.waitKey(24) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()    