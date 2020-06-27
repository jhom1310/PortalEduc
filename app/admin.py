from .models import Disciplinas, Curso
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# Register your models here.

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(Disciplinas)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ['nome']






