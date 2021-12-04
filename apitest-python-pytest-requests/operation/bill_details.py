from core.result_base import ResultBase
from api.bill_details import bill_details

def bill_details_create(category_id, type, amount, note, date, token):
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
    
    return ResultBase(res)

def bill_details_get_by_id(id, token):
    
    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
    }
    res = bill_details.get_bill_details_by_id(id, headers=header)

    return ResultBase(res)

def bill_details_one_month_list_by_date(date, token):
    
    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
    }
    param = {"date": date}
    res = bill_details.get_bill_details_list(params=param, headers=header)

    return ResultBase(res)

def bill_monthly_stat(date, token):
    
    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
    }
    param = {"date": date}
    res = bill_details.get_bill_monthly(params=param, headers=header)

    return ResultBase(res)