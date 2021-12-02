import pytest
import requests
from operation.user import login_user

@pytest.mark.parametrize('name, password',[('yuxiaomeng','20211030')])
def test_login(name, password):
    url = 'http://127.0.0.1:8080'
    payload = {'username': name, 'password': password}
    headers = {'Content-Type': 'application/json'}
    proxy = {'http':'http://127.0.0.1:8081'}
    r = requests.post(url+'/login', json=payload, proxies=proxy,headers=headers)
    assert r.status_code == 200

@pytest.mark.parametrize('username, password',[('yuxiaomeng','20211030.y')])
def test_login_2(username, password):
    result = login_user(username, password)
    assert result.response.status_code == 200
    assert result.success
    assert result.token

