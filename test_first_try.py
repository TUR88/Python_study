import pytest
import socket as s                # импортируем библиотеку socket, присваиваем переменной s


@pytest.fixture                   # запускаем фикстуру pytest
def socket(request):              # создаем функцию socket
    _socket = s.socket(s.AF_INET, s.SOCK_STREAM)

    def socket_teardown():        # создаем функцию socket_teardown
        _socket.close()
    request.addfinalizer(socket_teardown)
    return _socket


def test_server_connect(socket):   # проверяем наличие связи
    socket.connect(('localhost', 9090))
    assert socket
