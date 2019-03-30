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
    def __init__(self, sock):
        self.sock = sock

    def test_server_connect(self):
        self.sock.connect('localhost', 9090)
        assert self.sock


f = Fte(socket())
f.test_server_connect()
