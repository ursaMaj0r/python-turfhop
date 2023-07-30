# tests/test_forms.py
from pytest import fixture
from thapi import *
import vcr
from . import cfg

@fixture
def form_keys():
    # Responsible only for returning the test data
    return ['Id', 'CompanyId', 'Type']

@vcr.use_cassette('tests/vcr_cassettes/form-info.yml')
def test_form_info(form_keys):
    """Tests an API call to get a Form info"""

    form_instance = Form(cfg['test_ids']['form'])
    response = form_instance.info()

    assert isinstance(response, dict)
    assert response['Id'] == cfg['test_ids']['form'], "The ID should be in the response"
    assert set(form_keys).issubset(response.keys()), "All keys should be in the response"

@vcr.use_cassette('tests/vcr_cassettes/forms.yml')
def test_all_forms():
    forms = Form()
    response = forms.all()
    print(type(response))
    assert isinstance(response, list)
    assert response[0]['CompanyId'] == cfg['turfhop']['TH_COMPANY_ID']