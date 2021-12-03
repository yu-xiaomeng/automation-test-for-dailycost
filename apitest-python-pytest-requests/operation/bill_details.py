import json
from core.result_base import ResultBase
from api.bill_details import bill_details

def bill_details_create(category_id, type, amount, note, date, token):
    """
    记一笔
    :param category_id: 类别
    :param type: 支出/收入
    :param amount: 金额
    :param note: 备注
    :param date: 日期 
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase
    payload = {
        "categoryId": category_id,
        "type": type,
        "amount": amount,
        "note": note,
        "date": date
    }
    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
    }
    res = bill_details.create_new_bill_details(json=payload, headers=header)
    result.success = False
    if res.json()["code"] == 100:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.message = res.json()["message"]
    result.response = res
    return result

def bill_details_get_by_id(id, token):
    """
    记一笔
    :param id: 账单明细id
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase
    
    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
    }
    res = bill_details.get_bill_details_by_id(id, headers=header)
    result.success = False
    if res.json()["code"] == 100:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.message = res.json()["message"]
    result.response = res
    return result