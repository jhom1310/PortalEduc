from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from app.models import Disciplina, DisciplinasInstance, Curso

class DisciplinaForm(ModelForm):
    class Meta:
        model = DisciplinasInstance
        fields = ["disciplina", "prof", "alunos", "status"]
        widgets = {
            'categories': forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        super(DisciplinaForm, self).__init__(*args, **kwargs)

       # self.fields['disciplina_nome'].widget.attrs['class'] = 'form-control'
        self.fields['disciplina'].widget.attrs['class'] = 'form-control'
        self.fields['prof'].widget.attrs['class'] = 'form-control'
        self.fields['alunos'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-control'

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = ["nome", "disciplinas"]
        widgets = {
            'categories': forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        super(CursoForm, self).__init__(*args, **kwargs)

       # self.fields['disciplina_nome'].widget.attrs['class'] = 'form-control'
        self.fields['nome'].widget.attrs['class'] = 'form-control'
        self.fields['disciplinas'].widget.attrs['class'] = 'form-control'


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