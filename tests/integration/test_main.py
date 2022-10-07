import pytest
from main import hello_world

@pytest.mark.parametrize("expected", [
    'ini semua dunia'
])
def test_response(expected):
    # returns string
    assert hello_world() == expected