# Generated by Django 5.0.1 on 2024-03-20 18:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cronograma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('especializacao', models.CharField(max_length=100)),
                ('disponibilidade_manha', models.BooleanField()),
                ('disponibilidade_tarde', models.BooleanField()),
                ('disponibilidade_noite', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('turno', models.CharField(max_length=5)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_semana', models.IntegerField()),
                ('turma', models.IntegerField()),
                ('horario', models.IntegerField()),
                ('cronograma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AcademPy.cronograma')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AcademPy.disciplina')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AcademPy.professor')),
            ],
        ),
    ]
