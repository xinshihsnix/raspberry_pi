# coding: utf-8
import socket
import time
import os

from eye import Eye


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 8001))
    time.sleep(2)
    eye_x = Eye()
    s = eye_x.capture_img_to_base64()
    sock.send(s)
    print sock.recv(1024*100)
    sock.close()
