# coding: utf-8
import requests


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
    def upload_to_remote(cls, img_save_local_path, filename, dest_url):
        loader = cls(file_dir=img_save_local_path, filename=filename, dest_url=dest_url)
        loader.upload_file()


