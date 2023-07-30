# tests/test_jobs.py
from pytest import fixture
from thapi import *
import vcr

@fixture
def job_keys():
    # Responsible only for returning the test data
    return ['Id', 'CompanyId', 'ProjectManagerUserId', 'CustomerId']

@vcr.use_cassette('tests/vcr_cassettes/job-info.yml')
def test_job_info(job_keys):
    """Tests an API call to get a Job info"""

    job_instance = Job(cfg['test_ids']['job'])
    response = job_instance.info()

    assert isinstance(response, dict)
    assert response['Id'] == cfg['test_ids']['job'], "The ID should be in the response"
    assert set(job_keys).issubset(response.keys()), "All keys should be in the response"

@vcr.use_cassette('tests/vcr_cassettes/job-items.yml')
def test_job_items(job_keys):
    """Tests an API call to get a Job info"""

    job_instance = Job(cfg['test_ids']['job'])
    response = job_instance.items()

    assert isinstance(response, list)

@vcr.use_cassette('tests/vcr_cassettes/jobs.yml')
def test_all_jobs():
    jobs = Job()
    response = jobs.all()
    print(type(response))
    assert isinstance(response, list)
    assert response[0]['CompanyId'] == cfg['turfhop']['TH_COMPANY_ID']