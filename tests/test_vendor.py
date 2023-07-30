# tests/test_vendors.py
from pytest import fixture
from thapi import *
import vcr

@fixture
def vendor_keys():
    # Responsible only for returning the test data
    return ['Id', 'CompanyId', 'Name', 'State']

@vcr.use_cassette('tests/vcr_cassettes/vendor-info.yml')
def test_vendor_info(vendor_keys):
    """Tests an API call to get a Vendor info"""

    vendor_instance = Vendor(cfg['test_ids']['vendor'])
    response = vendor_instance.info()

    assert isinstance(response, dict)
    assert response['Id'] == cfg['test_ids']['vendor'], "The ID should be in the response"
    assert set(vendor_keys).issubset(response.keys()), "All keys should be in the response"

@vcr.use_cassette('tests/vcr_cassettes/vendors.yml')
def test_all_vendors():
    vendors = Vendor()
    response = vendors.all()
    print(type(response))
    assert isinstance(response, list)
    assert response[0]['Active'] == True