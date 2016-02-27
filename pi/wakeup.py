# coding: utf-8
import time

from settings import *
from eye.eye import Eye

if __name__ == '__main__':
    while True:
        eye = Eye()
        eye.save_img()
        # TODO
        # try:
        #     FileUploader.upload_to_remote()
        # except Exception, e:
        #     print 'eeeexe:', e
        time.sleep(PER_IMG_INTERVAL)