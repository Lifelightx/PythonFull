import socket

host = 'localhost'
port = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))
print("udp server is running..")


msg, addr  = s.recvfrom(1024)
print("Msg to server: ", msg.decode())
msg,addr = s.recvfrom(1024)
print(addr)
i = 0
while i<10:
    smsg = f"I am the sever sending msg to client {i}"
    i = i +1
    s.sendto(smsg.encode(),addr)
    

