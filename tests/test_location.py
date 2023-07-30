# tests/test_locations.py
from pytest import fixture
from thapi import *
import vcr
from . import cfg

@fixture
def location_keys():
    # Responsible only for returning the test data
    return ['Id', 'CompanyId', 'TaxRate']

@vcr.use_cassette('tests/vcr_cassettes/location-info.yml')
def test_location_info(location_keys):
    """Tests an API call to get a Location info"""

    location_instance = Location(cfg['test_ids']['location'])
    response = location_instance.info()

    assert isinstance(response, dict)
    assert response['Id'] == cfg['test_ids']['location'], "The ID should be in the response"
    assert set(location_keys).issubset(response.keys()), "All keys should be in the response"

@vcr.use_cassette('tests/vcr_cassettes/locations.yml')
def test_all_locations():
    locations = Location()
    response = locations.all()
    print(type(response))
    assert isinstance(response, list)
    assert response[0]['CompanyId'] == cfg['turfhop']['TH_COMPANY_ID']