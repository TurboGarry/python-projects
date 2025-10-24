import cv2
import numpy
from PIL import ImageGrab

def ScreenRecorder():
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter("output.avi", fourcc)