import pytest
from operation.user import login_user
from testcases.conftest import api_data

@pytest.fixture(scope='module')
def token():
    token = login_user('yuxiaomeng', '20211030.y').data["token"]
    return token

@pytest.fixture(scope="function")
def testcase_data(request):
    testcase_name = request.function.__name__
    return api_data.get(testcase_name)
