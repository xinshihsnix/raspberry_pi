# coding:utf-8
import cv2

from common.utils.format import time_now_str

capture = cv2.VideoCapture(0)

if capture.isOpened():
    ret, img = capture.read()
    cv2.imwrite(time_now_str(), img)