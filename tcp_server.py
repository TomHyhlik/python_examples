#!/usr/bin/env python

import socket
 
######################
# TCP_IP = '127.0.0.1'
TCP_IP = '192.168.200.51'
TCP_PORT = 11994
######################




print('AppStart....................................')
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((TCP_IP, TCP_PORT))
except:
    print('ERROR: Failed to bind', TCP_IP, ':', TCP_PORT,
    '\nProbably the port is used by another program')
    exit(0)

s.listen(1)
    
while 1:

    conn, addr = s.accept()

    print('Connected Client:', addr)

    while 1:
        data = conn.recv(1024)
        if not data: break
        print ("received data:", data)
        # conn.send(data)  # echo
        # conn.close()
    print('Closed connection to Client:', addr)




