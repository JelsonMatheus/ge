from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser



class Usuario(AbstractUser):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )
    ESTADO_CIVIL_CHOICES = (
        ("S", "Solteiro(a)"),
        ("C", "Casado(a)")
    )
    ZONA_CHOICES = (
        ("U", "Urbana"),
        ("R", "Rural")
    )
    class TipoUsuario(models.TextChoices):
        DIRETOR = 'D', _('Diretor')
        PROFESSOR = 'P', _('Professor')

    cpf = models.CharField(_('CPF'), max_length=11)
    tipo = models.CharField(max_length=2, choices=TipoUsuario.choices,
                            default=TipoUsuario.PROFESSOR)
    nome = models.CharField(_('Nome'),max_length=300)
    data_nascimento = models.DateField(_('Data de Nascimento'))
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    telefone = models.CharField(_('Telefone'),max_length=14)
    email = models.EmailField(_('Email'))
    estado_civil = models.CharField(_('Estado Civil'),max_length=1, choices=ESTADO_CIVIL_CHOICES)
    cep = models.CharField(_('Cep'),max_length=9 ,null= True,blank=True)
    endereco = models.CharField(_('Endereço'),max_length=200)
    zona = models.CharField(_('Zona'),max_length=1, choices=ZONA_CHOICES)


    def is_diretor(self):
        return self.tipo == self.TipoUsuario.DIRETOR

class Aluno(models.Model):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )
    ESTADO_CIVIL_CHOICES = (
        ("S", "Solteiro(a)"),
        ("C", "Casado(a)")
    )
    ZONA_CHOICES = (
        ("U", "Urbana"),
        ("R", "Rural")
    )
    RESPONSAVEL_CHOICES = (
        ("P", "Pai"),
        ("M", "Mãe")
    )

    cpf = models.CharField(_('CPF'), max_length=11)
    nome = models.CharField(_('Nome'),max_length=300)
    data_nascimento = models.DateField(_('Data de Nascimento'))
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    email = models.EmailField(_('Email'))
    estado_civil = models.CharField(_('Estado Civil'),max_length=1, choices=ESTADO_CIVIL_CHOICES)
    cep = models.CharField(_('Cep'),max_length=9 ,null= True,blank=True)
    endereco = models.CharField(_('Endereço'),max_length=200)
    zona = models.CharField(_('Zona'),max_length=1, choices=ZONA_CHOICES)
    nome_da_mae = models.CharField(_('Nome da Mãe'), max_length=300)
    nome_do_pai = models.CharField(_('Nome do Pai'), max_length=300)
    cpf_da_mae = models.CharField(_('CPF da Mãe'), max_length=11)
    cpf_do_pai = models.CharField(_('CPF do Pai'), max_length=11)
    responsavel = models.CharField(_('Responsável'), max_length=1, choices=RESPONSAVEL_CHOICES)


