import pytest
from operation.bill_details import bill_details_create, bill_details_get_by_id

@pytest.mark.bill
class TestBillDetails():
    @pytest.mark.parametrize('category_id, type, amount, note, date, status_code, message', [
        # ('5442d3b8-9d4a-4654-bf0b-d2249efef190', 'EXPENSE', 100.01, "note1111test", "2021-12-01", 200, "操作成功"),
        ('5442d3b8-9d4a-4654-bf0b-d2249efef190', 'INCOME', 100.01, "note1111test", "2021-12-01", 400, "记账类别不匹配")
        ])
    def test_bill_details_create(self, category_id, type, amount, note, date, status_code, message, token):
        result = bill_details_create(category_id, type, amount, note, date, token)
        assert result.response.status_code == status_code
        assert result.message == message

    @pytest.mark.parametrize('id, status_code, message',[
        ("596d6ded-db59-4720-a41b-b0ce3019ac8e", 200, "操作成功"),
        ("2bd10457-24ea-4eb8-8cc9-6de46ddd178a", 400, "无权访问该数据")
        ])
    def test_bill_details_get_by_id(self, id, status_code, message, token):
        result = bill_details_get_by_id(id, token)
        assert result.response.status_code == status_code
        assert result.message == message
