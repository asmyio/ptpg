import pytest
import json
from unittest import mock 

@pytest.fixture
def requests():
    return '{ "name":"John", "age":30, "city":"New York"}'

def test_fixture(requests):
    value = json.loads(requests)
    assert value["name"] == "John"