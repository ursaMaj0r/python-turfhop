from . import requests
from . import cfg

class Customer(object):
    def __init__(self, id=None,**kwargs):
        self.id = id
        self.query=kwargs

    def info(self):
        path = 'https://turfhop.com/api/customers/get?id={}'.format(self.id)
        response = requests.get(path)
        return response.json()['Result']['Customer']
    
    def all(self):
        path = 'https://turfhop.com/api/customers/getall?companyId={}'.format(cfg['turfhop']['TH_COMPANY_ID'])
        response = requests.get(path,params=self.query)
        return response.json()['Result']['Customers']