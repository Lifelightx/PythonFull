import socket

host  = 'localhost'
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.sendto(b"Msg from client to server: ",(host,port))
msg = "Nothing happening on India"
s.sendto(msg.encode(),(host,port))

i = 0
res, addr = s.recvfrom(1024)
while res:
    print("msg recieved from server: ", res.decode())
    res, addr = s.recvfrom(1024)
