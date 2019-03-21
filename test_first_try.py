import pytest
import socket as s


@pytest.fixture

def test_server_connect(socket):
    socket.connect(('localhost', 9090))
    assert socket