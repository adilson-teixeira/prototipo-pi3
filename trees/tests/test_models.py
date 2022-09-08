import pytest
from pytest_django.asserts import assertQuerysetEqual

from ..models import Tree
from .factories import TreeFactory

pytestmark = pytest.mark.django_db


# Testa o model das Praças
class TestSquareModel:
    def test___str__(self, square): # se retorna o nome da categoria
        assert square.__str__() == square.name
        assert str(square) == square.name

    def test_get_absolute_url(self, square): # testa a url absoluta para exibir as arvores de acordo com as praças
        url = square.get_absolute_url()
        assert url == f"/trees/square/{square.slug}/"
# Funciona semelhante ao teste das praças
class TestFamilyModel:
    def test___str__(self, family):
        assert family.__str__() == family.name
        assert str(family) == family.name

# funcionam semelhante aos testes das praças e famílias

class TestSpecieModel:
    def test___str__(self, specie):
        assert specie.__str__() == specie.name
        assert str(specie) == specie.name




class TestTreeModel:
    def test___str__(self, tree):
        assert tree.__str__() == tree.name
        assert str(tree) == tree.name

    def test_get_absolute_url(self, tree):
        url = tree.get_absolute_url()
        assert url == f"/trees/{tree.slug}/"

    def test_available_manager(self):
        TreeFactory(is_display=True)
        TreeFactory(is_display=False)

        assert Tree.objects.all().count() == 2 # no vídeo .all().count() == 2
        assert Tree.display.all().count() == 1 #no vídeo .all().count() == 1
        assertQuerysetEqual(
            Tree.display.all(),
            Tree.objects.filter(is_display=True),
            transform=lambda x: x,
        )