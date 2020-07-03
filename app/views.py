from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from app.forms import *
from app.models import Disciplinas


from .models import *
from django.contrib.auth.decorators import permission_required
# Create your views here.

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


############ Disciplinas ###################
@login_required(login_url='/login')
def all_disciplinas(request):
    disciplinas = Disciplinas.objects.all()
    return render(request, 'all-disciplinas.html', {'disciplinas': disciplinas})

@permission_required('app.add_disciplinas', login_url='/restrito')
@login_required(login_url='/login')
def add_disciplinas(request):
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
           form.save()
        return redirect('/all-disciplinas')
    else:
        form = DisciplinaForm()

    return render(request, 'add-disciplinas.html', {'form': form})

@permission_required('app.change_disciplinas', login_url='/restrito')
@login_required(login_url='/login')
def edit_disciplina(request, pk):
    teste = True
    disciplina = Disciplinas.objects.get(pk=pk)
    if request.method == "POST":
        form = DisciplinaForm(request.POST, instance=disciplina)
        if form.is_valid():
            form.save()
            disciplina.save()
            return redirect('/all-disciplinas')
    else:
        form = DisciplinaForm(instance=disciplina)
    return render(request, 'add-disciplinas.html', {'form': form, 'teste': teste})



############ Acesso negado ###################
def restrito(request):
    return render(request, '403.html')

def xx (request):
    return render(request, 'header.html')