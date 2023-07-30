from . import requests
from . import cfg

class Product(object):
    def __init__(self, id=None):
        self.id = id

    def info(self):
        path = 'https://turfhop.com/api/products/get?id={}'.format(self.id)
        response = requests.get(path)
        return response.json()['Result']['Product']
    
    def all(self):
        path = 'https://turfhop.com/api/products/getall?companyId={}'.format(cfg['turfhop']['TH_COMPANY_ID'])
        response = requests.get(path)
        return response.json()['Result']['Products']