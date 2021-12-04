from pytest import mark
from operation.bill_details import bill_details_get_by_id

@mark.bill
class TestBillDetailsGetById():
    @mark.smoke
    @mark.parametrize('id, status_code, message',[
        ("596d6ded-db59-4720-a41b-b0ce3019ac8e", 200, "操作成功")
        ])
    def test_bill_details_get_by_id_success(self, id, status_code, message, token):
        result = bill_details_get_by_id(id, token)
        
        assert result.status_code == status_code
        assert result.message == message
        assert result.data["id"] == id
        assert result.data["categoryId"] == "5442d3b8-9d4a-4654-bf0b-d2249efef190"
        assert result.data["amount"] == 3.31
        assert result.data["date"] == "2021-12-01"

                
    @mark.parametrize('id, status_code, message',[
        ("2bd10457-24ea-4eb8-8cc9-6de46ddd178a", 400, "无权访问该数据"),
        ("596d6ded-db59-4720-a41b-b0ce3019ac8ef", 400, "ID不存在")
        ])
    def test_bill_details_get_by_id_param_validate(self, id, status_code, message, token):
        result = bill_details_get_by_id(id, token)
        assert result.status_code == status_code
        assert result.message == message