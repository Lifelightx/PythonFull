import socket

import time as t

host = "http://127.0.0.1"
port  = 5000

s = socket.socket()

s.bind((host,port))
s.listen(1)
c, addr = s.accept()
print("Connection from: ", addr)

c.send(b"Hello I am The server Nice to meet you")
t.sleep(5)
msg = "Bye"
c.send(msg.encode())
c.close()