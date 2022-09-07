from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel
import uuid

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class DisplayManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_display=True)


class Square(TimeStampedModel):
    name = models.CharField('Nome', max_length=255, unique=True)
    is_display = models.BooleanField('Exibir', default=True)
    description = models.TextField('Descrição', blank=True) #implementado
    address = models.CharField('Endereço', max_length=255, blank=True)#implementado
    image1 = models.CharField('nome imagem 1', max_length=150, blank=True)#modificado original não tem 'imagem'
    altimg1 = models.CharField('Alt imagem 1', max_length=150, blank=True)
    image2 = models.CharField('nome imagem 2', max_length=150, blank=True)
    altimg2 = models.CharField('Alt imagem 2', max_length=150, blank=True)
    image3 = models.CharField('nome imagem 3', max_length=150, blank=True)
    altimg3 = models.CharField('Alt imagem 3', max_length=150, blank=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")


    objects = models.Manager()
    display = DisplayManager()

    class Meta:
        ordering = ("name",)
        verbose_name = "Praça"
        verbose_name_plural = "Praças"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("trees:list_by_square", kwargs={"slug": self.slug})

class Specie(TimeStampedModel):
    name = models.CharField('Nome', max_length=255, unique=True)
    description = models.TextField('Descrição', blank=True) #implementado

    class Meta:
        ordering = ("name",)
        verbose_name = "Espécie"
        verbose_name_plural = "Espécies"

    def __str__(self):
        return self.name

class Family(TimeStampedModel):
    name = models.CharField('Nome', max_length=255, unique=True)
    description = models.TextField('Descrição', blank=True) #implementado

    class Meta:
        ordering = ("name",)
        verbose_name = "Família"
        verbose_name_plural = "Famílias"

    def __str__(self):
        return self.name



    


class Tree(TimeStampedModel):
    SOURCE_CHOICES = (
        ('nativa', 'Nativa'),
        ('exótica', 'Exótica'),
        ('nativa e exótica', 'Nativa e Exótica')
    )
    
    square = models.ForeignKey(Square, related_name="trees", on_delete=models.CASCADE)#Category
    name = models.CharField('Nome popular', max_length=255) 
    specie = models.ForeignKey(Specie, related_name="species", on_delete=models.CASCADE) #implementado
    family = models.ForeignKey(Family, related_name="family", on_delete=models.CASCADE) #implementado
    source = models.CharField('Origem', max_length=20, choices=SOURCE_CHOICES)
    description = models.TextField('Descrição', blank=True)
    is_display = models.BooleanField('Exibir', default=True)
    image1 = models.CharField('nome imagem 1', max_length=150, blank=True)
    altimg1 = models.CharField('Alt imagem 1', max_length=150, blank=True)#modificado original não tem 'imagem'
    image2 = models.CharField('nome imagem 2', max_length=150, blank=True)
    altimg2 = models.CharField('Alt imagem 2', max_length=150, blank=True)#implementado
    image3 = models.CharField('nome imagem 3', max_length=150, blank=True)
    altimg3 = models.CharField('Alt imagem 3', max_length=150, blank=True)#implementado
    quantidade = models.PositiveIntegerField(default=1,null=False, blank=False)
  
    
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")
    
   

    objects = models.Manager()
    display = DisplayManager()

    class Meta:
        ordering = ("name",)
        verbose_name = "Árvore"
        verbose_name_plural = "Árvores"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("trees:detail", kwargs={"slug": self.slug})