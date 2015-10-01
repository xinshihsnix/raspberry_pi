# coding:utf-8
import cv2
import datetime

def time_now_str():
    return datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')

capture = cv2.VideoCapture(0)

print capture.isOpened()

if capture.isOpened():
    ret, img = capture.read()
    cv2.imwrite(time_now_str()+'.jpg', img)
    capture.release()
