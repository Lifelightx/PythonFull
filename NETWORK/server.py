import socket

import time as t

host = "localhost"
port  = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host,port))
s.listen(1)
c, addr = s.accept()
print("Connection from: ", addr)

c.send(b"Hello I am The server Nice to meet you")
t.sleep(5)
msg = "Bye"
c.send(msg.encode())
c.close()