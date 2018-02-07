import pytest
from fixture.application import Application

__author__ = 'viktor'


@pytest.fixture(scope = "session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
