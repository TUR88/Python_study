import pytest
import socket as s


@pytest.fixture
def socket(request):
    _socket = s.socket(s.AF_INET, s.SOCK_STREAM)

    def socket_teardown():
        _socket.close()
    request.addfinalizer(socket_teardown)
    return _socket


def test_server_data_check(socket):
    sock = s.socket()
    sock.connect(('localhost', 9090))
    sock.send('Hello, my name is Sergey'.encode())
    data = sock.recv(1024)
    assert data == ('Nice to meet you!'.encode())
    sock.close()
