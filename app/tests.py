from django.test import TestCase
from .models import *

# Create your tests here.

portugues = Teste.objects.create()
ciencia = Teste.objects.create(requisito=portugues)

inst = TesteInsta.objects.create(disc=ciencia)


print(inst.disc.requisito)