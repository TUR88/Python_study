import socket #импортируем библиотеку socket

sock = socket.socket() #создаем переменную sock ссылающуюся на параметр socket
sock.bind(('', 9090)) #задаем номер порта и хост. В данной программе и клиент, и сервер находились на одной машине.
sock.listen(3)
conn, addr = sock.accept() #соединяемся, присваиваимваем ip-адрес соединенного клиента и выводим на печать

print('connected:', addr)

while True:
    data = conn.recv(4096) #присваеиваем переменной полученные от клиента данные, указываем объем данных, ожидаем прием
    if not data:
        break
    print(data) #выводим данные на печать
    if data == ('Hello, my name is Sergey'.encode()): #если принятые данные равно одной величине высылаем один ответ
        conn.send('Nice to meet you!'.encode())
    else:
        conn.send('Go away'.encode()) #если принятые данные не равны данной величине высылвем другой ответ

conn.close() #закрываем соединение
