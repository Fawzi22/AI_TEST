import cv2
Test 01
cam = cv2.VideoCapture(0)

while True :
    _, frame = cam.read()
    cv2.imshow('Cam1',frame)
    if cv2.waitKey(1) == ord('q'):
        exit()
cam.release()
