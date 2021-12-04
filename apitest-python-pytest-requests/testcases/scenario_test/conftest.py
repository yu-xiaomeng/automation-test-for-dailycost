import pytest

@pytest.fixture(scope='session')
def core_env():
    return {"date": "2021-11"}