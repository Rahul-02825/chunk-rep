import socket
s=socket.socket()
s.connect(("localhost",5566))

tm=s.recv(1024).decode()

print(tm)

s.close()