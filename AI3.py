import cv2
#Multiwindow

cam = cv2.VideoCapture(0)

while True:
    _,frame = cam.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Color one ', frame)
    cv2.moveWindow('Color one ' ,0,0)

    cv2.imshow('Gray', gray)
    cv2.moveWindow('Gray', 640, 0)

    if cv2.waitKey(1) == ord('q'):
        exit()
cam.release()
