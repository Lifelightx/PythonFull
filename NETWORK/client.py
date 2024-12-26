import socket


host = 'localhost'
port = 5000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind((host,port))
s.connect((host,port))

msg = s.recv(1024)
while msg:
    print("Recieved: "+ msg.decode())
    msg = s.recv(1024)
s.close()
