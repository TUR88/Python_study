import pytest
import socket as s


class TestE:
    def __init__(self, message):
        self.message = message

    @pytest.fixture
    def socket(self, request):
        _socket = s.socket(s.AF_INET, s.SOCK_STREAM)

        def socket_teardown():
            _socket.close()
        request.addfinalizer(socket_teardown)
        return _socket

    def test_server_data_check(self):
        sock = s.socket()
        sock.connect(('localhost', 9090))
        sock.send('Hello, my name is '.encode())
        data = sock.recv(4096)
        data = str(data, 'utf-8')
        assert data == self.message
        sock.close()


f = TestE('Go Away')
f.test_server_data_check()
