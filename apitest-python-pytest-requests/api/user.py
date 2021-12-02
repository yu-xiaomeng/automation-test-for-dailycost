import os
from core.rest_client import RestClient
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
setting_config = data.load_ini(data_file_path)
api_root_url = setting_config["host"]["api_root_url"]
proxy = setting_config["host"]["proxy"]


class User(RestClient):
    def __init__(self, api_root_url, proxy,**kwargs):
        super(User, self).__init__(api_root_url, proxy, **kwargs)

    def register(self, **kwargs):
        return self.post("/user", **kwargs)
    
    def login(self, **kwargs):
        return self.post("/login", **kwargs)

user = User(api_root_url, proxy)
