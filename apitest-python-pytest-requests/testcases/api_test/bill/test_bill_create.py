from pytest import mark
from operation.bill import bill_create
from testcases.conftest import api_data

import allure

@mark.bill
class TestBillDetailsCreate():
    @mark.smoke
    @mark.parametrize('category_id, type, amount, note, date, status_code, message', 
                    api_data["test_bill_create_success"])
    def test_bill_create_success(self, category_id, type, amount, note, date, status_code, message, token):
        result = bill_create(category_id, type, amount, note, date, token)
        assert result.response.status_code == status_code
        assert result.message == message
        assert result.response.json()["data"]["id"]

    @mark.desp
    @allure.title("{description}")
    @mark.parametrize('description, category_id, type, amount, note, date, status_code, message', 
                    api_data["test_bill_create_param_validate_success"])
    def test_bill_create_param_validate_success(self, description, category_id, type, amount, note, date, status_code, message, token):
        result = bill_create(category_id, type, amount, note, date, token)
        assert result.response.status_code == status_code
        assert result.message == message