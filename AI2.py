import cv2

# Gray Video

cam = cv2.VideoCapture(0)

while True:
    _,frame = cam.read()
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray one ', gray)
    if cv2.waitKey(1) == ord('q'):
        exit()
cam.release()