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
    sock.send('Hello, I have no name'.encode())
    data = sock.recv(1024)
    assert data == ('Go away'.encode())
    sock.close()