# Generated by Django 4.1.3 on 2022-12-22 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_aluno_cpf_alter_aluno_cpf_da_mae_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turma',
            name='disciplina',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipo',
            field=models.CharField(blank=True, choices=[('D', 'Diretor'), ('P', 'Professor')], default='P', max_length=2),
        ),
        migrations.AddField(
            model_name='turma',
            name='disciplina',
            field=models.ManyToManyField(related_name='disciplinas', to='core.disciplina'),
        ),
    ]