import cv2

if __name__ == '__main__':

    val = True

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    out = cv2.VideoWriter("./test.avi", fourcc, 20.0, (640, 480), True)

    while val is True:
        ret, frame = cap.read()
        cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
        if frame is None:
            break
        else:
            out.write(frame)
            cv2.imshow("video", frame)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break

    cap.release()
    out.release()
