import cv2 as cv
def task1():
    cap = cv.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    while True:
        ret, frame = cap.read()
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        cv.imshow('hsv', hsv)
        if cv.waitKey(0) & 0xFF == 27:
            break

    cap.release()
    cv.destroyAllWindows()

task1()