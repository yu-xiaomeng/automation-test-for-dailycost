from core.result_base import ResultBase
from api.user import user

def login_user(username, password):
    
    payload = {
        "username": username,
        "password": password
    }
    header = {
        "Content-Type": "application/json"
    }
    res = user.login(json=payload, headers=header)

    return ResultBase(res)