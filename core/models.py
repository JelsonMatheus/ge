from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


class Usuario(AbstractUser):
    SEXO_CHOICES = (
        ("B", ""),
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )
    ESTADO_CIVIL_CHOICES = (
        ("B", ""),
        ("S", "Solteiro(a)"),
        ("C", "Casado(a)"),
        
    )
    ZONA_CHOICES = (
        ("B", ""),
        ("U", "Urbana"),
        ("R", "Rural")
    )
    # B significa que o campo está em branco , caso esteja em branco no banco pode ser isso
    class TipoUsuario(models.TextChoices):
        DIRETOR = 'D', _('Diretor')
        PROFESSOR = 'P', _('Professor')

    cpf = models.CharField(_('CPF'), max_length=11)
    tipo = models.CharField(max_length=2, choices=TipoUsuario.choices,
                            default=TipoUsuario.PROFESSOR)
    nome = models.CharField(_('Nome'),max_length=300)
    data_nascimento = models.DateField(_('Data de Nascimento'))
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES,default="B")
    telefone = models.CharField(_('Telefone'),max_length=14)
    email = models.EmailField(_('Email'))
    estado_civil = models.CharField(_('Estado Civil'),max_length=1, choices=ESTADO_CIVIL_CHOICES,default="B")
    cep = models.CharField(_('Cep'),max_length=9 ,null= True,blank=True)
    endereco = models.CharField(_('Endereço'),max_length=200)
    zona = models.CharField(_('Zona'),max_length=1, choices=ZONA_CHOICES,default="B")


    def is_diretor(self):
        return self.tipo == self.TipoUsuario.DIRETOR

class Aluno(models.Model):
    SEXO_CHOICES = (
        ("B", ""),
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )
    ESTADO_CIVIL_CHOICES = (
        ("B", ""),
        ("S", "Solteiro(a)"),
        ("C", "Casado(a)")
    )
    ZONA_CHOICES = (
        ("B", ""),
        ("U", "Urbana"),
        ("R", "Rural")
    )
    RESPONSAVEL_CHOICES = (
        ("B", ""),
        ("P", "Pai"),
        ("M", "Mãe")
    )

    cpf = models.CharField(_('CPF'), max_length=11)
    nome = models.CharField(_('Nome'),max_length=300)
    data_nascimento = models.DateField(_('Data de Nascimento'))
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES,default="B")
    email = models.EmailField(_('Email'))
    estado_civil = models.CharField(_('Estado Civil'),max_length=1, choices=ESTADO_CIVIL_CHOICES,default="B")
    cep = models.CharField(_('Cep'),max_length=9 ,null= True,blank=True)
    endereco = models.CharField(_('Endereço'),max_length=200)
    zona = models.CharField(_('Zona'),max_length=1, choices=ZONA_CHOICES,default="B")
    nome_da_mae = models.CharField(_('Nome da Mãe'), max_length=300)
    nome_do_pai = models.CharField(_('Nome do Pai'), max_length=300)
    cpf_da_mae = models.CharField(_('CPF da Mãe'), max_length=11)
    cpf_do_pai = models.CharField(_('CPF do Pai'), max_length=11)
    responsavel = models.CharField(_('Responsável'), max_length=1, choices=RESPONSAVEL_CHOICES,default="B")

class Disciplina(models.Model):
    nome = models.CharField(_('Nome Disciplina'),max_length=30)
    codigo = models.IntegerField(_('Codigo'),validators=[MinValueValidator(1),MaxValueValidator(20)])

class Turma(models.Model):
    TURNO_CHOICES = (
        ("B", ""),
        ("M", "Matutino"),
        ("V", "Vespertino"),
        ("N", "Noturno")
    )
    ATENDIMENTO_CHOICES = (
        ("B", ""),
        ("1", "Ensino Fundamental"),
        ("2", "Ensino Médio")
    )
    nome = models.CharField(_('Nome'),max_length=300)
    sala = models.IntegerField(_('Sala'),validators=[MinValueValidator(1),MaxValueValidator(100)])
    turno = models.CharField(max_length=1,choices=TURNO_CHOICES,default="B")
    tipo_atendimento = models.CharField(max_length=1,choices=ATENDIMENTO_CHOICES,default="B")
    dia_semana =  models.CharField(_('Dia da Semana'),max_length=20)
    disciplina = models.ForeignKey(Disciplina,on_delete=models.PROTECT)

