# coding: utf-8
import socket


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8001))
    sock.listen(5)
    while True:
        connection,address = sock.accept()
        try:
            connection.settimeout(5)
            buf = connection.recv(1024*100)
            connection.send(buf)
            # print '=====:', buf
            # if buf == '1':
            #     connection.send('welcome to server!')
            # else:
            #     connection.send('go out!')
        except Exception, e:
            print e
        connection.close()