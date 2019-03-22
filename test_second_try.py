import pytest


@pytest.fixture
def test_server_connect(socket):
    socket.connect(('localhost', 9090))
    assert socket
