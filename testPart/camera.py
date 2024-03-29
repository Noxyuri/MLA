import numpy as np
import cv2
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cv2.namedWindow("test")
img_counter = 0
while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)
    if k%256 == 27:
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        img_name = "opencv_frame_0.png"
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
cam.release()
cv2.destroyAllWindows()