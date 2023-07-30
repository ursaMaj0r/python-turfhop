# tests/test_events.py
from pytest import fixture
from thapi import *
import vcr

@fixture
def event_keys():
    # Responsible only for returning the test data
    return ['Id', 'CompanyId', 'DateCreated', 'JobId',
              'AllDay']

@vcr.use_cassette('tests/vcr_cassettes/event-info.yml')
def test_event_info(event_keys):
    """Tests an API call to get a Event info"""

    event_instance = Event(cfg['test_ids']['event'])
    response = event_instance.info()

    assert isinstance(response, dict)
    assert response['Id'] == cfg['test_ids']['event'], "The ID should be in the response"
    assert set(event_keys).issubset(response.keys()), "All keys should be in the response"

@vcr.use_cassette('tests/vcr_cassettes/events.yml')
def test_all_events():
    events = Event(cfg['test_ids']['job'])
    response = events.all()
    print(type(response))
    assert isinstance(response, list)
    assert response[0]['Precipitation'] == 0