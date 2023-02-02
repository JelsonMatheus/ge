# Generated by Django 4.1.3 on 2023-01-28 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_lotacao_professor_alter_lotacao_turma'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='lotacao',
            unique_together={('professor', 'turma', 'disciplina')},
        ),
        migrations.AlterUniqueTogether(
            name='matricula',
            unique_together={('aluno', 'turma')},
        ),
    ]
