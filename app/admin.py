from django.contrib import admin
from .models import Disciplinas, Curso
# Register your models here.

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['nome']



@admin.register(Disciplinas)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ['nome']