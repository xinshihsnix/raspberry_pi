# coding:utf-8
import cv2
import time

from utils import time_now_str

# capture = cv2.VideoCapture(0)
#
# print capture.isOpened()
#
# if capture.isOpened():
#     ret, img = capture.read()
#     cv2.imwrite(time_now_str()+'.jpg', img)
#     capture.release()

IMG_SAVE_URL = '/var/pi_media/'

class Divineye(object):
    def __init__(self):
        self.capture = cv2.VideoCapture(0)
        self.img_save_url = IMG_SAVE_URL

    def save_img(self):
        ret, img = self.capture.read()
        cv2.imwrite(self.img_save_url + time_now_str()+'.jpg', img)
        self.capture.release()

if __name__ == '__main__':
    while True:
        divineye = Divineye()
        divineye.save_img()
        time.sleep(5)