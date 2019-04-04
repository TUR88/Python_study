import pytest
import socket as s

sock = s.socket()
sock.connect(('localhost', 9090))


class TestClass1:

    @pytest.fixture
    def socket(request):
        _socket = s.socket(s.AF_INET, s.SOCK_STREAM)

        def socket_teardown():
            _socket.close()

        request.addfinalizer(socket_teardown)
        return _socket

    def test_server_connect(socket):
        assert socket


class TestClass2:
    def test_server_data_check_true(self):
        sock.send('Hello, my name is Sergey'.encode())
        data = sock.recv(1024)
        assert data == ('Nice to meet you!'.encode())
        sock.close()


class TestClass3:
    def test_server_data_check_false(self):
        sock.send('Nice to meet you!'.encode())
        data = sock.recv(1024)
        assert data == ('Go away'.encode())
        sock.close
