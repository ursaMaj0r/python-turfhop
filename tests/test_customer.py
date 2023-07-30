# tests/test_customers.py
from pytest import fixture
from thapi import *
import vcr

@fixture
def customer_keys():
    # Responsible only for returning the test data
    return ['Id', 'CompanyId', 'CompanyId', 'Name',
              'BusinessAccount', 'Lead', 'CustomerType',
              'JobZip', 'BillingSameAsJob', 'Website']

@vcr.use_cassette('tests/vcr_cassettes/customer-info.yml')
def test_customer_info(customer_keys):
    """Tests an API call to get a Customer info"""

    customer_instance = Customer(cfg['test_ids']['customer'])
    response = customer_instance.info()

    assert isinstance(response, dict)
    assert response['Id'] == cfg['test_ids']['customer'], "The ID should be in the response"
    assert set(customer_keys).issubset(response.keys()), "All keys should be in the response"

@vcr.use_cassette('tests/vcr_cassettes/customers.yml')
def test_all_customers():
    customers = Customer()
    response = customers.all()
    print(type(response))
    assert isinstance(response, list)
    assert response[0]['TaxExempt'] == False