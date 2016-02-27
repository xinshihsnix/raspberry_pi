# coding:utf-8
import cv2
import base64
import time

from settings import *


class Eye(object):
    def __init__(self):
        self.capture = cv2.VideoCapture(0)
        self.img_save_path = IMG_SAVE_PATH

    def save_img(self):
        ret, img = self.capture.read()
        cv2.imwrite(self.img_save_path + str(time.time()).replace('.', '') + '.jpg', img)
        self.capture.release()

    def capture_img_to_base64(self):
        """ 把拍到的图片转为base64字符串 """
        ret, img = self.capture.read()
        s = base64.b64encode(img)
        return s

