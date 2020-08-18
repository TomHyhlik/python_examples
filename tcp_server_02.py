#!/usr/bin/env python

# use command bellow to free the tcp port 11999 on linux
# sudo fuser -k 11999/tcp

import socket
import time
from datetime import datetime
import atexit

######################
TCP_PORT = 11999
######################

print('AppStart....................................')
 
def getMyIpAddr():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    MyIpAddr = s.getsockname()[0]
    s.close()
    return MyIpAddr

def writeToFile(fileData):
    f = open(fileName,"a+")
    f.write(fileData)
    f.close()

# utility to close socket when program is terminated
global conn
def exit_handler():
    conn.close()
    print("Socked closed")
atexit.register(exit_handler)


### create file name for the log
now = datetime.now()
# dt_string = now.strftime("%d-%m-%Y_%H:%M:%S")
dt_string = now.strftime("%Y_%m-%d")
fileName = "./logs/log_" + dt_string + ".txt"


# get the server IP Address automatically or manually
TCP_IP = getMyIpAddr()
# TCP_IP = '192.168.200.51'         

### create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((TCP_IP, TCP_PORT))
except:
    print('ERROR: Failed to bind', TCP_IP, ':', TCP_PORT,
    '\nProbably the port is used by another program.\nOn Linux you can try to free the port by running \n"sudo fuser -k 11999/tcp"')
    exit(0)
s.listen(1)
    

while 1:
    conn, addr = s.accept()
    print('Connected Client:', addr)

    while 1:
        data = conn.recv(1024).decode()
        if not data: break
        print (data, end='')
        writeToFile(data)
        # conn.send(data)  # echo
        # conn.close()
    print('Closed connection to Client:', addr)




