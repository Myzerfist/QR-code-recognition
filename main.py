import cv2 as cv
import numpy as np
import webbrowser
import os
import re

cap = cv.VideoCapture(0)
detector = cv.QRCodeDetector()

def show_camera():
    while True:
        _, img = cap.read()
        data, bbox, _ = detector.detectAndDecode(img)

        gray = cv.cvtColor(img, cv.COLOR_RGB2RGBA)

        cv.imshow('frame', gray)

        if data:
            webbrowser.open(data)
            print("Opened " + str(data))
            break

        if cv.waitKey(1) == ord('q'):
            break

if not cap.isOpened():
    print("Cannot open camera")
    exit()
else:
    show_camera()

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
