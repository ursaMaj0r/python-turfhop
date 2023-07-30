from . import requests
from . import cfg

class Job(object):
    def __init__(self, id=None,**kwargs):
        self.id = id
        self.query=kwargs

    def info(self):
        path = 'https://turfhop.com/api/jobs/get?id={}'.format(self.id)
        response = requests.get(path)
        return response.json()['Result']['Job']
    
    def items(self):
        path = 'https://turfhop.com/api/jobs/getlineitems?jobId={}'.format(self.id)
        response = requests.get(path)
        return response.json()['Result']
    
    def all(self):
        path = 'https://turfhop.com/api/jobs/getall?companyId={}'.format(cfg['turfhop']['TH_COMPANY_ID'])
        response = requests.get(path,params=self.query)
        return response.json()['Result']['Jobs']