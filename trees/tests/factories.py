import factory
import factory.fuzzy

from ..models import Family, Square, Specie, Tree

# Cada Factory fuzzy usado pelas fixture no arquivo conftest.py, preenche todos os campos que usam testos criando praças, especies, familias, árvores e texto alternativos das imagens com letras aleatórias de acordo com os modelos do arquivo model.py.

#Nas descrições o factory Faker cria um parágrafo de acordo com o parâmetro inserido
# O factory.django.ImageFild() cria imagens testes para testar o modelo no banco de dados

class SquareFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()
    description = factory.Faker("paragraph", nb_sentences=3, variable_nb_sentences=True)
    address = factory.fuzzy.FuzzyText()
    image1 = factory.django.ImageField()
    altimg1 = factory.fuzzy.FuzzyText()
    image2 = factory.django.ImageField()
    altimg2 = factory.fuzzy.FuzzyText()
    image3 = factory.django.ImageField()
    altimg3 = factory.fuzzy.FuzzyText()

    class Meta:
        model = Square


class SpecieFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()
    description = factory.Faker("paragraph", nb_sentences=3, variable_nb_sentences=True)

    class Meta:
        model = Specie

class FamilyFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()
    description = factory.Faker("paragraph", nb_sentences=3, variable_nb_sentences=True)

    class Meta:
        model = Family



class TreeFactory(factory.django.DjangoModelFactory):
    square = factory.SubFactory(SquareFactory)
    name = factory.fuzzy.FuzzyText()
    specie = factory.SubFactory(SpecieFactory)
    family = factory.SubFactory(FamilyFactory)
    description = factory.Faker("paragraph", nb_sentences=3, variable_nb_sentences=True)
    is_display = factory.Faker("pybool") 
    image1 = factory.django.ImageField()
    altimg1 = factory.fuzzy.FuzzyText()
    image2 = factory.django.ImageField()
    altimg2 = factory.fuzzy.FuzzyText()
    image3 = factory.django.ImageField()
    altimg3 = factory.fuzzy.FuzzyText()
    quantidade = factory.fuzzy.FuzzyInteger(low=1)
   

    class Meta:
        model = Tree