import os
from core.rest_client import RestClient
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]


class BillDetails(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(BillDetails, self).__init__(api_root_url, **kwargs)

    def create_new_bill_details(self, **kwargs):
        return self.post("/bill/details", **kwargs)
    
    def get_bill_details_list(self, **kwargs):
        return self.get("/bill/details/list", **kwargs)
    
    def get_bill_details_by_id(self, id, **kwargs):
        return self.get("/bill/details/{}".format(id), **kwargs)
    
    def update_bill_details(self, **kwargs):
        return self.put("/bill/details", **kwargs)

    def delete_bill_details_by_id(self, id, **kwargs):
        return self.delete("/bill/details/{}".format(id), **kwargs)


bill_details = BillDetails(api_root_url)