from core.result_base import ResultBase
from api.bill import bill

def bill_create(category_id, type, amount, note, date, token):
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
    res = bill.create_new_bill(json=payload, headers=header)
    
    return ResultBase(res)

def bill_get_by_id(id, token):
    
    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
    }
    res = bill.get_bill_by_id(id, headers=header)

    return ResultBase(res)

def one_month_bill_list_get_by_date(date, token):
    
    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
    }
    param = {"date": date}
    res = bill.get_bill_list(params=param, headers=header)

    return ResultBase(res)

def bill_monthly_stat(date, token):
    
    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
    }
    param = {"date": date}
    res = bill.get_bill_monthly(params=param, headers=header)

    return ResultBase(res)