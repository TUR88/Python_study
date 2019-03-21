import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

print('connected:', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    print(data)
    if data == ('Hello, my name is Sergey'.encode()):
        conn.send('Nice to meet you!'.encode())
    else:
        conn.send('Go away'.encode())

conn.close()
