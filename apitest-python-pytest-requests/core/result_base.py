from requests.models import Response

class ResultBase():
    def __init__(self, res):
        self.response = res
        self.status_code = res.status_code
        self.code = res.json()["code"]
        self.message = res.json()["message"]
        self.data = res.json()["data"]
        