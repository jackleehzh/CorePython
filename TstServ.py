#!/usr/bin/env python

from socket import *
from time import sleep, ctime
import _thread

def reply(tcpSerSock):
    while True:
        data = tcpCliSock.recv(BUFSIZ)
        print(tcpCliSock.getpeername())
        if not data:
            break
        #tcpCliSock.send('[%s] %s' % (bytes(ctime(), 'utf-8'), data))
        tcpCliSock.send(bytes('[%s] %s' % (ctime(), data.decode('utf-8')), 'utf-8'))

    tcpCliSock.close()

HOST = ''
PORT = 21562
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)
    _thread.start_new_thread(reply, (tcpSerSock, ))
    
tcpSerSock.close()
