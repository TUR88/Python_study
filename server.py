import socket   # импортируем библиотеку
sock = socket.socket()  # cоздаем переменную sock
sock.bind(('', 9090))  # задаем номер порта и хост
sock.listen(3)
conn, addr = sock.accept()  # соединяемся, присваиваимваем ip-адрес

print('connected:', addr)

while True:
    data = conn.recv(4096)  # присваеиваем переменной полученные данные
    if not data:
        break
    print(data)  # выводим данные на печать
    if data == ('Hello, my name is Sergey'.encode()):
        conn.send('Nice to meet you!'.encode())
    else:
        conn.send('Go away'.encode())  # высылаем другой ответ

conn.close()  # закрываем соединение
