from . import requests
from . import cfg

class Invoice(object):
    def __init__(self, id=None,**kwargs):
        self.id = id
        self.query=kwargs
        
    def info(self):
        path = 'https://turfhop.com/api/invoices/get?id={}'.format(self.id)
        response = requests.get(path)
        return response.json()['Result']['Invoice']

    def all(self):
        path = 'https://turfhop.com/api/invoices/getall?companyId={}'.format(cfg['turfhop']['TH_COMPANY_ID'])
        response = requests.get(path,params=self.query)
        return response.json()['Result']['Invoices']

