import pytest

from application import App


@pytest.fixture
def app():
    fixture = App()
    return fixture