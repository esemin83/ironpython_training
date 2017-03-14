import pytest

from fixture.application import App


#@pytest.fixture
#def app():
#    fixture = App(path="C:\\addressbook_exe\\AddressBook.exe")
#    return fixture


@pytest.fixture(scope="session")
def app(request):
    fixture = App(path="C:\\addressbook_exe\\AddressBook.exe")
    def fin():
        fixture.exit()
    request.addfinalizer(fin)
    return fixture