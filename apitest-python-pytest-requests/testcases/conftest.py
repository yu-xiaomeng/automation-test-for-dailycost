import pytest
from operation.user import login_user

@pytest.fixture(scope='session')
def token():
    token = login_user('yuxiaomeng', '20211030.y').data["token"]
    return token
