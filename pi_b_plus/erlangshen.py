# coding:utf-8
import cv2
import time

from utils import time_now_str
import requests
# capture = cv2.VideoCapture(0)
#
# print capture.isOpened()
#
# if capture.isOpened():
#     ret, img = capture.read()
#     cv2.imwrite(time_now_str()+'.jpg', img)
#     capture.release()

IMG_SAVE_PATH = '/home/pi/what_i_see/'
PER_IMG_INTERVAL = 5    # 间隔时间, 单位为秒


class FileUploader(object):
    def __init__(self, file_dir='', filename='', dest_url=''):
        self.file_dir = file_dir
        self.filename = filename
        self.dest_url = dest_url
        self.file_path = self.file_dir + self.filename

    def upload_file(self):
        files={
                'pi_img':(self.filename,open(self.file_path,'rb'),'application/octet-stream'),
               }
        req = requests.post(url = self.dest_url, files = files)
        return req


    @classmethod
    def upload_to_xsite(cls):
        loader = cls(file_dir=IMG_SAVE_PATH, filename='%s.jpg'%time_now_str(), dest_url='http://192.168.1.102:9527/upload_file/')
        loader.upload_file()


class Divineye(object):
    def __init__(self):
        self.capture = cv2.VideoCapture(0)
        self.img_save_path = IMG_SAVE_PATH

    def save_img(self):
        ret, img = self.capture.read()
        cv2.imwrite(self.img_save_path + time_now_str()+'.jpg', img)
        self.capture.release()

if __name__ == '__main__':
    while True:
        divineye = Divineye()
        divineye.save_img()
        try:
            FileUploader.upload_to_xsite()
        except Exception, e:
            print 'eeeexe:', e
        time.sleep(PER_IMG_INTERVAL)
