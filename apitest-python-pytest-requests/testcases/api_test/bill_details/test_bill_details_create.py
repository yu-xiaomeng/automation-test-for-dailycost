from pytest import mark
from operation.bill_details import bill_details_create

@mark.bill
class TestBillDetailsCreate():
    @mark.skip
    @mark.smoke
    @mark.parametrize('category_id, type, amount, note, date, status_code, message', [
        ('5442d3b8-9d4a-4654-bf0b-d2249efef190', 'EXPENSE', 100.01, "note1111test", "2021-12-01", 200, "操作成功")
        ])
    def test_bill_details_create_success(self, category_id, type, amount, note, date, status_code, message, token):
        result = bill_details_create(category_id, type, amount, note, date, token)
        assert result.response.status_code == status_code
        assert result.message == message
        assert result.response.json()["data"]["id"]

    @mark.parametrize('category_id, type, amount, note, date, status_code, message', [
        ('66c22fad-be9d-481d-a445-c57d266bf937', 'INCOME', 100.01, "note1111test", "2021-12-01", 400, "类别ID不存在"), # 无权访问该数据
        ('5442d3b8-9d4a-4654-bf0b-d2249efef190f', 'INCOME', 100.01, "note1111test", "2021-12-01", 400, "类别ID不存在"),
        ('5442d3b8-9d4a-4654-bf0b-d2249efef190', 'MYTYPE', 100.01, "note1111test", "2021-12-01", 400, "type must be EXPENSE or INCOME"),
        ('5442d3b8-9d4a-4654-bf0b-d2249efef190', 'INCOME', 100.01, "note1111test", "2021-12-01", 400, "记账类别不匹配"),
        ('5442d3b8-9d4a-4654-bf0b-d2249efef190', 'EXPENSE', -1, "note1111test", "2021-12-01", 400, "amount must be greater than or equal to 0.0"),
        ])
    def test_bill_details_create_param_validate_success(self, category_id, type, amount, note, date, status_code, message, token):
        result = bill_details_create(category_id, type, amount, note, date, token)
        assert result.response.status_code == status_code
        assert result.message == message