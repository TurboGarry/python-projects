import cv2
import numpy
from PIL import ImageGrab

def ScreenRecorder():
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter("output.avi", fourcc, 30.0, (1366, 768))

    while True:
        img = ImageGrab.grab()
        img_np = numpy.array(img)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        cv2.imshow("Screen Recorder", frame)
        out.write(frame)

        if cv2.waitKey(1) == 27:
            break

    out.release()
    cv2.destroyAllWindows()

ScreenRecorder()