from . import requests
from . import cfg

class Vendor(object):
    def __init__(self, id=None,**kwargs):
        self.id = id
        self.query=kwargs

    def info(self):
        path = 'https://turfhop.com/api/vendors/get?id={}'.format(self.id)
        response = requests.get(path)
        return response.json()['Result']['Vendor']
    
    def all(self):
        path = 'https://turfhop.com/api/vendors/getall?companyId={}'.format(cfg['turfhop']['TH_COMPANY_ID'])
        response = requests.get(path,params=self.query)
        return response.json()['Result']['Vendors']