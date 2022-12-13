from django import forms
from core.models import Usuario, Aluno
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _


class UsuarioForms(UserCreationForm):
    
    class Meta:
        model = Usuario
        exclude = ('first_name','last_name')

class AlunoForms(forms.ModelForm):
    class Meta:
        model = Aluno
        exclude = ()