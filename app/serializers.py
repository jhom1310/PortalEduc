from .models import Disciplinas
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import models



class DisciplinasSerializer(serializers.ModelSerializer):
    group = models.Group.objects.get(name='Professores')

    prof = serializers.SlugRelatedField(
        many=False,
        slug_field='first_name',
        queryset=group.user_set.all()

    )
    alunos = serializers.SlugRelatedField(
        many=True,
        slug_field='first_name',
        queryset=User.objects.all()
    )
    requisitos = serializers.SlugRelatedField(
        many=True,
        slug_field='nome',
        queryset=Disciplinas.objects.all()
    )

    class Meta:
        model = Disciplinas
        fields = ('id', 'nome', 'prof', 'requisitos', 'alunos', 'status')


