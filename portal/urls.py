"""portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf.urls import include
from app.views import DisciplinasViewSet
from rest_framework import routers
############ API ##############
router = routers.DefaultRouter()
router.register(r'disciplinas', DisciplinasViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_inicial),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    #path('register/submit', views.submit_cadastro),
    #path('register/', views.cadastro),
    path('cadastro/', views.cadastrar_usuario),
    path('', views.user_inicial),
    path('all-alunos', views.all_alunos, name='all-alunos'),
    path('all-professores', views.all_professores, name='all-professores'),
    path('add-professores/<int:pk>', views.add_professor, name='add-professores'),
    path('all-courses', views.all_courses, name='all-courses'),
    path('all-disciplinas', views.all_disciplinas, name='all-disciplinas'),
    path('xx/', views.xx),
    path('restrito/', views.restrito),
    path('add-courses', views.add_curso, name='add-courses'),
    path('add-disciplinas', views.add_disciplinas, name='add-disciplina'),
    path('minhas-disciplinas', views.minhas_discipinas, name='minhas-disciplinas'),
    path('disciplina/<int:pk>/edit/', views.edit_disciplina, name='edit-disciplina'),
    path('curso/<int:pk>/edit/', views.edit_curso, name='edit-course'),
    path('disciplina/<int:pk>/view/', views.view_disciplina, name='view-disciplina'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]

