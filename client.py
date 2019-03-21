import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
sock.send('Hello, my name is Sergey'.encode())

data = sock.recv(1024)
sock.close()

print (data)