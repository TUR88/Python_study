import pytest
import socket as s


@pytest.fixture
def socket(request):
    _socket = s.socket(s.AF_INET, s.SOCK_STREAM)

    def socket_teardown():
        _socket.close()
    request.addfinalizer(socket_teardown)
    return _socket


class Fte:
    def __init__(self, message):
        self.message = message

    def test_server_data_check(self):
        sock = s.socket()
        sock.connect(('localhost', 9090))
        sock.send('Hello, my name is Sergey'.encode())
        data = sock.recv(4096)
        assert data == self.message
        sock.close()


f = Fte('Nice to meet you!')
f.test_server_data_check()
