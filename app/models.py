from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=50)
    disciplinas = models.ManyToManyField('Disciplinas')

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']

class Disciplinas(models.Model):
    nome = models.CharField(max_length=50)
    requisitos = models.ForeignKey('self', on_delete=models.CASCADE, null='true', blank='true')

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']

