import pytest
import requests
from operation.user import login_user

@pytest.mark.parametrize('username, password',[('yuxiaomeng','20211030.y')])
def test_login(username, password):
    result = login_user(username, password)
    assert result.response.status_code == 200
    assert result.success
    assert result.token

