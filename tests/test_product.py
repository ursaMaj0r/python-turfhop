# tests/test_products.py
from pytest import fixture
from thapi import *
import vcr

@fixture
def product_keys():
    # Responsible only for returning the test data
    return ['Id', 'CompanyId', 'ProductCategoryId', 'Type']

@vcr.use_cassette('tests/vcr_cassettes/product-info.yml')
def test_product_info(product_keys):
    """Tests an API call to get a Product info"""

    product_instance = Product(cfg['test_ids']['product'])
    response = product_instance.info()

    assert isinstance(response, dict)
    assert response['Id'] == cfg['test_ids']['product'], "The ID should be in the response"
    assert set(product_keys).issubset(response.keys()), "All keys should be in the response"

@vcr.use_cassette('tests/vcr_cassettes/products.yml')
def test_all_products():
    products = Product()
    response = products.all()
    print(type(response))
    assert isinstance(response, list)
    assert response[0]['CompanyId'] == cfg['turfhop']['TH_COMPANY_ID']