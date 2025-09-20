import cv2 as cv
def task1():
    cap = cv.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    while True:
        ret, frame = cap.read()
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        cv.imshow('hsv', hsv)
        if cv.waitKey(33) & 0xFF == 27:
            break

    cap.release()
    cv.destroyAllWindows()

def nothing(args): pass

def task2():
    cv.namedWindow("setup")
    cv.createTrackbar("b1", "setup", 0, 255, nothing)
    cv.createTrackbar("g1", "setup", 0, 255, nothing)
    cv.createTrackbar("r1", "setup", 0, 255, nothing)
    cv.createTrackbar("b2", "setup", 255, 255, nothing)
    cv.createTrackbar("g2", "setup", 255, 255, nothing)
    cv.createTrackbar("r2", "setup", 255, 255, nothing)
    # img = cv.imread("C:/Users/Kurdicks/PycharmProjects/PythonProject2/Lab_2/red_october.png")
    cap = cv.VideoCapture(0)
    while True:
        # img_copy = img.copy()
        ret, img_copy = cap.read()
        b1 = cv.getTrackbarPos('b1', 'setup')
        g1 = cv.getTrackbarPos('g1', 'setup')
        r1 = cv.getTrackbarPos('r1', 'setup')
        b2 = cv.getTrackbarPos('b2', 'setup')
        g2 = cv.getTrackbarPos('g2', 'setup')
        r2 = cv.getTrackbarPos('r2', 'setup')

        min_p = (g1, b1, r1)
        max_p = (g2, b2, r2)

        mask = cv.inRange(img_copy, min_p, max_p)
        cv.imshow('Red Mask', mask)


        contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        print(f"Найдено контуров: {len(contours)}")
        if(len(contours) > 0):
            largest_contour = max(contours, key=cv.contourArea)
            area = cv.contourArea(largest_contour)
            print(f"Площадь наибольшего контура: {area}")

            if cv.contourArea(largest_contour) > 10:
                x, y, w, h = cv.boundingRect(largest_contour)
                cv.rectangle(img_copy, (x, y), (x+w, y+h), (255, 0, 0), 7)
                print(f"Bounding box: x={x}, y={y}, w={w}, h={h}")

        cv.imshow('original', img_copy)

        if cv.waitKey(33) & 0xFF == 27:
            break

    cv.destroyAllWindows()
    cap.release()

def task2HSV(source, is_image = False):
    cv.namedWindow("setup")

    cv.createTrackbar("h1_low", "setup", 0, 179, nothing)
    cv.createTrackbar("h1_high", "setup", 10, 179, nothing)
    cv.createTrackbar("s1_low", "setup", 120, 255, nothing)
    cv.createTrackbar("s1_high", "setup", 255, 255, nothing)
    cv.createTrackbar("v1_low", "setup", 70, 255, nothing)
    cv.createTrackbar("v1_high", "setup", 255, 255, nothing)
    cv.createTrackbar("h2_low", "setup", 170, 179, nothing)
    cv.createTrackbar("h2_high", "setup", 179, 179, nothing)
    cv.createTrackbar("s2_low", "setup", 120, 255, nothing)
    cv.createTrackbar("s2_high", "setup", 255, 255, nothing)
    cv.createTrackbar("v2_low", "setup", 70, 255, nothing)
    cv.createTrackbar("v2_high", "setup", 255, 255, nothing)

    # cap = cv2.VideoCapture("C:/Users/Kurdicks/PycharmProjects/PythonProject2/Lab_2/red_october.png")
    cap = cv.VideoCapture(0)
    while True:
        # img_copy = img.copy()
        ret, img_copy = cap.read()
        if not ret:
            print("Ошибка чтения кадра")
            break

        hsv = cv.cvtColor(img_copy, cv.COLOR_BGR2HSV)

        h1_low = cv.getTrackbarPos('h1_low', 'setup')
        h1_high = cv.getTrackbarPos('h1_high', 'setup')
        s1_low = cv.getTrackbarPos('s1_low', 'setup')
        s1_high = cv.getTrackbarPos('s1_high', 'setup')
        v1_low = cv.getTrackbarPos('v1_low', 'setup')
        v1_high = cv.getTrackbarPos('v1_high', 'setup')
        h2_low = cv.getTrackbarPos('h2_low', 'setup')
        h2_high = cv.getTrackbarPos('h2_high', 'setup')
        s2_low = cv.getTrackbarPos('s2_low', 'setup')
        s2_high = cv.getTrackbarPos('s2_high', 'setup')
        v2_low = cv.getTrackbarPos('v2_low', 'setup')
        v2_high = cv.getTrackbarPos('v2_high', 'setup')

        min_p1 = (h1_low, s1_low, v1_low)
        max_p1 = (h1_high, s1_high, v1_high)
        min_p2 = (h2_low, s2_low, v2_low)
        max_p2 = (h2_high, s2_high, v2_high)

        mask1 = cv.inRange(hsv, min_p1, max_p1)
        mask2 = cv.inRange(hsv, min_p2, max_p2)
        mask = cv.bitwise_or(mask1, mask2)

        cv.imshow('Red Mask', mask)

        contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        print(f"Найдено контуров: {len(contours)}")
        if len(contours) > 0:
            largest_contour = max(contours, key=cv.contourArea)
            area = cv.contourArea(largest_contour)
            print(f"Площадь наибольшего контура: {area}")

            if cv.contourArea(largest_contour) > 10:
                x, y, w, h = cv.boundingRect(largest_contour)
                cv.rectangle(img_copy, (x, y), (x + w, y + h), (255, 0, 0), 7)
                print(f"Bounding box: x={x}, y={y}, w={w}, h={h}")

        cv.imshow('original', img_copy)

        if cv.waitKey(33) & 0xFF == 27:
            break

    cv.destroyAllWindows()
    cap.release()

def task3(source, is_image = False):
    if is_image:
        img = cv.imread(source)
    else:
        cap = cv.VideoCapture(source)

    cv.namedWindow("setup")
    cv.createTrackbar("h1_low", "setup", 0, 179, nothing)
    cv.createTrackbar("h1_high", "setup", 10, 179, nothing)
    cv.createTrackbar("s1_low", "setup", 120, 255, nothing)
    cv.createTrackbar("s1_high", "setup", 255, 255, nothing)
    cv.createTrackbar("v1_low", "setup", 70, 255, nothing)
    cv.createTrackbar("v1_high", "setup", 255, 255, nothing)
    cv.createTrackbar("h2_low", "setup", 170, 179, nothing)
    cv.createTrackbar("h2_high", "setup", 179, 179, nothing)
    cv.createTrackbar("s2_low", "setup", 120, 255, nothing)
    cv.createTrackbar("s2_high", "setup", 255, 255, nothing)
    cv.createTrackbar("v2_low", "setup", 70, 255, nothing)
    cv.createTrackbar("v2_high", "setup", 255, 255, nothing)

    # Позиционируем окна
    cv.moveWindow("setup", 0, 0)


    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5,5))

    while True:
        if is_image:
            img_copy = img.copy()
        else:
            ret, img_copy = cap.read()

        hsv = cv.cvtColor(img_copy, cv.COLOR_BGR2HSV)

        h1_low = cv.getTrackbarPos('h1_low', 'setup')
        h1_high = cv.getTrackbarPos('h1_high', 'setup')
        s1_low = cv.getTrackbarPos('s1_low', 'setup')
        s1_high = cv.getTrackbarPos('s1_high', 'setup')
        v1_low = cv.getTrackbarPos('v1_low', 'setup')
        v1_high = cv.getTrackbarPos('v1_high', 'setup')
        h2_low = cv.getTrackbarPos('h2_low', 'setup')
        h2_high = cv.getTrackbarPos('h2_high', 'setup')
        s2_low = cv.getTrackbarPos('s2_low', 'setup')
        s2_high = cv.getTrackbarPos('s2_high', 'setup')
        v2_low = cv.getTrackbarPos('v2_low', 'setup')
        v2_high = cv.getTrackbarPos('v2_high', 'setup')

        min_p1 = (h1_low, s1_low, v1_low)
        max_p1 = (h1_high, s1_high, v1_high)
        min_p2 = (h2_low, s2_low, v2_low)
        max_p2 = (h2_high, s2_high, v2_high)

        mask1 = cv.inRange(hsv, min_p1, max_p1)
        mask2 = cv.inRange(hsv, min_p2, max_p2)
        mask = cv.bitwise_or(mask1, mask2)

        opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel, iterations=1)
        closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel, iterations=1)

        cv.imshow('Red Mask', mask)
        cv.imshow('Opening', opening)
        cv.imshow('Closing', closing)

        cv.moveWindow("Red Mask", 500, 0)
        cv.moveWindow("Opening", 0, 500)
        cv.moveWindow("Closing", 500, 5000)

        cv.imshow('original', img_copy)
        cv.moveWindow("original", 1000, 0)
        if cv.waitKey(33) & 0xFF == 27:
            break

def task4(source, is_image = False):
    if is_image:
        img = cv.imread(source)
    else:
        cap = cv.VideoCapture(0)

    cv.namedWindow("setup")
    cv.namedWindow("Red Mask")
    cv.namedWindow("Opening")
    cv.namedWindow("Closing")
    cv.namedWindow("original")

    cv.moveWindow("setup", 0, 0)
    cv.moveWindow("Red Mask", 500, 0)
    cv.moveWindow("Opening", 1000, 0)
    cv.moveWindow("Closing", 0, 500)
    cv.moveWindow("original", 500, 500)

    cv.createTrackbar("h1_low", "setup", 0, 179, nothing)
    cv.createTrackbar("h1_high", "setup", 10, 179, nothing)
    cv.createTrackbar("s1_low", "setup", 120, 255, nothing)
    cv.createTrackbar("s1_high", "setup", 255, 255, nothing)
    cv.createTrackbar("v1_low", "setup", 70, 255, nothing)
    cv.createTrackbar("v1_high", "setup", 255, 255, nothing)
    cv.createTrackbar("h2_low", "setup", 170, 179, nothing)
    cv.createTrackbar("h2_high", "setup", 179, 179, nothing)
    cv.createTrackbar("s2_low", "setup", 120, 255, nothing)
    cv.createTrackbar("s2_high", "setup", 255, 255, nothing)
    cv.createTrackbar("v2_low", "setup", 70, 255, nothing)
    cv.createTrackbar("v2_high", "setup", 255, 255, nothing)

    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))

    while True:
        if is_image:
            img_copy = img.copy()
        else:
            ret, img_copy = cap.read()

        hsv = cv.cvtColor(img_copy, cv.COLOR_BGR2HSV)

        h1_low = cv.getTrackbarPos('h1_low', 'setup')
        h1_high = cv.getTrackbarPos('h1_high', 'setup')
        s1_low = cv.getTrackbarPos('s1_low', 'setup')
        s1_high = cv.getTrackbarPos('s1_high', 'setup')
        v1_low = cv.getTrackbarPos('v1_low', 'setup')
        v1_high = cv.getTrackbarPos('v1_high', 'setup')
        h2_low = cv.getTrackbarPos('h2_low', 'setup')
        h2_high = cv.getTrackbarPos('h2_high', 'setup')
        s2_low = cv.getTrackbarPos('s2_low', 'setup')
        s2_high = cv.getTrackbarPos('s2_high', 'setup')
        v2_low = cv.getTrackbarPos('v2_low', 'setup')
        v2_high = cv.getTrackbarPos('v2_high', 'setup')

        min_p1 = (h1_low, s1_low, v1_low)
        max_p1 = (h1_high, s1_high, v1_high)
        min_p2 = (h2_low, s2_low, v2_low)
        max_p2 = (h2_high, s2_high, v2_high)

        mask1 = cv.inRange(hsv, min_p1, max_p1)
        mask2 = cv.inRange(hsv, min_p2, max_p2)
        mask = cv.bitwise_or(mask1, mask2)

        opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel, iterations=1)
        closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel, iterations=1)

        cv.imshow('Red Mask', mask)
        cv.imshow('Opening', opening)
        cv.imshow('Closing', closing)

        contours, hierarchy = cv.findContours(opening, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        print(f"Найдено контуров: {len(contours)}")
        if len(contours) > 0:
            largest_contour = max(contours, key=cv.contourArea)
            area = cv.contourArea(largest_contour)
            print(f"Площадь наибольшего контура: {area}")

            if cv.contourArea(largest_contour) > 10:
                moments = cv.moments(largest_contour)
                m00 = moments['m00']
                m10 = moments['m10']
                m01 = moments['m01']

                if m00 != 0:
                    center_x = int(m10/m00)
                    center_y = int(m01/m00)
                    print(f"m10 = {m10}, m01 = {m01}")
                    print(f"center of masses = {center_x}, {center_y}")
                else:
                    print(f"m00 = 0, center of masses is not identity")
                    center_x = 0
                    center_y = 0

                x, y, w, h = cv.boundingRect(largest_contour)
                cv.rectangle(img_copy, (x, y), (x + w, y + h), (0, 0, 0), 3)

                cv.circle(img_copy, (center_x, center_y), 5, (0, 0, 255), -1)

            cv.imshow('original', img_copy)

            if cv.waitKey(33) & 0xFF == 27:
                break
# task1()
# task2HSV(0)
# task3(0)
task4(0)
