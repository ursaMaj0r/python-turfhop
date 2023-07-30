import os
import requests
import configparser

cfg = configparser.ConfigParser()
cfg.read('config.ini')

TH_COMPANY_ID = cfg['turfhop']['TH_COMPANY_ID']

class CompanyIdMissingError(Exception):
    pass

if TH_COMPANY_ID is None:
    raise CompanyIdMissingError(
        "All methods require a company ID."
    )

from .customer import *
from .crew import *
from .employee import *
from .event import *
from .form import *
from .location import *
from .invoice import *
from .vendor import *
from .job import *
from .asset import *
from .product import *