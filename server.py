import socket
import os
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip=''
s.bind((ip,9879))
s.listen(4)
socketclient,addr=s.accept()
print("Got connection from",addr)
con=True
while con:
    msg=socketclient.recv(1024).decode()
    print("Client=>",msg)
    if msg=='shutdown':
        os.system("shutdown /s /t 1")
    elif msg=='quit':
        s.close()
    else:
        msg=input('Enter your message')
        msg=bytes(msg,'utf-8')
        socketclient.send(msg)
        