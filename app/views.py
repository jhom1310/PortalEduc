from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from app.forms import *
from app.models import Disciplina, DisciplinasInstance
from .models import *
from django.contrib.auth.decorators import permission_required
from rest_framework import viewsets
from .serializers import DisciplinasSerializer
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import models
import datetime

def logout_user(request):
    logout(request)
    return redirect('/login/')

############ Login ###################
def login_inicial (request):
    return render(request, 'login.html')

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuario ou Senha inválido.')
    return redirect('/login/')

############ Cadastro ###################
'''
def cadastro(request):
    return render(request, 'register.html')
'''
def cadastrar_usuario(request):
    if request.method == 'POST':
        f = SignUpForm(request.POST)
        if f.is_valid():
            try:
                usuario_aux = User.objects.get(email=request.POST['email'])

                if usuario_aux:
                    messages.error(request, 'Erro! Email já em uso.')
                    return redirect('/cadastro')
            except User.DoesNotExist:
                my_group = Group.objects.get(name='Alunos')
                f.save().groups.add(my_group)
                messages.success(request, 'Conta criada com sucesso!')
                return redirect('/login')

    else:
        f = SignUpForm()

    return render(request, 'cadastro.html', {'form': f})
'''
@require_POST
def submit_cadastro(request):

    try:
        usuario_aux = User.objects.get(email=request.POST['email'])

        if usuario_aux :
            messages.error(request, 'email já em uso.')
            return redirect('/register')


    except User.DoesNotExist:
     first_name = request.POST['name']
     username = request.POST['username']
     email = request.POST['email']
     password = request.POST['password']

    novoUsuario = User.objects.create_user(username=username, email=email, password=password, first_name= first_name)
    novoUsuario.save()
    my_group = Group.objects.get(name='Alunos')
    novoUsuario.groups.add(my_group)
    return redirect('/login/')
'''

############ Home ###################
@login_required(login_url='/login')
def user_inicial (request):
    return render(request, 'user_Home.html')

############ Curso ###################
#@permission_required('app.change_curso', login_url='/restrito')
@login_required(login_url='/login')
def all_courses (request):
    cursos = Curso.objects.all()
    return render(request, 'all-courses.html', {'cursos': cursos})

@permission_required('app.add_curso', login_url='/restrito')
@login_required(login_url='/login')
def add_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/all-courses')
    else:
        form = CursoForm()

    return render(request, 'add-curso.html', {'form': form})

@permission_required('app.change_disciplinas', login_url='/restrito')
@login_required(login_url='/login')
def edit_curso(request, pk):
    teste = True
    curso = Curso.objects.get(pk=pk)
    if request.method == "POST":
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            curso.save()
            return redirect('/all-courses')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'add-curso.html', {'form': form, 'teste': teste})


############ Disciplinas ###################
@login_required(login_url='/login')
def all_disciplinas(request):
    disciplinas = DisciplinasInstance.objects.all()
    return render(request, 'all-disciplinas.html', {'disciplinas': disciplinas})

@permission_required('app.add_disciplinas', login_url='/restrito')
@login_required(login_url='/login')
def add_disciplinas(request):
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            if request.user.groups.filter(name='Professores').exists():
                disciplina = form.save(commit=False)
                disciplina.prof = request.user
                disciplina.save()
            else:
                form.save()
        return redirect('/all-disciplinas')
    else:
        form = DisciplinaForm()

    return render(request, 'add-disciplinas.html', {'form': form})

@permission_required('app.change_disciplinas', login_url='/restrito')
@login_required(login_url='/login')
def edit_disciplina(request, pk):
    teste = True
    disciplina = DisciplinasInstance.objects.get(pk=pk)
    if request.method == "POST":
        form = DisciplinaForm(request.POST, instance=disciplina)
        if form.is_valid():
            form.save()
            disciplina.save()
            return redirect('/all-disciplinas')
    else:
        form = DisciplinaForm(instance=disciplina)
    return render(request, 'add-disciplinas.html', {'form': form, 'teste': teste})

@permission_required('app.change_disciplinas', login_url='/restrito')
@login_required(login_url='/login')
def minhas_discipinas(request):
    user = request.user
    disciplinas = DisciplinasInstance.objects.filter(prof=user)
    return render(request, 'minhas-disciplinas.html', {'disciplinas': disciplinas})

def view_disciplina(request, pk):
    disc = DisciplinasInstance.objects.get(pk=pk)
    alunos = disc.alunos.all()
    return render(request, 'view-disciplina.html', {'alunos': alunos})


########## Professores #################

@login_required(login_url='/login')
def all_professores(request):
    alunos = User.objects.filter(groups__name='Professores')
    return render(request, 'all-professores.html', {'alunos': alunos})

def add_professor(request, pk):
    professor = User.objects.get(pk=pk)
    my_group = Group.objects.get(name='Professores')
    professor.groups.add(my_group)
    professor.save()
    return redirect('/all-professores')
############ Alunos ###################

@login_required(login_url='/login')
def all_alunos(request):
    alunos = User.objects.filter(groups__name='Alunos')
    return render(request, 'all-alunos.html', {'alunos': alunos})

############ Acesso negado ###################
def restrito(request):
    return render(request, '403.html')

def xx (request):
    return render(request, 'header.html')


########## API #################
class DisciplinasViewSet(viewsets.ModelViewSet):
    queryset = DisciplinasInstance.objects.all()
    serializer_class = DisciplinasSerializer