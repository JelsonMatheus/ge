from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    class TipoUsuario(models.TextChoices):
        DIRETOR = 'D', _('Diretor')
        PROFESSOR = 'P', _('Professor')

    cpf = models.CharField(_('CPF'), max_length=11)
    tipo = models.CharField(max_length=2, choices=TipoUsuario.choices,
                            default=TipoUsuario.PROFESSOR)
    
    def is_diretor(self):
        return self.tipo == self.TipoUsuario.DIRETOR

