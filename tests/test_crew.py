# tests/test_crews.py
from pytest import fixture
from thapi import *
import vcr
from . import cfg

@fixture
def crew_keys():
    # Responsible only for returning the test data
    return ['Id', 'CompanyId', 'Name']

@vcr.use_cassette('tests/vcr_cassettes/crew-info.yml')
def test_crew_info(crew_keys):
    """Tests an API call to get a Crew info"""

    crew_instance = Crew(cfg['test_ids']['crew'])
    response = crew_instance.info()

    assert isinstance(response, dict)
    assert response['Id'] == cfg['test_ids']['crew'], "The ID should be in the response"
    assert set(crew_keys).issubset(response.keys()), "All keys should be in the response"

@vcr.use_cassette('tests/vcr_cassettes/crews.yml')
def test_all_crews():
    crews = Crew()
    response = crews.all()
    print(type(response))
    assert isinstance(response, list)
    assert response[0]['CompanyId'] == cfg['turfhop']['TH_COMPANY_ID']