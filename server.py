import socket  # импортируем библиотеку


while True:
    sock = socket.socket()  # cоздаем переменную sock
    sock.bind(('', 9090))  # задаем номер порта и хост
    sock.listen(10)
    conn, addr = sock.accept()  # соединяемся, присваиваимваем ip-адрес

    print('connected:', addr)
    data = conn.recv(1024)  # присваеиваем переменной полученные данные
    print(data)  # выводим данные на печать
    if data == ('Hello, my name is Sergey'.encode()):
        conn.send('Nice to meet you!'.encode())
    else:
        conn.send('Go away'.encode())  # высылаем другой ответ
