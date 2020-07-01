from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from app.models import Disciplinas

class DisciplinaForm(ModelForm):
    class Meta:
        model = Disciplinas
        fields = ["nome", "requisitos", "prof", "alunos", "status"]

    def __init__(self, *args, **kwargs):
        super(DisciplinaForm, self).__init__(*args, **kwargs)

        self.fields['nome'].widget.attrs['class'] = 'form-control'
        self.fields['requisitos'].widget.attrs['class'] = 'form-control'
        self.fields['prof'].widget.attrs['class'] = 'form-control'
        self.fields['alunos'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-control'


class SignUpForm(UserCreationForm):
    #nome = forms.CharField(max_length=30, required=False)
    #sobrenome = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2')




    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'