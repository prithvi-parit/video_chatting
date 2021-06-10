import socket
import cv2
import numpy
s=socket.socket()
port=2222
ip=""
s.bind((ip,port))
s.listen()
info,addr=s.accept()
while True:
    data_value=info.recv(90496)
    array_value=numpy.frombuffer(data_value,numpy.uint8)
    photo=cv2.imdecode(array_value,cv2.IMREAD_COLOR)
    if photo is not None:
        cv2.imshow('video',photo)
        cv2.waitKey(10)
    else:
        pass
cv2.destroyAllWindows()
