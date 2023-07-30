from . import requests
from . import cfg

class Asset(object):
    def __init__(self, id=None,**kwargs):
        self.id = id
        self.query=kwargs

    def info(self):
        path = 'https://turfhop.com/api/trackableassets/get?id={}'.format(self.id)
        response = requests.get(path)
        return response.json()['Result']['TrackableAsset']
    
    def all(self):
        path = 'https://turfhop.com/api/trackableassets/getall?companyId={}'.format(cfg['turfhop']['TH_COMPANY_ID'])
        response = requests.get(path,params=self.query)
        return response.json()['Result']['TrackableAssets']