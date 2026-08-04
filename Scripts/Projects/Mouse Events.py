import cv2

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, f"{x},{y}", (x, y), font, 0.6, (255, 0, 0), 2)
        cv2.imshow("Ironman", img)

    if event == cv2.EVENT_RBUTTONDOWN:
        print(x, y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, f"{x},{y}", (x, y), font, 0.6, (0, 0, 255), 2)
        cv2.imshow("Ironman", img)

if __name__ == "__main__":

    img = cv2.imread(r"C:\Users\asus\OneDrive\Desktop\Learn_CV\images\Ironman.jpg")

    # Resize image to 40% of the original size
    scale_percent = 40
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    img = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)

    cv2.imshow("Ironman", img)
    cv2.setMouseCallback("Ironman", click_event)

    cv2.waitKey(0)
    cv2.destroyAllWindows()