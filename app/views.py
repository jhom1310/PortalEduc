from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from .models import *
# Create your views here.

def logout_user(request):
    logout(request)
    return redirect('/login/')

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


def cadastro(request):
    return render(request, 'register.html')

@require_POST
def submit_cadastro(request):
    try:
        usuario_aux = User.objects.get(email=request.POST['email'])

        if usuario_aux :
            messages.error(request, 'Email ou Usuario já em uso.')
            return redirect('/register')


    except User.DoesNotExist:
     first_name = request.POST['name']
     username = request.POST['username']
     email = request.POST['email']
     password = request.POST['password']

    novoUsuario = User.objects.create_user(username=username, email=email, password=password, first_name= first_name)
    novoUsuario.save()

    return redirect('/login/')

@login_required(login_url='/login')
def user_inicial (request):
    return render(request, 'user_Home.html')

@login_required(login_url='/login')
def all_courses (request):
    cursos = Curso.objects.all()
    return render(request, 'all-courses.html', {'cursos': cursos})

def xx (request):
    return render(request, 'header.html')