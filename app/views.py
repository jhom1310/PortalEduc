from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
# Create your views here.
def login_inicial (request):
    return render(request, 'log.html')

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

@require_POST
def submit_cadastro(request):
    try:
        usuario_aux = User.objects.get(email=request.POST['emailsignup'])

        if usuario_aux :
            messages.error(request, 'Email ou Usuario já em uso.')
            return redirect('/login/#toregister')


    except User.DoesNotExist:
     first_name = request.POST['name']
     username = request.POST['usernamesignup']
     email = request.POST['emailsignup']
     password = request.POST['passwordsignup']

    novoUsuario = User.objects.create_user(username=username, email=email, password=password, first_name= first_name)
    novoUsuario.save()

    return redirect('/login/')

def user_inicial (request):
    return render(request, 'userHome.html')