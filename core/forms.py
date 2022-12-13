from django import forms
from core.models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _


class UsuarioForms(UserCreationForm):
    
    class Meta:
        model = Usuario
        exclude = ('first_name','last_name')