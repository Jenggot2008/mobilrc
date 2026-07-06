import cv2

cap = cv2.VideoCapture("rtsp://172.15.5.130:8554/mjpeg/1")

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow("RTSP", frame)

    if cv2.waitKey(1) == 27:
        break