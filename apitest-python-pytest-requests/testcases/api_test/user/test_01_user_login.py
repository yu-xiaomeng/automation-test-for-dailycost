from pytest import mark
from operation.user import login_user
import allure

@mark.user
class TestUserLogin():
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("用户登陆成功")
    @allure.title("已注册用户使用正确的用户名和密码登陆成功：{username}/{password}")
    @mark.smoke
    @mark.parametrize('username, password',[('yuxiaomeng','20211030.y')])
    def test_login_success(self,username, password):
        result = login_user(username, password)
        assert result.status_code == 200
        assert result.data["token"]

