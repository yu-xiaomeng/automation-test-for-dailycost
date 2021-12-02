import pytest
from operation.bill_details import bill_details_create


@pytest.mark.parametrize('category_id, type, amount, note, date', [('5442d3b8-9d4a-4654-bf0b-d2249efef190', 'EXPENSE', 100.01, "note1111test", "2021-12-01")])
def test_bill_details_create(category_id, type, amount, note, date):
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ5dXhpYW9tZW5nIiwiZXhwIjoxNjM4NDIxNjI4fQ.Gci8e4aXmtUcMpgCHPgImglN7EuDQuRtAeJu7GLi4apZzBNQMkVKxOQqaNbImhDuKvZLrHcC1OT56H_K63TTTw"
    result = bill_details_create(category_id, type, amount, note, date, token)
    assert result.response.status_code == 401
    assert result.success == False