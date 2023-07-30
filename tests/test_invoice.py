# tests/test_invoices.py
from pytest import fixture
from thapi import *
import vcr
from . import cfg

@fixture
def invoice_keys():
    # Responsible only for returning the test data
    return ['Id', 'CustomerId', 'EventId']

@vcr.use_cassette('tests/vcr_cassettes/invoice-info.yml')
def test_invoice_info(invoice_keys):
    """Tests an API call to get a Invoice info"""

    invoice_instance = Invoice(cfg['test_ids']['invoice'])
    response = invoice_instance.info()

    assert isinstance(response, dict)
    assert response['Id'] == cfg['test_ids']['invoice'], "The ID should be in the response"
    assert set(invoice_keys).issubset(response.keys()), "All keys should be in the response"

@vcr.use_cassette('tests/vcr_cassettes/invoices.yml')
def test_all_invoices():
    invoices = Invoice()
    response = invoices.all()
    print(type(response))
    assert isinstance(response, list)
    assert int(response[0]['Number']) > 0