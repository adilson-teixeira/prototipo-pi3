import pytest

#from orders.tests.factories import ItemFactory, OrderFactory
from trees.tests.factories import SquareFactory, SpecieFactory, FamilyFactory, TreeFactory 


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def square():
    return SquareFactory()


@pytest.fixture
def specie():
    return SpecieFactory()


@pytest.fixture
def family():
    return FamilyFactory()



@pytest.fixture
def tree():
    return TreeFactory()


#@pytest.fixture
#def order():
#    return OrderFactory()


#@pytest.fixture
#def item():
#    return ItemFactory()


#@pytest.fixture
#def order_form_data():
#    return {
#        "cpf": "401.142.450-10",
#        "name": "Fulano",
#        "email": "test@fulano.com",
#        "postal_code": "76900-649",
#        "address": "Rua Castro Alves",
#        "number": "123",
#        "district": "Jardim dos Migrantes",
#        "state": "RO",
#        "city": "Ji-Paraná",
#    }