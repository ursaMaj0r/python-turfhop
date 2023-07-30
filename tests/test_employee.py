# tests/test_employees.py
from pytest import fixture
from thapi import *
import vcr

@fixture
def employee_keys():
    # Responsible only for returning the test data
    return ['Id', 'CompanyId', 'LinkedUserId', 'FirstName',
              'LastName', 'Email', 'Phone',
              'DefaultCrewId', 'Title', 'Image']

@vcr.use_cassette('tests/vcr_cassettes/employee-info.yml')
def test_employee_info(employee_keys):
    """Tests an API call to get a Employee info"""

    employee_instance = Employee(cfg['test_ids']['employee'])
    response = employee_instance.info()

    assert isinstance(response, dict)
    assert response['Id'] == cfg['test_ids']['employee'], "The ID should be in the response"
    assert set(employee_keys).issubset(response.keys()), "All keys should be in the response"

@vcr.use_cassette('tests/vcr_cassettes/employees.yml')
def test_all_employees():
    employees = Employee()
    response = employees.all()
    print(type(response))
    assert isinstance(response, list)
    assert response[0]['Active'] == True
    
@vcr.use_cassette('tests/vcr_cassettes/employees_time_logs.yml')
def test_time_logs():
    employee_instance = Employee(cfg['test_ids']['employee'])
    response = employee_instance.time_logs()
    assert isinstance(response, list)