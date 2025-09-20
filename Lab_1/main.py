import cv2 as cv
def task2():
    img1 = cv.imread("BOB.jpg", flags=0)
    img2 = cv.imread("JUK.png", flags=1)
    img3 = cv.imread("BOB.jpg", flags=1)
    img4 = cv.imread("BOB.jpg", flags=2)
    cv.namedWindow("Display window1", cv.WINDOW_FULLSCREEN)
    cv.namedWindow("Display window2", cv.WINDOW_AUTOSIZE)
    cv.namedWindow("Display window3", cv.WINDOW_NORMAL)
    cv.namedWindow("Display window4", cv.WINDOW_NORMAL)
    cv.imshow('Display window1', img1)
    cv.waitKey(0)
    cv.destroyWindow('Display window1')
    cv.imshow('Display window2', img2)
    cv.waitKey(0)
    cv.destroyWindow('Display window2')
    cv.imshow('Display window3', img3)
    cv.waitKey(0)
    cv.destroyWindow('Display window3')
    cv.imshow('Display window4', img4)
    cv.waitKey(0)
    cv.destroyWindow('Display window4')

def task3():
    files = ["video.mp4", "gif.gif"]

    for file in files:
        cap = cv.VideoCapture(file, cv.CAP_ANY)
        while True:
            ret, frame = cap.read()
            if not ret:
                cap.set(cv.CAP_PROP_POS_FRAMES, 0)
                continue

            cv.imshow('frame', frame)

            if cv.waitKey(1) & 0xFF == 27:
                cap.release()
                cv.destroyAllWindows()
                return

            if cv.waitKey(1) & 0xFF == 27:
                break

        cap.release()
        cv.destroyAllWindows()

def FileWriteTOFile(file):
    video = cv.VideoCapture()
    ok, img = video.read()
    w = int(video.get(cv.CAP_PROP_FRAME_WIDTH))
    h = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    video_writer = cv.VideoWriter("output.mov", fourcc, 25, (w, h))
    # while (True):
    #     ok, img = video.read()
    #     cv.imshow('img', img)
    #     video_writer.write(img)
    #     if cv.waitKey(1) & 0xFF == ord('q'):
    #         break
    video.release()
    cv.destroyAllWindows()

def print_cam():
    cap = cv.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    while True:
        ret, frame = cap.read()
        # Convert to grayscale
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # Display the resulting frame
        cv.imshow('frame', gray)
        if cv.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv.destroyAllWindows()

def task5():
    frame = cv.imread("BOB.jpg")
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    cv.namedWindow("Display window2", cv.WINDOW_NORMAL)
    cv.imshow('Display window2', frame)
    cv.waitKey(0)
    cv.namedWindow("Display window1", cv.WINDOW_NORMAL)
    cv.imshow('Display window1', hsv)
    cv.waitKey(0)

def task6():
    cap = cv.VideoCapture(0)
    width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    cap.set(3, 640)
    cap.set(4, 480)
    while True:
        ret, frame = cap.read()

        center_x, center_y = width // 2, height // 2
        color = (0,0,255)

        cv.rectangle(frame, (center_x - 40, center_y - 10), (center_x + 40, center_y + 10), color)
        cv.rectangle(frame, (center_x - 10, center_y - 40), (center_x + 10, center_y + 40),  color)

        cv.imshow('frame', frame)
        if cv.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv.destroyAllWindows()

def task7():
    output_file = "video_saved_task7.mp4"

    cap = cv.VideoCapture(0)
    w = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

    vr = cv.VideoWriter_fourcc(*'H264')
    out = cv.VideoWriter(output_file, vr, 20, (w, h))

    rec = True

    while rec:
        ret, frame = cap.read()
        cv.imshow("Cam", frame)

        out.write(frame)

        if cv.waitKey(1) & 0xFF == 27:
            rec = False

    out.release()
    cap.release()
    cv.destroyAllWindows()

    cap_play = cv.VideoCapture(output_file)

    while True:
        ret, frame = cap_play.read()

        cv.imshow('frame', frame)

        if cv.waitKey(1) & 0xFF == 27:
            break

    cap_play.release()
    cv.destroyAllWindows()

def draw_cross_RGB(frame, width, height):
    center_X = width // 2
    center_Y = height // 2

    b, g, r = frame[center_Y, center_X]
    max_value = max(b,g,r)
    if max_value == r:
        color = (0,0,255)
    elif max_value == g:
        color = (0, 255, 0)
    else:
        color = (255, 0, 0)

    cv.rectangle(frame, (center_X - 40, center_Y - 10), (center_X + 40, center_Y + 10), color)
    cv.rectangle(frame, (center_X - 10, center_Y - 40), (center_X + 10, center_Y + 40), color)

    return frame

def task8():
    cap = cv.VideoCapture(0)

    width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

    while True:
        ret, frame = cap.read()

        frame = draw_cross_RGB(frame, width, height)

        cv.imshow("RGB_cross", frame)

        if cv.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv.destroyAllWindows()

def task9():
    cap = cv.VideoCapture(1)

    width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

    while True:
        ret, frame = cap.read()

        frame = draw_cross_RGB(frame, width, height)

        cv.imshow("RGB_cross", frame)

        if cv.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv.destroyAllWindows()

# FileWriteTOFile("video.mp4")
# task5()
# print_cam()
# task6()
task7()
# task8()
# task9()