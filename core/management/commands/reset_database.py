from django.core.management.base import BaseCommand
from django.core import management
from django.utils.translation import gettext_lazy as _
from ge import settings
import os


class Command(BaseCommand):
    help = _('Clean database and load fixtures.')

    def handle(self, *args, **kwargs):
        if os.path.isfile(settings.BASE_DIR / 'db.sqlite3'):
            os.remove(settings.BASE_DIR / 'db.sqlite3')

        management.call_command('makemigrations')
        management.call_command('migrate')
        management.call_command('loaddata', 'fixtures/usuarios.json')
        self.stdout.write(self.style.SUCCESS('Successfully reset databas.'))