# tests/test_assets.py
from pytest import fixture
from thapi import *
import vcr

@fixture
def asset_keys():
    # Responsible only for returning the test data
    return ['Id', 'CompanyId', 'Type', 'Status']

@vcr.use_cassette('tests/vcr_cassettes/asset-info.yml')
def test_asset_info(asset_keys):
    """Tests an API call to get a Asset info"""

    asset_instance = Asset(cfg['test_ids']['asset'])
    response = asset_instance.info()

    assert isinstance(response, dict)
    assert response['Id'] == cfg['test_ids']['asset'], "The ID should be in the response"
    assert set(asset_keys).issubset(response.keys()), "All keys should be in the response"

@vcr.use_cassette('tests/vcr_cassettes/assets.yml')
def test_all_assets():
    assets = Asset()
    response = assets.all()
    print(type(response))
    assert isinstance(response, list)
    assert response[0]['CompanyId'] == cfg['turfhop']['TH_COMPANY_ID']