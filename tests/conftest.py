import pytest
from app import my_app


@pytest.fixture
def app():
    return my_app
