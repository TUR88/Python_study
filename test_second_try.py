import pytest
import socket as s


class TestClass:

    @pytest.fixture
    def socket(request):
        _socket = s.socket(s.AF_INET, s.SOCK_STREAM)

        def socket_teardown():
            _socket.close()

        request.addfinalizer(socket_teardown)
        return _socket

    def test_server_connect(socket):  # проверяем наличие связи
        sock = s.socket()
        sock.connect(('localhost', 9090))
        assert socket

    def test_server_data_check_true(self):
        sock = s.socket()
        sock.connect(('localhost', 9090))
        sock.send('Hello, my name is Sergey'.encode())
        data = sock.recv(1024)
        assert data == ('Nice to meet you!'.encode())
        sock.close()

    def test_server_data_check_false(self):
        sock = s.socket()
        sock.connect(('localhost', 9090))
        sock.send('Hello, I have NO name'.encode())
        data = sock.recv(1024)
        assert data == ('Go away'.encode())
        sock.close
