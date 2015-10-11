# coding:utf-8
import cv2
from utils import time_now_str

capture = cv2.VideoCapture(0)

print capture.isOpened()

if capture.isOpened():
    ret, img = capture.read()
    cv2.imwrite(time_now_str()+'.jpg', img)
    capture.release()
