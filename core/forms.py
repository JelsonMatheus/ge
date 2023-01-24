from django import forms
from core.models import Usuario, Aluno, Turma, Disciplina, Lotacao
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _



DIAS = [(0, 'Segunda-Feira'), (1, 'Terça-Feira'), (2, 'Quarta-Feira'), 
        (3, 'Quinta-Feira'), (4,'Sexta-Feira'), (5, 'Sábado'), (6, 'Domingo')]


class UsuarioForms(UserCreationForm):
    
    class Meta:
        model = Usuario
        exclude = ('first_name','last_name', 'date_joined', 'password')


class UsuarioFormsEdit(UserChangeForm):
    
    class Meta:
        model = Usuario
        exclude = ('first_name','last_name', 'date_joined','password', 'password1','password2','username')


class AlunoForms(forms.ModelForm):
    class Meta:
        model = Aluno
        exclude = ()


class AlunoFormsEdit(UserChangeForm):
    class Meta:
        model = Aluno
        exclude = ()


class TurmaForms(forms.ModelForm):
    disciplinas = forms.ModelMultipleChoiceField(
        queryset=Disciplina.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'}),
        required=True
    )
    dia_semana = forms.MultipleChoiceField(
        choices=DIAS,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'}),
        required=True
    )

    class Meta:
        model = Turma
        exclude = ()
        
    def clean(self):
        data = super().clean()
        dias = data['dia_semana']
        data['dia_semana'] = ','.join(dias)
        return data


class LotacaoForms(forms.ModelForm):
    class Meta:
        model = Lotacao
        exclude = ()
    
    def __init__(self, *args, **kwargs):
        super(LotacaoForms, self).__init__(*args, **kwargs)
        self.fields['professor'].queryset = Usuario.objects.filter(tipo=Usuario.TipoUsuario.PROFESSOR)