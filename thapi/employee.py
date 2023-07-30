from . import requests
from . import cfg

class Employee(object):
    def __init__(self, id=None):
        self.id = id

    def info(self):
        path = 'https://turfhop.com/api/employees/get?id={}'.format(self.id)
        response = requests.get(path)
        return response.json()['Result']['Employee']

    def all(self):
        path = 'https://turfhop.com/api/employees/getall?companyId={}'.format(cfg['turfhop']['TH_COMPANY_ID'])
        response = requests.get(path)
        return response.json()['Result']

