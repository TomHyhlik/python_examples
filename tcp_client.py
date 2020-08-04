import socket
import time

######################
# TCP_IP = '127.0.0.1'
TCP_IP = '192.168.200.51'
TCP_PORT = 11997
######################

 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))


i = 0
while (1):

    MESSAGE = "SampleMessage_%i" % (i)
    i += 1

    s.send(MESSAGE.encode())
    time.sleep(1)



# data = s.recv(1024)
# s.close()
# print("Received:", data)