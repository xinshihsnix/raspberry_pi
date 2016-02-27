# coding:utf-8
import cv2
import time
import base64

capture = cv2.VideoCapture(0)

print capture.isOpened()

if capture.isOpened():
    ret, img = capture.read()

    s = base64.b64encode(img)
    print '--------', s

    cv2.imwrite('/home/xinshi/picture/' + str(time.time()).replace('.', '')+'.jpg', img)
    capture.release()
