from . import requests
from . import cfg

class Event(object):
    def __init__(self, id=None):
        self.id = id

    def info(self):
        path = 'https://turfhop.com/api/events/get?id={}'.format(self.id)
        response = requests.get(path)
        return response.json()['Result']

    def all(self):
        path = 'https://turfhop.com/api/events/getall?jobId={}'.format(self.id)
        response = requests.get(path)
        return response.json()['Result']

