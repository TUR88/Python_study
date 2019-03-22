import pytest

@pytest.fixture()
def test_strings_a_3():
    print ("test a*3")
    assert 'a'*3 == 'aaa'