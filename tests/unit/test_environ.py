import os
import pytest 
from unittest import mock 

@pytest.fixture(autouse=True)
def mock_env_vars():
    with mock.patch.dict(os.environ, 
    {"NAME_OF_THE_ENVIRONMENT" : "THE_VALUE",
        "NAME_OF_THE_ENVIRONMENT_2" : "THE_SECOND_VALUE"}):
        yield

def test_first_value():
    assert os.environ["NAME_OF_THE_ENVIRONMENT"] == "THE_VALUE"

def test_second_value():
    assert os.environ["NAME_OF_THE_ENVIRONMENT_2"] == "THE_SECOND_VALUE"
