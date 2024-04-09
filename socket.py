import socket
import time

ss=socket.socket()

ss.bind(("localhost",5566))
ss.listen(5)


while True:
    conn,addr=ss.accept()
    print("Got connection ",str(addr))
    cur_time=time.ctime(time.time()) + "\r\n"
    conn.send(cur_time.encode())
    conn.close()