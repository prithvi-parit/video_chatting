import cv2
import socket
s=socket.socket()
serverip="127.0.0.1"
serverport=2222
s.connect((serverip,serverport))
c=cv2.VideoCapture(0)
while True:
    c=cv2.VideoCapture(0)
    while(c.isOpened()):
        ret, photo = c.read()
        value = cv2.imencode('.jpg', photo)[1].tostring()
        s.sendall(value)
