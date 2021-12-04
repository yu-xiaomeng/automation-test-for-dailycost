from _pytest.fixtures import fixture
import allure
import pytest
from operation.user import login_user
from operation.bill_details import bill_details_one_month_list_by_date, bill_monthly_stat

@pytest.mark.core
class TestCoreScenario:

    @allure.title("01: user[yuxiaomeng] login")
    @allure.story('story_1')
    def test_user_login(self, core_env):
        result = login_user('yuxiaomeng', '20211030.y')
        assert result.status_code == 200
        assert result.data["token"]
        core_env["token"] = result.data["token"]

    @allure.title("02: get homepage info - bill details list")
    @allure.story('story_1')
    def test_get_current_month_monthly_bill_list(self, core_env):
        result = bill_details_one_month_list_by_date(core_env["date"], core_env["token"])
        assert result.status_code == 200
        assert len(result.data) == 2
        assert result.data[0]["date"] == "2021-11-11"
        assert result.data[0]["expense"] == 510.5

    @allure.title("03: get homepage info - bill monthly statistics ")
    @allure.story('story_1')
    def test_get_current_month_bill(self, core_env):
        result = bill_monthly_stat(core_env["date"], core_env["token"])
        assert result.status_code == 200
        assert result.data["expense"]
    
