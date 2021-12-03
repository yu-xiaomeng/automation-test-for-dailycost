from pytest import mark
from operation.user import login_user

@mark.user
class TestUserLogin():
    @mark.smoke
    @mark.parametrize('username, password',[('yuxiaomeng','20211030.y')])
    def test_login_success(self,username, password):
        result = login_user(username, password)
        assert result.status_code == 200
        assert result.data["token"]

