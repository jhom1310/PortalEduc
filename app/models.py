from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User, Group
import uuid

# Create your models here.

class Curso(models.Model):
    nome = models.CharField(max_length=50)
    disciplinas = models.ManyToManyField('Disciplinas')


    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        '''
        permissions = (
                ('permissao_editar_curso', 'Pode editar cursos'),
                ('permissao_add_curso', 'Pode adicionar'),
                ('permissao_excluir_curso', 'Pode adicionar'),
            ) '''


class Disciplinas(models.Model):
    nome = models.CharField(max_length=50)
    requisitos = models.ManyToManyField('self', null=True, blank=True, symmetrical=False)
    prof = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'groups__name': 'Professores'})
    alunos = models.ManyToManyField(User,related_name='Alunos', blank=True, limit_choices_to={'groups__name':'Alunos'})
    LOAN_STATUS = (
        ('a', 'Aberta'),
        ('f', 'Fechada'),
        ('e', 'Execução'),
        ('l', 'Finalizada'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='f',
        help_text='Status da Disciplina',
    )

    def __str__(self):
        return str(self.nome)

    class Meta:
        ordering = ['id']


