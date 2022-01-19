import os
from core.rest_client import RestClient
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
setting_config = data.load_ini(data_file_path)
api_root_url = setting_config["host"]["api_root_url"]
proxy = setting_config["host"]["proxy"]


class Bill(RestClient):
    def __init__(self, api_root_url, proxy, **kwargs):
        super(Bill, self).__init__(api_root_url, proxy, **kwargs)

    def create_new_bill(self, **kwargs):
        return self.post("/bill", **kwargs)
    
    def get_bill_list(self, **kwargs):
        return self.get("/bill/list", **kwargs)
    
    def get_bill_by_id(self, id, **kwargs):
        return self.get("/bill/{}".format(id), **kwargs)
    
    def update_bill(self, **kwargs):
        return self.put("/bill", **kwargs)

    def delete_bill_details_by_id(self, id, **kwargs):
        return self.delete("/bill/{}".format(id), **kwargs)

    def get_bill_monthly(self, **kwargs):
        return self.get("/bill/stat/monthly", **kwargs)


bill = Bill(api_root_url, proxy)